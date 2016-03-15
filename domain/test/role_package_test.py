# coding=utf-8

import unittest
from security_platform.role_package.model import RolePackage
from security_platform.role.service import RoleService
from security_platform.role_package.service import RolePackageService
from security_platform.access_profile.service import AccessProfileService
from security_platform.exceptions import ServiceException


class RolePackageDomainTest(unittest.TestCase):


    def setUp(self):
        self.role_service = RoleService()
        self.role_package_service = RolePackageService()
        self.access_profile_service = AccessProfileService()


    def create_role(self, role_name, uuid_publisher):
        role_json = dict(name = role_name, description = "description", uuid_publisher = uuid_publisher)
        role = self.role_service.create_role(**role_json)
        return role


    def test_should_create_role_package(self):
        #GIVEN
        role = self.create_role("name1", "123456uuid123456")
        role_package_json = dict(name = "name", description = "description", _roles = [role._id], uuid_publisher = "123456uuid123456")

        #WHEN
        self.role_package_service.create_role_package(**role_package_json)
        role_package_model = RolePackage.query.get(name = "name")

        #THEN
        self.assertEqual(role_package_model.name, "name")
        self.assertEqual(role_package_model.roles[0].name, "name1")


    def test_should_create_role_package_with_same_name_from_another_publisher(self):
        #GIVEN
        role = self.create_role("name1", "123456uuid654321")
        role_package_json = dict(name = "name", description = "description", _roles = [role._id], uuid_publisher = "123456uuid654321")

        #WHEN
        self.role_package_service.create_role_package(**role_package_json)
        role_package_model = RolePackage.query.get(name = "name")

        #THEN
        self.assertEqual(role_package_model.name, "name")
        self.assertEqual(role_package_model.roles[0].name, "name1")


    def test_should_create_role_package_with_different_name_from_same_publisher(self):
        #GIVEN
        role = self.create_role("name111", "123456uuid123456")
        role_package_json = dict(name = "name111", description = "description", _roles = [role._id], uuid_publisher = "123456uuid123456")

        #WHEN
        self.role_package_service.create_role_package(**role_package_json)
        role_package_model = RolePackage.query.get(name = "name111")

        #THEN
        self.assertEqual(role_package_model.name, "name111")
        self.assertEqual(role_package_model.roles[0].name, "name111")


    def test_should_not_create_role_package_with_same_name_and_same_publisher(self):
        #GIVEN
        role = self.create_role("name", "123456uuid123456")
        role_package_json = dict(name = "name25", description = "description", _roles = [role._id], uuid_publisher = "123456uuid123456")
        self.role_package_service.create_role_package(**role_package_json)
        role_package_json2 = dict(name = "name25", description = "description", _roles = [role._id], uuid_publisher = "123456uuid123456")

        try:
            #WHEN
            self.role_package_service.create_role_package(**role_package_json2)
            self.assertFalse(True)
        except ServiceException as e:
            #THEN
            self.assertTrue(True)


    def test_should_delete_role_package(self):
        #GIVEN
        role_package_model = RolePackage.query.get(name = "name111")

        #WHEN
        self.role_package_service.delete_role_package(role_package_model)

        #THEN
        self.assertEqual(len(self.role_package_service.find_all()), 2)


    def test_should_not_delete_role_package_associated_with_access_profile(self):
        #GIVEN
        role_package_model = RolePackage.query.get(name = "name")

        access_profile_json = dict(name = "nameeeee", description = "description", _roles_packages = [role_package_model._id], uuid_publisher = "123456uuid123456", id_group = 1)
        self.access_profile_service.create_access_profile(**access_profile_json)

        try:
            #WHEN
            self.role_package_service.delete_role_package(role_package_model)
            self.assertFalse(True)
        except ServiceException as e:
            #THEN
            self.assertTrue(True)
