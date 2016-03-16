# coding=utf-8

from flask import Flask
import os
import pkgutil
import importlib
from flask import Blueprint
from flask_cors import CORS


def create_app(config_name):
    """
    Create Flask application
    :param config_name:
    :return: app
    """

    #Create Flask configuration
    app = Flask(__name__)
    app.config.from_object(config_name)

    #Create cors configuration
    CORS(app, resources={r"/api/*": {"origins": "*"}})


    #Register blueprints
    register_blueprints(app)

    return app



def register_blueprints(app):
    """
    Register all blueprints
    :param app: Flask app
    :return: register
    """
    package_name = __name__
    package_path = __path__

    register = []
    for _, name, _ in pkgutil.iter_modules(package_path):
        module = importlib.import_module('%s.%s' % (package_name, name))
        for item in dir(module):
            item = getattr(module, item)
            if isinstance(item, Blueprint):
                app.register_blueprint(item)
            register.append(item)

    return register