..  _getting-started:

Getting Started
###############

..  include::   /references.inc

Welcome to COSC1315 Fundamentals of Programming. This course is designed for
beginners to programming, and for those who will not be pursuing advanced
programming courses. Since computers are such a fundamental part of our working
world, it is important that we all have at least a basic understanding of how
these machines are controlled, and how we can get them to do work for us.

Learning Objectives
*******************

    1.  Recognize basic computer hardware architecture constructs such as
    instructions sets, memory, CPU, external devices, and data representation.

    2.  Use programming software tools including compilers, linkers, editors, and
    integrated development environments to create and test programs.

    3.  Demonstrate problem solving skills by developing algorithms to solve
    problems incorporating the concept of variables and constants of basic data
    types in a computer program.

    4.  Utilize programming constructs which uses input and output devices for
    acquiring and displaying data including sequential files.

    5.  Create programming designs which includes step-by-step algorithms and desk
    checking to validate problem solutions.

    6.  Incorporate the use of sequential, selection and repetition control
    structures into the algorithms implemented as computer programs.

    7.  Demonstrate an understanding of structured design by implementing programs
    with functions and passing of parameters to solve more complex problems and to
    promote the concept of efficient use of code.

    8.  Design and implement programs using arrays.

Problem Solving
***************

We will explore problem solving techniques, and spend time working on our
thinking process. In order to use a computer to do your work, you have to be
very precise in how you explain things. The machine cannot use "common sense"
to fill in the missing details. For most humans, you are not used to that kind
of precision. We all assume others just know" what we mean, even if that if
often not true at all.

We need to analyze our problems, find a way to solve them, and then express
that solution process in a very clear manner if we ever hope to get a dumb
machine to do that work for us.

Course Textbook
***************

We are using a custom edition of two books for this course. The first part is
designed to teach you how to think through problems, and not how to program
using a modern programming language. 

We will use something called "pseudo-code", which is
much like structured English text, but short and crisp, to write down our
solution ideas! We are focusing on the solution steps when we write this
"pseudo-code" now worrying about explaining what is going on any more than
necessary. 

The first part of the book also shows a diagramming technique called "flow
charting" as a way to express your solution process.  That technique is very
old, and works reasonable well using pencil and paper, but who uses those
things anymore. We do not have a good computer tool to produce those diagrams,
so I am not going to require that you use "flow charts" in our class. Instead
you can fire up an editor and generate "pseudo-code"!

The second part of the custom text is an introduction to C++, one of the most
popular, and powerful, programming tools available. We will keep this part
simple, since the goal is to introduce you to programming, not turn you into
masters of that craft.

We will also use a tool called Scratch_ in our early assignments, to introduce
you to solving a few basic problems in a fun environment. We are not using
Scratch for playing games, although many folks do exactly that. Instead, we
will use it to explore the basic tools we use in solving problems. The problems
will be simple, and Scratch is fun to work with. Unfortunately, it is not a
real programming language tool, so later in the course we will switch to C++
and give you a basic look at that programming tool!


First Week Work
***************

This first week is an introduction. You should read the syllabus and the course
introduction (this page) completely. Then you should work through setting up
your personal machine so you can do the assignments. If you have any problems
getting set up, contact me immediately and we will figure out a solution. In
many cases, bringing your (hopefully portable) system in to my office will
solve things.

Readings on Blackboard 
======================

You should read the material in the textbook to get started:

    * Appendix A (Number Systems)

    * Appendix B (Problem Solving)

Important Notes on Assignments
******************************

You will submit a number of homework problems and lab assignments. Each
assignment will list exactly what needs to be submitted. In most cases, the
names on the files will be specified, be sure to name your files correctly.

Also, I want you to identify yourself on every file you submit. You should
include at least the following information:

    * Your name
    * The course this is for
    * The assignment this is for

You would be surprised at some things I see submitted. I have puzzled if the
material is even for my course at times!

..  warning::

    I may provide started code for some problems. The required identification
    lines will be present in those files, but they will include my name. If you
    submit work with my name in the file, I get the points for that assignment, not
    you! Pay attention to this!


What we will cover
******************

* This is a *Fundamentals* course! 

* We will introduce you to the idea that computers can be used to solve
  problems for us!  
  
    * if only we can figure out how to tell them how to do that.

* We will focus on the problem solving process

    * We will use C++ as an example language later in the course

What is a computer
******************

* Here is one I used to run:

..  image:: Cray1.png
    :align: center
    :height: 350


