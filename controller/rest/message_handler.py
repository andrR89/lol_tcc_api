# coding=utf-8

import json
from ming.exc import MingException
from security_platform.exceptions import ServiceException


class MessageHandler():

    type = ""
    message = ""


    def __init__(self):
        type = ""
        message = ""


    def error_message(self,text):
        self.type = "ERROR"
        self.message = text
        return json.dumps(self, default=lambda o: o.__dict__)


    def warning_message(self,text):
        self.type = "WARNING"
        self.message = text
        return json.dumps(self, default=lambda o: o.__dict__)


    def sucess_message(self,text):
        self.type = "SUCCESS"
        self.message = text
        return json.dumps(self, default=lambda o: o.__dict__)


def register_messages(app):

    message =  MessageHandler()


    @app.errorhandler(MingException)
    def integrity_error_handler(erro):
        return message.error_message(str(erro.args[0])), 400

    @app.errorhandler(ServiceException)
    def integrity_error_handler(erro):
        return message.error_message(str(erro.args[0])), 400


    @app.errorhandler(Exception)
    def error_handler(erro):
        return message.error_message(str(erro.args[0])), 500
