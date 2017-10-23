# Math 9 Introduction to Programming for Numerical Analysis 

Instructor: Peter McHale 

Course webpage: https://eee.uci.edu/17f/44600

## Getting set up (the software below is FREE!)

In what follows, you will need to access the 'command line'. 
On a Mac, this is done by opening the `Terminal` app. On the lab (Windows) machines,
this is done via `Start` -> `Anaconda Prompt` (type this into the search field to locate the program). 
Your TA will help you with this. 

If on your own machine, install Python and Jupyter by installing 
[Anaconda](https://www.continuum.io/downloads) (Python 3.x version).
 Anaconda conveniently installs Python, the Jupyter Notebook, and other commonly used packages for scientific computing.
Please 
[create a conda environment using Python 2.x](https://conda.io/docs/user-guide/tasks/manage-environments.html#creating-an-environment-with-commands) and [activate it](https://conda.io/docs/user-guide/tasks/manage-environments.html#activating-an-environment).
Your TA will help you with this.

If you are working at a lab computer, which already has Python and Jupyter installed, then 
type `python --version` at the command prompt to 
check the version of Python that is installed. It will hopefully say Python 2.x, which is what we will use in this course. 

Open a Jupyter notebook by navigating to the directory in which it is located (the `cd` command is useful here, 
as is the `ls` command in `Terminal` or equivalently, the `dir` command in Windows)
and typing `jupyter notebook` at the 
command prompt. 
A tab will open in your browser revealing the contents of the current directory. 
Seek out the TA for help.

Once you’re finished editing/running your notebook, press `ctrl-c`
twice at the command prompt.

If Jupyter complains that a specific package is missing when you 
run your notebook, then return to the command line, execute 
`conda install <name of package>`, and re-run the offending notebook cell. 

PLEASE BRING USB DRIVE TO LAB TO SAVE YOUR WORK.

## Acknowledgements 

This course is adapted from [Umut Isik's course](https://www.math.uci.edu/~isik/teaching/17W_MATH9/index.html)

## Book 
We will not be following a specific textbook in this course. 
However, if you would like to read a book to help you with the course, I recommend: 
[Scientific Computation: Python Hacking for Math Junkies](http://calculuscastle.com/pythonbook.html), by B. Shapiro.

## Schedule

If time permits, I will try to indicate relevant sections of Shapiro's book in the column entitled `Sections`.

Click on the links to see nbviewer-rendered versions of the lecture. 

|Wk|Date|Lec|Sections|Topics
|---|---|---|---|---
|0|9/29|1||[Markdown vs code cell, math operators, library functions, strings](http://nbviewer.jupyter.org/github/petermchale/math9/blob/master/lectures/Lecture01.ipynb)
|1|10/2|2||[Variables, types, functions](http://nbviewer.jupyter.org/github/petermchale/math9/blob/master/lectures/Lecture02.ipynb)
||10/4|3||[Tracking variables, graphing, if-else, comparisons, boolean ops](http://nbviewer.jupyter.org/github/petermchale/math9/blob/master/lectures/Lecture03.ipynb)
||10/6|4||[While loops, checking for primeness](http://nbviewer.jupyter.org/github/petermchale/math9/blob/master/lectures/Lecture04.ipynb)
|2|10/9|5||[Don't use == on floats, division with remainder case study](http://nbviewer.jupyter.org/github/petermchale/math9/blob/master/lectures/Lecture05.ipynb)
||10/11|6||[Checking primes more efficiently, Euclids Algorithm](http://nbviewer.jupyter.org/github/petermchale/math9/blob/master/lectures/Lecture06.ipynb)
||10/13|7||[Break and continue, lists](http://nbviewer.jupyter.org/github/petermchale/math9/blob/master/lectures/Lecture07.ipynb)
|3|10/16|8||[List comprehension, mutable vs. immutable](http://nbviewer.jupyter.org/github/petermchale/math9/blob/master/lectures/Lecture08.ipynb)
||10/18|9||[More on mutable vs immutable, selection-sort](http://nbviewer.jupyter.org/github/petermchale/math9/blob/master/lectures/Lecture09.ipynb)
||10/20|10||[Selection sort, algorithm complexity](http://nbviewer.jupyter.org/github/petermchale/math9/blob/master/lectures/Lecture10.ipynb)
|4|10/23|11||[Recursion](http://nbviewer.jupyter.org/github/petermchale/math9/blob/master/lectures/Lecture11.ipynb)
||10/25|12||Flattening lists with recursion, map, reduce, filter
||10/27|13||More functional programming methods, map, reduce, filter
|5|10/30|||Review of previous exams
||11/1||L1 - L13|Midterm Exam
||11/3|14||Classes
|6|11/6|15||Lists of lists, Numpy arrays, matplotlib
||11/8|16||More numpy and matplotlib, plot, showimg, apply along axis
||11/10||No class|Veterans’ Day
|7|11/13|17||More about slicing numpy arrays, working with images, historams
||11/15|18||Probability and randomness, random(), randomint
||11/17|19||Choice, mean and std of data-set, random simulations
|8|11/20|20||Random walks
||11/22|21||Law of large numbers and the central limit theorem
||11/24||No class|Thanksgiving
|9|11/27|22||Minimizing/maximizing functions, Gradient Descent
||11/29|23||Linear Regression
||12/1|24||Solving linear regression by gradient descent
|10|12/4|25||Singular Value Decomposition, Principal Component Analysis, Eigenfaces
|9|12/6|26||Matlab tutorial, key differences with Python
||12/8|27||Review of previous exams
|11|12/11||L1 - L27|Final Exam 10.30am – 12.30pm

