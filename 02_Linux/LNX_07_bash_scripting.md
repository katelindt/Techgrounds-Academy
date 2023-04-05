# Bash scripting

Scripting is used to automate the execution of the tasks (without performing them individually). Bash scripting is a great way to automate different types of tasks in a system. 

## Key terminology

- Script - a file, which contains a set of commands that the command shell will perform automatically in the given order.
- Bash "Bourne-Again SHell" - command language interpreter.
- Variable - a character string to which we assign a value.
- Path - PATH is an environmental variable in Linux and other Unix-like operating systems that tells the shell which directories to search for executable files (i.e., ready-to-run programs) in response to commands issued by a user.


## Exercise 1:

- Create a directory called ‘scripts’. Place all the scripts you make in this directory.
- Add the scripts directory to the PATH variable.
- Create a script that appends a line of text to a text file whenever it is executed.
- Create a script that installs the httpd package, activates httpd, and enables httpd. Finally, your script should print the status of httpd in the terminal.

## Exercise 2:

- Create a script that generates a random number between 1 and 10, stores it in a variable, and then appends the number to a text file.

## Exercise 3:

- Create a script that generates a random number between 1 and 10, stores it in a variable, and then appends the number to a text file only if the number is bigger than 5. If the number is 5 or smaller, it should append a line of text to that same text file instead.



### Sources

[http://www.linfo.org/path_env_var.html](http://www.linfo.org/path_env_var.html)

[https://askubuntu.com/questions/551990/what-does-path-mean](https://askubuntu.com/questions/551990/what-does-path-mean)

[https://stackoverflow.com/questions/1194882/how-to-generate-random-number-in-bash](https://stackoverflow.com/questions/1194882/how-to-generate-random-number-in-bash)

[https://ubuntu.com/server/docs/web-servers-apache](https://ubuntu.com/server/docs/web-servers-apache)


****

### Overcome challenges

Find out that on Ubuntu package is called apache2 (not httpd)


### Results
Created a directory called 'scripts'

![screenshot](/00_includes/linux_07_1_1_screenshot.png)

Added the scripts directory to the PATH variable

![screenshot](/00_includes/linux_07_1_2_screenshot.png)

![screenshot](/00_includes/linux_07_1_3_screenshot.png)

Created a script that appends a line of text to a text file whenever it is executed.

![screenshot](/00_includes/linux_07_1_4_screenshot.png)

![screenshot](/00_includes/linux_07_1_5_screenshot.png)

Created a script that installs the apache2 package, activates apache2, and enables apache2.

![screenshot](/00_includes/linux_07_1_6_screenshot.png)

![screenshot](/00_includes/linux_07_1_7_screenshot.png)

Created a script that generates a random number between 1 and 10, stores it in a variable, and then appends the number to a text file. Then created a script that makes the same but appends the number to a text file only if the number is bigger than 5. If the number is 5 or smaller, it append a line of text to that same text file instead.

![screenshot](/00_includes/linux_07_2_and_3_screenshot.png)

![screenshot](/00_includes/linux_07_2_screenshot.png)

![screenshot](/00_includes/linux_07_3_screenshot.png)

