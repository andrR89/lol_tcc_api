# coding=utf-8
""" Implementação REST do service da Plataforma Financeira """
import datetime
import json
import os

import httplib2



class HelloLoL(object):
    """ Classe PFCServiceRest """


    def __init__(self):
        self.conn = httplib2.Http()
        self.url_service = "https://global.api.pvp.net/api/lol/static-data/br/v1.2/champion?champData=lore&api_key=dad3cbe4-23a8-419b-984b-8ba98b134928"
        self.headers = {"Content-type": "application/json", "Accept": "application/json", "Accept-Language":"en-US"
                        ,"Accept-Charset":"ISO-8859-1,utf-8-US"}


    # TODO: Verificar o tratamento correto para quando o PFC não está no ar e não é possivel fazer uma chamada.
    def get_all_lores(self):
        try:
            response, content = self.conn.request(self.url_service, "GET", "",
                                                  self.headers)
            return content
        except Exception as e:
            raise Exception(e)
