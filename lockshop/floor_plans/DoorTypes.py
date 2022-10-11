from flask import request
import logging
from lockshop.skel.skel_res import SkelRes
from lockshop.sql_util.utils import session_wrap
from .models import DoorType

@session_wrap()
@SkelRes()
def PostDoorTypes(session, *args, **kwargs):
    logging.info("You hit the floor_post method successfully.")
    request_body = request.get_json()
    logging.info(f"request_body: {request_body}")
    if not request_body:
        logging.error("Missing the request body.")
        return {
            "_code": 400,
            "message": "Missing the request body."
        }
    name = request_body.get("name")

    if name == None:
        logging.error("'name' param missing in the body.")
        return {
            "_code": 400,
            "message": "name param missing in the body."
        }
    door_frame_data = DoorType.create(session=session, name=name)
    session.commit()

    return {
        "_code": 200,
        "message": "Success",
        "door_type": door_frame_data.sanitize()
    }


@session_wrap()
@SkelRes()
def GetDoorTypes(session, *args, **kwargs):
    logging.info("You hit floot_get method successfully")
    request_body = request.get_json()
    id = request_body.get("id")
    data = None

    if id == None:
        return {
            "_code": 200,
            "message": "error",
            "door_type": None,
            "reason": "id is empty"
        }

    door_type_data = DoorType.get_by_id(session=session, id=int(id))
    if not door_type_data:
        return {
            "_code": 400,
            "message": f"No record found with id: {id}",
        }
    data = door_type_data.sanitize()

    return {
        "_code": 200,
        "message": "Success",
        "door_type_data": data
    }