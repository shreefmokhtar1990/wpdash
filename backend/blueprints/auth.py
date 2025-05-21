
from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from ..extensions import db
from ..models import User

auth_bp = Blueprint('auth', __name__, url_prefix='/api/auth')

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    user = User.query.filter_by(email=email).first()
    if user and user.check_password(password):
        token = create_access_token(identity={'id': user.id, 'email': email, 'role': user.role})
        return jsonify({'token': token})
    return jsonify({'msg': 'Bad credentials'}), 401
