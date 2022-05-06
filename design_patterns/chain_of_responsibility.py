from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Optional
from unittest import result


class HandlerInterface(ABC):
    """
    The handler interface declares a method for building chaing of handlers.
    It also declares a method for executing a request
    """

    @abstractmethod
    def set_next(self, handler: HandlerInterface) -> HandlerInterface:
        pass

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass


class BaseHandler(HandlerInterface):
    """
    Default chaining behaviour
    """
    _next_handler: HandlerInterface = None

    def set_next(self, handler: HandlerInterface) -> HandlerInterface:
        self._next_handler = handler
        # returning a handler here will let us link handlers in a convinient way like this
        # cat.set_next(dog).set_next(monkey).set_next(goat)

        return handler

    def handle(self, request) -> Optional[str]:
        if self._next_handler:
            return self._next_handler.handle(request)
        return None


"""
All concrete handlers either handle a request or pass to the next handler in the chain
"""


class DogHandler(BaseHandler):

    def handle(self, request) -> Optional[str]:
        if request == "Meat":
            return f"Dog: I will eat the {request}."
        return super().handle(request)


class CatHandler(BaseHandler):

    def handle(self, request) -> Optional[str]:
        if request == "Milk":
            return f"Cat: I will drink the {request}."
        return super().handle(request)


class MonkeyHandler(BaseHandler):

    def handle(self, request) -> Optional[str]:
        if request == "Banana":
            return f"Monkey: I will eat the {request}."
        return super().handle(request)


def client_code(handler: HandlerInterface):
    """
    The client code is usually suited to work with a single handler.
    In most cases it is not even aware that the handler is part of chain.
    """
    for food in ["Meat", "Coffee", "Milk", "Banana", "Apple"]:
        print(f"\nClient: Who wants a {food}?")
        result = handler.handle(food)
        if result:
            print(f"[>]  {result}", end="")
        else:
            print(f"[X]  {food} was left untouched.", end="")


if __name__ == "__main__":
    monkey = MonkeyHandler()
    dog = DogHandler()
    cat = CatHandler()
    dog.set_next(cat).set_next(monkey)
    # the client should be able to send a request to any handler, not just the first one
    print(f"Chain: Dog > Cat > Monkey")
    client_code(dog)
    """
    Chain: Dog > Cat > Monkey

    Client: Who wants a Meat?
    [>]  Dog: I will eat the Meat.
    Client: Who wants a Coffee?
    [X]  Coffee was left untouched.
    Client: Who wants a Milk?
    [>]  Cat: I will drink the Milk.
    Client: Who wants a Banana?
    [>]  Monkey: I will eat the Banana.
    Client: Who wants a Apple?
    [X]  Apple was left untouched.
    """
    
    print(f"\nChain: Cat > Monkey")
    client_code(cat)
    """
    Chain: Cat > Monkey

    Client: Who wants a Meat?
    [X]  Meat was left untouched.
    Client: Who wants a Coffee?
    [X]  Coffee was left untouched.
    Client: Who wants a Milk?
    [>]  Cat: I will drink the Milk.
    Client: Who wants a Banana?
    [>]  Monkey: I will eat the Banana.
    Client: Who wants a Apple?
    [X]  Apple was left untouched.
    """

"""
# NOTE when to use ?
====================
    [>] Use the Chain of Responsibility pattern when your program is expected to process different kinds of requests in various ways, 
    but the exact types of requests and their sequences are unknown beforehand.

    The pattern lets you link several handlers into one chain and, upon receiving a request, “ask” each handler whether it can process it. 
    This way all handlers get a chance to process the request.

    [>] Use the pattern when it's essential to execute several handlers in a particular order.

    Since you can link the handlers in the chain in any order, all requests will get through the chain exactly as you planned.

    [>] Use the CoR pattern when the set of handlers and their order are supposed to change at runtime.

    If you provide setters for a reference field inside the handler classes, you'll be able to insert, remove or reorder handlers dynamically.



"""