This is the first computer I got to work on when I went into the Air Force to
start my career - it is a Cray 1 Supercomputer that cost about $8,000,000 back
in 1973.

Here is another one
===================

* OK, this one is pretty small!

..  image:: Microcontroller.png
    :align: center

* It might live in a thermostat!


This one is something you could put in a thermostat you mount on the wall.  It
is called a `microcontroller`, but it is just another computer, only this one
costs less than a buck!

Actually a computer is a simple electronic device capable of manipulating a
bunch of switch-like components at incredible speeds, using a set of fairly
primitive commands that determine how those switches get changed.

Huh! That does not sound like a good definition of a computer - but it is!

We will look at the internals of a computer in one of our first lectures, but
they really are fairly simple machines. We are going to learn how to `program`
these beasts in this course.

What is a program
*****************

* Here is a typical listing :-)

..  image:: ProgramListing.png
    :align: center


This is a program listing that I might have produced when I was working on my
first Master's degree in Aerospace Engineering back in 1970.  Fortunately, no
one produces this kind of program listing anymore!

Modern programs
===============

    * Simply stated, a program is:
        * a simple (but very precise) list of instructions 
        * written in a language the computer can understand
         
    * These lists can be long (as the picture shows!) 

    * They can be written in many different programming languages
        * We will use one of the most popular ones - C++

    
Are computers smart?
********************

    * Contrary to what many people think, computers are just plain dumb!     
        
        * but, boy are they fast! 
    
    * We need to find a way to tell the computer exactly how we want it to
      solve our problems
        
        * then let it do the work for us!

My favorite saying
==================

    * Computers are dumb!

    * But they are dumb so fast, they look smart!

Using a computer to solve problems
**********************************

    * First, figure out how you would solve the problem

        * The solution needs to be very precise
        
        * This can be difficult at first, but you will learn how to do it!
    
    * Translate that process into something the computer can perform
        
        * Program code written in some programming language
    
    * Process that code into a form that the computer can run
    
    * Run the code to solve the problem!

The computer does not really know how to solve our problems, we need to figure
that out. So, we have two important things to deal with here. First, we have to
figure out how to solve our problems. Actually we need to learn how to figure
out how to solve problems - which is something else entirely!  Then we will
apply those methods to real problems and figure out how to solve them. Second,
we need to figure out how to explain to the computer what we want it to do to
solve our problem.

Why do I want to learn that?
****************************

    * Make you a better thinker

    * Help you learn how to solve all kinds of problems

    * Understand what computers can (and cannot) do

    * Make you a better worker (even if you never write another program)
 
        * The skills you learn here help you become more employable!
    
    * Perhaps hook you into learning more about computers!
    
        * My career path took a hard right turn when I did this!

Well, actually, many people think that learning about computer programming is
just a waste of their time! They would rather just buy a commercial computer
program that does the work they need done and be done with it.  That is fine
for a lot of the problems we want computers to work on for us.  But there comes
a time when no readily available computer program will do what you want done -
so you are stuck! You (or someone you can convince to do this for you - usually
after a transfer of cash) need to create a new computer program that will do
your new job. You are the person needing the work done, you are the `domain
expert` (we hope), and we hope you can figure out how to solve your problem
clearly enough to either create the program yourself, or explain the process to
the person who will. Learning how to do all of this is what this course is all
about. The skills you will learn will help you in your future career - even if
you never program a computer again. You will be a better thinker, and have a
better idea of the place computers have in your life and career.

Learning how to solve problems
==============================

* We will learn how to be very precise in how we explain things

    * especially those things we will eventually ask a computer to do for us. 
    
    * This takes patience and practice. 

* We need to overcome a common human trait
    
    * Depending on common experiences to fill in missing details
        
        * Remember, computers cannot do what you want them to do
        
        * The only do what you tell them to do!

Humans are notorious for leaving things out, and equally notorious for filling
in blanks (many times wrongly) when we deal with missing information. We cannot
let these things happen when we work on problems for the computer to solve.

Learning how to program
======================= 

* Start off by learning how to tear a problem apart into smaller pieces

    * We call this decomposition
    
    * We will use a few standard tools to do this

* Take these pieces and break them apart as needed until things are clear

* Translate your solution into a programming language

    * Process your code to find errors in the way you used that language

* Run your program to see if it solves the problem

    * Fix any errors in your thinking

* Sell your program and make millions (well, it is possible!)


