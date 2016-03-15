# coding=utf-8

import unittest
import json
from controller.rest import create_app


class RoleResourceTest(unittest.TestCase):


    def setUp(self):
        app = create_app('config')
        self.app = app.test_client()
        self.app.testing = True
        self.headers = [('Content-Type', 'application/json')]


    def test_should_get_all_roles_by_publisher_uuid(self):
        #GIVEN
        uuid = "123456uuid654321"

        #WHEN
        response = self.app.get('/roles/publisher/'+uuid)

        #THEN
        self.assertEqual(response.status_code, 200)


    def test_should_not_get_all_roles_by_invalid_publisher_uuid(self):
        #GIVEN
        uuid = "123456uuid65432154"

        #WHEN
        response = self.app.get('/roles/publisher/'+uuid)

        #THEN
        self.assertEqual(response.status_code, 404)


    def test_should_create_role(self):
        #GIVEN
        data = dict(name = "Nome", description = "Descricao", uuid_publisher = "123456uuid123456")

        #WHEN
        response = self.app.post('/roles', headers=self.headers, data=json.dumps(data))

        #THEN
        self.assertEqual(response.status_code, 200)


    def test_should_create_role_with_same_name_from_another_publisher(self):
        #GIVEN
        data = dict(name = "Nome", description = "Descricao", uuid_publisher = "123456uuid654321")

        #WHEN
        response = self.app.post('/roles', headers=self.headers, data=json.dumps(data))

        #THEN
        self.assertEqual(response.status_code, 200)


    def test_should_create_role_with_different_name_from_same_publisher(self):
        #GIVEN
        data = dict(name = "Nome2222", description = "Descricao", uuid_publisher = "123456uuid123456")

        #WHEN
        response = self.app.post('/roles', headers=self.headers, data=json.dumps(data))

        #THEN
        self.assertEqual(response.status_code, 200)


    def test_should_not_create_new_role_with_same_name_and_same_publisher(self):
        #GIVEN
        data = dict(name = "Nome", description = "Descricao", uuid_publisher = "123456uuid123456")

        #WHEN
        response = self.app.post('/roles', headers=self.headers, data=json.dumps(data))

        #THEN
        self.assertEqual(response.status_code, 400)
