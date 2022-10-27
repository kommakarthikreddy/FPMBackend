import logging
# TODO: Fix logging
from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
from lockshop.floor_plans.BuildingRoutes import PostBuilding, GetBuilding
from lockshop.floor_plans.FloorRoutes import PostFloor, GetFloor
from lockshop.floor_plans.DoorCategoryRoutes import PostDoorCategory, GetDoorCategory
from lockshop.floor_plans.DoorFrameRoutes import PostDoorFrame , GetDoorFrame
from lockshop.floor_plans.DoorTypes import PostDoorTypes , GetDoorTypes
from lockshop.floor_plans.DoorTransomRoutes import PostDoorTransom , GetDoorTransom
from lockshop.floor_plans.DoorHingesRoutes import PostDoorHinge , GetDoorHinge
from lockshop.floor_plans.DoorContinousHinge import PostDoorContinousHinge , GetDoorContinousHinge
from lockshop.floor_plans.DoorPivotRoutes import PostDoorPivot , GetDoorPivot
from lockshop.floor_plans.DoorPowerTransferRoutes import PostDoorPowerTransfer, GetDoorPowerTransfer
from lockshop.floor_plans.DoorLockSet import PostDoorLockSet , GetDoorLockSet
from lockshop.floor_plans.DoorExitDeviceRoutes import PostDoorExitDevice , GetDoorExitDevice
from lockshop.floor_plans.DoorTrimRoutes import PostDoorTrim , GetDoorTrim
from lockshop.floor_plans.DoorDelayEgress import PostDelayEgress , GetDoorDelayEgress
from lockshop.floor_plans.DoorCylinder import PostDoorCylinder , GetDoorCylinder
from lockshop.floor_plans.DoorCloserRoutes import PostDoorCloser , GetDoorCloser
from lockshop.floor_plans.DoorAutoOperatorRoutes import PostDoorAutoOperator , GetDoorAutoOperator
from lockshop.floor_plans.DoorAOWallPlate import PostDoorAOWallPlate , GetDoorAOWallPlate
from lockshop.floor_plans.DoorCordinatorRoutes import PostDoorCoordinator , GetDoorCoordinator
from lockshop.floor_plans.DoorFlushRoutes import PostDoorFlushBolt , GetDoorFlushBolt
from lockshop.floor_plans.DoorMagHolderRoutes import PostDoorMagHolder , GetDoorMagHolder
from lockshop.floor_plans.DoorStopRoutes import PostDoorStop , GetDoorStop
from lockshop.floor_plans.DoorAstragal import PostDoorAstragal , GetDoorAstragal
from lockshop.floor_plans.DoorSealRoutes import PostDoorSeal , GetDoorSeal
from lockshop.floor_plans.DoorSweepRoutes import PostDoorSweep , GetDoorSweep
from lockshop.floor_plans.DoorAutoDrBtmRoutes import PostDoorAutoDrBtm , GetDoorAutoDrBtm
from lockshop.floor_plans.DoorThresholdRoutes import PostDoorThreshold , GetDoorThreshold
from lockshop.floor_plans.DoorRoutes import PostDoor

app = Flask(__name__, static_folder="lockshop/static", static_url_path="/static")
CORS(app)
# resources={r"/api/*": {"origins": "*"}}
# from app_configuration import configure_application
# configure_application()

#\sql
#\coneect root@localhost;

