..  _square-root-solution:

Solving the Square Root Problem
###############################

For most of you, solving the `Square Root` was not easy. It was not supposed to
be! You have probably not thought through problems in as much detail as this
requires, and that was the point. To express your `instructions` to a mindless
computer, you have to be very precise. The computer is not going to know what
to do, it will only do `exactly` what you tell it to do:

    Computers are insanely stupid. They are just stupid so fast, they look
    smart!

Typical Answers
***************

The two most common solutions I see go like this:

User guesses
============

You set up some kind of solution where the user enters a number, and you tell
them if they are right or wrong. 

This is not a `solution` at all. All you are doing is telling the user what the
square of the number they entered is, and leaving it to the user to figure out
if they guessed right.

Approach it Slowly
==================

You pick some very small number like 0.00000001, and sloooowly creep up on the
answer. You start at something like zero, multiply that times itself and see if
you have hit the number. If so quit. Otherwise, add your small number and try
again.

There are two problems with this approach.

    1. You are wasting a lot of time approaching the answer slowly.

    2. It is hard for a computer to hit the answer `exactly`. Computers do not
       do math they way humans might. Their math is limited in power and cannot
       express certain numbers accurately (like 1/3, for example!)

A Better Solution
*****************

There are many very good approaches to solving this problem. All involve doing
some simple task over and over again. We call that using a `loop` to solve the
problem.

Here is one idea:

Starting Guess
==============

Since our solution only needs to find the square root of a positive number,
let's begin finding the square root of some number `N` by guessing a starting
value of `N/2` as our starting point. Let's call our initial guess something
easy to remember. How about `guess`.

Starting Adjustment
===================

We also need to come up with a number to use to adjust our `guess` if it is not
right. This is like the second approach given earlier but we do not start with
a tiny number, we start with something simple, like one. We will call this
adjustment number `delta`.

Check your Guess
================

Evaluate `guess * guess` and compare that to `N`. Is the result too big? If so,
`guess` is too big. Is the result too small? If so, `guess` is not big enough.
In either case, we need to adjust our guess by adding (or subtracting) in our
`delta` and come up with a new value for `guess`.

Think about what we need to do if our `guess` is wrong. If we were too big, we
need to subtract something to make our `guess` smaller. If we were too small,
we need to add something to make our `guess` bigger. So, we have to ask a
question about what happened and decide which thing we need to do. This need to
make a `decision` is another common thing we have to do when writing programs!

Adjusting our Delta
*******************

When we started this process, we set `delta` to one, and probably found our
first `guess` was too small. So, we add `delta` to it and find out it is still
too small. We keep on `looping` adding `delta` to our `guess` until we find out
our value for guess is too big!

What now?
=========

Well, if we just subtract our current `delta` from our current `guess`, we will
just bounce back and forth between our last two values for `guess`. One is too
small, and one is too big! The answer is somewhere i the middle.

Let's cut our value for `delta` in half, and try again. This time when we find
the new place where one guess is too small and the next too big, we are going
to be closer to the answer than we were the last time. If we cut `delta` in
half again, and keep on doing this, eventually `delta` will be pretty durn
small, and we might decide we are `close enough`!

Stopping
********

We always need to be able to prove to ourselves that this process will
eventually stop. In our case, we will stop when the answer (our current value
for `guess` is as close as we need it to be. Engineers might pick something
like "within 000001 of the real answer". This is wrong in some sense, but not
so wrong it is not usable.

You are used to this if you have ever used a calculator. You can only see so
many digits on the calculator screen, and you are happy with that.

What Have We Learned?
*********************

What did we learn about solving this problem?

Well, creating a set of steps that can be followed precisely is a bit hard for
humans to do, but it gets easier with practice. Humans are notorious at
leaving "obvious" things out, but you cannot do that when designing a solution
for a computer. The computer will not fill missing steps in for you. Your steps
have to be clear and complete, and you have to convince yourself, by testing
them, that the steps actually give you the result you are after. That is a tall
order!

We also saw the three most important concepts in computer programming. They
are these:

    1. Do things in order, in a `sequence`. No skipping steps allowed in
       general.
    
    2. Repeat things in a `loop` if needed. We perform a set of steps over and
       over in a `loop`. Obviously, we need some way to stop this loop. In our
       example, we stop when we get an answer that is "close enough".

    3. We need to ba able to ask questions about what is going on. We need to
       make a `decision` that will change what we are going to do. In our
       example above, if our `guess` was too big we need to subtract something
       to get a better `guess`. If it was too small, we need to add something to
       get a better `guess`. `Decisions` in computer programming are always
       true/false questions. We will see more on that later.

Believe it or not, if you can master using these three most basic `constructs`
in any programming language you encounter, you can get a computer to solve real
problems for you. There is a bit more to understand, of course. We need to
figure out how to represent our problem in the computer in the first place, but
once we know how our data is being managed in the computer, we can set up a
sequence of `instructions` for the computer to follow to massage those data and
turn them into something more useful!

Welcome to the world of computer programming!


..  vim:filetype=rst spell:
