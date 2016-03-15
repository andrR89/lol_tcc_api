# coding=utf-8

from security_platform.abstract_repository import AbstractRepository
from security_platform.access_profile.model import AccessProfile
from bson.objectid import ObjectId


class AccessProfileRepository(AbstractRepository):

    __model__ = AccessProfile


    def find_all_access_profiles_by_role_package_id(self, role_package_id):
        access_profiles = self.__model__.query.find({'_roles_packages':ObjectId(role_package_id)}).all()
        return access_profiles
