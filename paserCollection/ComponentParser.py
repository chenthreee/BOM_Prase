from abc import ABC, abstractmethod

class ComponentParser(ABC):
    @abstractmethod
    def parse(self, description):
        pass
