import re

from flask import Flask, jsonify

app = Flask(__name__)

from flask import request
from flasgger import Swagger,LazyString,LazyJSONEncoder
from flasgger import swag_from

app.json_encoder = LazyJSONEncoder

swagger_template = {"swagger":"2.0",
    "info" : {
        "title": "API Documentation for Data Processing and Modeling",
        "version" :"1.0.0",
        "description" :"Dokumentasi API untuk Data Processing and Modeling",
    },
}
    
swagger_config = {
    "headers":[],
    "specs": [
        {
            "endpoint": 'docs',
            "route": '/docs.json'
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/docs/"
}
swagger = Swagger(app, template=swagger_template,
                 config=swagger_config)

@swag_from("docs/hello_world.yml", methods=['GET'])
@app.route('/',methods=['GET'])
def hello_world():
    json_response = {
        'status_code':200,
        'description': "Menyapa Hello World",
        'data': "Hello World",
    }
    
    response_data = jsonify(json_response)
    return response_data

@app.route('/text', methods=['GET'])
def text():
    json_response = {
        'status_code': 200,
        'description': "Original Text",
        'data': "Hello, apa kabar semua?"
    }

    response_data = jsonify(json_response)
    return response_data

@app.route('/text-clean', methods=['GET'])
def text_clean():
    json_response = {
        'status_code': 200,
        'description' : "Original Text",
        'data': re.sub(r'[^a-zA-Z0-9]',' ',"Hello Apa Kabar Semua?" ),
    }

    response_data = jsonify(json_response)
    return response_data 


if __name__ == '__main__':
    app.run()