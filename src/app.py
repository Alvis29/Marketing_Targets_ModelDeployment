from flask import Flask, render_template, request
from predict_pipeline import PredictPipline, CustomData
import pandas as pd
from logger import logging
from exception import CustomException, error_details


application = Flask(__name__)
app = application


# Route for a home page
@app.route('/')
def index():
    return render_template('index.html')

@app.route("/predict", methods=['GET','POST'])
def predict():
    if request.method=='GET':
        return render_template('home.html')
    else:
        try:
            logging.info("geting data from website")
            input_data = CustomData(
                        age = request.form.get('age'),
                        job = request.form.get('job'),
                        marital = request.form.get('marital'),
                        education = request.form.get('education'),
                        default = request.form.get('default'),
                        balance = request.form.get('balance'),
                        housing = request.form.get('housing'),
                        loan = request.form.get('loan'),
                        contact = request.form.get('contact'),
                        day = request.form.get('day'),
                        month = request.form.get('month'),
                        duration = request.form.get('duration'),
                        campaign = request.form.get('campaign'),
                        pdays = request.form.get('pdays'),
                        previous = request.form.get('previous'),
                        poutcome = request.form.get('poutcome')
            )
            logging.info("data gathered")
            logging.info("convering into dataframe")
            input_df = input_data.get_data_as_dict()
            print(input_df)
            logging.info("converted into dataframe")
            logging.info("prediction has started")
            predict_pipeline = PredictPipline()
            result = predict_pipeline.final_prediction(input_df)
            logging.info("prediciton done.")
            return render_template('home.html',results = result[0])
        
        except Exception:
            raise CustomException(error_details())


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
