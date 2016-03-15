# coding=utf-8

from flasgger.utils import swag_from
from flask import Blueprint, request, abort
from security_platform.role_package.service import RolePackageService
import json


bp = Blueprint('roles-packages', __name__)
role_package_service = RolePackageService()

@swag_from('swagger/role-package/get.yml')
@bp.route("/roles-packages", methods=['GET'])
def find_all():
    response = role_package_service.find_all()
    if response is None or len(response) is 0:
        return '', 204
    return json.dumps(__as_dict_array___(response))


@swag_from('swagger/role-package/get-by-id.yml')
@bp.route("/roles-packages/<id>", methods=['GET'])
def find_by_id(id):
    response = role_package_service.find_role_package_by_id(id)
    if response is None:
        return '', 404
    return json.dumps(response.__as_dict__())


@swag_from('swagger/role-package/get-by-publisher-uuid.yml')
@bp.route("/roles-packages/publisher/<uuid>", methods=['GET'])
def find_all_by_publisher_uuid(uuid):
    response = role_package_service.find_all_roles_packages_by_publisher_uuid(uuid)
    if response is None or len(response) is 0:
        return '', 404
    return json.dumps(__as_dict_array___(response))


@swag_from('swagger/role-package/post.yml')
@bp.route("/roles-packages", methods=['POST'])
def create():
    if not request.json:
        abort(400)
    response = role_package_service.create_role_package(**request.json)
    return json.dumps(response.__as_dict__())


@swag_from('swagger/role-package/put.yml')
@bp.route("/roles-packages/<id>", methods=['PUT'])
def update(id):
    if not request.json:
        abort(400)
    response = role_package_service.find_role_package_by_id(id)
    if response is None:
        return '', 404
    role_updated = role_package_service.update_role_package(**request.json)
    return json.dumps(role_updated.__as_dict__())


@swag_from('swagger/role-package/delete.yml')
@bp.route("/roles-packages/<id>", methods=['DELETE'])
def delete(id):
    model = role_package_service.find_role_package_by_id(id)
    if model is None:
        return '', 404
    role_package_service.delete_role_package(model)
    return '', 204


#REMOVER e Criar/Utilizar JsonEncoder
def __as_dict_array___(array):
    list = []
    for role_package in array:
        list.append(role_package.__as_dict__())
    return list
