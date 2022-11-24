from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# ---------------------------- Metadata Image Entity--------------------------------------

from app.application.model.client.ClientDAO import ClientDAO

# ---------------------------- inventory Entity--------------------------------------

from app.application.model.inventory.InventoryDAO import InventoryDAO
from app.application.model.inventory.ControlerDeviceDAO import ControlerDeviceDAO

# ---------------------------- product Entity--------------------------------------

from app.application.model.product.ControlTechnicalServiceDAO import ControlTechnicalServiceDAO
from app.application.model.product.TechnicalServiceDAO import TechnicalServiceDAO

# ---------------------------- sale Entity--------------------------------------

from app.application.model.sale.PriceDAO import PriceDAO
from app.application.model.sale.PriceInventoryDAO import PriceInventoryDAO
from app.application.model.sale.InvoiceDAO import InvoiceDAO

# ----------------------------- Enum -----------------------------------------------------

from app.application.model.enum.PersitemEnum import PersitemEnum