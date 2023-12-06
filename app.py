from flask import Flask
from api.user import bp as user
from api.admin import bp as admin
from extensions import db
app=Flask(__name__)
app.config.from_pyfile('settings.py')
db.init_app(app)
app.register_blueprint(admin, url_prefix='/admin')
app.register_blueprint(user, url_prefix='/user')
app.run(debug=True)