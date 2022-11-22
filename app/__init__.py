from flask import Flask
import logging
from config import Config
from flask_cors import CORS

print("init {0}...".format(Config.APP_NAME))

try:
	app = Flask(__name__)
	CORS(app)
	app.debug = True



	# add settings folder system

	app.setting_config_name_app = Config.APP_NAME

	from app.application.Route import Route
	from app.application.model import db
	
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
	app.config.from_object(Config)
	Route(app)
	""" """
	db.init_app(app)


	with app.app_context():
		table_names = list(db.metadata.tables.keys())
		for name in table_names:
			db.metadata.tables[name].schema = Config.DB_SCHEMA_NAME
		db.create_all()

	

except Exception as e:
	print("Error app -> {0}".format(e))
	raise e

print("================================================================")
print("start {0}...\n launch: on \nhost:{1}\nport:{2}".format(
	Config.APP_NAME,
	Config.APP_HOST,
	Config.APP_PORT
	))


if __name__ == '__main__':
    app.run(host = "0.0.0.0")