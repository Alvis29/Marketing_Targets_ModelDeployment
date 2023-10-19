import flask
import pandas as pd
from logger import logging
from exception import CustomException, error_details
from predict_pipeline import PredictPipline


app = flask.Flask(__name__)


@app.route("/predict", methods=['POST'])
def predict():
    try:
        logging.info("receiving the test input")
        test_input = flask.request.json
        logging.info("test input received")
        logging.info("converting input to dataframe")
        query = pd.DataFrame(test_input)
        logging.info("input to dataframe converted")
        logging.info("final prediction has started")
        predict_pipeline = PredictPipline()
        result = predict_pipeline.final_prediction(query)
            
        return flask.jsonify({"Prediction": result})

    except Exception:
        raise CustomException(error_details())

if __name__ == "__main__":
    app.run(debug=True, port=8000)
