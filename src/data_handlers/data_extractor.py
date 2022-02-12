import pandas as pd
from src.data_handlers.data_interface import IRepository


class DataExtractor(IRepository):

    def fetch_db(self: object) -> pd.DataFrame:
        self.connect()
        print(f'Extracting data from {self._database}. Please, wait...')
        df = pd.read_sql_table(self._database, con=self._engine)
        return df

    def execute(self: object) -> None:
        df: pd.DataFrame = self.fetch_db()
        print(f'Here is a preview of your table {df.head(5)}')
