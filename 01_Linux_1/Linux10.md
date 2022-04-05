# [Linux- Bash Script]
A Bash script is a series of commands written in a text file. You can execute multiple commands in a row by just executing the script.
Additional logic can be applied with the use of variables, conditions, and loops among others.

In order to be able to execute the script, a user needs to have permissions to execute (x) the file.
Linux will only be able to find the script if you specify the path name, or if you add the path to the directory in which the script lives to the PATH variable.
# Variables:
You can assign a value to a string of characters so that the value can be read somewhere else in the script.
Assigning a variable is done using ‘=’.
Reading the value of a variable is done using ‘$<insert variable name here>’.


## Key-terms

- Apache HTTPD is one of the most used web servers on the Internet. Apache HTTP Server is a free software/open source web server for Unix-like systems and other operating systems. A web server is a daemon that speaks the http(s) protocol, a text-based protocol for sending and receiving objects over a network connection


## Opdracht
## Exercise 1:
- Create a directory called ‘scripts’. Place all the scripts you make in this directory.
- Add the scripts directory to the PATH variable.
- Create a script that appends a line of text to a text file whenever it is executed.
- Create a script that installs the httpd package, activates httpd, and enables httpd. Finally, your script should print the status of httpd in the terminal.
 
## Exercise 2:
Create a script that generates a random number between 1 and 10, stores it in a variable, and then appends the number to a text file.

## Exercise 3:
Create a script that generates a random number between 1 and 10, stores it in a variable, and then appends the number to a text file only if the number is bigger than 5. If the number is 5 or smaller, it should append a line of text to that same text file instead.

### Gebruikte bronnen
https://linuxhint.com/30_bash_script_examples/#t26
https://linuxconfig.org/how-to-add-directory-path-to-path-variable
https://blog.eduonix.com/shell-scripting/generating-random-numbers-in-linux-shell-scripting/
### Ervaren problemen


### Resultaat
To add a directory to $PATH permanently, we’ll need to edit the .bashrc file of the user you want to change. Use nano or your favorite text editor to open the file, stored in the home directory.

At the end of this file, put your new directory that you wish to permanently add to $PATH.

export PATH="/bin/myscripts:$PATH"

![alt text](https://github.com/techgrounds/cloud-6-repo-rupaliBC/blob/main/00_includes/B1.png)

A script that appends a line of text to a text file whenever it is executed.

![alt text](https://github.com/techgrounds/cloud-6-repo-rupaliBC/blob/main/00_includes/bsh1.png)

![alt text](https://github.com/techgrounds/cloud-6-repo-rupaliBC/blob/main/00_includes/bsh2.png)

## Excercise 2:
Generating a random number between 1 and 10, stores it in a variable, and then appends the number to a text file.:
  
  ![alt text](https://github.com/techgrounds/cloud-6-repo-rupaliBC/blob/main/00_includes/ran.png)
  
  ![alt text](https://github.com/techgrounds/cloud-6-repo-rupaliBC/blob/main/00_includes/ran1.png)
  
## Excercise 3:
 
![alt text](https://github.com/techgrounds/cloud-6-repo-rupaliBC/blob/main/00_includes/ifrand1.png)
  

