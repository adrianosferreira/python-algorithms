from flask import request
import redis

r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)


def insert():
    r.hset('books%d' % request.get_json()['book_id'], 'id', request.get_json()['book_id'])
    r.hset('books%d' % request.get_json()['book_id'], 'name', request.get_json()['book_name'])


def get(id):

    if not r.hget('books%s' % id, 'id'):
        return None

    data = {
        'id': r.hget('books%s' % id, 'id'),
        'name': r.hget('books%s' % id, 'name')
    }

    return data
