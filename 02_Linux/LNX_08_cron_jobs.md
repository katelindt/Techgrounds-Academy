# Cron jobs

 Doing the same task over and over again can be quite a chore. Scheduling cron jobs let users automate tasks on a virtual private server or any Unix-like operating system. This saves precious time and allows users to focus on other essential tasks.


## Key terminology

 - Cron - daemon for repeating tasks at a later time.

 - Cron Job -  a task scheduled by script or command to run automatically at certain intervals.

 - Crontab - a file which contains the schedule of cron entries to be run and at specified times. 

- Commands: 
    - df - “disk filesystem“, is used to get a full summary of available and used disk space usage of the file system on the Linux system.

## Exercise

- Create a Bash script that writes the current date and time to a file in your home directory.
- Register the script in your crontab so that it runs every minute.
- Create a script that writes available disk space to a log file in ‘/var/logs’. Use a cron job so that it runs weekly.



### Sources

[https://ostechnix.com/a-beginners-guide-to-cron-jobs/](https://ostechnix.com/a-beginners-guide-to-cron-jobs/)

[https://medium.com/blockchain-research-lab-akgec/introduction-to-cron-job-ac04e72a4b67](https://medium.com/blockchain-research-lab-akgec/introduction-to-cron-job-ac04e72a4b67)

[https://crontab.guru/#*_*_*_*_*](https://crontab.guru/#*_*_*_*_*)

[https://opensource.com/article/18/7/how-check-free-disk-space-linux](https://opensource.com/article/18/7/how-check-free-disk-space-linux)

[https://unix.stackexchange.com/questions/127732/system-crontab-or-root-crontabhttps://unix.stackexchange.com/questions/127732/system-crontab-or-root-crontab](https://unix.stackexchange.com/questions/127732/system-crontab-or-root-crontab)


****

### Overcome challenges




### Results
Created a Bash script that writes the current date and time to a file in my home directory.

![screenshot](/00_includes/linux_08_1_screenshot.png)

![screenshot](/00_includes/linux_08_2_screenshot.png)

Registered the script in my crontab so that it runs every minute.

![screenshot](/00_includes/linux_08_3_screenshot.png)

![screenshot](/00_includes/linux_08_4_screenshot.png)

Created a script that writes available disk space to a log file in ‘/var/logs’. Used a cron job (changed in root's crontab) so that it runs weekly.

![screenshot](/00_includes/linux_08_5_screenshot.png)

![screenshot](/00_includes/linux_08_6_screenshot.png)

![screenshot](/00_includes/linux_08_7_screenshot.png)



