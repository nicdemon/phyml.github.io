import subprocess, os, shutil
from fonctions_phyml import *

class RunPhyml():
    __ID = 0
    def __init__(self, json):
#ID à générer à chaque fois que runPhyml ou généré par JS
        self.__id = int(RunPhyml.__ID)
#Path absolu du dossier Git
        self.__path = get_path()
#Devrait recevoir un dict en format json
        self.__json = extract_json(json)
#Path à phyML
        self.__phyml = self.__path + "/phyML/PhyML-3.1/PhyML-3.1_linux64 "
#Path pour output resultat
        self.__output = self.__path + "/static/results/" + str(self.__id)
        RunPhyml.__ID += 1

    def run(self):
        os.mkdir(self.__output)
        for file in os.listdir(self.__path + "/static/results/"):
            if file.endswith(".phy"):
                shutil.move(self.__path + "/static/results/" + file,self.__output)
        fh = open(self.__output + "/output.txt", "w")
        cmd = self.__phyml + generer_cmd(self.__json, self.__output)
        self.out = subprocess.Popen(cmd,cwd=self.__output,shell=True,stdout=fh)

    def status(self):
        try:
            if self.out.poll() == None:
                return {"result": "en cours"}
            elif self.out.poll() == 0:
                return {"result": "terminé avec succès"}
            elif self.out.poll() < 0:
                return {"result": "terminé avec un échec"}
        except AttributeError:
            return {"result": "non commencé"}

    def get_id():
        return self.__id

    def reset(self):
        try:
            shutil.rmtree(self.__output)
            self.out.kill()
            self.out = None
            return self.__id
        except AttributeError:
            return "Aucun processus à réinitialiser"

    def list_output_files(self):
        return os.listdir(self.__output)

    def get_execution(self):
        record = []
        record.append(int(self.__id))
        record.append(self.__json)
        record.append(self.__output)
        return record

    def read_file(self, file):
        if os.path.exists(self.__output + "/" + file):
            fh = open(self.__output + "/" + file,"r")
            tmp = []
            for line in fh.readlines():
                tmp.append(line)
            return "".join(tmp)
            fh.close
        else:
            return "Fichier inexistant"
