### MySQL server reset root password
- ERROR 1698 (28000): Access denied for user 'root'@'localhost' at Ubuntu 18.04
- **solution**: 
`sudo mysql -u root` 
 `ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'new-password';`