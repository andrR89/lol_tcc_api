# coding=utf-8

from security_platform.role.repositoy import RoleRepository
from security_platform.role_package.service import RolePackageService
from security_platform.exceptions import ServiceException
from pymongo.errors import DuplicateKeyError, InvalidId


class RoleService():


    def __init__(self):
        self.role_repository = RoleRepository()
        self.role_package_service = RolePackageService()


    def find_all(self):
        return self.role_repository.find_all()


    def find_all_roles_by_publisher_uuid(self, uuid_publisher):
        return self.role_repository.find_by_publisher_uuid(uuid_publisher)


    def find_role_by_id(self, role_id):
        try:
            return self.role_repository.find_by_id(role_id)
        except InvalidId as e:
            raise ServiceException(e)


    def create_role(self, **kwargs):
        try:
            return self.role_repository.create(**kwargs)
        except DuplicateKeyError as e:
            raise ServiceException(e)


    def update_role(self, **kwargs):
        return self.role_repository.update(**kwargs)


    def delete_role(self, model):
        roles_packages = self.role_package_service.find_all_roles_packages_by_role_id(model._id)
        if roles_packages is not None and len(roles_packages) is not 0:
            raise ServiceException("Integrity constraint error!")
        self.role_repository.delete(model)