def existingRoutes ():
    api_url = "/api/lockshop/building"
    handler = PostBuilding
    methods = "POST"
    route = [api_url, handler, [methods]]
    app.add_url_rule(api_url, "{}|{}".format(route, handler), handler, methods=[methods])

    api_url = "/api/lockshop/building"
    handler = GetBuilding
    methods = "GET"
    route = [api_url, handler, [methods]]
    app.add_url_rule(api_url, "{}|{}".format(route, handler), handler, methods=[methods])

    # floor
    api_url = "/api/lockshop/floor"
    handler = PostFloor
    methods = "POST"
    route = [api_url, handler, [methods]]
    app.add_url_rule(api_url, "{}|{}".format(route, handler), handler, methods=[methods])

    api_url = "/api/lockshop/floor"
    handler = GetFloor
    methods = "GET"
    route = [api_url, handler, [methods]]
    app.add_url_rule(api_url, "{}|{}".format(route, handler), handler, methods=[methods])

    # DoorCategory
    api_url = "/api/lockshop/doorcategory"
    handler = PostDoorCategory
    methods = "POST"
    route = [api_url, handler, [methods]]
    app.add_url_rule(api_url, "{}|{}".format(route, handler), handler, methods=[methods])

    api_url = "/api/lockshop/doorcategory"
    handler = GetDoorCategory
    methods = "GET"
    route = [api_url, handler, [methods]]
    app.add_url_rule(api_url, "{}|{}".format(route, handler), handler, methods=[methods])

    # DoorFrame
    api_url = "/api/lockshop/doorframe"
    handler = PostDoorFrame
    methods = "POST"
    route = [api_url, handler, [methods]]
    app.add_url_rule(api_url, "{}|{}".format(route, handler), handler, methods=[methods])

    api_url = "/api/lockshop/doorframe"
    handler = GetDoorFrame
    methods = "GET"
    route = [api_url, handler, [methods]]
    app.add_url_rule(api_url, "{}|{}".format(route, handler), handler, methods=[methods])

    # DoorTypes
    api_url = "/api/lockshop/doortype"
    handler = PostDoorTypes
    methods = "POST"
    route = [api_url, handler, [methods]]
    app.add_url_rule(api_url, "{}|{}".format(route, handler), handler, methods=[methods])

    api_url = "/api/lockshop/doortype"
    handler = GetDoorTypes
    methods = "GET"
    route = [api_url, handler, [methods]]
    app.add_url_rule(api_url, "{}|{}".format(route, handler), handler, methods=[methods])

    # DoorTransom
    api_url = "/api/lockshop/doortransom"
    handler = PostDoorTransom
    methods = "POST"
    route = [api_url, handler, [methods]]
    app.add_url_rule(api_url, "{}|{}".format(route, handler), handler, methods=[methods])

    api_url = "/api/lockshop/doortransom"
    handler = GetDoorTransom
    methods = "GET"
    route = [api_url, handler, [methods]]
    app.add_url_rule(api_url, "{}|{}".format(route, handler), handler, methods=[methods])

    # DoorHinge
    api_url = "/api/lockshop/doorhinge"
    handler = PostDoorHinge
    methods = "POST"
    route = [api_url, handler, [methods]]
    app.add_url_rule(api_url, "{}|{}".format(route, handler), handler, methods=[methods])

    api_url = "/api/lockshop/doorhinge"
    handler = GetDoorHinge
    methods = "GET"
    route = [api_url, handler, [methods]]
    app.add_url_rule(api_url, "{}|{}".format(route, handler), handler, methods=[methods])

    # DoorContinuousHinge
    api_url = "/api/lockshop/doorconitnuoushinge"
    handler = PostDoorContinousHinge
    methods = "POST"
    route = [api_url, handler, [methods]]
    app.add_url_rule(api_url, "{}|{}".format(route, handler), handler, methods=[methods])

    api_url = "/api/lockshop/doorcontinuoushinge"
    handler = GetDoorContinousHinge
    methods = "GET"
    route = [api_url, handler, [methods]]
    app.add_url_rule(api_url, "{}|{}".format(route, handler), handler, methods=[methods])

    # DoorPivot
    api_url = "/api/lockshop/doorpivot"
    handler = PostDoorPivot
    methods = "POST"
    route = [api_url, handler, [methods]]
    app.add_url_rule(api_url, "{}|{}".format(route, handler), handler, methods=[methods])

    api_url = "/api/lockshop/doorpivot"
    handler = GetDoorPivot
    methods = "GET"
    route = [api_url, handler, [methods]]
    app.add_url_rule(api_url, "{}|{}".format(route, handler), handler, methods=[methods])

    # DoorPowerTransform
    api_url = "/api/lockshop/doorpowertransfer"
    handler = PostDoorPowerTransfer
    methods = "POST"
    route = [api_url, handler, [methods]]
    app.add_url_rule(api_url, "{}|{}".format(route, handler), handler, methods=[methods])

    api_url = "/api/lockshop/doorpowertransfer"
    handler = GetDoorPowerTransfer
    methods = "GET"
    route = [api_url, handler, [methods]]
    app.add_url_rule(api_url, "{}|{}".format(route, handler), handler, methods=[methods])

    # DoorLockSet
    api_url = "/api/lockshop/doorlockset"
    handler = PostDoorLockSet
    methods = "POST"
    route = [api_url, handler, [methods]]
    app.add_url_rule(api_url, "{}|{}".format(route, handler), handler, methods=[methods])

    api_url = "/api/lockshop/doorlockset"
    handler = GetDoorLockSet
    methods = "GET"
    route = [api_url, handler, [methods]]
    app.add_url_rule(api_url, "{}|{}".format(route, handler), handler, methods=[methods])

    # DoorStrike
    api_url = "/api/lockshop/doorstrike"
    handler = PostDoorLockSet
    methods = "POST"
    route = [api_url, handler, [methods]]
    app.add_url_rule(api_url, "{}|{}".format(route, handler), handler, methods=[methods])

    api_url = "/api/lockshop/doorstrike"
    handler = GetDoorLockSet
    methods = "GET"
    route = [api_url, handler, [methods]]
    app.add_url_rule(api_url, "{}|{}".format(route, handler), handler, methods=[methods])

    # DoorStrike
    api_url = "/api/lockshop/doorexitdevice"
    handler = PostDoorExitDevice
    methods = "POST"
    route = [api_url, handler, [methods]]
    app.add_url_rule(api_url, "{}|{}".format(route, handler), handler, methods=[methods])

    api_url = "/api/lockshop/doorexitdevice"
    handler = GetDoorExitDevice
    methods = "GET"
    route = [api_url, handler, [methods]]
    app.add_url_rule(api_url, "{}|{}".format(route, handler), handler, methods=[methods])

    # DoorTrim
    api_url = "/api/lockshop/doortrim"
    handler = PostDoorTrim
    methods = "POST"
    route = [api_url, handler, [methods]]
    app.add_url_rule(api_url, "{}|{}".format(route, handler), handler, methods=[methods])

    api_url = "/api/lockshop/doortrim"
    handler = GetDoorTrim
    methods = "GET"
    route = [api_url, handler, [methods]]
    app.add_url_rule(api_url, "{}|{}".format(route, handler), handler, methods=[methods])

    # DoorDelayEgress
    api_url = "/api/lockshop/doordelayegress"
    handler = PostDelayEgress
    methods = "POST"
    route = [api_url, handler, [methods]]
    app.add_url_rule(api_url, "{}|{}".format(route, handler), handler, methods=[methods])

    api_url = "/api/lockshop/doordelayegress"
    handler = GetDoorDelayEgress
    methods = "GET"
    route = [api_url, handler, [methods]]
    app.add_url_rule(api_url, "{}|{}".format(route, handler), handler, methods=[methods])

    # DoorCylinder
    api_url = "/api/lockshop/doorcylinder"
    handler = PostDoorCylinder
    methods = "POST"
    route = [api_url, handler, [methods]]
    app.add_url_rule(api_url, "{}|{}".format(route, handler), handler, methods=[methods])

    api_url = "/api/lockshop/doorcylinder"
    handler = GetDoorCylinder
    methods = "GET"
    route = [api_url, handler, [methods]]
    app.add_url_rule(api_url, "{}|{}".format(route, handler), handler, methods=[methods])

    # DoorCloser
    api_url = "/api/lockshop/doorcloser"
    handler = PostDoorCloser
    methods = "POST"
    route = [api_url, handler, [methods]]
    app.add_url_rule(api_url, "{}|{}".format(route, handler), handler, methods=[methods])

    api_url = "/api/lockshop/doorcloser"
    handler = GetDoorCloser
    methods = "GET"
    route = [api_url, handler, [methods]]
    app.add_url_rule(api_url, "{}|{}".format(route, handler), handler, methods=[methods])

    # DoorAutoOperator
    api_url = "/api/lockshop/doorautooperator"
    handler = PostDoorAutoOperator
    methods = "POST"
    route = [api_url, handler, [methods]]
    app.add_url_rule(api_url, "{}|{}".format(route, handler), handler, methods=[methods])

    api_url = "/api/lockshop/doorautooperator"
    handler = GetDoorAutoOperator
    methods = "GET"
    route = [api_url, handler, [methods]]
    app.add_url_rule(api_url, "{}|{}".format(route, handler), handler, methods=[methods])

    # DoorAOWallPlate
    api_url = "/api/lockshop/dooraowallplate"
    handler = PostDoorAOWallPlate
    methods = "POST"
    route = [api_url, handler, [methods]]
    app.add_url_rule(api_url, "{}|{}".format(route, handler), handler, methods=[methods])

    api_url = "/api/lockshop/dooraowallplate"
    handler = GetDoorAOWallPlate
    methods = "GET"
    route = [api_url, handler, [methods]]
    app.add_url_rule(api_url, "{}|{}".format(route, handler), handler, methods=[methods])

