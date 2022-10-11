from flask import request
import logging
from lockshop.skel.skel_res import SkelRes
from lockshop.sql_util.utils import session_wrap
from .models import DoorHinge

@session_wrap()
@SkelRes()
def PostDoorHinge(session, *args, **kwargs):
    logging.info("You hit the floor_post method successfully.")
    request_body = request.get_json()
    logging.info(f"request_body: {request_body}")
    if not request_body:
        logging.error("Missing the request body.")
        return {
            "_code": 400,
            "message": "Missing the request body."
        }
    type = request_body.get("type")

    if type == None:
        logging.error("'type' param missing in the body.")
        return {
            "_code": 400,
            "message": "type param missing in the body."
        }
    door_hinge_data = DoorHinge.create(session=session, type=type)
    session.commit()

    return {
        "_code": 200,
        "message": "Success",
        "door_hinge": door_hinge_data.sanitize()
    }


@session_wrap()
@SkelRes()
def GetDoorHinge(session, *args, **kwargs):
    logging.info("You hit floot_get method successfully")
    request_body = request.get_json()
    id = request_body.get("id")
    data = None

    if id == None:
        return {
            "_code": 200,
            "message": "error",
            "door_hinge": None,
            "reason": "id is empty"
        }

    door_type_data = DoorHinge.get_by_id(session=session, id=int(id))
    if not door_type_data:
        return {
            "_code": 400,
            "message": f"No record found with id: {id}",
        }
    data = door_type_data.sanitize()

    return {
        "_code": 200,
        "message": "Success",
        "door_hinge_data": data
    }