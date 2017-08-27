Course Topics
#############

An interesting way to visualize the topics we will be studying in this course
is something called a "MindMap", a tool designed to show how topics are broken
down into subtopics, and further broken down into subsubtopics. This way of
visualizing things helps show how topics are related.

The learning objectives for this course are given here:

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



To build the `mindmap`, we need to reduce these topics to a simpler form:

    1. Computer Hardware

    2. Program Development Tools

    3. Problem Solving

    4. Input and Output

    5. Designing Programs

    6. Basic Structures

    7. Using Functions

    8. Using Arrays


Here is the topic map we will follow:

..  circuits::
    :align: center
    :width: 600
    :tikzlibs: mindmap

    [root concept/.append style={concept color=blue!20, minimum size=2cm},
        level 1 concept/.append style={level distance=7cm, sibling angle=45},
        mindmap]
    \node [concept] {Programming\\Fundamentals}
        [clockwise from=90]
        child [concept color=red!50] {node [concept] {Hardware} 
            [clockwise from=170]
            child {node [concept] {Processor} }
            child {node [concept] {Memory} }
            child {node [concept] {Disk Drives} }
        }
        child [concept color=blue!50] {node [concept] {Dev\\Tools} 
            [clockwise from=100]
            child {node [concept] {Editors} }
            child {node [concept] {Compilers} }
            child {node [concept] {Debuggers} }
        }
        child [concept color=green!50] {node [concept] {Problem\\Solving} 
            [clockwise from=40]
            child {node [concept] {Logical\\Thinking} }
            child {node [concept] {Basic\\Strictures} }
            child {node [concept] {Pseudo\\Code} }
        }
        child [concept color=green!50] {node [concept] {Designing\\Programs}
            [clockwise from=0]
            child {node [concept] {Top-Down} }
            child {node [concept] {Baby Steps} } 
        }
        child [concept color=green!50] {node [concept] {Basic\\Structures}
           [clockwise from=-20]
           child {node [concept] {Sequence} }
           child {node [concept] {Decisions} }            
           child {node [concept] {Loops} }
        }
        child [concept color=red!50] {node [concept] {Input\\Output} 
            [clockwise from=10]
            child {node [concept] {Keyboard} }
            child {node [concept] {Screen} }
            child {node [concept] {Files} }
        }
        child [concept color=blue!50] {node [concept] {Functions} 
            [clockwise from=-40]
            child {node [concept] {Parameters} }
            child {node [concept] {Local\\Variables} }
            child {node [concept] {Return\\Values} }
            child {node [concept] {Testing} }
        }
        child [concept] {node [concept] {Arrays} 
            [clockwise from=-75]
            child {node [concept] {Dimensions} }
            child {node [concept] {Data} }
            child {node [concept] {Strings} }
        };
    
