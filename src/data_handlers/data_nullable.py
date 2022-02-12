import pandas as pd
from src.data_handlers.data_interface import IRepository


class DataNullable(IRepository):

    def execute(self: object) -> pd.DataFrame:
        raise Exception('Invalid Option')
