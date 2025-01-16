import os
import tqdm
import shutil
import subprocess

from utils import *
from db import database

class RunPhyML():
    def __init__(self, id, config):
        # Dynamic content
        self.id = id
        self.config = config
        self.out = os.path.join('outputs',f'{id}')
        self.cmd = ""
        # Static content
        self._exec = os.path.join('binaries','PhyML-3.1_linux64')
        self._db = 'results.db'
        # Execution
        self._generateCmd()
        if not os.path.isdir(self.out):
            os.makedirs(self.out)

    def run(self):
        # TODO: Implement fx in utils.genCmd -> launch exec here
        return None
    
    def status(self):
        # TODO: Fetch status + progressbar w/ tqdm
        return None
    
    def _generateCmd(self):
        # TODO: Translate self.config into command-line for phyml
        return None
    
    def _outFiles(self):
        # TODO: Read results ds files + add to db -> delete files
        return None
    
    def _execDetails(self):
        # TODO: Show exec options
        return None
    
    def _readResults(self):
        # TODO: Show analysis results
        return None
    