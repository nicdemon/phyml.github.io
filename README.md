# PhyML web interface project

The project was developped localy by students at the DESS in bioinformatics at Université du Québec à Montréal (UQAM) for class INF8214.

The project consisted in two steps:
1. Implement python classes and scripts for launching the PhyML linux CLI precompiled binaries from a local terminal
2. Implement a web interface for running the python PhyML python classes created in step 1.
    * The frontend interface uses HTML, JavaScript JQuery, and Bootstrap CSS
    * The backend leverages a Flask server and an SQLite3 database

Team:
* Abdellatif El Ghizi
* Latifa Mohammadi
* Nicolas de Montigny
* Wanlin Li

## Dependency
Running this app requires to have a Python 3 interpreter installed and the Flask package installed.
```
python3 -m pip install flask
```

## Execution
As the project was not hosted on a web server, it is only available for running locally on a linux OS.
To start the web app, run the following command in a terminal from the repo root directory:
```
python3 app.py
```
Afterwards, the web interface can be accessed in a web browser at the address `localhost:5000` or another port given by the flask server.

## PhyMl details
[PhyML](http://www.atgc-montpellier.fr/phyml/) is a software developped and maintained by the French bioinformatics institute.

PhyMl's repo i hosted on [Github](https://github.com/stephaneguindon/phyml).

PhyML's article citation:
```
"New Algorithms and Methods to Estimate Maximum-Likelihood Phylogenies: Assessing the Performance of PhyML 3.0."
Guindon S., Dufayard J.F., Lefort V., Anisimova M., Hordijk W., Gascuel O.
Systematic Biology, 59(3):307-21, 2010.
```