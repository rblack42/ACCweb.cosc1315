Compiling Graphics Projects in Xcode
####################################

It seems we get more students sporting Macs in school these days. I cannot
complain, my primary development systems are Macs, but I hardly ever use an IDE
to build my projects. I prefer working with command line tools, since I work on
remote servers all the time.

However, you do need to install Xcode to get anywhere building programs on the
Mac, so let's see if we can build a graphics project using Xcode.

Step 1: Fire up Xcode
*********************

Start the Xcode app.

Step 2: Create a Project
************************

Start a new project by clicking on :menuselection:`FIle -> New -> Project`.

In the box that opens up, click on :menuselection:`OS X -> Applications ->
Command Line Tool`, then click on `Next`.

Enter a name for your project. Something like "Graphics Test". Select ``C++``
as the language, and enter something line ``com.ACC.GraphicsTest`` as that
silly "Organization Identifier" (whatever that is!) Your user name will
probably be sitting in the "Organization Name" box.

Once this is set, click on ``Next``.

Save the Project
================

Next, you need to save this project somewhere on your system. Create a folder
for the project, then click on ``Create``.

Step 3: Add Your Files
***********************

You should be back in the IDE looking at a blank project with a default
``main.cpp`` file. Right-click on that file and select ``Delete``. We will
replace it in our next step.

Now, download the three test files from the lecture notes:

    * ``main.cpp``
    * ``Graphics.h``
    * ``Graphics.cpp``

..  note::

    Make sure your ``Graphics.h`` has lines that select the right header for
    your system. It should mention Windows, Linux, and Apple systems. If not,
    download the file again, I updated it recently to deal with all three
    systems in my classes!

Right-Click on the Project name at the top left ("Graphics Test" is what mine
shows). Click on ``Add Files to "Graphics Test"`` and add the three files you
downloaded.

Step 4: Configure for Graphics
*******************************

Now click on the project name again. This time you will see a menu with several
choices in the right panel. Click on ```Build Settings``. Click on ``Build
Phases``, then on ``Link Binary with Libraries``.

Click on the small plus symbol at the bottom of the box that opens. We need to
add three libraries from the list that pops up:

    * Cocoa.framework
    * GLUT.framework
    * OpenGL.framework

Step 5: Test Your Code
**********************

As soon as you have this step completed, you should be able to compile and run
your code. Click on :menuselection:`Product -> Run`` ans hopefully, you will
see the test image on the screen.

