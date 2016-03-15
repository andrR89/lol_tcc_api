# coding=utf-8

from flasgger.utils import swag_from
from flask import Blueprint, request, abort
from security_platform.user.service import UserService
import json


bp = Blueprint('users', __name__)
user_service = UserService()

@swag_from('swagger/user/get.yml')
@bp.route("/users", methods=['GET'])
def find_all():
    response = user_service.find_all()
    if response is None or len(response) is 0:
        return '', 204
    return json.dumps(__as_dict_array___(response))


@swag_from('swagger/user/get-by-publisher-uuid.yml')
@bp.route("/users/publisher/<uuid>", methods=['GET'])
def find_all_by_publisher_uuid(uuid):
    response = user_service.find_all_users_by_publisher_uuid(uuid)
    if response is None or len(response) is 0:
        return '', 404
    return json.dumps(__as_dict_array___(response))


@swag_from('swagger/user/find_by_email.yml')
@bp.route("/users/<email>", methods=['GET'])
def find_by_email(email):
    response = user_service.find_user_by_email(email)
    if response is None:
        return '', 404
    return json.dumps(response.__as_dict__())


@swag_from('swagger/user/post.yml')
@bp.route("/users", methods=['POST'])
def create():
    if not request.json:
        abort(400)
    response = user_service.create_user(**request.json)
    return json.dumps(response.__as_dict__())


@swag_from('swagger/user/put.yml')
@bp.route("/users/<id>", methods=['PUT'])
def update(id):
    if not request.json:
        abort(400)
    response = user_service.find_user_by_id(id)
    if response is None:
        return '', 404
    role_updated = user_service.update_user(**request.json)
    return json.dumps(role_updated.__as_dict__())


#REMOVER e Criar/Utilizar JsonEncoder
def __as_dict_array___(array):
    list = []
    for user in array:
        list.append(user.__as_dict__())
    return list
