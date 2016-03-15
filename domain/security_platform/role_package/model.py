# coding=utf-8

from ming import schema
from ming.odm import MappedClass, FieldProperty, ForeignIdProperty, RelationProperty
from security_platform import odm_session
from security_platform.role.model import Role


class RolePackage(MappedClass):

    class __mongometa__:
        session = odm_session
        name = 'role_package'
        custom_indexes = [
            dict(fields=('name','uuid_publisher',), unique=True)
        ]

    _id = FieldProperty(schema.ObjectId)
    name = FieldProperty(schema.String(required=True))
    description = FieldProperty(schema.String(required=True))
    uuid_publisher = FieldProperty(schema.String(required=True))

    _roles = ForeignIdProperty(Role, uselist=True)
    roles = RelationProperty(Role)

    users = RelationProperty('AccessProfile')


    def __as_dict__(self):
        roles_list = []
        for role in self.roles:
            roles_list.append(role.__as_dict__())

        return {"_id":str(self._id),"name":self.name,"description":self.description, "roles":roles_list,"uuid_publisher":self.uuid_publisher}


    def __repr__(self):
        return ""
