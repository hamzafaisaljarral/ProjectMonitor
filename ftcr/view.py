import json

from flask import request, jsonify
from flask_restful import Resource
from resources.errors import mongo_error,sql_server, server_down
from methods import check_mongo, check_api

class PortalMonitoring(Resource):
    # @jwt_required()
    def get(self):
        ftcr = []
        check_mongo_server = check_mongo()
        check_api_server = check_api()
        if check_mongo_server is not True:
            project = 'FTCR(iptv)'
            status_code = 400
            reason = "mongo server down"
            ftcr.extend([project,status_code,reason])
            return ftcr
        elif check_api_server is not True:
            project = 'FTCR(iptv)'
            status_code = 400
            reason = "API not working"
            ftcr.append([project, status_code, reason])
            return ftcr
        project = 'FTCR(iptv)'
        status_code = 200
        reason = "Project working"
        ftcr.append([project, status_code, reason])
        return ftcr







