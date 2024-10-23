import os

from flask import Flask, request, render_template, jsonify, session
from runPhyml import RunPhyml
from fonctions_phyml import *
from werkzeug.exceptions import BadRequestKeyError
from werkzeug.utils import secure_filename
import db
from datetime import *
import shutil

app = Flask(__name__, template_folder='.')
path = get_path()
app.config['UPLOAD_FOLDER'] = path + "/static/results"
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
ALLOWED_EXTENSIONS = set(['phy'])
db.init_db()

#Definir tache à ext pour accéder partout et non seulement ds fx

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def info():
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.readlines ()
        listToStr = ' '.join([str(elem) for elem in content])
    return render_template("/static/home.html", listToStr=listToStr)

@app.route('/new')
def new():
    return render_template("/static/index.html")


@app.route('/run', methods=["GET","POST"])
def run():
    if request.method == 'POST':
        global tache
        result = request.form #récupère les données
        v=json.dumps(result, indent=4, sort_keys=False) #change en Json
        try:
            filename=app.config['UPLOAD_FOLDER']+"/textarea.phy"
            fh = open(filename, "w")
            x = request.form['input']
            fh.write(x)
            fh.close()
            tache = RunPhyml(v)
            tache.run()
            execution = tache.get_execution()
            execution.append(str(datetime.now()))
            db.add_params(execution)
        except BadRequestKeyError:
            file = request.files['file']
            if file.filename == '':
                flash('No file selected for uploading')
                return redirect("./static/results")
            elif file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                tache = RunPhyml(v)
                tache.run()
                execution = tache.get_execution()
                execution.append(str(datetime.now()))
                db.add_params(execution)
        return render_template("./static/pageAttente.html")

@app.route('/status', methods=["GET","POST"])
def status():
    if request.method == 'POST':
        try :
            if tache != None:
                data=tache.status()
                return jsonify(data)
        except Exception as e:
            data = {"Resultat:":" Non commencé"}
            return jsonify(data)
        else:
            return jsonify(data)
    elif request.method == 'GET':
        try :
            if tache != None:
                data=tache.status()
                return render_template("./static/status.html",data=data)
        except Exception as e:
            data = {"Resultat:":" Non commencé"}
            return render_template("./static/status.html",data=data)
        else:
            return render_template("./static/status.html",data=data["result"])

""""
@app.route('/view')
def view():
    files = tache.list_output_files()
    return render_template("./static/pageView.html",files=files)

@app.route('/read')
def read():
    files = tache.list_output_files()
    list_data = {}
    for file in files:
        data = tache.read_file(str(file))
        list_data[file]=data
    return render_template("./static/pageRead.html")
"""

@app.route('/reset')
def reset():
    try:
        id = tache.reset()
        data = "le dossier "+ str(id) + " a été bien supprimé"
        return render_template("./static/status.html", data= data)
    except Exception:
        data = "Resultat: Aucun processus lancé"
        return render_template("./static/status.html",data=data)



@app.route('/view')
def view():
    try:
        data = tache.list_output_files()
        #liste= jsonify(data)
        return render_template("./static/status.html", data=data)
    except Exception as e :
        liste= "Pas de fichiers - pas de processus ou supprimer avec reset"
        return render_template("./static/status.html", liste= liste)


@app.route('/read')
def read():
    try :
        print(tache)
        id = tache.get_id()
        files = []
        for file in os.listdir(app.config['UPLOAD_FOLDER'] + "/" + id):
            if file.endswith(".txt"):
                files.append(file)
                if len(files) == 5:
                    data1 = tache.read_file(app.config['UPLOAD_FOLDER'] + "/results/" + id + "/" + str(files[1]))
                    data2 = tache.read_file(app.config['UPLOAD_FOLDER'] + "/results/" + id + "/" + str(files[2]))
                    data3 = tache.read_file(app.config['UPLOAD_FOLDER'] + "/results/" + id + "/"+ str(files[3]))
                    data4 = tache.read_file(app.config['UPLOAD_FOLDER'] + "/results/" + id + "/"+ str(files[4]))
                    data5 = tache.read_file(app.config['UPLOAD_FOLDER'] + "/results/" + id + "/"+ str(files[5]))
                    return render_template("./static/pageRead.html",data1=data1,data2=data2,data3=data3,data4=data4,data5=data5)
                elif len(files) == 3:
                    data1 = tache.read_file(app.config['UPLOAD_FOLDER'] + "/results/" + id + "/"+ str(files[1]))
                    data2 = tache.read_file(app.config['UPLOAD_FOLDER'] + "/results/" + id + "/"+ str(files[2]))
                    data3 = tache.read_file(app.config['UPLOAD_FOLDER'] + "/results/" + id + "/"+ str(files[3]))
                    data4 = "Rien à afficher"
                    data5 = "Rien à afficher"
                    return render_template("./static/pageRead.html",data1=data1,data2=data2,data3=data3,data4=data4,data5=data5)
    except Exception as e:
        data = "Aucun résultat"
        return render_template("./static/status.html",data=data)

if __name__ == '__main__':
    app.run(debug = True, port = '5000')
