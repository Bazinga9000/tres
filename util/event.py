from dataclasses import dataclass
from typing import Callable, Self



@dataclass(frozen=True, eq=False) # hashing should be id-based, not value-based
class EventHandler[**P]:
    func: Callable[P, None]
    
    def __repr__(self):
        return f"EventHandler({self.func.__name__})"

class Event[**P]:
    def __init__(self):
        self._handlers: list[EventHandler[P]] = list()
    
    def subscribe(self, func: Callable[P, None]) -> EventHandler[P]:
        handler = EventHandler(func)
        self._handlers.append(handler)
        return handler
    
    def unsubscribe(self, handler: EventHandler[P]):
        if handler in self._handlers:
            self._handlers.remove(handler)
            return True
        return False
    
    def fire(self, *args: P.args, **kwargs: P.kwargs):
        for handler in self._handlers:
            try:
                handler.func(*args, **kwargs)
            except Exception as e:
                print(f"Error in event handler {handler}: {e}")
    
    def __call__(self, *args: P.args, **kwargs: P.kwargs):
        self.fire(*args, **kwargs)
    
    def __iadd__(self, func: Callable[P, None] | None) -> Self:
        if func:
            self.subscribe(func)
        return self
    
    def __isub__(self, handler: EventHandler[P]) -> Self:
        self.unsubscribe(handler)
        return self

def event[**P](func: Callable[P, None]) -> Event[P]:
    event = Event[P]()
    event += func
    return event
