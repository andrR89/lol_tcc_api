# coding=utf-8

from security_platform.abstract_repository import AbstractRepository
from security_platform.role_package.model import RolePackage
from bson.objectid import ObjectId


class RolePackageRepository(AbstractRepository):

    __model__ = RolePackage


    def find_roles_packages_by_role_id(self, role_id):
        roles_packages = self.__model__.query.find({'_roles':ObjectId(role_id)}).all()
        return roles_packages
