from __future__ import annotations
from abc import ABC, abstractmethod

from click import command


class Command(ABC):
    """The command declares a method for executing a command"""
    @abstractmethod
    def execute(self) -> None:
        pass


class SimpleCommand(Command):
    """Some commands can implement simple operations"""

    def __init__(self, payload) -> None:
        self._payload = payload

    def execute(self) -> None:
        print(
            f"SimpleCommand: I can do simple operations. Like printing {self._payload}")


class ComplexCommand(Command):
    """However some commands can delegate more complex operations to other objects, called receivers"""

    def __init__(self, receiver: Receiver, a: str, b: str) -> None:
        """Complex commands can accept one or several receiver objects along with any context data"""
        self._receiver = receiver
        self._a = a
        self._b = b

    def execute(self) -> None:
        """commands can delegate to any methods of receiver"""
        print("ComplexCommand: complex operations should be done by a receiver object")
        self._receiver.do_something(self._a)
        self._receiver.do_something_else(self._b)


class Receiver:
    """receiver classes contain some important business logic. Any class may serve as a receiver."""

    def do_something(self, a: str) -> None:
        print(f"\nReceiver: Working on ({a}.)", end="")

    def do_something_else(self, b: str) -> None:
        print(f"\nReceiver: Also working on ({b}.)", end="")


class Invoker:
    """The invoker is associated with one or several commands. It sends a request to the command"""
    _on_start = None
    _on_finish = None

    def set_on_start(self, command: Command) -> None:
        self._on_start = command

    def set_on_finish(self, command: Command) -> None:
        self._on_finish = command

    def do_something_important(self) -> None:
        """The invoker does not depend on concrete command or receiver classes
        The invoker passes a request to a receiver indirectly, by executing a command.
        """
        print("Invoker: Does anybody want something done before I begin?")
        
        if isinstance(self._on_start, Command):
            self._on_start.execute()
        
        print("Invoker: ...doing something really important...")

        print("Invoker: Does anybody want something done after I finish?")
        
        if isinstance(self._on_finish, Command):
            self._on_finish.execute()


if __name__ == "__main__":
    """
    The client code can parameterize an invoker with any commands.
    """
    invoker = Invoker()

    invoker.set_on_start(SimpleCommand('say Hellooo'))

    receiver = Receiver()

    invoker.set_on_finish(ComplexCommand(receiver, "Send Email", "Save report"))

    invoker.do_something_important()

    """
    # NOTE output
    Invoker: Does anybody want something done before I begin?
    SimpleCommand: I can do simple operations. Like printing say Hellooo
    Invoker: ...doing something really important...
    Invoker: Does anybody want something done after I finish?
    ComplexCommand: complex operations should be done by a receiver object

    Receiver: Working on (Send Email.)
    Receiver: Also working on (Save report.)
    
    """