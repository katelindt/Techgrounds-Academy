# Setting up

Connecting to Linux VM


## Key terminology
- Linux - a family of open-source operating systems that use the same kernel
- CLI - command line, where a program can be controlled through entered commands.
- GUI - grafical user interface, which contains dashboards where a program can be controlled
- VM - virtual Machine, an operating system that runs on its own on top of another hosting operating system and uses a separate part of the hardware resources.
- SSH - Secure Shell is a network communication protocol that enables two computers to communicate and share data.

## Exercise
- Make an SSH-connection to your machine. SSH requires the key file to have specific permissions, so you might need to change those.
- When the connection is successful, type whoami in the terminal. This command should show your username.



### Sources

[https://phoenixnap.com/kb/ssh-to-connect-to-remote-server-linux-or-windows](https://phoenixnap.com/kb/ssh-to-connect-to-remote-server-linux-or-windows)

[https://askubuntu.com/questions/1111994/login-with-ssh-authorized-key-with-changed-ssh-port](https://askubuntu.com/questions/1111994/login-with-ssh-authorized-key-with-changed-ssh-port)

****

### Overcome challenges

I forgot to change permissions of the key but I quickly realized and corrected this mistake.

### Results

![screenshot](/00_includes/linux_01_screenshot.png)


ssh -i pemfile-location username@ipaddress -p portnumber where

i is the identity file(file from which the identity key or the private key is read for public key authentication)

-p - port to connect to remote server

username - account used to login to the server

ip address - ip address of the remote server.
