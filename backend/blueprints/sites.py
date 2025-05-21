
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from ..extensions import db
from ..models import Site

sites_bp = Blueprint('sites', __name__)

@sites_bp.route('/', methods=['GET'])
@jwt_required()
def list_sites():
    sites = Site.query.all()
    return jsonify([{'id': s.id, 'name': s.name, 'url': s.url} for s in sites])

@sites_bp.route('/', methods=['POST'])
@jwt_required()
def add_site():
    data = request.get_json()
    site = Site(name=data['name'], url=data['url'])
    db.session.add(site)
    db.session.commit()
    return jsonify({'id': site.id})
