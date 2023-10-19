# Problem Statement : to predict if the client will subscribe to a term deposit

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
> http://127.0.0.1:8000/predict

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
