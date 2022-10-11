from flask import request
import logging
from lockshop.skel.skel_res import SkelRes
from lockshop.sql_util.utils import session_wrap
from .models import Door

@session_wrap()
@SkelRes()
def PostDoor(session, *args, **kwargs):
    logging.info("You hit the floor_post method successfully.")
    request_body = request.get_json()
    logging.info(f"request_body: {request_body}")
    if not request_body:
        logging.error("Missing the request body.")
        return {
            "_code": 400,
            "message": "Missing the request body."
        }
    data = request_body["data"]

    if data == None:
        logging.error("'data' param missing in the body.")
        return {
            "_code": 400,
            "message": "data param missing in the body."
        }

    door_no = data["door_no"]
    floor_no = data["floor_no"]
    building_id = data["building_id"]
    door_name = data["door_name"]
    complaince_id = data["complaince_id"]
    fire_rating_id = data["fire_rating_id"]
    category_id = data["category_id"]
    frame_id = data["frame_id"]
    size = data["size"]
    type_id = data["type_id"]
    vision_lite = data["vision_lite"]
    transom_id = data["transom_id"]
    side_lite = data["side_lite"]
    hinge_id = data["hinge_id"]
    hinge_size = data["hinge_size"]
    continous_hinge_id = data["continous_hinge_id"]
    pivot_id = data["self.pivot_id"]
    power_transfer_id = data["power_transfer_id"]
    lockset_id = data["lockset_id"]
    electric_lockset_id = data["electric_lockset_id"]
    strike_id = data["strike_id"]
    exit_device_id = data["exit_device_id"]
    electric_exit_device = data["electric_exit_device"]
    mullion = data["mullion"]
    trim_id = data["trim_id"]
    delay_egress_id = data["delay_egress_id"]

    door = Door(session = session, door_no=door_no, floor_no=floor_no, building_id=building_id, door_name=door_name,
                complaince_id=complaince_id, fire_rating_id=fire_rating_id,
                category_id=category_id, frame_id=frame_id, size=size, type_id=type_id, vision_lite=vision_lite,
                transom_id=transom_id, side_lite=side_lite,
                hinge_id=hinge_id, hinge_size=hinge_size, continous_hinge_id=continous_hinge_id, pivot_id=pivot_id,
                power_transfer_id=power_transfer_id,
                lockset_id=lockset_id, electric_lockset_id=electric_lockset_id, strike_id=strike_id,
                exit_device_id=exit_device_id,
                electric_exit_device=electric_exit_device, mullion=mullion, trim_id=trim_id,
                delay_egress_id=delay_egress_id)

    session.commit ()

    return {
        "_code": 200,
        "message": "Success",
        "door_data": door.sanitize()
    }
