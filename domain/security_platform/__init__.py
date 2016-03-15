# coding=utf-8

from ming import create_datastore, Session
from ming.odm import ODMSession
import os


session = Session()
session.bind = create_datastore(os.environ.get('DATABASE_URL'))
odm_session = ODMSession(session)
