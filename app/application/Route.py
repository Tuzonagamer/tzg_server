from app.application.routes.main.Welcome import Welcome
from app.application.routes.inventory.Inventory import Inventory

class Route:
	def __init__(self, app):
		"""
		Route class Route, 
		:autor: Jajoya
		:date: 2022-11-23
		"""
		print("------------------ Launch Context -----------------------------")
		
		
		Welcome(app,title=app.setting_config_name_app)
		Inventory(app)
		print("---------------------------------------------------------------")