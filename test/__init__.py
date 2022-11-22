from app import app as application
from config import test_config as config
import pytest
from app.application.model import db


@pytest.fixture()
def app():
    app = application
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": config.SQLALCHEMY_DATABASE_URI
    })
    # app.config.from_object(config)

    with app.app_context():
        if config.DB_SCHEMA_NAME != "":
            table_names = list(db.metadata.tables.keys())
            for name in table_names:
                db.metadata.tables[name].schema = config.DB_SCHEMA_NAME
        db.drop_all()
        db.create_all()
    # other setup can go here
    yield app
    # clean up / reset resources here


@pytest.fixture()
def ctx(app):
    with app.app_context() as ctx:
        yield ctx

@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
