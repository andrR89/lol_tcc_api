# coding=utf-8

from flasgger.utils import swag_from
from flask import Blueprint, request, abort
from security_platform.role.service import RoleService
import json


bp = Blueprint('roles', __name__)
role_service = RoleService()

@swag_from('swagger/role/get.yml')
@bp.route("/roles", methods=['GET'])
def find_all():
    response = role_service.find_all()
    if response is None or len(response) is 0:
        return '', 204
    return json.dumps(__json_array__(response))


@swag_from('swagger/role/get-by-id.yml')
@bp.route("/roles/<id>", methods=['GET'])
def find_by_id(id):
    response = role_service.find_role_by_id(id)
    if response is None:
        return '', 404
    return json.dumps(response.__as_dict__())


@swag_from('swagger/role/get-by-publisher-uuid.yml')
@bp.route("/roles/publisher/<uuid>", methods=['GET'])
def find_all_by_publisher_uuid(uuid):
    response = role_service.find_all_roles_by_publisher_uuid(uuid)
    if response is None or len(response) is 0:
        return '', 404
    return json.dumps(__json_array__(response))


@swag_from('swagger/role/post.yml')
@bp.route("/roles", methods=['POST'])
def create():
    if not request.json:
        abort(400)
    response = role_service.create_role(**request.json)
    return json.dumps(response.__as_dict__())


@swag_from('swagger/role/put.yml')
@bp.route("/roles/<id>", methods=['PUT'])
def update(id):
    if not request.json:
        abort(400)
    response = role_service.find_role_by_id(id)
    if response is None:
        return '', 404
    role_updated = role_service.update_role(**request.json)
    return json.dumps(role_updated.__as_dict__())


@swag_from('swagger/role/delete.yml')
@bp.route("/roles/<id>", methods=['DELETE'])
def delete(id):
    model = role_service.find_role_by_id(id)
    if model is None:
        return '', 404
    role_service.delete_role(model)
    return '', 204


#REMOVER e Criar/Utilizar JsonEncoder
def __json_array__(array):
    list = []
    for a in array:
        list.append(a.__as_dict__())
    return list
