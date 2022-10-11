from flask import request
import logging
from lockshop.skel.skel_res import SkelRes
from lockshop.sql_util.utils import session_wrap
from .models import DoorContinousHinge

@session_wrap()
@SkelRes()
def PostDoorContinousHinge(session, *args, **kwargs):
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
    door_hinge_data = DoorContinousHinge.create(session=session, name=name)
    session.commit()

    return {
        "_code": 200,
        "message": "Success",
        "door_hinge": door_hinge_data.sanitize()
    }


@session_wrap()
@SkelRes()
def GetDoorContinousHinge(session, *args, **kwargs):
    logging.info("You hit floot_get method successfully")
    request_body = request.get_json()
    id = request_body.get("id")
    data = None

    if id == None:
        return {
            "_code": 200,
            "message": "error",
            "door_continuous_hinge_data": None,
            "reason": "id is empty"
        }

    door_continuous_hinge_data = DoorContinousHinge.get_by_id(session=session, id=int(id))
    if not door_continuous_hinge_data:
        return {
            "_code": 400,
            "message": f"No record found with id: {id}",
        }
    data = door_continuous_hinge_data.sanitize()

    return {
        "_code": 200,
        "message": "Success",
        "door_continuous_hinge_data": data
    }