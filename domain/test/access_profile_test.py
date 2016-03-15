# coding=utf-8

import unittest
from security_platform.access_profile.model import AccessProfile
from security_platform.user.service import UserService
from security_platform.access_profile.service import AccessProfileService
from security_platform.role_package.service import RolePackageService
from security_platform.role.service import RoleService
from security_platform.exceptions import ServiceException


class AccessProfileDomainTest(unittest.TestCase):


    def setUp(self):
        self.role_service = RoleService()
        self.role_package_service = RolePackageService()
        self.access_profile_service = AccessProfileService()
        self.user_service = UserService()


    def create_role(self, role_name, uuid_publisher):
        role_json = dict(name = role_name, description = "description", uuid_publisher = uuid_publisher)
        role = self.role_service.create_role(**role_json)
        return role


    def create_role_package(self, role_package_name, role, uuid_publisher):
        role_package_json = dict(name = role_package_name, description = "description", _roles = [role._id], uuid_publisher = uuid_publisher)
        role_package = self.role_package_service.create_role_package(**role_package_json)
        return role_package


    def create_access_profile(self, access_profile_name, role_package, uuid_publisher):
        access_profile_json = dict(name = access_profile_name, description = "description", _roles_packages = [role_package._id], uuid_publisher = uuid_publisher, id_group = 1)
        access_profile = self.access_profile_service.create_access_profile(**access_profile_json)
        return access_profile


    def create_user(self, user_name, access_profile, uuid_publisher):
        user_json = dict(name = user_name, surname = "Sobrenome", email = "teste@teste.com", _access_profiles = [access_profile._id], uuid_publisher = uuid_publisher)
        user = self.user_service.create_user(**user_json)
        return user


    def test_should_create_new_access_profile(self):
        #GIVEN
        role = self.create_role("role_name","123456uuid123456")
        role_package = self.create_role_package("role_package_name", role,"123456uuid123456")

        #WHEN
        self.create_access_profile("access_profile_name", role_package,"123456uuid123456")
        access_profile_model = AccessProfile.query.get(name = "access_profile_name")

        #THEN
        self.assertEqual(access_profile_model.name, "access_profile_name")
        self.assertEqual(access_profile_model.roles_packages[0].name, "role_package_name")
        self.assertEqual(access_profile_model.roles_packages[0].roles[0].name, "role_name")


    def test_should_create_access_profile_with_same_name_from_another_publisher(self):
        #GIVEN
        role = self.create_role("role_name","123456uuid654321")
        role_package = self.create_role_package("role_package_name", role,"123456uuid654321")

        #WHEN
        self.create_access_profile("access_profile_name", role_package,"123456uuid654321")
        access_profile_model = AccessProfile.query.get(name = "access_profile_name")

        #THEN
        self.assertEqual(access_profile_model.name, "access_profile_name")
        self.assertEqual(access_profile_model.roles_packages[0].name, "role_package_name")
        self.assertEqual(access_profile_model.roles_packages[0].roles[0].name, "role_name")


    def test_should_create_access_profile_with_different_name_from_same_publisher(self):
        #GIVEN
        role = self.create_role("role_name77777","123456uuid123456")
        role_package = self.create_role_package("role_package_name77777", role,"123456uuid123456")

        #WHEN
        self.create_access_profile("access_profile_name77777", role_package,"123456uuid123456")
        access_profile_model = AccessProfile.query.get(name = "access_profile_name77777")

        #THEN
        self.assertEqual(access_profile_model.name, "access_profile_name77777")
        self.assertEqual(access_profile_model.roles_packages[0].name, "role_package_name77777")
        self.assertEqual(access_profile_model.roles_packages[0].roles[0].name, "role_name77777")


    def test_should_not_create_access_profile_with_same_name_and_same_publisher(self):
        #GIVEN
        role = self.create_role("role_name8","123456uuid123456")
        role_package = self.create_role_package("role_package_name8", role,"123456uuid123456")
        self.create_access_profile("access_profile_name9", role_package,"123456uuid9")

        try:
            #WHEN
            self.create_access_profile("access_profile_name9", role_package,"123456uuid9")
            self.assertFalse(True)
        except ServiceException as e:
            #THEN
            self.assertTrue(True)


    def test_should_delete_access_profile(self):
        #GIVEN
        access_profile_model = AccessProfile.query.get(name = "access_profile_name77777")

        #WHEN
        self.access_profile_service.delete_access_profile(access_profile_model)

        #THEN
        self.assertEqual(len(self.access_profile_service.find_all()), 2)


    def test_should_not_delete_access_profile_associated_with_user(self):
        #GIVEN
        access_profile = AccessProfile.query.get(name = "access_profile_name")
        self.create_user("user3", access_profile,"123456uuid123456")

        try:
            #WHEN
            self.access_profile_service.delete_access_profile(access_profile)
            self.assertFalse(True)
        except ServiceException as e:
            #THEN
            self.assertTrue(True)