Once we have a clear idea as to how we want to proceed to solve our problem, we
need to express the solution technique to the computer using a `programming
language` of some sort. Unfortunately, that language you will need to use to
create the program will not be English! We will need to learn to use one of
many available languages designed to explain things to computers. This can be
fun, but it is new, and learning new languages can be difficult for some of
you. Others will pick things up quickly. Do not worry about this, we will go
slowly and you should find yourself controlling a computer's actions in no
time!

My own path to programming
************************** 

* I never started off to be a programmer, I wanted to be an aeronautical engineer!

..  image:: Factory1.jpg
    :align: center


Heck, back when I first started college, computers were hidden away in large
buildings and only the chosen few were allowed to go near them.  Today, you
cannot get farther than a few feet from a computer wherever you go!

I had to work my way through college, since my parents could not afford to send
me to school. I entered a ''Cooperative Engineering Program'' where a student
could work in the industry they wanted to work in when they graduated- learning
about that area and earning money to pay for college.  We would go to school
one term, then work the next term all through college. It ended up taking five
years to complete a four year program, but I was able to earn enough to pay my
own way through school. 

I got a job with McDonnell Aircraft in St. Louis while they were building the
Gemini space capsules for NASA, and Phantom-II jets for the military. I got to
work at a number of exciting jobs over the years I worked there. It was an
amazing place to spend time, and it kept my interest level up so I did pretty
well in college. 

During one term, I was working in the Flight Test Division where they tested
the Phantom jets before delivering them to the Air Force and Navy.  My job that
term was to analyze data collected during a test flight. The data was recorded
on a paper tape by an instrument driven pen (remember, computers were new back
then), and on magnetic tape.  I was given a choice.  I could spend the term
measuring squiggles on the paper tape with a ruler, record the data, then
calculate a bunch of numbers with a mechanical calculator, or learn how to
program a computer to just process the magnetic tape.  Since the first process
sounded way too boring, I chose to try the second one - and my career working
with computers was off and running.

I had a ball that term, actually getting to place my hands on a real computer
for the first time, and working on problems that seemed very important at the
time. I was way ahead of my class mates in learning all this stuff, and I found
it a lot of fun. I want your first exposure to programming to be just as much
fun.

What do you need to know to start?
**********************************

    * Not much! 

    * This course does not assume you know much about computers

    * You should know the basics

        * How to use the file manager (Windows Explorer)
        
        * How to use the Internet
        
        * How to load new programs on your system
    
    * Do not worry if this is new to you, I will help!
    
        * Use email to get rapid help!

What are we going to do?
========================

    * This is a ``fundamentals`` course
    
        * we are going to look inside the computer a bit to see how it works

    * We will look at how humans express things in their world to the computer

    * We will explore those *languages* we spoke of earlier. 

    * We will practice our problem solving skills

    * Hopefully, we will work on some problems that are fun - not just boring
      add-up-a-bunch-of-numbers stuff!

        * That will come later in the course, after we get the basics down

Programming Tools
-----------------

    *  We will be analyzing several problems in this course

        * You will be using a graphical tool to start learning how to build programs

        * You will get to follow along as that logic is exercised

        * Then you will learn how to rethink things to get it right/better

Course Resources
**************** 

    * My notes will cover the important points

        * You should be reading the assigned chapters in the text as well

    * You will have homework problems and lab assignments from the text

        * I may add other work to make things a bit more interesting

    * I will use Blackboard to post grades. 
    
        * Distance students will submit work using Blackboard as well

Keep in touch
*************

    * I cannot help you if you do not talk to me. 

        * See me during office hours (or by appointment)
    
        * Send email as soon as you get into trouble doing the work
    
            * Any question is fair game.
        
            * How often you contact me counts as participation in the course!

    * I can meet with you  at most campuses if needed. My office hours usually
    * include times at two campuses each term. Check the syllabus for where I
    * will be this term.
      office hours

        * We can work out other times/places as needed

Have fun!
*********

    * My goal is to make this course fun

        * That is not the same thing as easy!

    * You do need to do the work

        * Do not let yourself fall behind!

    * We will learn a technique I call ``Baby Steps`` to do the work

        * Trust me - it will help get you through!


All during my career I asked folks I worked with, or who worked for me, to make
sure they were having fun in what they did. If you do not truly enjoy the work
you do, you will not find satisfaction in that one thing that you will spend a
great deal of your waking hours working on. It better be fun!  My job is to try
to make this course fun, and teach you something very useful in the process. I
would appreciate your help in tuning the course materials so we succeed in
learning and having fun at the same time!

..  vim:filetype=rst spell:

