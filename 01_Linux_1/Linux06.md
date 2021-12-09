## Linux Commands for file permissions
Every file in Linux contains a set of permissions. There are separate permissions for reading, writing, and executing files (rwx). There’s also three types of entities that can have different permissions: the owner of the file, a group, and everyone else. Root does not need permissions to read, write or execute a file.
You can view a file’s permissions by creating a long listing. A file’s permissions, as well as its owner and group, can be changed as well.
Any user listed in /etc/passwd can be assigned as owner of a file.
Any group listed in /etc/group can be assigned as the group of a file.


## Key-terms

1. owner – The Owner permissions apply only the owner of the file or directory, they will not impact the actions of other users.
2. group – The Group permissions apply only to the group that has been assigned to the file or directory, they will not effect the actions of other users.
3. all users – The All Users permissions apply to all other users on the system, this is the permission group that you want to watch the most.
4. read – The Read permission refers to a user’s capability to read the contents of the file.
5. write – The Write permissions refer to a user’s capability to write or modify a file or directory.
6. execute – The Execute permission affects a user’s capability to execute a file or view the contents of a directory.
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
https://www.pluralsight.com/blog/it-ops/linux-file-permissions

https://www.linux.com/training-tutorials/understanding-linux-file-permissions/


### Ervaren problemen


### Resultaat
1. cat > newfile1.txt
This is a new file

![alt text](https://user-images.githubusercontent.com/95618055/145082904-93a6a6ca-f285-456b-a487-cdd919e93440.png)
2. ls -l
3. chmod u+x newfile1.txt
4. chmod g-rw newfile1.txt
5. chown rupali newfile1.txt
6. groupadd grp1
7. chown :grp1 newfile.txt
