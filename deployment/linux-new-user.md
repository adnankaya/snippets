
- If you are root user then do following steps. 
1. `adduser adnan` : Use the adduser command to add a new user to your system
2. `usermod -aG sudo adnan` : Use the usermod command to add the user to the sudo group
3. `su - adnan` : testing sudo access

## Generating SSH KEY for the user

```bash
ssh-keygen -t rsa -b 4096 -C "adnankayace@example.com"

```
- Copy .pub ssh key to the github ssh keys to access github repo

## Copying local PC SSH KEY into server .ssh/authorized_keys for accessing server new user(adnan)
1. Copy your local ssh key(.pub) under the .ssh folder
2. `nano .ssh/authorized_keys` and PASTE and save and exit.