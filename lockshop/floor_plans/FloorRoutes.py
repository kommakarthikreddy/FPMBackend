from flask import request
import logging
from lockshop.skel.skel_res import SkelRes
from lockshop.sql_util.utils import session_wrap
from .models import Floor

@session_wrap()
@SkelRes()
def PostFloor(session, *args, **kwargs):
    logging.info("You hit the floor_post method successfully.")
    request_body = request.get_json()
    logging.info(f"request_body: {request_body}")
    if not request_body:
        logging.error("Missing the request body.")
        return {
            "_code": 400,
            "message": "Missing the request body."
        }
    floor_no = request_body.get ("floor_no")
    building_id = request_body.get ("building_id")
    if floor_no == None or building_id == None:
        logging.error("'floor_no or building_id' param missing in the body.")
        return {
            "_code": 400,
            "message": "floor_no or building_id param missing in the body."
        }
    floor_data = Floor.create(session=session, floor_no=floor_no, building_id=building_id)
    session.commit()

    return {
        "_code": 200,
        "message": "Success",
        "test_record": floor_data.sanitize()
    }


@session_wrap()
@SkelRes()
def GetFloor(session, *args, **kwargs):
    logging.info("You hit floot_get method successfully")
    request_body = request.get_json()
    floor_no = request_body.get("floor_no")
    building_id = request_body.get ("building_id")
    data = None
    if floor_no != None and building_id != None:
        floor_data = Floor.get_by_id(session=session, floor_no=int(floor_no), building_id=int (building_id))
        if not floor_data:
            return {
                "_code": 400,
                "message": f"No record found with id: {id}",
            }
        data = floor_data.sanitize()
    elif building_id != None:
        records = Floor.query(session=session, building_id =int(building_id), floor_no=None)
        data = [record.sanitize() for record in records]

    return {
        "_code": 200,
        "message": "Success",
        "building_data": data
    }