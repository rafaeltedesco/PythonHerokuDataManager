from typing import Dict
from src.data_handlers.data_interface import IRepository
from src.data_handlers.data_loader import DataLoader
from src.data_handlers.data_extractor import DataExtractor
from src.config.config import DB_CONNECTION
from src.data_handlers.data_nullable import DataNullable
from src.manager.data_manager import DataManager


data_classes = {'1': DataLoader, '2': DataExtractor}


def load_json_file(config) -> Dict:
    json_path = input('Write Json Full File Path: ')
    config.update({'full_file_path': json_path})


if __name__ == '__main__':
    print('1 - Load Data From Json to Database')
    print('2 - Extract and show Data loaded in Database')

    opt: str = input('What do you want to do? ')

    dataStrategy: IRepository = data_classes.get(opt, DataNullable)
    if opt == '1':
        load_json_file(config=DB_CONNECTION)

    manager = DataManager(dataStrategy(config=DB_CONNECTION))
    df = manager.execute()
    