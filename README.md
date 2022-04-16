# Interpreted-Programming-Language-Version-1
Interpreted Programming Language using Python 3 as an Interpreter.

Purpose: Resume


How to use: 

To run the interpreter,... 

1). Start by running the AnthemOS.py file. 
2). You will then be asked to run a program, type in the name of a program file in the Programs folder located about the AnthemOS.py file.
3). The selected program will then run.


To make a program,...

1). Start by creating a .txt file and name it the whatever you want to call he program. 
2). Using the Documentation.txt as a reference for the syntax write your code into .txt file.
3). Save the file and its good to run.

How it works:

This program was my first attempt at writting and developing a custom programming language. To accomplish this I wrote an interpreter using Python 3 which would read .txt files and process them as if they were code. It does this by reading in the contents of the .txt file and running any autorun code, which assigned starting variables, and takes any procedures and creates references in the memory to it for future use. The code acts like an interpreted programming language in that it runs line by line and does not compile before runnning. The language and syntax is meant to be a cross between Python 3, 8086 Assembly and C#, with the language taking bits and pieces of each language into self. 

Notable Things:

Because this program is using Python 3 as an interpreter and is using .txt files to hold the code is allowed for the programs to self modify during the running of the code. What this means is if file A.txt has some code which can run and add / or change code to a .txt file and this file A.txt targets file A.txt then it code modify its own code and then tell the interpreter to rerun itself from where it left off and the program could have fundimentally changes itself or corrected an error that it encountered. This change that was made would be permanent and visable to the user if they check the .txt file after the fact.

This allows for the langauge to have error corrections build into the program its self where is a user makes a typo or a syntax error the code could correct it automatically during runtime or pause the code and prompt the user to type what was meant to be there and then the code will continue from where it left off. Meaning students who are learning to program could use this as a learning tool which can stop at an error, say what the error is, give possible solutions, let the student enter what they meant and then continue as if it didn't happen. 
