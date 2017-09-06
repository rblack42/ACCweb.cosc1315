..  _data-types:

Storing Data in a Computer
##########################

..  seealso::   Text: Chapter 2: 2.2-2.5

We looked briefly at how computers store data in the memory of the machines.
Some folks like to say this::

    It is all zeros and nes inside the machine!

In fact, this is almost right! There really are no zeros or ones anywhere in
the machine. Instead there are `voltages` we interpret as zeros or ones. Thank
the electronics engineers for dealing with that problem!

We encode data in simple ways. We assign binary codes to each kind of data we
want to manipulate. Almost all computer programming languages support a simple
set of standard kinds of data:

    * Unsigned (positive) integers (with no decimal point)

    * Signed (positive or negative integers (with no decimal point)

    * Floating point (fractional data)

    * Characters (simple letters from the keyboard)

    * Boolean (true/false only)

Data Types
**********

We call these kinds of data `data types`. It is important to realize that the
encoding for each different kind of data is different. If the computer looks at
an encoding, it really cannot tell what kind of data it is looking at. It is up
to the `program` to make sure you are manipulating those data properly.

Think about it. What does it mean to multiply the letter `A` by the letter `Q`?
To the computer, those letters are stored in the machine as codes which are
just numbers. The computer knows how to multiply numbers! But to us,
multiplying those two letters is probably meaningless, so we cannot interpret
the resulting number in any meaningful way! Good programming languages protect
us against such silliness!

We can build up more complex things by storing multiple copies of these standard
`data types`. We call these more complex data containers `data structures`. For
now, let's keep things simple.

Variables
=========

We create containers to hold our data. In most languages, you have to `declare`
these containers before you can use them. Part of the `declaration` process
involves telling the computer how big the container should be, and what
`operations` are legal for that kind of data. The language processor will make
sure you do not do silly things. (Unless you really want to see "A" * "Q"!)

We call these `containers` `variables` because the actual value we store in
that container can change as processing takes place.

`Variables` are always named by the programmer. The name chosen must follow
some simple rules, and it really should help the reader of the program
understand what the variable is all about. `max_value` is a much better name
that `x24c`. (Unless you are actually working on the NASA X24C, which was a
research vehicle that looked like the Space Shuttle, long before they built
that vehicle!)

Constants
=========

Some values should not be allowed to change while processing takes place. These
containers will be marked as `constants` which tells the computer not to mess
with the value stored there. Things like the standard math value for `pi`
(3.1415926...) would logically be treated as a constant.

Note that it is important that you tell the computer to treat certain
containers as constants. The computer really has no idea what `pi` is, or why
it should not change. Only you know that!

How Big Can Nembers Be?
***********************

There is one huge issue with working with numbers in a computer. The computer
can only hold numbers of some fixed size. As an example, let's say we use 8
bits (binary digits) to store a number. How big can that number be?

Well, according to our rules for forming binary numbers that is this:

..  code-block:: text

    1 * 2^0 = 1
    + 1* 2^1 = 2
    + 1 * 2^2 = 4
    + 1 * 2^3 = 8
    + 1 * 2^4 = 16
    + 1 * 2^5 = 32
    + 1 * 2^5 = 64
    + 1 * 2^6 = 128
    ---------------
    255

An easier way to figure this out is this:

..  code-block:: text

    N = 2^(number of bits used) -1
      = 2^8 -1
      = 256 - 1 = 255

Not a very big number, is it. If we use 32 bits, we can store a number around 4
billion. Much better.

Manuals for language processing tools will tell you how big the numbers can be
for the different data types. It is up to the programmer to decide how big the
numbers can be, and how big a container is needed. That is something we will
look at when we study at a real programming language later in the course.

BTW, I suspect storing the number of students only needs a few bits. I doubt
that I will ever see a class with 4 billion students! However, those Massive
online Courses do get to tens of thousands of students! Yikes! Who is going to
grade all that work. Guess who! Computers!


