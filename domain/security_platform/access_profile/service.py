# coding=utf-8

from security_platform.access_profile.repositoy import AccessProfileRepository
from security_platform.user.service import UserService
from security_platform.exceptions import ServiceException
from pymongo.errors import DuplicateKeyError, InvalidId


class AccessProfileService():


    def __init__(self):
        self.access_profile_repository = AccessProfileRepository()
        self.user_service = UserService()


    def find_all(self):
        return self.access_profile_repository.find_all()


    def find_all_access_profiles_by_publisher_uuid(self, uuid_publisher):
        return self.access_profile_repository.find_by_publisher_uuid(uuid_publisher)


    def find_access_profile_by_id(self, access_profile_id):
        try:
            return self.access_profile_repository.find_by_id(access_profile_id)
        except InvalidId as e:
            raise ServiceException(e)


    def create_access_profile(self, **kwargs):
        try:
            return self.access_profile_repository.create(**kwargs)
        except DuplicateKeyError as e:
            raise ServiceException(e)


    def update_access_profile(self, **kwargs):
        return self.access_profile_repository.update(**kwargs)


    def find_all_access_profiles_by_role_package_id(self, role_package_id):
        access_profiles = self.access_profile_repository.find_all_access_profiles_by_role_package_id(role_package_id)
        return access_profiles


    def delete_access_profile(self, model):
        users = self.user_service.find_all_users_by_access_profile_id(model._id)
        if users is not None and len(users) is not 0:
            raise ServiceException("Integrity constraint error!")
        self.access_profile_repository.delete(model)
