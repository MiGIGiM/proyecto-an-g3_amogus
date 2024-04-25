from dataclasses import dataclass
import typing

@dataclass
class Dims:
    width: int
    height: int

@dataclass
class MethodInfo:
    disp: str
    slug: str

@dataclass 
class LatexSection:
    mode: str
    title: str
    data: typing.Any

    def __iter__(self):
        return iter((self.mode, self.title, self.data))