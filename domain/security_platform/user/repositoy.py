# coding=utf-8

from security_platform.abstract_repository import AbstractRepository
from security_platform.user.model import User
from bson.objectid import ObjectId


class UserRepository(AbstractRepository):

    __model__ = User


    def find_by_email(self, email):
        model = self.__model__.query.find({'email':email}).first()
        return model


    def find_all_users_by_access_profile_id(self, access_profile_id):
        access_profiles = self.__model__.query.find({'_access_profiles':ObjectId(access_profile_id)}).all()
        return access_profiles


    def delete_user(self, model):
        self.__model__.query.update({'_id': model._id}, {'$set': {'fg_active':0}})
        self.__commit__()
