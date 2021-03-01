"""
A mixin is a special kind of multiple inheritance. There are two main situations where mixins are used:

1.You want to provide a lot of optional features for a class.
2. You want to use one particular feature in a lot of different classes.

"""


class Logger():
    def __init__(self):
        self.title = ''

    def log(self):
        print(f"Log message from {self.title}")


class Connection():
    def __init__(self):
        self.server = ''

    def connect(self):
        print(f"Connecting to database on {self.server}")


class SQLDatabase(Connection, Logger):
    def __init__(self):
        self.title = 'SQL connection demo'
        self.server = 'Awesome_Server'


class JustLogging(Logger):
    def __init__(self):
        self.title = 'just log me'

def framework(item):
    if isinstance(item, Connection):
        item.connect()
    if isinstance(item, Logger):
        item.log()


sql_db = SQLDatabase()
just_log = JustLogging()
framework(sql_db)
print("-----------------------")
framework(just_log)
