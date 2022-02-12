from typing import Dict
from src.data_handlers.data_interface import IRepository
import pandas as pd


class DataLoader(IRepository):

    def __init__(self: object, config: Dict) -> None:
        super().__init__(config)
        self.__full_file_path = config.get('full_file_path')

    def execute(self: object) -> None:
        if not self.__full_file_path:
            raise Exception('Full File Path is a must')
        df = self.load_json_file_as_df(self.__full_file_path)
        self.load_to_database(df)

    def load_json_file_as_df(self: object, full_file_path: str) -> pd.DataFrame:
        print('Json file converted to df')
        df = pd.read_json(full_file_path)
        df = df.dropna()
        return df

    def load_to_database(self: object, df: pd.DataFrame) -> None:
        self.connect()
        print('Loading to postgres...')
        df.to_sql(self._database, con=self._engine,
                  index=0, if_exists='replace')
        print(f'{df.shape[0]} registers loaded!')
