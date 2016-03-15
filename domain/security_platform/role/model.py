# coding=utf-8

from ming import schema
from ming.odm import MappedClass, FieldProperty, RelationProperty
from security_platform import odm_session


class Role(MappedClass):

    class __mongometa__:
        session = odm_session
        name = 'role'
        custom_indexes = [
            dict(fields=('name','uuid_publisher',), unique=True)
        ]

    _id = FieldProperty(schema.ObjectId)
    name = FieldProperty(schema.String(required=True))
    description = FieldProperty(schema.String(required=True))
    uuid_publisher = FieldProperty(schema.String(required=True))

    roles_packages = RelationProperty('RolePackage')


    def __as_dict__(self):
        return {"_id":str(self._id),"name":self.name,"description":self.description,"uuid_publisher":self.uuid_publisher}


    def __repr__(self):
        return ""
