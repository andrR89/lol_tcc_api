# coding=utf-8

from security_platform.abstract_repository import AbstractRepository
from security_platform.role.model import Role


class RoleRepository(AbstractRepository):

    __model__ = Role
