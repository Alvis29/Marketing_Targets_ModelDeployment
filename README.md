# Problem Statement : to predict if the client will subscribe to a term deposit

## Pre-requisite step:
     1. (mandetory) go to https://www.dropbox.com/scl/fo/ts0sdza10yylflk7xwmgy/h?rlkey=w8golgugeobj2dom280er4k12&dl=0 and downlad all files to the src/components/transformation_objects folder 
     2. (optional: if needed) go to https://www.dropbox.com/scl/fo/wh8smv0tn536o7phgyvd8/h?rlkey=fw0fpdsse0wtbwe10ukh1lbru&dl=0 link and download RandomForest.joblib file to the src/components/model folder

# create conda enviroment
> conda create --name venv python=3.10

# activate the conda env and install libraries 
> conda activate venv

> pip install -r reqs.txt
#### only if above above requirements file gives any error
> pip install -r requirements.txt

# deactivate the enviroment
> conda deactivate 



# request url 
> http://127.0.0.1:8080/predict

# request method: 
> post 


# request data in json 

{    "age": [80],
     "job": ["student"],
     "marital": ["married"],
     "education": ["secondary"],
     "default": ["no"],
     "balance": [-500],
     "housing": ["no"],
     "loan": ["no"],
     "contact": ["cellular"],
     "day": [5],
     "month": [5],
     "duration": [650],
     "campaign": [5],
     "pdays": [-1],
     "previous": [3],
     "poutcome": ["unknown"]
 }

# Response:

> yes or no
