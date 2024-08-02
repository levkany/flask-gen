from pathlib import Path
import os


class IFileEntity(object):
    def name(self):
        raise NotImplementedError("property `name` must be implemented")

    def create(self):
        raise NotImplementedError("method `create` must be implemented")

    def path(self):
        raise NotImplementedError("property `path` must be implemented")


class IWriteable:
    def write(self, text: str):
        raise NotImplementedError("method `write` most be implemeneted")


class FileEntity(IFileEntity):
    def __init__(self, path: str):
        super().__init__()
        self.__path = Path(path)
        self.__name = Path(path).name

    @property
    def path(self) -> Path:
        return self.__path

    @path.setter
    def path(self, path: Path) -> None:
        self.__path = path

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, val: str) -> None:
        self.__name = val

    def create(self) -> None:
        with open(str(self.path.absolute()), "w") as file:
            file.write("")


class File(FileEntity, IWriteable):
    def __init__(self, path: str):
        super().__init__(path)

    def write(self, text: str):
        self.path.parent.mkdir(parents=True, exist_ok=True)

        with open(self.path, "w", encoding="utf-8") as f:
            f.write(text)
