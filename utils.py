import os
import json

def read_json(file):
    return json.loads(file)

def genCmd(config, path):
    cmd = ["-i"]
    # TODO: Parse options from dict after form was created
