from flask import request
import logging
from lockshop.skel.skel_res import SkelRes
from lockshop.sql_util.utils import session_wrap
from .models import DoorCategory

@session_wrap()
@SkelRes()
def PostDoorCategory(session, *args, **kwargs):
    logging.info("You hit the floor_post method successfully.")
    request_body = request.get_json()
    logging.info(f"request_body: {request_body}")
    if not request_body:
        logging.error("Missing the request body.")
        return {
            "_code": 400,
            "message": "Missing the request body."
        }
    name = request_body.get ("name")
    if name == None:
        logging.error("'name' param missing in the body.")
        return {
            "_code": 400,
            "message": "name param missing in the body."
        }
    floor_data = DoorCategory.create(session=session, name=name)
    session.commit()

    return {
        "_code": 200,
        "message": "Success",
        "test_record": floor_data.sanitize()
    }


@session_wrap()
@SkelRes()
def GetDoorCategory(session, *args, **kwargs):
    logging.info("You hit floot_get method successfully")
    request_body = request.get_json()
    id = request_body.get("id")
    data = None

    if id == None:
        return {
            "_code": 200,
            "message": "error",
            "door_category": None,
            "reason": "id is empty"
        }

    door_category_data = DoorCategory.get_by_id(session=session, id=int(id))
    if not door_category_data:
        return {
            "_code": 400,
            "message": f"No record found with id: {id}",
        }
    data = door_category_data.sanitize()

    return {
        "_code": 200,
        "message": "Success",
        "door_category_data": data
    }