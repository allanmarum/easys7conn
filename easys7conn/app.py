# -*- coding: utf-8 -*-
"""

    easys7conn.app

    The Restful API. 

"""

from flask import Flask, request, jsonify
from flask_restful import Resource, Api, fields, marshal_with

app = Flask(__name__)
api = Api(app)

class ReadData(Resource):
    def get(self):
        """Return data from S7 PLC Datablock."""
        return {'message': 'value'}, 200

class WriteData(Resource):
    """Write data to S7 PLC Datablock."""
    def put(self):
        """Write data to S7 PLC Datablock."""
        auth = request.headers['X-Api-Key']
        if auth == 'key':
            return {'message': 'value'}, 201
        else:
            return {"message": "ERROR: Unauthorized"}, 401

class GetSystemInfo(Resource):
    """Return system information from S7 300/400 PLC."""
    def get(self):
        """Return system information from S7 300/400 PLC."""
        return {'message': 'value'}, 200

@app.route('/')
def api_doc():
    return 'To be implemented.'

read_data_path = '/read-data/'    
api.add_resource(ReadData, read_data_path)

write_data_path = '/write-data/'    
api.add_resource(WriteData, write_data_path)

get_system_info = '/get-system-info/'    
api.add_resource(GetSystemInfo, get_system_info)

def main():
    app.run('127.0.0.1', debug=True)

if __name__ == "__main__":
    main()