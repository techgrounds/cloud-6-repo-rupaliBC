# [Linux Commannds]
[Linux uses files and folders, like you’re used to with any OS you’ve used. Folders in Linux are called directories, so use that word when looking for commands or information.
]

## Key-terms
1. pwd - Current working directory
2. ls- To list all files and directories
3. mkdir- to create new directory
4. cat - to create new file
5. cd - to change the path
## Opdracht
**

- Use the echo command and output redirection to write a new sentence into your text file using the command line. 
- The new sentence should contain the word ‘techgrounds’.
- Use a command to write the contents of your text file to the terminal. Make use of a command to filter the output so that only the sentence containing ‘techgrounds’ appears.
- Read your text file with the command used in the second step, once again filtering for the word ‘techgrounds’. This time, redirect the output to a new file called ‘techgrounds.txt’.




**
### Gebruikte bronnen


### Ervaren problemen


### Resultaat
1. cat > test.txt
My first file
2. echo " Welcome to techgrounds" >> test.txt
3. cat test.txt | grep "techgrounds"
4. cat test.txt | grep "techgrounds" > test1.txt
