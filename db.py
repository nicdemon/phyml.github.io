import sqlite3

def init_db():
    conn = sqlite3.connect('phyml.db')
    query = ''' CREATE TABLE IF NOT EXISTS PhyML (
                    id                    INTEGER  NOT NULL,
		            ligne_commande  	  TEXT	   NOT NULL,
		            path_output       	  TEXT     NOT NULL,
                    start_time            TEXT     NOT NULL,
                    liste_fichier_output  TEXT     NULL,
		            PRIMARY KEY (id)
	        ) '''
    conn.cursor().execute(query)

#Execution doit être un dictionnaire
#Doit être exécuté avant runPhyml
def add_params(execution):
    try:
        conn = sqlite3.connect('phyml.db')
        conn.cursor().execute("INSERT INTO PhyML (id,ligne_commande,path_output,start_time) VALUES (?,?,?,?)", execution)
        conn.commit()
    except sqlite3.Error as e:
        print (e)

#Doit être exécuté après runPhyml
def add_fichiers(liste):
    try:
        conn = sqlite3.connect('phyml.db')
        conn.cursor().execute("INSERT INTO PhyML (liste_fichier_output) VALUES (?)", liste)
        conn.commit()
    except sqlite3.Error as e:
        print (e)

#Utilisé dans reset pour enlever les fichiers générés de la db
def delete_fichiers(id):
    try:
        conn = sqlite3.connect('phyml.db')
        conn.cursor().execute("DELETE liste_fichier_output FROM PhyML WHERE id=(?)", id)
        conn.commit()
    except sqlite3.Error as e:
        print (e)

#Afficher liste des ID en vue de choisir celui à reset
def list_reset():
    try:
        conn = sqlite3.connect('phyml.db')
        list_id = conn.cursor().execute("SELECT id FROM PhyML")
        return list_id
    except sqlite3.Error as e:
        print(e)

#Reset l'output du ID sélectionné
def reset(id):
    try:
        conn = sqlite3.connect('phyml.db')
        cmd = conn.cursor().execute("SELECT ligne_commande FROM PhyML WHERE id=(?)", id)
        out = conn.cursor().execute("SELECT path_output FROM PhyML WHERE id=(?)", id)
        alignment = conn.cursor().execute("SELECT phylip FROM PhyML WHERE id=(?)", id)
        return cmd, out, alignment
    except sqlite3.Error as e:
        print(e)

#Pour afficher la liste de fichiers consultables
#Doit être transformé en dictionnaire puis en json (ennumerate)
def list_fichiers(id):
    try:
        conn = sqlite3.connect('phyml.db')
        fichiers = conn.cursor().execute("SELECT liste_fichier_output FROM PhyML WHERE id=?", id)
        return " ".split(fichiers)
    except sqlite3.Error as e:
        print(e)

def historique():
    try:
        id = "*"
        conn = sqlite3.connect('phyml.db')
        fichiers = conn.cursor().execute("SELECT id, liste_fichier_output FROM PhyML WHERE id=?", id)
        return " ".split(fichiers)
    except sqlite3.Error as e:
        print(e)
