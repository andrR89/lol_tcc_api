# coding=utf-8

from security_platform import odm_session
from bson.objectid import ObjectId


class AbstractRepository(object):

    __model__ = None


    def __commit__(self):
        try:
            odm_session.flush()
            odm_session.clear()
        except Exception as e:
            odm_session.clear()
            raise e


    def find_all(self):
        return self.__model__.query.find().all()


    def find_by_id(self, id):
        return self.__model__.query.get(_id=ObjectId(id))


    def find_by_publisher_uuid(self, uuid_publisher):
        return self.__model__.query.find({'uuid_publisher':uuid_publisher}).all()


    def create(self, **kwargs):
        model = self.__model__(**kwargs)
        self.__commit__()
        return model


    def update(self, **kwargs):
        id = kwargs['_id']
        kwargs.pop("_id", None)
        return self.__model__.query.find_and_modify(query={'_id': ObjectId(id)}, update={'$set': kwargs}, new=True)


    def delete(self, model):
        self.__model__.query.remove({'_id': model._id})
        self.__commit__()
