from flask import request, make_response, jsonify
import logging
from lockshop.skel.skel_res import SkelRes
from lockshop.sql_util.utils import session_wrap
from .models import Building
from flask_cors import cross_origin

@session_wrap()
@SkelRes()
def PostBuilding(session, *args, **kwargs):
    logging.info("You hit the test_database_post method successfully.")
    request_body = request.get_json()
    logging.info(f"request_body: {request_body}")
    if not request_body:
        logging.error("'message' param missing in the body.")
        return {
            "_code": 400,
            "message": "'message' param missing in the body."
        }
    name = request_body.get ("name")
    code = request_body.get ("code")
    no_of_floors = request_body.get ("no_of_floors")
    if not name or not code or not no_of_floors:
        logging.error("'name or code or no_of_floors' param missing in the body.")
        return {
            "_code": 400,
            "message": "'message' param missing in the body."
        }
    building_data = Building.create(name=name, session=session, code=code, no_of_floors=no_of_floors)
    session.commit()

    return {
        "_code": 200,
        "message": "Success",
        "test_record": building_data.sanitize()
    }


@session_wrap()
@SkelRes()
# @cross_origin()
def GetBuilding(session, *args, **kwargs):
    logging.info("You hit test_database_get method successfully")
    id = request.args.get("id")
    data = None
    if id:
        building_data = Building.get_by_id(session=session, id=int(id))
        if not building_data:
            return {
                "_code": 400,
                "message": f"No record found with id: {id}",
            }
        data = building_data.sanitize()
    else:
        records = Building.get_all(session=session)
        data = [record.sanitize() for record in records]

    # response = make_response(jsonify({
    #                                     "_code": 200,
    #                                     "message": "Success",
    #                                     "building_data": data}
    #         ),
    #         200,
    #     )

    # response.headers.set('Access-Control-Allow-Origin','*')

    # return response

    return {
        "_code": 200,
        "message": "Success",
        "building_data": data
    }