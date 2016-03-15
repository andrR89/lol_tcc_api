# coding=utf-8

from ming import schema
from ming.odm import MappedClass, FieldProperty, ForeignIdProperty, RelationProperty
from security_platform import odm_session
from security_platform.role_package.model import RolePackage


class AccessProfile(MappedClass):

    class __mongometa__:
        session = odm_session
        name = 'access_profile'
        custom_indexes = [
            dict(fields=('name','uuid_publisher',), unique=True)
        ]

    _id = FieldProperty(schema.ObjectId)
    name = FieldProperty(schema.String(required=True))
    description = FieldProperty(schema.String(required=True))
    id_group = FieldProperty(schema.Int(required=True))
    uuid_publisher = FieldProperty(schema.String(required=True))

    _roles_packages = ForeignIdProperty(RolePackage, uselist=True)
    roles_packages = RelationProperty(RolePackage)

    users = RelationProperty('User')


    def __as_dict__(self):
        roles_packages_list = []
        for roles_package in self.roles_packages:
            roles_packages_list.append(roles_package.__as_dict__())

        return {"_id":str(self._id),"name":self.name,"description":self.description, "roles_packages":roles_packages_list,"uuid_publisher":self.uuid_publisher,"id_group":self.id_group}


    def __repr__(self):
        return ""
