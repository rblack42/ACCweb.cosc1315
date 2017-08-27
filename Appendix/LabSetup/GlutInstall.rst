..  _glut-install:

COSC 1315 Graphics Setup
########################

..  include::   /references.inc

To make our later lab project more interesting, we are going to add a graphics
package to our systems. This is a bit complex for some systems, so bear with
me. If you are running Dev-C++, the addition you need is pretty simple to add.
If you are using some other C++ system, you may need some help. Please try to
follow the instructions on the link provided below. Email me if you run into
problems, telling me exactly what system you have, and the problem you ran
into. I have managed to get my students through this many times in the past.

..  note::

    The Computer Studies lab computers at most campuses are already set up
    correctly for the graphics projects, so if you can't get your home setup
    working, you can use these labs do the graphics problems if you choose.

Dev C++ (5.x) Instructions
****************************

..  note:: 

    Unless your system is pretty old, odds are it has a 64-bit
    processor. Older systems may have a 32-bit processor. You need to know
    which kind you have to do this install correctly. If you are unsure.
    check with me for help in finding out. (One clue is the presence of a
    ``Program Files (x86)`` folder on your "C" drive).

1.  First, we need to install some new libraries with graphics code we
    will be using. We'll be using two packages called OpenGL (Open Graphics
    Library) and GLUT (OpenGL Utility Toolkit).  The OpenGL package should
    be installed by default, so the first step is to verify this.

    a.  Start Dev C++ and click :menuselection:`File -->  New -->  Project`.

    b.  Click on the :menuselection:`Multimedia` tab.

    c.  If you see an OpenGL icon, you're all set. If not, talk to me.

2.  Now we need to install the FreeGLUT package. Follow these steps to install
    FreeGLUT on Dev C++.

    a. Depending on your system, download one of these two files:

        * :download:`freeglut-2.8.1-mingw32-1rrb.DevPak`
        * :download:`freeglut-2.8.1-mingw64-1rrb.DevPak`

    b. Using the `Package Manager` tool in Dev-C++, install the package using
    the `Install` menu option.

..  warning::

    On Windows 8 and Windows 10, you will need to run the Package Manager
    outside of Dev-C++. You need administrator privileges to install things in
    the default installation of Dev-C++. Navigate to the Dev-Cpp folder using
    the File Explorer tool. You are looking for "pacman.exe (Not the game, I am
    afraid). The file is probably in ``C:\Program Files (x86)\Dev-Cpp``).
    Right-click on that file, and select "Run as Administrator". Once the
    program starts, click on "Install" and browse to the freeglut devpak you
    downloaded. It should install correctly. 

    You can check to make sure by looking in the ``MinGW64/lib`` folder inside
    Dev-Cpp and make sure you see ``freeglut.dll`` in that folder.

3. Test your installation

    a. Create a new project

        * Select :menuselection:`Multimedia --> Freeglut`

    b. Compile and run the demo program. If it does not work, contact me for help.

MinGW-w64 PC Instructions
*************************

..  warning::

    This section is not needed if you are using either Dev-C++ or Code::Blocks)


I do most of my work on the command line, so I have set my systems up to be as
consistent as I can make them, so moving between all three major platforms is
less of a hassle.  The notes in this section show how I configured my Window 7
laptop so I can build graphics programs.

1. Create an Environment

   a. Both Mac and Linux install user tools in a folder named ``/usr/local``,
      so I create such a place on my PC systems. The easiest way to do this
      is to use the ``Windows Explorer`` tool to create new folders.

      You want to create these directories:

      ..  code-block:: text

            C:
            |
            +- usr/
                |
                +- local/
                    |
                    +- bin\
                    |
                    +- include\
                    |
                    +- lib\

   b. Add ``\usr\local\bin`` to the System PATH. This will let us drop simple
      programs into this folder so they can run from the command line.

   c. Install MinGW-w64. Download this file:

      - :download:`mingw-w64-install.exe`

      This is a network installer that will copy the files you need to your
      system. Run this program and let it install in the default location. Be
      sure to note where it ends up (in ``c:\Program Files
      (x86)\mingw-w64...``.

   d. I hate where this lands, the path is UGLY!. So I am going to copy the tools to a better place.

      Use ``Windows Explorer`` to find the installed tools, then copy the
      ``mingw32`` folder to ``C:\usr\local``. It should create a new ``mingw32``
      folder in that directory.

   e. Add ``C:\usr\local\mingw32\bin`` to your System PATH.

   f. Navigate to the new ``mingw32\bin`` and find the ``make`` program. It
      will be called ``mingw32-make``. Rename it to just ``make``. Test it to
      see that it works on the command line using this command:

      ..  code-block:: text

          $ make --version
          GNU Make 4.1
          ...
      

   f. Check that this works:

      ..  code-block:: text
          
          $ g++ --version
          g++ (i686-posix-dwarf-rev0, Built by MinGW-W65 project) 5.2.0
          ...

    g. Download freeglut from this link:

       - :download:`freeglut-MinGW-3.0.0-1.mp.zip` 

    h. This step is annoying, but makes life a bit easier later. Use ``Windows
       Explorer`` to extract all the files in this "zip" file. Inside this, you
       will find a "freeglut" folder with three subdirectories: ``bin``,
       ``include``, and ``lib``. You need to use ``Windows Explorer`` to copy
       the contents of each of those directories into the equivalent ``c:\usr\local\bin``,
       etc, folders. This takes a bit of time, but is easy enough to do.
    
          
Mac OS-X 
********

On my mac, I have installed :program:`XCode` and the `command line tools` that
are a part of that package. Although some developers prefer to use
:program:`XCode` to build their projects, I actually prefer to work on the
:term:`command line`, and this setup lets you do that. I have also installed
:program:`gcc` using Homebrew_, a good tool to install on your Mac that lets
you install additional tools easily.

With Homebrew_ installed, adding FreeGLUT is simple:

..  code-block:: text

    $ brew install freeglut
    
This will install all the header files and libraries needed for the projects in
this class. 

