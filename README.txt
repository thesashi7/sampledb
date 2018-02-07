To use the MySQL from Python, please make sure the you have started the MySQL server. For example, on a Mac, the command is “mysql.server start”.

We are using the following defaults for our MySQL Server:
host=“localhost”
user=“root”
passwd=“password”

mysql -u root -h localhost -p
ENTER PASSWORD: password

Running main.py should work from there.

PLEASE NOTE: When creating and deleting tables, “GROUP” appears as a syntax error. As is such, we have changed the name of the table to “GROUPS”