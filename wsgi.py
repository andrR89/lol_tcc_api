# coding=utf-8

from rest import create_app
from flasgger import Swagger

app = create_app('config.default')

app.config['SWAGGER'] = {
    "swagger_version": "2.0",
    "specs": [
        {
            "version": "1.0.0",
            "title": "Security Financial Platform",
            "endpoint": 'v1_spec',
            "route": '/v1/spec',
            "description": "Security Financial Platform API"
        }
    ]
}

Swagger(app)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
