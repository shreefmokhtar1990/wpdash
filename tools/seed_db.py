
import os, sys
sys.path.append('.')
from backend.app import create_app
from backend.extensions import db
from backend.models import User, Site

app = create_app()
with app.app_context():
    email = os.getenv('ADMIN_EMAIL', 'admin@example.com')
    password = os.getenv('ADMIN_PASSWORD', 'password')
    if not User.query.filter_by(email=email).first():
        u = User(email=email, role='admin')
        u.set_password(password)
        db.session.add(u)
        db.session.commit()
        print('Admin user created')
    else:
        print('Admin already exists')
    if not Site.query.first():
        s = Site(name='Demo WP', url='http://localhost:8080')
        db.session.add(s)
        db.session.commit()
        print('Demo site added')
