import json, os
from os import path
from pathlib import Path

def get_path():
    path = Path.cwd()
    return str(path)

def extract_json(string):
    dict = json.loads(string)
    return dict

def save_local(alignment, path):
    fh = open(path + "/input.txt","w")
    print(alignment,file=fh)
    fh.close()

def generer_cmd(dict,path):
    cmd = []
    cmd.append("-i")
    try:
        save_local(dict["textarea"], path)
        cmd.append(path + "/*.phy")
    except KeyError:
        cmd.append(path + "/*.phy")
    for k, v in dict.items():
        if k == "SequenceTypeOption":
            cmd.append("-d")
            cmd.append(str(v))
        elif k == "sequential":
            if v != "n":
                cmd.append("-q")
        elif k == "bootstrapOption":
            cmd.append("-b")
            try:
                cmd.append(dict["NbBtsDataSets"])
            except KeyError:
                cmd.append("n")
        elif k == "multiple":
            if v != "n":
                cmd.append("-n")
                cmd.append(str(v))
        elif k == "pars":
            if v != "n":
                cmd.append("-p")
        elif k == "model":
                cmd.append("-m")
                cmd.append(str(v))
        elif k == "FqOption":
            cmd.append("-f")
            cmd.append(str(v))
        elif k == "tstv":
            if v != "e":
                cmd.append("-t")
                cmd.append(str(v))
            else:
                cmd.append("-t")
                cmd.append("e")
        elif k == "pinv":
            try:
                if 0 < int(v) < 1:
                    cmd.append("-v")
                    cmd.append(str(v))
            except ValueError:
                cmd.append("-v")
                cmd.append("e")
        elif k == "nclasses":
            cmd.append("-c")
            cmd.append(str(v))
        elif k == "alpha":
            try:
                if 0 < int(v):
                    cmd.append("-a")
                    cmd.append(str(v))
            except ValueError:
                cmd.append("-a")
                cmd.append("e")
        elif k == "useMedian":
            if v != "n":
                cmd.append("--use_median")
        elif k == "codposOption":
            if v != "n":
                cmd.append("--codpos")
                cmd.append(str(v))
        elif k == "params":
            cmd.append("-o")
            cmd.append(str(v))
        elif k == "search":
            cmd.append("-s")
            cmd.append(str(v))
        elif k == "randstart":
            if v != "n":
                cmd.append("--rand_start")
                cmd.append("--n_rand_starts")
                cmd.append(str(v))
        elif k == "rSeedOption":
            if v != "n":
                cmd.append("--r_seed")
                cmd.append(str(v))
        elif k == "printSiteLnl":
            if v != "n":
                cmd.append("--print_site_lnl")
        elif k == "printTrace":
            if v != "n":
                cmd.append("--print_trace")
        elif k == "runID":
            if v != "n":
                cmd.append("--run_id")
                cmd.append(str(v))
        elif k == "noMemoryCheck":
            if v != "n":
                cmd.append("--no_memory_check")
        elif k == "noColalias":
            if v != "n":
                cmd.append("--no_colalias")
        elif k == "quietMode":
            if v != "n":
                cmd.append("--quiet")
    cmd = " ".join(cmd)
    return cmd
