# Users and groups


## Key terminology

- User - an entity, that can manipulate files and perform several other operations.

- Root - the superuser account in Unix and Linux. It is a user account for administrative purposes, and typically has the highest access rights on the system. The root user always have the User ID 0.


- Commands: 
    - sudo - "substitute user do" or "super user do" and it allows you to temporarily elevate your current user account to have root privileges.
    - useradd - a command which creates a new user or sets the default information for new users.
    - cat - one of its most common usages is to print the content of a file onto the standard output stream. Other than that, the cat command also allows us to write some texts into a file.



## Exercise
- Create a new user in your VM. 
    - The new user should be part of an admin group.
    - The new user should have a password.
    - The new user should be able to use ‘sudo’
- Locate the files that store users, passwords, and groups. - See if you can find your newly created user’s data in there.




### Sources

[https://www.beyondtrust.com/blog/entry/unix-linux-privileged-management-should-you-sudo](https://www.beyondtrust.com/blog/entry/unix-linux-privileged-management-should-you-sudo)

[https://www.tecmint.com/add-users-in-linux/](https://www.tecmint.com/add-users-in-linux/)

[https://www.cyberciti.biz/faq/linux-set-change-password-how-to/](https://www.cyberciti.biz/faq/linux-set-change-password-how-to/)


****

### Overcome challenges

I made it more challenging for me and found how and in what form the password for the user is stored.


### Results
I added new user named katya, checked that I can log in, checked my newly created user's password is in there
![screenshot](/00_includes/linux_04_1_screenshot.png)
Checked my newly created user's group is in there
![screenshot](/00_includes/linux_04_2_screenshot.png)
The last line shows the password I created for the user in encrypted form
![screenshot](/00_includes/linux_04_3_screenshot.png)

