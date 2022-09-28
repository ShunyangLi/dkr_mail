from app import api
from flask import make_response, jsonify, request
from flask_restplus import abort, Resource
from utils.request_handling import get_request_args,get_header
from utils.db_handling import query_db
from utils.presenter_handling import handle_presenter, handle_upload
from utils.update_presenter import update_presenter

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
        # handle_presenter(nstudents, nnstudents, ndate, nndate)
        print(nstudents, nnstudents, ndate, nndate)
        return make_response(jsonify({"message": "send success"}), 200)


@mails.route('/notice')
class Notice(Resource):
    @mails.response(200, 'Success')
    @mails.response(400, 'Missing args')
    @mails.doc(description="Three presenters and their present date")
    def post(self):
        students = get_request_args("student", str)
        students = students.split(',')
        handle_upload(students)
        return make_response(jsonify({"message": "send success"}), 200)


@mails.route('/history')
class History(Resource):
    @mails.response(200, 'Success')
    @mails.response(400, 'Missing args')
    @mails.doc(description="Three presenters and their present date")
    def get(self):
        data = query_db("select name, count(name) as number from past group by name")

        return make_response(jsonify({"message": "success", "data": data}), 200)


@mails.route('/current')
class Current(Resource):
    @mails.response(200, 'Success')
    def get(self):
        names = []
        data = query_db("select name from current")
        for d in data:
            names.append(d["name"])
        return make_response(jsonify({"message": "success", "names": names}), 200)


@mails.route('/get-user-info')
class GetUserInfo(Resource):

    @mails.response(200, 'Success')
    @mails.doc(description="Return all the users with their username")
    def get(self):
        users = query_db("select * from contact")
        for index, user in enumerate(users):
            user["key"] = index + 1
        return make_response(jsonify({"message": "success", "users": users}), 200)


@mails.route('/edit')
class GetUserInfo(Resource):

    @mails.response(200, 'Success')
    @mails.response(400, 'Missing args')
    @mails.param("name", "Student name")
    @mails.param("email", "Student email")
    @mails.param("institution", "Student institution")
    @mails.doc(description="Add new student")
    def post(self):
        name = get_request_args("name", str)
        email = get_request_args("email", str)
        institution = get_request_args("institution", str)

        query_db("insert into contact values(?,?,?)", (name, email, institution, ))
        return make_response(jsonify({"message": "success"}), 200)

    @mails.response(200, 'Success')
    @mails.param("name", "Student name")
    @mails.param("email", "Student email")
    @mails.response(400, 'Missing args')
    @mails.doc(description="Update student information")
    def put(self):
        name = get_request_args("name", str)
        email = get_request_args("email", str)

        query_db("update contact set email = ? where name = ?", (email, name, ))
        return make_response(jsonify({"message": "success"}), 200)


@mails.route('/delete')
class DeleteUserInfo(Resource):
    @mails.response(200, 'Success')
    @mails.param("name", "Student name")
    @mails.response(400, 'Missing args')
    @mails.doc(description="delete student information")
    def post(self):
        name = get_request_args("name", str)
        print(name)

        query_db("delete from contact where name = ?", (name,))
        return make_response(jsonify({"message": "success"}), 200)


@mails.route('/next')
class NextWeekP(Resource):
    @mails.response(200, 'Success')
    @mails.doc(description="return next week's presenters")
    def get(self):
        data = query_db("select name, email, institution, present from current ")
        for index, d in enumerate(data):
            d["key"] = index + 1

        return make_response(jsonify({"message": "success", "data": data}), 200)

    @mails.response(400, 'Missing args')
    def put(self):
        name = get_request_args("name", str)
        email = get_request_args("email", str)
        institution = get_request_args("institution", str)

        query_db("update current set name = ?, email = ? where institution = ?", (name, email, institution))
        update_presenter(email, True)

        return make_response(jsonify({"message": "success"}), 200)


@mails.route('/nnext')
class NNextWeekP(Resource):
    @mails.response(200, 'Success')
    @mails.doc(description="return next next week's presenters")
    def get(self):
        data = query_db("select name, email, institution, present from next ")
        for index, d in enumerate(data):
            d["key"] = index + 1

        return make_response(jsonify({"message": "success", "data": data}), 200)

    @mails.response(400, 'Missing args')
    def put(self):
        name = get_request_args("name", str)
        email = get_request_args("email", str)
        institution = get_request_args("institution", str)

        query_db("update next set name = ?, email = ? where institution = ?", (name, email, institution))
        update_presenter(email, False)
        return make_response(jsonify({"message": "success"}), 200)


