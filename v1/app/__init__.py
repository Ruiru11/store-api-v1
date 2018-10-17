from flask import Flask

from .config import Config_by_name
from app.views.products_views import don_item
from app.views.sales_views import don_sale


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(Config_by_name[config_name])
    app.register_blueprint(don_item)
    app.register_blueprint(don_sale)
    return app
