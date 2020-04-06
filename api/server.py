from flask import Flask, request
from flask_restful import Resource, Api
import book as book_utils

app = Flask(__name__)
app.config['DEBUG'] = True
api = Api(app)


class Book(Resource):
    def get(self, book_id):
        res = book_utils.get(book_id)

        if not res:
            return {'message': 'Not found'}, 404

        return res

    def post(self):
        book_utils.insert()
        return {'success': 'Saved'}, 201


@app.before_request
def authentication():
    token = request.headers.get('X-Token')

    if not token:
        return {'error': 'Token is missing'}, 401


api.add_resource(Book, '/api/v1/books/<string:book_id>', '/api/v1/books')
app.run()
