
from flask import Flask, jsonify
from .config import Config
from .extensions import db, migrate, jwt, metrics
from .blueprints.auth import auth_bp
from .blueprints.sites import sites_bp
from .blueprints.ai import ai_bp

def create_app():
    app = Flask(__name__, static_folder=None)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    metrics.init_app(app)

    app.register_blueprint(auth_bp)
    app.register_blueprint(sites_bp, url_prefix='/api/sites')
    app.register_blueprint(ai_bp, url_prefix='/api/ai')

    @app.route('/api/ping')
    def ping():
        return jsonify({'msg': 'pong'})

    return app
