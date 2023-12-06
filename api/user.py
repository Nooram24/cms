from flask import Blueprint, jsonify, request
from models import Test

bp=Blueprint('user', __name__)

@bp.get('/test/')
def test_get():
    data= Test.objects
    return jsonify(success=True, message='',data=data), 200

@bp.post('/test/')
def test_post():
    Test(**request.json).save()
    return jsonify(success=True, message='',data=None), 200



