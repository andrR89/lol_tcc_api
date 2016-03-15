# coding=utf-8

import unittest
from security_platform.role.model import Role
from security_platform.role.service import RoleService
from security_platform.role_package.service import RolePackageService
from security_platform.exceptions import ServiceException
from ming import mim


class RoleDomainTest(unittest.TestCase):


    def setUp(self):
        self.role_service = RoleService()
        self.role_package_service = RolePackageService()
        self.connection = mim.Connection()


    def test_should_create_role(self):
        #GIVEN
        role_json = dict(name = "Nome", description = "Descricao", uuid_publisher = "123456uuid123456")

        #WHEN
        self.role_service.create_role(**role_json)

        #THEN
        role_model = Role.query.get(name = "Nome")
        self.assertEqual(role_model.name, "Nome")


    def test_should_create_new_role_with_same_name_from_another_publisher(self):
        #GIVEN
        role_json = dict(name = "Nome", description = "Descricao", uuid_publisher = "123456uuid654321")

        #WHEN
        self.role_service.create_role(**role_json)

        #THEN
        role_model = Role.query.get(name = "Nome")
        self.assertEqual(role_model.name, "Nome")


    def test_should_create_new_role_with_different_name_from_same_publisher(self):
        #GIVEN
        role_json = dict(name = "Nome2222", description = "Descricao", uuid_publisher = "123456uuid123456")

        #WHEN
        self.role_service.create_role(**role_json)

        #THEN
        role_model = Role.query.get(name = "Nome2222")
        self.assertEqual(role_model.name, "Nome2222")


    def test_should_not_create_new_role_with_same_name_and_same_publisher(self):
        #GIVEN
        role_json = dict(name = "Teste2", description = "Descricao", uuid_publisher = "123456uuid123456")
        self.role_service.create_role(**role_json)
        role_json2 = dict(name = "Teste2", description = "Descricao", uuid_publisher = "123456uuid123456")

        try:
            #WHEN
            self.role_service.create_role(**role_json2)
            self.assertFalse(True)
        except ServiceException as e:
            #THEN
            self.assertTrue(True)


    def test_should_delete_role(self):
        #GIVEN
        role_model = Role.query.get(name = "Nome2222")

        #WHEN
        self.role_service.delete_role(role_model)

        #THEN
        self.assertEqual(len(self.role_service.find_all()), 2)


    def test_should_not_delete_role_associated_with_role_package(self):
        #GIVEN
        role_model = Role.query.get(name = "Nome")

        role_package_json = dict(name = "name", description = "description", _roles = [role_model._id], uuid_publisher = "123456uuid123456")
        self.role_package_service.create_role_package(**role_package_json)

        try:
            #WHEN
            self.role_service.delete_role(role_model)
            self.assertFalse(True)
        except ServiceException as e:
            #THEN
            self.assertTrue(True)
