# coding=utf-8

from ming import schema
from ming.odm import MappedClass, FieldProperty, ForeignIdProperty, RelationProperty
from security_platform import odm_session
from security_platform.access_profile.model import AccessProfile


class User(MappedClass):

    class __mongometa__:
        session = odm_session
        name = 'user'
        unique_indexes = [('email',)]

    _id = FieldProperty(schema.ObjectId)
    name = FieldProperty(schema.String(required=True))
    surname = FieldProperty(schema.String(required=True))
    email = FieldProperty(schema.String(required=True))
    fg_active = FieldProperty(schema.Int(if_missing=1))
    uuid_publisher = FieldProperty(schema.String(required=True))

    _access_profiles = ForeignIdProperty(AccessProfile, uselist=True)
    access_profiles = RelationProperty(AccessProfile)


    def __as_dict__(self):
        access_profiles_list = []
        for access_profile in self.access_profiles:
            access_profiles_list.append(access_profile.__as_dict__())

        return {"_id":str(self._id),"name":self.name,"surname":self.surname, "email":self.email, "access_profiles":access_profiles_list,"fg_active":self.fg_active,"uuid_publisher":self.uuid_publisher}


    def __repr__(self):
        return ""
