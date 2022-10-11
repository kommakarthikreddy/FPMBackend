from flask import request
import logging
from lockshop.skel.skel_res import SkelRes
from lockshop.sql_util.utils import session_wrap
from .models import DoorFrame

@session_wrap()
@SkelRes()
def PostDoorFrame(session, *args, **kwargs):
    logging.info("You hit the floor_post method successfully.")
    request_body = request.get_json()
    logging.info(f"request_body: {request_body}")
    if not request_body:
        logging.error("Missing the request body.")
        return {
            "_code": 400,
            "message": "Missing the request body."
        }
    material = request_body.get ("material")

    if material == None:
        logging.error("'material' param missing in the body.")
        return {
            "_code": 400,
            "message": "Material param missing in the body."
        }
    door_frame_data = DoorFrame.create(session=session, material=material)
    session.commit()

    return {
        "_code": 200,
        "message": "Success",
        "test_record": door_frame_data.sanitize()
    }


@session_wrap()
@SkelRes()
def GetDoorFrame(session, *args, **kwargs):
    logging.info("You hit floot_get method successfully")
    request_body = request.get_json()
    id = request_body.get("id")
    data = None

    if id == None:
        return {
            "_code": 200,
            "message": "error",
            "door_frame": None,
            "reason": "id is empty"
        }

    door_frame_data = DoorFrame.get_by_id(session=session, id=int(id))
    if not door_frame_data:
        return {
            "_code": 400,
            "message": f"No record found with id: {id}",
        }
    data = door_frame_data.sanitize()

    return {
        "_code": 200,
        "message": "Success",
        "door_frame_data": data
    }