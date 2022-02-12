from typing import Dict

import sqlalchemy
from abc import ABC, abstractmethod


class IRepository(ABC):

    def __init__(self: object, config: Dict) -> None:
        self._database = config.get('database')
        self._connection_string = config.get('connection_string')
        self._engine = None

    @abstractmethod
    def execute(self: object) -> None:
        pass

    def connect(self: object) -> None:
        if not self._engine:
            self._engine = sqlalchemy.create_engine(self._connection_string)
