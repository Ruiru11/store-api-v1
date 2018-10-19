from flask import Flask

from .config import Config_by_name
from app.views.products_views import don_item
from app.views.sales_views import don_sale
from app.views.users_views import don_user


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(Config_by_name[config_name])
    app.register_blueprint(don_item)
    app.register_blueprint(don_sale)
    app.register_blueprint(don_user)

    @app.route('/')
    def root():
        return redirect("https://documenter.getpostman.com/view/5475581/RWguwbzr")
    return app
