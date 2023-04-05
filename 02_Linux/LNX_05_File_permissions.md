# File permissions
Setting and changing the permissions of the file.

## Key terminology

- Commands: 
    
    - chmod -command, which is used to manage file system access permissions on Unix and Unix-like systems.

    - chown (change owner) is used to  to change the file Owner or group. 

    - chgrp (change group) is used to change the group ownership of a file or directory.


## Exercise
- Create a text file.
- Make a long listing to view the file’s permissions. Who is the file’s owner and group? What kind of permissions does the file have?
- Make the file executable by adding the execute permission (x).
- Remove the read and write permissions (rw) from the file for the group and everyone else, but not for the owner. Can you still read it?
- Change the owner of the file to a different user. If everything went well, you shouldn’t be able to read the file unless you assume root privileges with ‘sudo’.
- Change the group ownership of the file to a different group.


### Sources

[https://linuxize.com/post/chmod-command-in-linux/](https://linuxize.com/post/chmod-command-in-linux/)

[https://www.geeksforgeeks.org/chown-command-in-linux-with-examples/](https://www.geeksforgeeks.org/chown-command-in-linux-with-examples/)

[https://www.geeksforgeeks.org/chgrp-command-in-linux-with-examples/](https://www.geeksforgeeks.org/chgrp-command-in-linux-with-examples/)


****

### Overcome challenges 

The syntax for permissions

### Results

![screenshot](/00_includes/linux_05_screenshot.png)

