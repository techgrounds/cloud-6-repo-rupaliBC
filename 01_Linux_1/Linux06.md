 [Linux Commannds]
Every file in Linux contains a set of permissions. There are separate permissions for reading, writing, and executing files (rwx). There’s also three types of entities that can have different permissions: the owner of the file, a group, and everyone else. Root does not need permissions to read, write or execute a file.
You can view a file’s permissions by creating a long listing. A file’s permissions, as well as its owner and group, can be changed as well.
Any user listed in /etc/passwd can be assigned as owner of a file.
Any group listed in /etc/group can be assigned as the group of a file.


## Key-terms
1.
## Opdracht
**

- Create a text file.
- Make a long listing to view the file’s permissions. Who is the file’s owner and group? What kind of permissions does the file have?
- Make the file executable by adding the execute permission (x).
- Remove the read and write permissions (rw) from the file for the group and everyone else, but not for the owner. Can you still read it?
- Change the owner of the file to a different user. If everything went well, you shouldn’t be able to read the file unless you assume root privileges with ‘sudo’.
- Change the group ownership of the file to a different group.




**
### Gebruikte bronnen


### Ervaren problemen


### Resultaat
1. cat > newfile1.txt
This is a new file
2. ls -l
3. chmod u+x newfile1.txt
4. chmod g-rw newfile1.txt
5. chown rupali newfile1.txt
6. groupadd grp1
7. chown :grp1 newfile.txt
