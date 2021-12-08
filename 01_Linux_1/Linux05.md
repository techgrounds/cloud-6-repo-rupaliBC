# [Linux]
[Linux has users, similar to accounts on Windows and MacOS. Every user has their own home directory. Users can also be part of groups.
There is a special user called ‘root’. Root is allowed to do anything.
To gain temporary root permissions, you can type ‘sudo’ in front of a command, but that only works if you’re allowed to do that.]

## Key-terms
1. 
## Opdracht


-  Create a new user in your VM. 
-  The new user should be part of an admin group that also contains the user you created during installation.
-  The new user should have a password.
-  The new user should be able to use ‘sudo’
-  Locate the files that store users, passwords, and groups. See if you can find your newly created user’s data in there.




### Gebruikte bronnen

### Ervaren problemen


### Resultaat
1. sudo adduser user1
2. password
3. retype password
4. groups user1
5. sudo su
6. usermod -aG sudo user1
7. cat /etc/passwd




