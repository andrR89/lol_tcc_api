# coding=utf-8

from flasgger.utils import swag_from
from flask import Blueprint, request, abort

from lol.hello_lol import HelloLoL
from security_platform.access_profile.service import AccessProfileService
import json
import simplejson

bp = Blueprint('access-profiles', __name__)
access_profile_service = AccessProfileService()

@swag_from('swagger/access-profile/get.yml')
@bp.route("/access-profiles", methods=['GET'])
def find_all():
    response = access_profile_service.find_all()
    if response is None or len(response) is 0:
        return '', 204
    return json.dumps(__as_dict_array___(response))

@bp.route("/lol/static",  methods=['GET'])
def find_static():
    return simplejson.dumps(HelloLoL().get_all_lores(), ensure_ascii=False)

@swag_from('swagger/access-profile/get-by-id.yml')
@bp.route("/access-profiles/<id>", methods=['GET'])
def find_by_id(id):
    response = access_profile_service.find_access_profile_by_id(id)
    if response is None:
        return '', 404
    return json.dumps(response.__as_dict__())


@swag_from('swagger/access-profile/get-by-publisher-uuid.yml')
@bp.route("/access-profiles/publisher/<uuid>", methods=['GET'])
def find_all_by_publisher_uuid(uuid):
    response = access_profile_service.find_all_access_profiles_by_publisher_uuid(uuid)
    if response is None or len(response) is 0:
        return '', 404
    return json.dumps(__as_dict_array___(response))


@swag_from('swagger/access-profile/post.yml')
@bp.route("/access-profiles", methods=['POST'])
def create():
    if not request.json:
        abort(400)
    response = access_profile_service.create_access_profile(**request.json)
    return json.dumps(response.__as_dict__())


@swag_from('swagger/access-profile/put.yml')
@bp.route("/access-profiles/<id>", methods=['PUT'])
def update(id):
    if not request.json:
        abort(400)
    response = access_profile_service.find_access_profile_by_id(id)
    if response is None:
        return '', 404
    role_updated = access_profile_service.update_access_profile(**request.json)
    return json.dumps(role_updated.__as_dict__())


@swag_from('swagger/access-profile/delete.yml')
@bp.route("/access-profiles/<id>", methods=['DELETE'])
def delete(id):
    model = access_profile_service.find_access_profile_by_id(id)
    if model is None:
        return '', 404
    access_profile_service.delete_access_profile(model)
    return '', 204


#REMOVER e Criar/Utilizar JsonEncoder
def __as_dict_array___(array):
    list = []
    for access_profile in array:
        list.append(access_profile.__as_dict__())
    return list
