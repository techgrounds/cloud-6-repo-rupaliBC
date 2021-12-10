## Linux Processes

Processes in Linux can be divided into three categories: Daemons, Services, and Programs.
A daemon runs in the background and is non-interactive. A Service responds to requests from programs. A service may be interactive. A program is run and used by users (e.g. Vim).
In order to connect to remote Linux machines (virtual or not), you can use ssh (secure shell). To make this connection to your machine possible, you’ll have to start the ssh service by starting the ssh daemon.
A process is an instance of running code. All code is stored in files somewhere on the system. In order to find these files, Linux will look in the $PATH variable (more about that in a later exercise). Every process has its own PID (Process ID) number.


## Key-terms
- Process - A process is a running instance of a program.
- Services - Services responds to request which is coming from programs.
- Process ID - Process identifier, also known as process ID or PID, is a unique number to identify each process running in an operating system such as Linux, Windows, and Unix.
- SSH is the primary way to connect to remote Linux and Unix-like servers through the command line. It provides a secure connection that you can use to run commands, interact with the system.
- Daemon -  A daemon is a service process that runs in the background and supervises the system or provides functionality to other processes. These are specail types of background processes that start at system startup  and keep running forever as a service.They dont die.

## Opdracht
- Start the ssh daemon.
- Find out the PID of the ssh daemon.
- Find out how much memory the sshd is using.
- Stop or kill the sshd process.


## Gebruikte bronnen

https://www.cyberciti.biz/faq/howto-start-stop-ssh-server/

https://linux.die.net/man/1/pgrep

https://www.cyberciti.biz/faq/howto-display-process-pid-under-linux-unix/


## Ervaren problemen
## Resultaat
1. To start SSH daemon - sudo service ssh start

![alt text](https://github.com/techgrounds/cloud-6-repo-rupaliBC/blob/main/00_includes/startSSh.png)

2. To identify process id -  pgrep ssh   

![alt text](https://github.com/techgrounds/cloud-6-repo-rupaliBC/blob/main/00_includes/pidssh.png)

3. To find out how much memory ssh is using- pmap -x PID 

-x : This option is used to display the memory map in an extended format


![alt text](https://github.com/techgrounds/cloud-6-repo-rupaliBC/blob/main/00_includes/memory.png)

4. To stop the ssh service - sudo service ssh stop

![alt text](https://github.com/techgrounds/cloud-6-repo-rupaliBC/blob/main/00_includes/stop.png)

