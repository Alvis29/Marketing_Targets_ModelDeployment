import sys
from logger import logging


def error_details():
    """
    Function to return an error message with its location.
    """
    _, error_msg, details = sys.exc_info()
    file_name = details.tb_frame.f_code.co_filename
    error_message = f'''Error occurred in python scripy name [{file_name}]
                                line number [{details.tb_lineno}] 
                                error message [{error_msg}]'''
    return error_message


class CustomException(Exception):
    def __int__(self, arg):
        self.msg = arg


if __name__ == '__main__':
    try:
        print(1/0)

    except Exception:
        logging.info('cannot divide by zero')
        raise CustomException(error_details())
