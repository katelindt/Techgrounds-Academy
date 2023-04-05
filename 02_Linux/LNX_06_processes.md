# Processes

## Key terminology

- Process - a task that your machine is currently working on.
- Service - a process that runs in the background and accepts requests from different programs.
- Daemon - a process that runs in the background to maintain the processes that run in the foreground. It needs no interference from the user.
- Telnet - a protocol that allows connection between a system and another remote system. The data being transfered through Telnet is not encrypted, and therefore it's an insecure connection.
- PID - the identification number of a process in Linux.


- Commands: 
    
    - apt - a powerful command-line tool, which works with Ubuntu's Advanced Packaging Tool (APT) performing such functions as installation of new software packages, upgrade of existing software packages, updating of the package list index, and even upgrading the entire Ubuntu system.
    - systemctl (system control) command which is used to examine and control the status of the system and service manager.
    - ps - a tool to monitor processes running on your Linux system. A process is associated with any program running on your system, and is used to manage and monitor a program's memory usage, processor time, and I/O resources..
    - grep - command-line tool used to search for a string of characters in a specified file. 


## Exercise
- Start the telnet daemon.
- Find out the PID of the telnet daemon.
- Find out how much memory telnetd is using.
- Stop or kill the telnetd process.




### Sources
[https://en.wikipedia.org/wiki/Telnet](https://en.wikipedia.org/wiki/Telnet)

[https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6/html/security_guide/sect-security_guide-tcp_wrappers_and_xinetd-xinetd](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6/html/security_guide/sect-security_guide-tcp_wrappers_and_xinetd-xinetd)

[https://linuxways.net/ubuntu/how-to-install-telnet-server-and-client-on-ubuntu/](https://linuxways.net/ubuntu/how-to-install-telnet-server-and-client-on-ubuntu/)

[https://stackoverflow.com/questions/22372960/is-this-explanation-about-vss-rss-pss-uss-accurate](https://stackoverflow.com/questions/22372960/is-this-explanation-about-vss-rss-pss-uss-accurate)


****

### Overcome challenges

In Ubuntu it is impossible to run the telnet service directly, so I used the inetd service



### Results

![screenshot](/00_includes/linux_06_screenshot.png)

The PID of the telnet daemon is 8494 and it's using 2080K of memory.
