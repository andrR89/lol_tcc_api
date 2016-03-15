# coding=utf-8

from security_platform.user.repositoy import UserRepository
from security_platform.exceptions import ServiceException
from pymongo.errors import DuplicateKeyError, InvalidId


class UserService():


    def __init__(self):
        self.user_repository = UserRepository()


    def find_all(self):
        return self.user_repository.find_all()


    def find_all_users_by_publisher_uuid(self, uuid_publisher):
        return self.user_repository.find_by_publisher_uuid(uuid_publisher)


    def create_user(self, **kwargs):
        try:
            return self.user_repository.create(**kwargs)
        except DuplicateKeyError as e:
            raise ServiceException(e)


    def update_user(self, **kwargs):
        return self.user_repository.update(**kwargs)


    def find_user_by_id(self, user_id):
        try:
            return self.user_repository.find_by_id(user_id)
        except InvalidId as e:
            raise ServiceException(e)


    def find_user_by_email(self, email):
        return self.user_repository.find_by_email(email)


    def find_all_users_by_access_profile_id(self, access_profile_id):
        users = self.user_repository.find_all_users_by_access_profile_id(access_profile_id)
        return users


    def delete_user(self, model):
        self.user_repository.delete_user(model)
