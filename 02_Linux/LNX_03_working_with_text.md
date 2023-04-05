# Working with text (CLI)

Input/output and redirection


## Key terminology

- Input/Output (I/O) redirection in Linux refers to the ability of the Linux operating system that allows us to change the standard input ( stdin ) and standard output ( stdout ) when executing a command on the terminal. By default, the standard input device is your keyboard and the standard output device is your screen.
- Pipe |  is used to combine two or more commands

- Commands: 
    
    - echo - display line of text/string that are passed as an argument. The echo can be used with a redirect operator to output to a file and not standard output.
    - cat - one of its most common usages is to print the content of a file onto the standard output stream. Other than that, the cat command also allows us to write some texts into a file.
    - grep - command-line tool used to search for a string of characters in a specified file. 


## Exercise
- Use the echo command and output redirection to write a new sentence into your text file using the command line. The new sentence should contain the word ‘techgrounds’.
- Use a command to write the contents of your text file to the terminal. Make use of a command to filter the output so that only the sentence containing ‘techgrounds’ appears.
- Read your text file with the command used in the second step, once again filtering for the word ‘techgrounds’. This time, redirect the output to a new file called ‘techgrounds.txt’.



### Sources

[https://www.educative.io/answers/how-to-do-input-output-redirection-in-linux](https://www.educative.io/answers/how-to-do-input-output-redirection-in-linux)

[https://opensource.com/article/18/8/introduction-pipes-linux](https://opensource.com/article/18/8/introduction-pipes-linux)

[https://www.digitalocean.com/community/tutorials/grep-command-in-linux-unix](https://www.digitalocean.com/community/tutorials/grep-command-in-linux-unix)


****



### Results

![screenshot](/00_includes/linux_03_screenshot.png)

