..  _glossary:

Glossary
########

..  include::   /references.inc

..  glossary::
    :sorted:

    Domain Name
        Servers on the Internet are all part of some registered domain, which
        has a name associated with it. I own `pylit.org` for example. The last
        part is used to brand the kind of domain I am part of, in this case a
        non-profit organization. The first part is often chosen to identify the
        company involved. You can add a machine name to the front of this
        name. Often `www` is tacked on to identify a web server where the
        companies website is found.

    DNS
    Domain Name Service
        A phone book like service that maps domain names, like ``www.pylit.org``,
        to an IP address.

    DDNS
    DynDNS
    Dynamic DNS
        A service that updates :term:`DNS` tables used by Internet services to
        map domain names to addresses. These services are helpful if your
        network address changes often, as it might if you are working from home
        and want to set up a server.

    URL
    Uniform Resource Locator
        The specific location of a web "resource", which is normally a web
        page, but can be a file or anything that your browser can download to
        your system using the web protocol named `HTTP`. 

    Code of Conduct
        Every profession has a defined set of rules they expect members of that
        profession to follow. Most of the time, these rules are common sense,
        but they are defined to make sure every member understands what the
        profession seeks to present itself to the public. You are expected to
        know these rules and follow them when you join the profession. Look
        into each profession's primary organization for guidance. For computer
        folks, this is probably the `Association for Computing Machinery
        <http://www.acm.org>`_.


    Refactor
        Modify a programs code to improve its quality without changing how it
        works. This is a clean-up step in development designed to keep ugly
        code out of a project, and use best-practices in how code is presented.

    Comment
    Comments
        Short chunks of text added to program code that seeks to explain when
        is going on. Far too often, this text just repeats what the code
        actually says, making them useless. Comments should explain the "why" of
        a block of code.

    Shell
    Command Prompt
    Command Line
        The "old fashioned" way of controlling a computer. On Windows systems,
        this involves opening a window where you can type in commands. On Mac
        and Linux systems, you open up a :program:`Terminal` program.

    Directory
    Directory Tree
        The operating system on most computers, today, uses tree-like
        structure to store files.  The top of this tree, called the root of the
        tree, is a directory (or folder as Microsoft want us to call it). The
        name of this directory is either "/" on a Linux/Mac system, or "\" on a
        Windows system.

        A Directory is a container that can hold either files (objects that
        contain only data, such as text, images, of other binary data) or other
        directory objects (called subdirectories). Subdirectories have names
        that follow the rules for the operating system.  Any directory
        or subdirectory can hold files of further subdirectories, giving the
        entire file system a (upside down) tree-like structure.

    Parameter
    Parameters
        Values passed to a sub-program for it to use in it's work.

    Command Line 
        A simple text line on your screen where you can type in a
        command to the operating system.
 
    Command 
        A series of space-separated text items handed to the operating system.
        The first of these items is the name of some program (which may be
        internal to the operating system) you want to run. The rest of the
        items are called parameters which are processed by the program
        and control exactly what that program does. 

    Open-Source
        An open-source project is freely made available to the public in source
        code form. Such projects are usually protected by a license of some
        kind, designed to protect the rights of the author(s).

    OPC
    Other People's Code
        You should study code written by other folks, especially those who seem
        to do the job well. Eventually, you will learn how to write well
        respected code and become the author of what others read. Just make
        sure you give credit for anything you decide to incorporate into your
        projects, and respect the license that goes with the code.

    Problem Statement
        Every programming project should start with a problem statement that
        you analyze to see exactly what you are supposed to create. Your job is
        to create a solution to some problem. You may need to go to the
        originator of the statement to clarify things, and you should do this
        rather than guess at what is really wanted. 

    OOP
    Object Oriented Programming
        A design technique where the fundamental program components model
        objects from the real world the application is to serve.

    Old School
        The place where old methods were learned. These methods are any methods
        not accepted as modern by current workers.

    Side Effects
        Functions usually operate as self contained blocks of code. They get
        information from the outside world through the parameter list, and
        produce results that are returned to the caller as return values. If
        the function modifies anything in the outside world as it performs its
        task, these are called side effects. Generally, these are bad things,
        and should be avoided.

    Baby Step
    Baby Steps
        A software development process that focuses on making very small
        changes to your code, followed by a quick test using the compiler to
        make sure you can run your code, and a run that generates output you
        can inspect to see how your changes are working. The key to this is
        doing this sequence often.

    Blasting Code
    Blast Code
        An "old school" method of software development. This method
        involves long sessions of writing code with few attempts to test the
        code. The result is often long sessions fixing typing mistakes,
        followed by long sessions with a debugger trying to figure out why
        things do not work.

    Debugger
        A software development tool that is used to step a program one line at
        a time, then allows the developer to inspect the internal state of the
        machine as the program runs. They are a vital, and often under-used
        tool in programming.

    Syntax
        The formal rules that define how to write a construct in a particular
        programming language. These rules are simple and precise.

    Semantics
        A properly written programming language construct causes the computer
        to do something. Exactly what that something is is called the semantics
        of that construct. You must understand the semantics in order to make
        sure you use that construct properly. This is called picking the right
        tool for the job!

    Compile
    Compiler
    Compilers
        When we process a program written in a high-level programming language,
        the tool we use is called a compiler. That tool converts our
        program into the machine language the processor actually
        understands. We say we compile our programs.


    High-Level Language 
        Most programming languages are designed to help humans instruct a
        machine in how to solve some problem. These languages do not care what
        processor they will run on, and are called "machine independent".  You
        use a compiler designed to convert your high-level code into
        machine language for a particular processor. Different
        compilers support different machines.

    Drag and Drop
        A modern method of constructing programs, or executing commands by
        dragging an icon on the screen and dropping it onto another place.
        Learning how all of this works can make you highly productive!

    Execute
    Executes
    Executable
    Executable File
        In spite of the negative connotations of the term, we say a computer
        executes a program. The program that can be run is called
        executable.

    Link
    Linking
    Linker
        A phase in transforming your program into a final executable
        file where one or more `object files` are combined with system
        libraries` to build a final :term:`executable` file. The tool that does
        this work is called a linker.
        

    Unresolved Reference
    Unresolved References
        When you try to link your program and there are references to items
        that cannot be found, we say these are "unresolved references".
        The final executable file cannot be constructed in this case.
        System Library System Libraries Files containing code needed by a
        program to actually complete the transformation of a high-level
        language into machine language. In these libraries, we find
        code for input and output, code needed to interface with the
        operating system, etc.

    OS
    Operating System
        All general purpose machines need a piece of software to manage the
        hardware of the system. Typically, these programs provide a user
        interface to make controlling the machine simple. No on buys a system
        just for the OS. Instead, you pick an OS based on the
        applications you need to use to do real work (or play) on that system.

    Flow Chart
        A form of diagram showing the logic of a program. These diagrams have
        been around for almost as long as computers have been available. They
        are a great way (but not the only way) to visualize how your program
        will "flow" and think about what will happen when you run the program.

    Syntax
        This is a term referring to exactly what a statement in a programming
        language looks like when written in a program.

    Syntax Analysis
    Syntax Analyzer
        The process of examining each construct in your program to make sure it
        is properly formed. Only when this is true can the analysis tool move
        on the "semantic analysis" to figure out what each construct
        means. The tool that checks the syntax is called a "syntax
        analyzer", usually part of a compiler.

    System Library
        A file containing references needed by programs to connect to operating
        system of language specific functions.

    Syntax Diagram 
    Railroad Diagram 
        A visual representation of a rule in EBNF. These rules define
        the syntax of a language.

    Semantics
        This term refers to the meaning of a construct in a programming
        language. Only a construct that passes the syntax analysis
        phase of transformation has any meaning.

    Semantic Analysis
        The process of taking a properly formed construct in a programming
        language and converting it into another form the has the same meaning
        as the original construct. Typically, a tool like a compiler
        transforms your high-level code into machine language the
        processor can actually run.

    Hidden File
        Most operating systems "hide" file names that start with a dot ".".
        These normally contain configuration information that should not be
        modified unless you know what you are doing You need to use a special
        command to display these files when generating a directory list.

    Camel Case
        A naming convention where the name is made up of multiple words, each
        with the first letter capitalized, and spaces removed. For example:
        "CamelCase".

    Real World
        A fictitious place everyone claims exists. In this world things work
        perfectly (or at least better than in your present world!)

    Style Guide
        A document specifying the style to be used to projects in some
        organization. These guides lay out how program code should be
        presented, how variable names are formed, or how files should be
        organized to meet standards everyone in the organization will follow.
        Some of these guides can be extensive, others, very informal.

    reStructuredText
        A simple markup language designed to make documentation readable with
        no processing. Processing tools like SPhinx_ can turn documents written
        in this markup into HTML or PDF output that looks very nice!

    Professional Image
        You have an image on the Web. Like it or not, this image follows you
        everywhere, even into the first job interview. Are you proud of that
        image? May folks post the most outrageous junk on their FaceBook pages,
        thinking no one but their "Friends" look at it. Not so! Unfortunately,
        your potential employer might check you out and not like what they see.
        Your choice. I recommend making sure you look like someone others want
        to employ, or at least someone who does more with their lives than just
        keep everyone informed about every aspect of your life on FaceBook!
        YMMV!

    Gravatar
        A service that will provide your image when you log into a number of
        web sites. That image can be viewed by others to make sure they
        recognize the you they are communicating with. I consider using such a
        service part of setting up a :term:`professional image`.

    Avatar
        A graphical representation of a user. Often an image, but it can be a
        cartoon-like character as well. To make the web more personal (and less
        anonymous), sites like Gravatar_ help users show their chosen avatar on
        many web sites. I consider this usage part of setting up a
        professional image.

    Texas Four-Step
        All computer processors use a four step process to do their work. The
        four steps are called `Fetch`, `Decode`, `Execute`,
        and `Store` (or `Retire`.

    Execute
    Execution
        We call the act of actually processing something in a computer
        `executing` that something. The something can be a single
        `Machine Instruction`, or a complete program. We sure are a brutal
        race of beings!

    Home Directory
        Most operating systems create a directory you are to use for all of
        your files on that system. This directory is tied to the user account
        you log into when you access that system. On Windows, this is the
        directory where your "My Documents" folder is found, usually a place
        like ``C:\Users\username``. On Linux systems the directory will be in
        ``/home/username``. On Macs, it will be in ``/Users/username``.

    IDE
    Integrated Development Environment
    Integrated Development Environments
        A collection of common programmer's tools integrated into a single
        application with features that can greatly speed up program
        development. Unfortunately, typical IDE systems are complex and may not
        support all the languages you use, or be available on all the platforms
        you use.
        
    GUI
    Graphical User Interface 
        A user interface were the mouse and windows are
        used to control applications. 

    System path
        Most operating systems search for files to execute by examining
        directories listed in a system variable called the ``PATH``. 
        
    Script
        Programs designed to control computers are often called scripts. Most
        scripts are written using simple languages like `bash` on a Linux
        system or Python.

    Voltage
        This is a measure of the "force" driving electricity through a circuit.
        Think of pressure in a water pipe.

    Current 
        This is the flow of electrons through a circuit. Moving electrons
        generate heat and electromagnetic waves as a by-product of this motion.

    Environment Variable
    Environment Variables
        Named strings managed by the command line processor. These strings are
        available to programs and are commonly used to set up data for a
        variety of purposes. 

    data
        A set of bits in memory representing an encoded thing from our human
        world.    

    encoding
        Creating a way to figure out a particular human thing from a simple
        number. There should be a unique number for each unique thing from our
        world.

    refer
        To use a name when you want to manipulate a piece of data. The computer
        will figure out the actual memory address for the item based on the
        name.    

    variable name
        A human friendly name we pick to `refer` to a piece of data in
        memory.   

    literal data
        In your program, you can enter a series of text characters that
        represent the data item you want in your program. This text will be
        converted to internal binary form and used in your program.  

    keyword
        A word defined by the programming language. Most of the time, you
        should never try to use one of these words as the name of a data item
        in your program. Look for a list of these in the documentation for your
        programming language.

    address
        The location in memory where something is stored. Usually this is a
        simple number (index) into the memory.



..  vim: set filetype=rst spell
