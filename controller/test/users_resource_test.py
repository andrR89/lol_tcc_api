# coding=utf-8

import unittest
import json
from controller.rest import create_app


class UserResourceTest(unittest.TestCase):


    def setUp(self):
        app = create_app('config')
        self.app = app.test_client()
        self.app.testing = True
        self.headers = [('Content-Type', 'application/json')]


    def test_should_create_user(self):
        #GIVEN
        data = {'name':"NexxUser 2",'surname':"NexxAdmin 2",'email':"nexx.admin@nexxera.com",'registration_type':'CNPJ','registration_number':"00123456789000199","uuid_publisher":"123456uuid123456"}

        #WHEN
        response = self.app.post('/users', headers=self.headers, data=json.dumps(data))
        response_json = json.loads(response.data.decode('utf-8'))

        #THEN
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_json['name'], 'NexxUser 2')


    def test_should_get_all_users_by_publisher_uuid(self):
        #GIVEN
        response = self.app.get('/users/publisher/123456uuid123456')

        #WHEN
        response_json = json.loads(response.data.decode('utf-8'))

        #THEN
        self.assertEqual(len(response_json), 1)
        self.assertEqual(response.status_code, 200)


    def test_should_not_get_all_users_by_invalid_publisher_uuid(self):
        #GIVEN
        uuid_publisher = "123456uuid12345699"

        #WHEN
        response = self.app.get('/users/publisher/'+uuid_publisher)

        #THEN
        self.assertEqual(response.status_code, 404)


    def test_should_get_user_by_email(self):
        #GIVEN
        response = self.app.get('/users/nexx.admin@nexxera.com')

        #WHEN
        response_json = json.loads(response.data.decode('utf-8'))

        #THEN
        self.assertEqual(response_json['email'], "nexx.admin@nexxera.com")
