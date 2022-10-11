from main import app
from lockshop.sql_util.utils import Base, engine
import lockshop.test as test

Base.metadata.create_all(engine)

api_routes = []
api_routes += test.api_routes

def configure_app_routes():
    for route in api_routes:
        api_url = route[0]
        handler = route[1]
        methods = route[2]
        app.add_url_rule(api_url, "{}|{}".format(route, handler), handler, methods=methods)
