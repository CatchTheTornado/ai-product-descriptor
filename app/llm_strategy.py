from abc import ABC, abstractmethod

class LLMStrategy(ABC):
    @abstractmethod
    def describe(self, image_url: str):
        pass