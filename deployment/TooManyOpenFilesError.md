# Too Many Open Files Error

### How to Fix NGINX: Too Many Open Files Error

- By `ulimit` command we can see soft and hard limit values on our system

- ```bash
  myuser@ip-123:~$ ulimit -Hn #hard limit
  1048576
  myuser@ip-123:~$ ulimit -Sn #soft limit
  1024
  ```

- If you want to increase the limit shown by `ulimit -n`, you should:

  - Modify `/etc/systemd/user.conf` and `/etc/systemd/system.conf` with the following line (this takes care of graphical login):

    ```
     DefaultLimitNOFILE=65535
    ```

  - Modify `/etc/security/limits.conf` with the following lines (this takes care of non-GUI login):

    ```
    nginx           soft    nofile          65535
    nginx           hard    nofile          65535
    httpd           soft    nofile          65535
    httpd           hard    nofile          65535
    myuser       soft    nofile          65535
    myuser       hard    nofile          65535
    root            soft    nofile          65535
    root            hard    nofile          65535
    ```

  - Reboot your computer for changes to take effect.

##### Debian Specific

There is a bug in Debian. To increase `ulimit` you need to add this into the `/etc/pam.d/common-session` file:

```
session required pam_limits.so
```

and in `/etc/security/limits.conf` add:

```
*               soft    nofile          65535
*               hard    nofile          65535
```

Then reboot the system.

##### In some cases

As others have noted, raise the limit in `/etc/security/limits.conf` and also file descriptors was an issue for me personally, so I did

```py
sudo sysctl -w fs.file-max=100000 
```

And added to /etc/sysctl.conf:

```py
fs.file-max = 100000
```

Reload with:

```py
sudo sysctl -p
```





### Resources

- https://serverfault.com/questions/610130/how-to-set-ulimit-value-permanently/702074#702074
- https://stackoverflow.com/questions/16526783/python-subprocess-too-many-open-files/40270723#40270723
- https://superuser.com/questions/1200539/cannot-increase-open-file-limit-past-4096-ubuntu/1200818#1200818
- https://fedingo.com/how-to-fix-nginx-too-many-open-files-error/