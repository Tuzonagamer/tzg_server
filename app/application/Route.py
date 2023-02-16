from app.application.routes.main.Welcome import Welcome
from app.application.routes.inventory.Inventory import Inventory
from app.application.routes.price.Price import Price
from app.application.routes.enum.Enum import Enum
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
		Price(app)
		Enum(app)
		print("---------------------------------------------------------------")