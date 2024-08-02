"""
this class is used to generate the actuall source directories and files
"""

from src.flask_gen.file import File
from typing import Dict
from pathlib import Path


class IGenerator:
    def load(self, struct: dict):
        raise NotImplementedError("load() must be implemented")

    def generate(self):
        raise NotImplementedError("generate() must be implemented")

    def root_dir(self):
        raise NotImplementedError("@root_dir property must be implemented")


class Generator(IGenerator):
    """loads a struct and generate the directories and files for it"""

    def __init__(self, struct: Dict[str, str] = None, root_dir: Path = None):
        super().__init__()
        self.struct = struct
        self.__root_dir = root_dir

    @property
    def root_dir(self):
        return self.__root_dir

    @root_dir.setter
    def root_dir(self, root_dir: Path):
        self.__root_dir = root_dir

    def load(self, struct: Dict[str, str]):
        self.struct = struct

    def generate(self):
        for file, data in self.struct.items():
            file = File(str(self.__root_dir.joinpath(file).absolute()))
            file.write(data)
