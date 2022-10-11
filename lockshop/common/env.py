import logging
import os
from re import S

version = os.environ.get("GAE_VERSION")


def is_production():
    return os.environ.get("GOOGLE_CLOUD_PROJECT", "").lower() == "usc-trojan-lockshop"

if is_production():
     """ =====================================================
    PROD Environment
    ========================================================="""
elif not is_production():
    """ =====================================================
    DEV Environment
    ========================================================="""

    NAKED_URL = os.environ.get("NAKED_URL", 'http://127.0.0.1:9090/')
    PRODUCT_NAME = "usc-trojan-lockshop-dev"

    logging.info("Running dev server in local.")
    
    SQL_DB_PASS = "uscfpmlockshop"
    SQL_DB_USER = "root"
    SQL_DB_NAME = "lockshop_db"
    SQL_INSTANCE_URI = f"mysql+pymysql://{SQL_DB_USER}:{SQL_DB_PASS}@localhost/{SQL_DB_NAME}"