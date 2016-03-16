from flask import Blueprint, jsonify, request

from lol.static_service import HelloLoL

bp = Blueprint('lol-static', __name__)
hello_lol = HelloLoL()


@bp.route("/lol/static/champions", methods=['GET'], )
def find_champions():
    return jsonify(HelloLoL().get_champions(request.args))


@bp.route("/lol/static/champions/<id>", methods=['GET'], )
def find_champions_by_id(id):
    return jsonify(HelloLoL().get_champions_by_id(id, request.args))
