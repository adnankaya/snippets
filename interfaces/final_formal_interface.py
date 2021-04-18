from abc import ABCMeta, abstractmethod

class IPerson(metaclass=ABCMeta):
    '''A formal interface definition '''
    @classmethod
    def __subclasshook__(cls, subclass):
        return (
            hasattr(subclass,'get_email')and
            callable(subclass.get_email)and
            hasattr(subclass,'send_greeting')and
            callable(subclass.send_greeting)or
            NotImplemented
        )
    
    @abstractmethod
    def get_email(self, fname:str, lname:str, domain:str) -> str:
        raise NotImplementedError
    
    @abstractmethod
    def send_greeting(self, greeting:str) -> str:
        raise NotImplementedError


class Employee(IPerson):
    def get_email(self, fname, lname, domain):
        return f"{fname}.{lname}@{domain}"
    def send_greeting(self, greeting):
        return f"Hey, {greeting}"
class Friend(IPerson):
    def get_email(self, fname, lname, domain):
        return f"{fname}.{lname}@{domain}"
    def send_greeting(self, greeting):
        return f"Hey, {greeting}"
    # pass
try:
    e = Employee()
    f = Friend()
    print("It Worked ^-^ ")
except Exception as e:
    raise e