from app import api
from flask import make_response, jsonify, request
from flask_restplus import abort, Resource
from utils.request_handling import get_request_args,get_header
from utils.db_handling import query_db
from utils.presenter_handling import handle_presenter, handle_upload

mails = api.namespace('user', description="Get all the user names")


@mails.route('/get-user')
class GetUser(Resource):

    @mails.response(200, 'Success')
    @mails.doc(description="Return all the users with their username")
    def get(self):
        names = []
        data = query_db("select name from contact")
        for user in data:
            names.append(user["name"])

        return make_response(jsonify({"message": "success", "names": names}), 200)


@mails.route('/send')
class Send(Resource):

    @mails.response(200, 'Success')
    @mails.response(400, 'Missing args')
    @mails.doc(description="Three presenters and their present date")
    def post(self):
        nstudents = get_request_args("nstudents", str)
        nnstudents = get_request_args("nnstudents", str)

        ndate = get_request_args("ndate", str)
        nndate = get_request_args("nndate", str)

        nstudents = nstudents.split(',')
        nnstudents = nnstudents.split(',')

        if len(nstudents) < 3 or len(nnstudents) < 3:
            abort(403, message="Not enough students")
        print(nstudents, nnstudents, ndate, nndate)
        # handle_presenter(nstudents, nnstudents, ndate, nndate)
        return make_response(jsonify({"message": "send success"}), 200)


@mails.route('/notice')
class Notice(Resource):
    @mails.response(200, 'Success')
    @mails.response(400, 'Missing args')
    @mails.doc(description="Three presenters and their present date")
    def post(self):
        handle_upload()
        return make_response(jsonify({"message": "send success"}), 200)


@mails.route('/history')
class History(Resource):
    @mails.response(200, 'Success')
    @mails.response(400, 'Missing args')
    @mails.doc(description="Three presenters and their present date")
    def get(self):
        data = query_db("select name, count(name) as number from past group by name")

        return make_response(jsonify({"message": "success", "data": data}), 200)





