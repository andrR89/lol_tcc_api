from flasgger.utils import swag_from
from flask import Blueprint, jsonify, request

from domain.lol.static_service import HelloLoL

bp = Blueprint('lol-static', __name__)
hello_lol = HelloLoL()

@swag_from('swagger/champions/get.yml')
@bp.route("/lol/static/champions", methods=['GET'], )
def find_champions():
    return jsonify(HelloLoL().get_champions(request.args))

@swag_from('swagger/champions/get_id.yml')
@bp.route("/lol/static/champions/<id>", methods=['GET'], )
def find_champions_by_id(id):
    return jsonify(HelloLoL().get_champions_by_id(id, request.args))
