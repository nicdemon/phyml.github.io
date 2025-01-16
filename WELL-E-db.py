import os
import sqlite3

import pandas as pd

from pathlib import PosixPath

__author__ = 'Nicolas de Montigny'

class dbOperator():
    """
    Database operations handling
    """
    # Initialisation
    #####################################################
    def __init__(self) -> None:
        self.connector = sqlite3.connect('metadata.db')
        self.cursor = self.connector.cursor()
        self._init_tables()

    def _init_tables(self) -> None:
        """
        Instantiate the tables required in the app
        """
        projectIDs = '''
            CREATE TABLE IF NOT EXISTS projectIDs (
                farm TEXT NOT NULL,
                season TEXT NOT NULL,
                year INTEGER NOT NULL,
                projectName TEXT NOT NULL,
                projectID TEXT NOT NULL
            )
        '''
        self.cursor.execute(projectIDs)
        testIDs = '''
            CREATE TABLE IF NOT EXISTS testIDs (
                testID TEXT NOT NULL,
                description TEXT NOT NULL
            )
        '''
        self.cursor.execute(testIDs)
        # projectNames = '''
        #     CREATE TABLE IF NOT EXISTS projectNames (
        #         name TEXT NOT NULL,
        #         description TEXT NOT NULL
        #     )
        # '''
        # self.cursor.execute(projectNames)
        expMeta = '''
            CREATE TABLE IF NOT EXISTS experimentsMetadata (
                projectID TEXT NOT NULL,
                testID TEXT NOT NULL,
                timestamp TEXT NOT NULL,
                equipmentID TEXT NOT NULL,
                storagePath TEXT NOT NULL,
                localPath TEXT NOT NULL
            )
        '''
        self.cursor.execute(expMeta)

    # Project ID
    #####################################################

    def get_projectIDs(self) -> list:
        """Get project IDs"""
        res = self.cursor.execute('SELECT DISTINCT projectID FROM projectIDs')
        return res.fetchall()

    def new_projectID(self, farm: str, season: str, year: int, name: str) -> None:
        """Set a new project ID"""
        id = f'{farm}{season[0:2]}{str(year)}{name}'
        self.cursor.execute('INSERT INTO projectIDs VALUES(?, ?, ?, ?, ?)',(farm,season,year,name,id,))
        self.connector.commit()
        return id

    # Project descriptors
    #####################################################
    
    def get_farmNames(self) -> list:
        """Get farm names"""
        res = self.cursor.execute('SELECT DISTINCT farm FROM projectIDs')
        return res.fetchall()

    def get_projectNames(self) -> list:
        """Get project names"""
        res = self.cursor.execute('SELECT DISTINCT projectName FROM projectIDs')
        return res.fetchall()

    # Test ID
    #####################################################

    def get_testIDs(self) -> list:
        """Get test IDs"""
        res = self.cursor.execute('SELECT DISTINCT testID FROM testIDs')
        return res.fetchall()

    def new_testID(self, id: str, description: str = '') -> None:
        """Set a new test ID"""
        self.cursor.execute('INSERT INTO testIDs VALUES(?,?)',(id,description))
        self.connector.commit()

    # Experiments metadata
    #####################################################

    def get_expMetadata(self, timestamp: str) -> pd.DataFrame:
        """Get metadata for a given timestamp"""
        res = self.cursor.execute('SELECT * FROM experimentsMetadata WHERE timestamp=?',(timestamp,))
        return res.fetchall()

    def new_fileMetadata(self, projectID: str, testID: str, timestamp: str, equipmentID: str, filePath) -> None:
        """Set a new project ID"""
        localPath = os.path.splitdrive(filePath)[1]
        file = os.path.basename(filePath)
        storagePath = PosixPath(os.path.join('/project/rpp-banire/well-eCloud/experiments',projectID,timestamp,file))
        self.cursor.execute('INSERT INTO experimentsMetadata VALUES(?,?,?,?,?,?)',(projectID,testID,timestamp,equipmentID,storagePath,localPath))
        self.connector.commit()