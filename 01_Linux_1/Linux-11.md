# [Linux- Cron jobs]

A cron job is a Linux command used for scheduling tasks to be executed sometime in the future. This is normally used to schedule a job that is executed periodically – for example, to send out a notice every morning.

# Keywords:

The command for creating and editing cron jobs is the same and simple

$ crontab -e

cron Syntax:

A B C D E USERNAME /path/to/command arg1 arg2

OR

A B C D E USERNAME /root/backup.sh

Explanation of above cron syntax:

A: Minutes range: 0 – 59

B: Hours range: 0 – 23

C: Days range: 0 – 31

D: Months range: 0 – 12

E: Days of the week range: 0 – 7. Starting from Monday, 0 or 7 represents Sunday

USERNAME: replace this with your username

/path/to/command – The name of the script or command you want to schedule


## Opdracht

Exercise:

- Create a Bash script that writes the current date and time to a file in your home directory.
- Register the script in your crontab so that it runs every minute.
- Create a script that writes available disk space to a log file in ‘/var/logs’. Use a cron job so that it runs weekly.




### Gebruikte bronnen

https://crontab.guru/

https://www.tecmint.com/create-and-manage-cron-jobs-on-linux/


### Ervaren problemen


### Resultaat
1

![alt text](https://github.com/techgrounds/cloud-6-repo-rupaliBC/blob/main/00_includes/cron1.png)

![alt text](https://github.com/techgrounds/cloud-6-repo-rupaliBC/blob/main/00_includes/cron2.png)

![alt text](https://github.com/techgrounds/cloud-6-repo-rupaliBC/blob/main/00_includes/cron3.png)

textfile name should be timedate.txt

![alt text](https://github.com/techgrounds/cloud-6-repo-rupaliBC/blob/main/00_includes/cron4.png)

![alt text](https://github.com/techgrounds/cloud-6-repo-rupaliBC/blob/main/00_includes/cronn1.png)

![alt text](https://github.com/techgrounds/cloud-6-repo-rupaliBC/blob/main/00_includes/cronn3.png)

![alt text](https://github.com/techgrounds/cloud-6-repo-rupaliBC/blob/main/00_includes/cronn4.png)