def setRoutes ():
    existingRoutes()

    # DoorCoordinator
    api_url = "/api/lockshop/doorcoordinator"
    handler = PostDoorCoordinator
    methods = "POST"
    route = [api_url, handler, [methods]]
    app.add_url_rule(api_url, "{}|{}".format(route, handler), handler, methods=[methods])

    api_url = "/api/lockshop/doorcoordinator"
    handler = GetDoorCoordinator
    methods = "GET"
    route = [api_url, handler, [methods]]
    app.add_url_rule(api_url, "{}|{}".format(route, handler), handler, methods=[methods])

    # DoorFlushBolt
    api_url = "/api/lockshop/doorflushbolt"
    handler = PostDoorFlushBolt
    methods = "POST"
    route = [api_url, handler, [methods]]
    app.add_url_rule(api_url, "{}|{}".format(route, handler), handler, methods=[methods])

    api_url = "/api/lockshop/doorflushbolt"
    handler = GetDoorFlushBolt
    methods = "GET"
    route = [api_url, handler, [methods]]
    app.add_url_rule(api_url, "{}|{}".format(route, handler), handler, methods=[methods])

    # DoorMagHolder
    api_url = "/api/lockshop/doormagholder"
    handler = PostDoorMagHolder
    methods = "POST"
    route = [api_url, handler, [methods]]
    app.add_url_rule(api_url, "{}|{}".format(route, handler), handler, methods=[methods])

    api_url = "/api/lockshop/doormagholder"
    handler = GetDoorMagHolder
    methods = "GET"
    route = [api_url, handler, [methods]]
    app.add_url_rule(api_url, "{}|{}".format(route, handler), handler, methods=[methods])

    # DoorStop
    api_url = "/api/lockshop/doorstop"
    handler = PostDoorStop
    methods = "POST"
    route = [api_url, handler, [methods]]
    app.add_url_rule(api_url, "{}|{}".format(route, handler), handler, methods=[methods])

    api_url = "/api/lockshop/doorstop"
    handler = GetDoorStop
    methods = "GET"
    route = [api_url, handler, [methods]]
    app.add_url_rule(api_url, "{}|{}".format(route, handler), handler, methods=[methods])

    # DoorAstragal
    api_url = "/api/lockshop/doorastragal"
    handler = PostDoorAstragal
    methods = "POST"
    route = [api_url, handler, [methods]]
    app.add_url_rule(api_url, "{}|{}".format(route, handler), handler, methods=[methods])

    api_url = "/api/lockshop/doorastragal"
    handler = GetDoorAstragal
    methods = "GET"
    route = [api_url, handler, [methods]]
    app.add_url_rule(api_url, "{}|{}".format(route, handler), handler, methods=[methods])

    # DoorSeal
    api_url = "/api/lockshop/doorseal"
    handler = PostDoorSeal
    methods = "POST"
    route = [api_url, handler, [methods]]
    app.add_url_rule(api_url, "{}|{}".format(route, handler), handler, methods=[methods])

    api_url = "/api/lockshop/doorseal"
    handler = GetDoorSeal
    methods = "GET"
    route = [api_url, handler, [methods]]
    app.add_url_rule(api_url, "{}|{}".format(route, handler), handler, methods=[methods])

    # DoorSweep
    api_url = "/api/lockshop/doorsweep"
    handler = PostDoorSweep
    methods = "POST"
    route = [api_url, handler, [methods]]
    app.add_url_rule(api_url, "{}|{}".format(route, handler), handler, methods=[methods])

    api_url = "/api/lockshop/doorsweep"
    handler = GetDoorSweep
    methods = "GET"
    route = [api_url, handler, [methods]]
    app.add_url_rule(api_url, "{}|{}".format(route, handler), handler, methods=[methods])

    # DoorAutoDrBtm
    api_url = "/api/lockshop/doorautodrbtm"
    handler = PostDoorAutoDrBtm
    methods = "POST"
    route = [api_url, handler, [methods]]
    app.add_url_rule(api_url, "{}|{}".format(route, handler), handler, methods=[methods])

    api_url = "/api/lockshop/doorautodrbtm"
    handler = GetDoorAutoDrBtm
    methods = "GET"
    route = [api_url, handler, [methods]]
    app.add_url_rule(api_url, "{}|{}".format(route, handler), handler, methods=[methods])

    # DoorThreshold
    api_url = "/api/lockshop/doorthreshold"
    handler = PostDoorThreshold
    methods = "POST"
    route = [api_url, handler, [methods]]
    app.add_url_rule(api_url, "{}|{}".format(route, handler), handler, methods=[methods])

    api_url = "/api/lockshop/doorthreshold"
    handler = GetDoorThreshold
    methods = "GET"
    route = [api_url, handler, [methods]]
    app.add_url_rule(api_url, "{}|{}".format(route, handler), handler, methods=[methods])

    # Door
    api_url = "/api/lockshop/door"
    handler = PostDoor
    methods = "POST"
    route = [api_url, handler, [methods]]
    app.add_url_rule(api_url, "{}|{}".format(route, handler), handler, methods=[methods])

setRoutes ()

@app.route('/')
def hello_world():
    return '<h1>Hello! The lockshop server is up and running.</h1>'


@app.errorhandler(404)
def page_not_found(e):
    response = {
        "status": "404 not Found",
        "message": "The requested url was not found on the server"
    }
    return jsonify(response), 404


@app.errorhandler(500)
def internal_server_error(e):
    print(e)
    response = {
        "status": "500 Internal Server Error.",
        "message": ""
    }
    return jsonify(response), 500

app.run()
