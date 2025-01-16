import os
import pymongo

import pandas as pd

from pathlib import PosixPath

class database():
    """
    Database operations handling
    """
    # Initialisation
    #####################################################
    def __init__(self):
        # Database connection
        self.connector = sqlite3.connect('history.db')
        self.cursor = self.connector.cursor()
        self._init_tables()

    def _init_tables(self) -> None:
        """
        Instantiate the tables required in the app
        """
        
        self.cursor.execute()

    # Analysis details
    #####################################################
    runs = '''
        CREATE TABLE IF NOT EXISTS runs (
            ID INTEGER NOT NULL 
        )
    '''
    self.cursor.execute(runs)
    parameters = '''
    '''
    self.cursor.execute(parameters)
    results = '''
    '''
    self.cursor.execute(results)