import numpy as np
import pandas as pd
import joblib


test_pipline_path = "/home/alvis/Terry/Projects/Marketing_Targets/src/components/" \
                    "Transformation_objects/test_pipline.joblib"

final_columns = ['age', 'job', 'marital', 'education', 'balance', 'housing', 'loan',
                 'contact', 'month', 'duration', 'campaign', 'pdays', 'previous',
                 'poutcome']

test_pipline = joblib.load(test_pipline_path)


def to_dataframe(test_data: dict) -> pd.DataFrame:
    """
     convert input into a dataframe """
    test_dataframe = pd.DataFrame.from_dict(test_data)
    return test_dataframe


def feature_selection(dataframe: pd.DataFrame) -> pd.DataFrame:
    """ drop the least significant features """

    dataframe.drop(columns=['default', 'day'], inplace=True)
    dataframe.columns = final_columns
    return dataframe


def prediction(dataframe: pd.DataFrame) -> np.ndarray:
    """ get the prediction array  """
    pred = test_pipline.predict(dataframe)
    return pred


# function to convert integer output to desired string output 'yes' or 'no'
def array_to_str(array: np.ndarray) -> list:
    """ prediction 'yes' or 'no' from predicted array"""

    pred_list = []
    for pred in array:
        if pred == 0:
            pred_list.append('no')

        if pred == 1:
            pred_list.append('yes')
    return pred_list
