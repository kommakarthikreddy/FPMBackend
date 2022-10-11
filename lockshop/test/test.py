from flask import request

from lockshop.skel.skel_res import SkelRes
from lockshop.sql_util.utils import session_wrap
from .models import TestTable
import logging


@SkelRes()
def test_custom_get():
    logging.info("You hit the test_custom_get method successfully.")
    return {
        "_code": 200,
        "message": "Your custom get route is successfully working"
    }


@SkelRes()
def test_custom_error():
    logging.info("You hit the test_custom_error method successfully.")
    return {
        "_code": 500,
        "message": "Your custom error route is successfully working."
    }


@SkelRes()
def test_custom_post():
    logging.info("You hit the test_custom_post method successfully.")
    request_body = request.get_json()
    logging.info(f"request_body: {request_body}")
    return {
        "_code": 200,
        "message": "Your custom post route is successfully working",
        "body": request_body
    }

@session_wrap()
@SkelRes()
def test_database_post(session, *args, **kwargs):
    logging.info("You hit the test_database_post method successfully.")
    request_body = request.get_json()
    message = request_body.get("message")
    logging.info(f"request_body: {request_body}")
    if not message:
        logging.error("'message' param missing in the body.")
        return {
            "_code": 400,
            "message": "'message' param missing in the body."
        }

    test_record = TestTable.create(message=message, session=session)
    session.commit()
    
    
    return {
        "_code": 200,
        "message": "Success",
        "test_record": test_record.sanitize()
    }


@session_wrap()
@SkelRes()
def test_database_get(session, *args, **kwargs):
    logging.info("You hit test_database_get method successfully")
    id = request.args.get("id")
    data = None
    if id:
        test_record = TestTable.get_by_id(session=session, id=int(id))
        if not test_record:
            return {
                "_code": 400,
                "message": f"No record found with id: {id}",
            }
        data = test_record.sanitize()
    else:
        records = TestTable.get_all(session=session)
        data = [record.sanitize() for record in records]
    
    return {
        "_code": 200,
        "message": "Success",
        "test_record": data
    }
