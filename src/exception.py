import sys
import logging



def error_message_details(error:Exception,error_details:sys):
    _,_,exc_tb=error_details.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
        #file_name=exc_tb.tb_frame.f_code.co_filename,
        file_name,exc_tb.tb_lineno,str(error)
    )
    return error_message


class CustomException(Exception):  
    def __init__(self,error_message, error_details:sys):
        super().__init__(error_message)
        self.error_message=error_message_details(error_message,error_details=error_details)


    def __str__(self):
        return self.error_message
    

    try:
        a=1/0
    except:
        logging.error("Divide by zero error")
        raise CustomException("Divide by zero error",sys) from None