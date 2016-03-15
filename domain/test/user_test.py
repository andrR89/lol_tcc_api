# coding=utf-8

import unittest
from security_platform.user.model import User
from security_platform.user.repositoy import UserRepository
from security_platform.access_profile.repositoy import AccessProfileRepository


class UserDomainTest(unittest.TestCase):


    def setUp(self):
        self.user_repository = UserRepository()
        self.access_profile_repository = AccessProfileRepository()


    def create_access_profile(self):
        access_profile_json = dict(name = "name1", description = "name2", uuid_publisher = "123456uuid123456", id_group = 1)
        access_profile = self.access_profile_repository.create(**access_profile_json)
        return access_profile


    def test_should_create_new_user(self):
        #GIVEN
        access_profile_model = self.create_access_profile()
        user_json = dict(name = "Nome", surname = "Sobrenome", email = "teste@teste.com", _access_profiles = [access_profile_model._id], uuid_publisher = "123456uuid123456")

        #WHEN
        self.user_repository.create(**user_json)

        #THEN
        user_model = User.query.get(name = "Nome")
        self.assertEqual(user_model.name, "Nome")


    def test_should_get_all_users_by_publisher_uuid(self):
        #GIVEN
        uuid_publisher = "123456uuid123456"

        #WHEN
        users = self.user_repository.find_by_publisher_uuid(uuid_publisher)

        #THEN
        self.assertEqual(len(users), 1)


    def test_should_not_get_all_users_by_invalid_publisher_uuid(self):
        #GIVEN
        uuid_publisher = "123456uuid12345699"

        #WHEN
        users = self.user_repository.find_by_publisher_uuid(uuid_publisher)

        #THEN
        self.assertEqual(len(users), 0)


    def test_should_get_by_email(self):
        #GIVEN
        email = "teste@teste.com"

        #WHEN
        user_model = self.user_repository.find_by_email(email)

        #THEN
        self.assertEqual(user_model.name, "Nome")


    def test_should_not_get_by_invalid_email(self):
        #GIVEN
        email = "teste@teste.commmm"

        #WHEN
        user_model = self.user_repository.find_by_email(email)

        #THEN
        self.assertEqual(user_model, None)
