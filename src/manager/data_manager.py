import pandas as pd
from src.data_handlers.data_interface import IRepository


class DataManager:

    def __init__(self: object, repository: IRepository) -> None:
        self.__repository = repository

    def change_repo(self: object, repository: IRepository) -> None:
        self.__repository = repository

    def execute(self: object) -> pd.DataFrame:
        return self.__repository.execute()
