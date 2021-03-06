# -*- coding: utf-8 -*-
"""
    sphinx.ext.circuits
    ~~~~~~~~~~~~~~~~~~~

    Include TiKz icircuits in Sphinx documents

    :copyright: 2016 by Roie R. Blacl
    :license: BSD, see LICENSE for details
"""
from sphinx.errors import SphinxError
from sphinx.util.nodes import set_source_info
from sphinx.util.compat import Directive
from docutils import nodes, utils
from docutils.parsers.rst import directives

import os
import shutil
import hashlib
import posixpath

CWD = os.getcwd()
LATEX_IMAGE_DIR = '_static/images/'
IMAGE_URL = '/_images/'
LATEX_BUILD_DIR = 'tmp/images'
BUILD_TMPDIR = 'tmp/tikz'

class CircuitsExtError(SphinxError):
    category = 'Tikz extension error'

    def __init__(self, msg, stderr=None, stdout=None):
        if stderr:
            msg += '\n[stderr]\n' + stderr.decode(sys_encoding, 'replace')
        if stdout:
            msg += '\n[stdout]\n' + stdout.decode(sys_encoding, 'replace')
        SphinxError.__init__(self, msg)

DOC_HEAD = r'''\documentclass[preview]{standalone}
\usepackage{tikz}
%s
'''

DOC_BODY = r'''
\begin{document}
\tikzstyle{branch}=[fill,shape=circle,minimum size=3pt,inner sep=0pt]
\begin{tikzpicture}%s
%s
\end{tikzpicture}
\end{document}
'''

class RenderCircuitsImage(object):

    def __init__(self, text, tikzopts, tikzlibs, builder, font_size=11):
        #print "Rendering", text, os.getcwd()
        self.text = text
        self.tikzopts = tikzopts
        self.tikzlibs = tikzlibs
        #print "Options:", tikzopts, tikzlibs
        self.builder = builder
        self.font_size = font_size
        self.imagedir = os.path.join(os.getcwd(),
        '_build','html','_images')

    def render(self):
        '''return name of final rendered image file'''
        shasum = "%s.png" % hashlib.md5(self.text).hexdigest()
        relfn = posixpath.join(self.builder.imgpath, 'circuits',shasum)
        outfn = os.path.join(self.builder.outdir, self.imagedir, 'circuits', shasum)
        
        if os.path.exists(outfn):
            return relfn, outfn

        # create temp file for running latex
        print "Rendering latex image as pdf", outfn
        tempdir = BUILD_TMPDIR
        curpath = os.getcwd()
        os.chdir(tempdir)

        # create latex file to process
        self.wrap_text()

        # run pdflates to build pdf file
        status = os.system('pdflatex --interaction=nonstopmode tikz')
        assert 0 == status

        # convert to png file
        status = os.system('convert -density 300 tikz.pdf -quality 90 tikz.png')

        # copy final image to image dir
        os.chdir(curpath)
        imagepath = os.path.join(os.path.abspath(self.imagedir),'circuits')
        if not os.path.exists(imagepath):
            os.makedirs(imagepath)
        print "Copying file to ", imagepath, outfn
        shutil.copyfile(os.path.join(tempdir, "tikz.png"), outfn)
        #shutil.rmtree(tempdir)
        return relfn, outfn

    def wrap_text(self):
        latex = DOC_HEAD % self.tikzlibs
        latex += (DOC_BODY) % (self.tikzopts, self.text)

        # write latex file
        f = file('tikz.tex','w')
        f.write(latex)
        f.close()


class circuits(nodes.General, nodes.Element):
    pass

class Circuits(Directive):

    has_content = True
    required_arguments = 0
    optional_arguments = 1
    final_argument_whitespace = True
    option_spec = {
        'label': directives.unchanged,
        'name': directives.unchanged,
        'nowrap': directives.flag,
        'width': directives.unchanged,
        'align': directives.unchanged,
        'tikzopts': directives.unchanged,
        'tikzlibs': directives.unchanged,
    }

    def run(self):
        latex = '\n'.join(self.content)
        node = circuits()
        node['latex'] = latex
        node['label'] = None
        node['docname'] = self.state.document.settings.env.docname
        style = ''
        if 'width' in self.options:
            style += 'width=%s' % self.options['width']
        if 'align' in self.options:
            style += ' class="align-%s"' % self.options['align']
        node['style'] = style

        if 'tikzopts' in self.options:
            tikzopts = '[%s]' % self.options['tikzopts']
        else:
            tikzopts = ''

        node['tikzopts'] = tikzopts

        if 'tikzlibs' in self.options:
            tikzlibs = '\usetikzlibrary{%s}' % self.options['tikzlibs']
        else:
            tikzlibs = ''
        node['tikzlibs'] = tikzlibs

        ret = [node]
        set_source_info(self,node)
        return ret

def html_visit_circuits(self, node):
    latex = node['latex']
    opts = node['tikzopts']
    libs = node['tikzlibs']
    try:
        imagedir = self.builder.imgpath
        fname, relfn = RenderCircuitsImage(latex, opts, libs, self.builder).render()
        #print "Rendered imge:", fname, relfn
    except CircuitsExtError, exc:
        msg = unicode(str(exc), 'utf-8', 'replace')
        sm = nodes.system_message(msg, type='WARNING', level=2,
                backrefs=[], source=node['latex'])
        raise nodes.SkipNode
        sm.walkabout(self)
        self.builder.warn('display latex %r: ' % node['latex'] + str(exc))
        raise nodes.SkipNode
    if fname is None:
        # something failed -- use text-only as a bad substitute
        self.body.append('<span class="circuits">%s</span>' %
                         self.encode(node['latex']).strip())
    else:
         c = ('<img src="%s" %s' % (fname,node['style']))
         self.body.append( c + '/>')
    raise nodes.SkipNode

def latex_visit_circuits(self, node):
    self.body.append('$' + node['latex'] + '$')
    raise nodes.SkipNode

def latex_visit_displaycircuits(self, node):
    self.body.append(node['latex'])
    raise nodes.SkipNode

def setup(app):
    app.add_node(circuits,
        latex=(latex_visit_circuits, None),
        html=(html_visit_circuits,None))
    app.add_directive('circuits', Circuits)

 
