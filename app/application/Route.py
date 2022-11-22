from app.application.routes.main.Welcome import Welcome

class Route:
	def __init__(self, app):
		"""Route class
		:autor: Jajoya
		:date: 2021-09-13
		"""
		Welcome(app,title=app.setting_config_name_app)