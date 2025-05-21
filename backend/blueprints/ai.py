
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from ..ai.openai_helper import chat

ai_bp = Blueprint('ai', __name__)

@ai_bp.route('/ask', methods=['POST'])
@jwt_required()
def ask():
    q = request.json.get('question', '')
    return jsonify({'answer': chat(q)})
