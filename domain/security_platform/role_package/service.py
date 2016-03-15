# coding=utf-8

from security_platform.role_package.repositoy import RolePackageRepository
from security_platform.access_profile.service import AccessProfileService
from security_platform.exceptions import ServiceException
from pymongo.errors import DuplicateKeyError, InvalidId


class RolePackageService():


    def __init__(self):
        self.role_package_repository = RolePackageRepository()
        self.access_profile_service = AccessProfileService()


    def find_all(self):
        return self.role_package_repository.find_all()


    def find_all_roles_packages_by_publisher_uuid(self, uuid_publisher):
        return self.role_package_repository.find_by_publisher_uuid(uuid_publisher)


    def find_role_package_by_id(self, role_package_id):
        try:
            return self.role_package_repository.find_by_id(role_package_id)
        except InvalidId as e:
            raise ServiceException(e)


    def create_role_package(self, **kwargs):
        try:
            return self.role_package_repository.create(**kwargs)
        except DuplicateKeyError as e:
            raise ServiceException(e)


    def update_role_package(self, **kwargs):
        return self.role_package_repository.update(**kwargs)


    def find_all_roles_packages_by_role_id(self, role_id):
        roles_packages = self.role_package_repository.find_roles_packages_by_role_id(role_id)
        return roles_packages


    def delete_role_package(self, model):
        access_profiles = self.access_profile_service.find_all_access_profiles_by_role_package_id(model._id)
        if access_profiles is not None and len(access_profiles) is not 0:
            raise ServiceException("Integrity constraint error!")
        self.role_package_repository.delete(model)
