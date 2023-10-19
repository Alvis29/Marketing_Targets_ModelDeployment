from utils import feature_selection, prediction, array_to_str, to_dataframe
from logger import logging
from exception import CustomException, error_details
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
    

class CustomData():
    def __init__(self,
                 age :int,
                 job :str,
                 marital :str,
                 education :str,
                 default :str,
                 balance :int,
                 housing :str,
                 loan :str,
                 contact :str,
                 day :int,
                 month :str,
                 duration :int,
                 campaign :int,
                 pdays :int,
                 previous :int,
                 poutcome :str):
        self.age = age
        self.job = job
        self.marital = marital
        self.education = education
        self.default = default
        self.balance = balance
        self.housing = housing
        self.loan = loan
        self.contact = contact
        self.day = day
        self.month = month
        self.duration = duration
        self.campaign = campaign
        self.pdays = pdays
        self.previous = previous
        self.poutcome = poutcome


    def get_data_as_dict(self):
        try:
            logging.info("creating an input dictionary")
            input_dict = {
                "age":[self.age],
                "job":[self.job],
                "marital":[self.marital],
                "education":[self.education],
                "default":[self.default],
                "balance":[self.balance],
                "housing":[self.housing],
                "loan":[self.loan],
                "contact":[self.contact],
                "day":[self.day],
                "month":[self.month],
                "duration":[self.duration],
                "campaign":[self.campaign],
                "pdays":[self.pdays],
                "previous":[self.previous],
                "poutcome":[self.poutcome]
            }
            logging.info("dictionary created")

            return pd.DataFrame(input_dict)
        
        except Exception:
            raise CustomException(error_details())


class PredictPipline():
    def __init__(self) -> None:
        pass

    def final_prediction(self, test_input) -> list:
        """ to get the prediction 'yes' or 'no' for the test input """
        try:
            logging.info("feature selection started")
            final_dataframe = feature_selection(test_input)
            logging.info("done with feature selection")
            logging.info("predicting the outcome array")
            pred = prediction(final_dataframe)
            logging.info("outcome predicted")
            logging.info("converting outcome array to string")
            pred = array_to_str(pred)
            logging.info("converted to string")
            return pred

        except Exception:
            raise CustomException(error_details())
    



if __name__ == '__main__':

    test_input1 = {"age": [80],
                   "job": ["student"],
                   "marital": ["married"],
                   "education": ["secondary"],
                   "default": ["no"],
                   "balance": [-500],
                   "housing": ["no"],
                   "loan": ["no"],
                   "contact": ["cellular"],
                   "day": [5],
                   "month": ['may'],
                   "duration": [650],
                   "campaign": [5],
                   "pdays": [-1],
                   "previous": [3],
                   "poutcome": ["unknown"]}

    
    predict_pipeline = PredictPipline()
    test_input1_df = to_dataframe(test_input1)
    result = predict_pipeline.final_prediction(test_input1_df)
    print(result)
