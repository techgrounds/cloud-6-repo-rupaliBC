# [Linux Commannds]
Every command in Linux has a standard input and output.
The standard input (stdin) is the keyboard. If I run ‘mkdir myfolder’, the mkdir command will know what folder to create, because I typed ‘myfolder’.
The standard output (stdout) is the terminal. The command ‘echo hello’ will write ‘hello’ in the terminal.

Both the input and output can be redirected to a file instead of the default. This is called input redirection and output redirection. 
A pipe can be used to have the output of one command be the input of another command.

## Key-terms
1. echo command in linux is used to display line of text/string that are passed as an argument . This is a built in command that is mostly used in shell scripts and batch files to output status text to the screen or a file.
2. Grep is a Linux / Unix command-line tool used to search for a string of characters in a specified file. The text search pattern is called a regular expression. When it finds a match, it prints the line with the result. The grep command is handy when searching through large log files.
## Opdracht
**

- Use the echo command and output redirection to write a new sentence into your text file using the command line. 
- The new sentence should contain the word ‘techgrounds’.
- Use a command to write the contents of your text file to the terminal. Make use of a command to filter the output so that only the sentence containing ‘techgrounds’ appears.
- Read your text file with the command used in the second step, once again filtering for the word ‘techgrounds’. This time, redirect the output to a new file called ‘techgrounds.txt’.




**
### Gebruikte bronnen
https://phoenixnap.com/kb/grep-command-linux-unix-examples#:~:text=Grep%20is%20a%20Linux%20%2F%20Unix,searching%20through%20large%20log%20files.

### Ervaren problemen


### Resultaat
1. cat > test.txt
My first file
2. echo " Welcome to techgrounds" >> test.txt
3. cat test.txt | grep "techgrounds"
4. cat test.txt | grep "techgrounds" > test1.txt
