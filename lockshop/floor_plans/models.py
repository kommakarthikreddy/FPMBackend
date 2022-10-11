from email.policy import default
from sqlalchemy.orm import backref, relationship
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey

from lockshop.sql_util.utils import *


class Building(Base):
    __tablename__ = "buildings"

    id = Column(Integer, primary_key=True)
    name = Column(String(5000),  nullable=False)
    code = Column(String(5000), nullable=False)
    no_of_floors = Column(Integer, default=0)
    has_basement = Column(Boolean, default=False)
    version = Column(String(500), default="v1")
    dt_created = Column(DateTime, default=datetime.datetime.utcnow)
    dt_updated = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    # Attributes from relationship to other tables
    floors = relationship("Floor", back_populates="building")
    doors = relationship("Door", back_populates="building")

    def sanitize(self):
        return {
            "id": self.id,
            "name": self.name,
            "code": self.code,
            "no_of_floors": self.no_of_floors,
            "has_basement": self.has_basement,
            "version": self.version,
            "dt_created": self.dt_created,
            "dt_updated": self.dt_updated
        }

    @classmethod
    def create(cls, session, name, code, no_of_floors, has_basement=False, version="v1"):
        building = Building(name=name, code=code, no_of_floors=no_of_floors, has_basement=has_basement, version=version or "v1")
        session.add(building)
        return building

    @classmethod
    def get_by_id(cls, session, id):
        return session.query(Building).get(int(id))

    @classmethod
    def get_all(cls, session):
        return session.query(Building).all()

    @classmethod
    def query(cls, session, building_id=None, name=None, code=None, no_of_floors=None, has_basement=None, version=None):
        buildings_query = session.query(Building)
        if building_id:
            buildings_query = buildings_query.filter(Building.id == int(id))

        if name:
            buildings_query = buildings_query.filter(Building.name == name)

        if code:
            buildings_query = buildings_query.filter(Building.code == code)

        if no_of_floors:
            buildings_query = buildings_query.filter(Building.no_of_floors == no_of_floors)

        if has_basement:
            buildings_query = buildings_query.filter(Building.has_basement == has_basement)
        
        if version:
            buildings_query = buildings_query.filter(Building.version == version)

        return buildings_query


class Floor(Base):
    __tablename__ = "floors"

    floor_no = Column(Integer, primary_key=True)
    building_id = Column(Integer, ForeignKey("buildings.id"), primary_key=True)
    version = Column(String(500), default="v1")
    dt_created = Column(DateTime, default=datetime.datetime.utcnow)
    dt_updated = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    # Attributes from relationship to other tables
    building = relationship("Building", back_populates="floors")
    doors = relationship("Door", back_populates="floor")

    def sanitize(self):
        return {
            "floor_no": self.floor_no,
            "building_id": self.building_id,
            "version": self.version,
            "dt_created": self.dt_created,
            "dt_updated": self.dt_updated
        }

    @classmethod
    def create(cls, session, floor_no, building_id, version="v1"):
        floor = Floor(floor_no=floor_no, building_id=building_id, version=version or "v1")
        session.add(floor)
        return floor

    @classmethod
    def get_by_id(cls, session, floor_no, building_id):
        return session.query(Floor).get((floor_no, building_id)) # TODO: Verify this works

    @classmethod
    def query(cls, session, floor_no, building_id, version = "v1"):
        floors_query = session.query(Floor)

        if floor_no:
            floors_query = floors_query.filter(Floor.floor_no == floor_no)

        if building_id:
            floors_query = floors_query.filter(Floor.building_id == building_id)

        if version:
            floors_query = floors_query.filter(Floor.version == version)

        return floors_query


class DoorCategory(Base):
    __tablename__ = "door_categories"

    id = Column(Integer, primary_key=True)
    name = Column(String(5000), nullable=False)
    version = Column(String(500), default="v1")
    dt_created = Column(DateTime, default=datetime.datetime.utcnow)
    dt_updated = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    doors = relationship("Door", back_populates="category")

    def sanitize(self):
        return {
            "id": self.id,
            "name": self.name,
            "version": self.version,
            "dt_created": self.dt_created,
            "dt_updated": self.dt_updated
        }

    @classmethod
    def create(cls, session, name, version = None):
        door_category = DoorCategory(name=name, version=version or "v1")
        session.add(door_category)
        return door_category

    @classmethod
    def get_by_id(cls, session, id):
        return session.query(DoorCategory).get(int(id))

    @classmethod
    def query(cls, session, id, name, version):
        door_category_query = session.query(DoorCategory)

        if id:
            door_category_query = door_category_query.filter(DoorCategory.id == id)

        if name:
            door_category_query = door_category_query.filter(DoorCategory.name == name)

        if version:
            door_category_query = door_category_query.filter(DoorCategory.version == version)

        return door_category_query


class DoorDefeciency(Base):
    __tablename__ = "door_defeciencies"

    id = Column(Integer, primary_key=True)
    description = Column(String(5000), nullable=False)
    version = Column(String(500), default="v1")
    dt_created = Column(DateTime, default=datetime.datetime.utcnow)
    dt_updated = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    def sanitize(self):
        return {
            "id": self.id,
            "description": self.description,
            "version": self.version,
            "dt_created": self.dt_created,
            "dt_updated": self.dt_updated
        }

    @classmethod
    def create(cls, session, description, version):
        door_defeciency = DoorDefeciency(description=description, version=version or "v1")
        session.add(door_defeciency)
        return door_defeciency

    @classmethod
    def get_by_id(cls, session, id):
        return session.query(DoorDefeciency).get(int(id))
    
    @classmethod
    def query(cls, session, id, description, version):
        door_defeciency_query = session.query(DoorDefeciency)

        if id:
            door_defeciency_query = door_defeciency_query.filter(DoorDefeciency.id == id)

        if description:
            door_defeciency_query = door_defeciency_query.filter(DoorDefeciency.description == description)

        if version:
            door_defeciency_query = door_defeciency_query.filter(DoorDefeciency.version == version)

        return door_defeciency_query


class Compliance(Base):
    __tablename__ = "compliancies"

    id = Column(Integer, primary_key=True)
    name = Column(String(5000), nullable=False)
    version = Column(String(500), default="v1")
    dt_created = Column(DateTime, default=datetime.datetime.utcnow)
    dt_updated = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    doors = relationship("Door", back_populates="compliance")

    def sanitize(self):
        return {
            "id": self.id,
            "name": self.name,
            "version": self.version,
            "dt_created": self.dt_created,
            "dt_updated": self.dt_updated
        }

    @classmethod
    def create(cls, session, name, version):
        compliance = Compliance(name=name, version=version or "v1")
        session.add(compliance)
        return compliance

    @classmethod
    def get_by_id(cls, session, id):
        return session.query(Compliance).get(int(id))

    @classmethod
    def query(cls, session, id, name, version):
        compliance_query = session.query(Compliance)

        if id:
            compliance_query = compliance_query.filter(Compliance.id == id)

        if name:
            compliance_query = compliance_query.filter(Compliance.name == name)

        if version:
            compliance_query = compliance_query.filter(Compliance.version == version)

        return compliance_query


class FireRating(Base):
    __tablename__ = "fire_ratings"

    id = Column(Integer, primary_key=True)
    name = Column(String(5000), nullable=False)
    version = Column(String(500), default="v1")
    dt_created = Column(DateTime, default=datetime.datetime.utcnow)
    dt_updated = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    doors = relationship("Door", back_populates="fire_rating")

    def sanitize(self):
        return {
            "id": self.id,
            "name": self.name,
            "version": self.version,
            "dt_created": self.dt_created,
            "dt_updated": self.dt_updated
        }

    @classmethod
    def create(cls, session, name, version):
        fire_rating = FireRating(name=name, version=version or "v1")
        session.add(fire_rating)
        return fire_rating

    @classmethod
    def get_by_id(cls, session, id):
        return session.query(FireRating).get(int(id))

    @classmethod
    def query(cls, session, id, name, version):
        fire_rating_query = session.query(FireRating)

        if id:
            fire_rating_query = fire_rating_query.filter(FireRating.id == id)

        if name:
            fire_rating_query = fire_rating_query.filter(FireRating.name == name)

        if version:
            fire_rating_query = fire_rating_query.filter(FireRating.version == version)

        return fire_rating_query


class DoorFrame(Base):
    __tablename__ = "door_frames"

    id = Column(Integer, primary_key=True)
    material = Column(String(5000), nullable=False)
    version = Column(String(500), default="v1")
    dt_created = Column(DateTime, default=datetime.datetime.utcnow)
    dt_updated = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    doors = relationship("Door", back_populates="frame")

    def sanitize(self):
        return {
            "id": self.id,
            "material": self.material,
            "version": self.version,
            "dt_created": self.dt_created,
            "dt_updated": self.dt_updated
        }

    @classmethod
    def create(cls, session, material, version = None):
        door_frame = DoorFrame(material=material, version=version or "v1")
        session.add(door_frame)
        return door_frame

    @classmethod
    def get_by_id(cls, session, id):
        return session.query(DoorFrame).get(int(id))

    @classmethod
    def query(cls, session, id, material, version):
        door_frame_query = session.query(DoorFrame)

        if id:
            door_frame_query = door_frame_query.filter(DoorFrame.id == id)

        if material:
            door_frame_query = door_frame_query.filter(DoorFrame.material == material)

        if version:
            door_frame_query = door_frame_query.filter(DoorFrame.version == version)

        return door_frame_query


class DoorType(Base):
    __tablename__ = "door_types"

    id = Column(Integer, primary_key=True)
    name = Column(String(5000), nullable=False)
    version = Column(String(500), default="v1")
    dt_created = Column(DateTime, default=datetime.datetime.utcnow)
    dt_updated = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    doors = relationship("Door", back_populates="type")

    def sanitize(self):
        return {
            "id": self.id,
            "name": self.name,
            "version": self.version,
            "dt_created": self.dt_created,
            "dt_updated": self.dt_updated
        }

    @classmethod
    def create(cls, session, name, version = None):
        door_type = DoorType(name=name, version=version or "v1")
        session.add(door_type)
        return door_type

    @classmethod
    def get_by_id(cls, session, id):
        return session.query(DoorType).get(int(id))

    @classmethod
    def query(cls, session, id, name, version):
        door_type_query = session.query(DoorType)

        if id:
            door_type_query = door_type_query.filter(DoorType.id == id)

        if name:
            door_type_query = door_type_query.filter(DoorType.name == name)

        if version:
            door_type_query = door_type_query.filter(DoorType.version == version)

        return door_type_query


class DoorTransom(Base):
    __tablename__ = "door_transoms"

    id = Column(Integer, primary_key=True)
    material = Column(String(5000), nullable=False)
    version = Column(String(500), default="v1")
    dt_created = Column(DateTime, default=datetime.datetime.utcnow)
    dt_updated = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    doors = relationship("Door", back_populates="transom")

    def sanitize(self):
        return {
            "id": self.id,
            "material": self.material,
            "version": self.version,
            "dt_created": self.dt_created,
            "dt_updated": self.dt_updated
        }

    @classmethod
    def create(cls, session, material, version = None):
        door_transom = DoorTransom(material=material, version=version or "v1")
        session.add(door_transom)
        return door_transom

    @classmethod
    def get_by_id(cls, session, id):
        return session.query(DoorTransom).get(int(id))

    @classmethod
    def query(cls, session, id, material, version):
        door_transom_query = session.query(DoorTransom)

        if id:
            door_transom_query = door_transom_query.filter(DoorTransom.id == id)

        if material:
            door_transom_query = door_transom_query.filter(DoorTransom.material == material)

        if version:
            door_transom_query = door_transom_query.filter(DoorTransom.version == version)

        return door_transom_query


class DoorHinge(Base):
    __tablename__ = "door_hinges"

    id = Column(Integer, primary_key=True)
    type = Column(String(5000), nullable=False)
    version = Column(String(500), default="v1")
    dt_created = Column(DateTime, default=datetime.datetime.utcnow)
    dt_updated = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    doors = relationship("Door", back_populates="hinge")

    def sanitize(self):
        return {
            "id": self.id,
            "type": self.type,
            "version": self.version,
            "dt_created": self.dt_created,
            "dt_updated": self.dt_updated
        }

    @classmethod
    def create(cls, session, type, version = None):
        door_hinge = DoorHinge(type=type, version=version or "v1")
        session.add(door_hinge)
        return door_hinge

    @classmethod
    def get_by_id(cls, session, id):
        return session.query(DoorHinge).get(int(id))

    @classmethod
    def query(cls, session, id, type, version):
        door_hinge_query = session.query(DoorHinge)

        if id:
            door_hinge_query = door_hinge_query.filter(DoorHinge.id == id)

        if type:
            door_hinge_query = door_hinge_query.filter(DoorHinge.type == type)

        if version:
            door_hinge_query = door_hinge_query.filter(DoorHinge.version == version)

        return door_hinge_query


class DoorContinousHinge(Base):
    __tablename__ = "door_continous_hinges"

    id = Column(Integer, primary_key=True)
    name = Column(String(5000), nullable=False)
    version = Column(String(500), default="v1")
    dt_created = Column(DateTime, default=datetime.datetime.utcnow)
    dt_updated = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    doors = relationship("Door", back_populates="continous_hinge")

    def sanitize(self):
        return {
            "id": self.id,
            "name": self.name,
            "version": self.version,
            "dt_created": self.dt_created,
            "dt_updated": self.dt_updated
        }

    @classmethod
    def create(cls, session, name, version = None):
        door_continuous_hinge = DoorContinousHinge(name=name, version=version or "v1")
        session.add(door_continuous_hinge)
        return door_continuous_hinge

    @classmethod
    def get_by_id(cls, session, id):
        return session.query(DoorContinousHinge).get(int(id))

    @classmethod
    def query(cls, session, id, name, version):
        door_continuous_hinge_query = session.query(DoorContinousHinge)

        if id:
            door_continuous_hinge_query = door_continuous_hinge_query.filter(DoorContinousHinge.id == id)

        if name:
            door_continuous_hinge_query = door_continuous_hinge_query.filter(DoorContinousHinge.name == name)

        if version:
            door_continuous_hinge_query = door_continuous_hinge_query.filter(DoorContinousHinge.version == version)

        return door_continuous_hinge_query


class DoorPivot(Base):
    __tablename__ = "door_pivots"

    id = Column(Integer, primary_key=True)
    type = Column(String(5000), nullable=False)
    version = Column(String(500), default="v1")
    dt_created = Column(DateTime, default=datetime.datetime.utcnow)
    dt_updated = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    doors = relationship("Door", back_populates="pivot")
    
    def sanitize(self):
        return {
            "id": self.id,
            "type": self.type,
            "version": self.version,
            "dt_created": self.dt_created,
            "dt_updated": self.dt_updated
        }

    @classmethod
    def create(cls, session, type, version = None):
        door_pivot = DoorPivot(type=type, version=version or "v1")
        session.add(door_pivot)
        return door_pivot

    @classmethod
    def get_by_id(cls, session, id):
        return session.query(DoorPivot).get(int(id))

    @classmethod
    def query(cls, session, id, type, version):
        door_pivot_query = session.query(DoorPivot)

        if id:
            door_pivot_query = door_pivot_query.filter(DoorPivot.id == id)

        if type:
            door_pivot_query = door_pivot_query.filter(DoorPivot.type == type)

        if version:
            door_pivot_query = door_pivot_query.filter(DoorPivot.version == version)

        return door_pivot_query


class DoorPowerTransfer(Base):
    __tablename__ = "door_power_transfers"

    id = Column(Integer, primary_key=True)
    type = Column(String(5000), nullable=False)
    version = Column(String(500), default="v1")
    dt_created = Column(DateTime, default=datetime.datetime.utcnow)
    dt_updated = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    doors = relationship("Door", back_populates="power_transfer")

    def sanitize(self):
        return {
            "id": self.id,
            "type": self.type,
            "version": self.version,
            "dt_created": self.dt_created,
            "dt_updated": self.dt_updated
        }

    @classmethod
    def create(cls, session, type, version = None):
        door_power_transfer = DoorPowerTransfer(type=type, version=version or "v1")
        session.add(door_power_transfer)
        return door_power_transfer

    @classmethod
    def get_by_id(cls, session, id):
        return session.query(DoorPowerTransfer).get(int(id))

    @classmethod
    def query(cls, session, id, type, version):
        door_power_transfer_query = session.query(DoorPowerTransfer)

        if id:
            door_power_transfer_query = door_power_transfer_query.filter(DoorPowerTransfer.id == id)

        if type:
            door_power_transfer_query = door_power_transfer_query.filter(DoorPowerTransfer.type == type)

        if version:
            door_power_transfer_query = door_power_transfer_query.filter(DoorPowerTransfer.version == version)

        return door_power_transfer_query


class DoorLockset(Base):
    __tablename__ = "door_locksets"

    id = Column(Integer, primary_key=True)
    type = Column(String(5000), nullable=False)
    version = Column(String(500), default="v1")
    dt_created = Column(DateTime, default=datetime.datetime.utcnow)
    dt_updated = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    doors = relationship("Door", back_populates="lockset")

    def sanitize(self):
        return {
            "id": self.id,
            "type": self.type,
            "version": self.version,
            "dt_created": self.dt_created,
            "dt_updated": self.dt_updated
        }

    @classmethod
    def create(cls, session, type, version = None):
        door_lockset = DoorLockset(type=type, version=version or "v1")
        session.add(door_lockset)
        return door_lockset

    @classmethod
    def get_by_id(cls, session, id):
        return session.query(DoorLockset).get(int(id))

    @classmethod
    def query(cls, session, id, type, version):
        door_lockset_query = session.query(DoorLockset)

        if id:
            door_lockset_query = door_lockset_query.filter(DoorLockset.id == id)

        if type:
            door_lockset_query = door_lockset_query.filter(DoorLockset.type == type)

        if version:
            door_lockset_query = door_lockset_query.filter(DoorLockset.version == version)

        return door_lockset_query


class DoorElectricLockset(Base):
    __tablename__ = "door_electric_locksets"

    id = Column(Integer, primary_key=True)
    type = Column(String(5000), nullable=False)
    version = Column(String(500), default="v1")
    dt_created = Column(DateTime, default=datetime.datetime.utcnow)
    dt_updated = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    doors = relationship("Door", back_populates="electric_lockset")

    def sanitize(self):
        return {
            "id": self.id,
            "type": self.type,
            "version": self.version,
            "dt_created": self.dt_created,
            "dt_updated": self.dt_updated
        }

    @classmethod
    def create(cls, session, type, version):
        door_electric_lockset = DoorElectricLockset(type=type, version=version or "v1")
        session.add(door_electric_lockset)
        return door_electric_lockset

    @classmethod
    def get_by_id(cls, session, id):
        return session.query(DoorElectricLockset).get(int(id))

    @classmethod
    def query(cls, session, id, type, version):
        door_electric_lockset_query = session.query(DoorElectricLockset)

        if id:
            door_electric_lockset_query = door_electric_lockset_query.filter(DoorElectricLockset.id == id)

        if type:
            door_electric_lockset_query = door_electric_lockset_query.filter(DoorElectricLockset.type == type)

        if version:
            door_electric_lockset_query = door_electric_lockset_query.filter(DoorElectricLockset.version == version)

        return door_electric_lockset_query


class DoorStrike(Base):
    __tablename__ = "door_strikes"

    id = Column(Integer, primary_key=True)
    type = Column(String(5000), nullable=False)
    version = Column(String(500), default="v1")
    dt_created = Column(DateTime, default=datetime.datetime.utcnow)
    dt_updated = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    doors = relationship("Door", back_populates="strike")

    def sanitize(self):
        return {
            "id": self.id,
            "type": self.type,
            "version": self.version,
            "dt_created": self.dt_created,
            "dt_updated": self.dt_updated
        }

    @classmethod
    def create(cls, session, type, version = None):
        door_strike = DoorStrike(type=type, version=version or "v1")
        session.add(door_strike)
        return door_strike

    @classmethod
    def get_by_id(cls, session, id):
        return session.query(DoorStrike).get(int(id))

    @classmethod
    def query(cls, session, id, type, version):
        door_strike_query = session.query(DoorStrike)

        if id:
            door_strike_query = door_strike_query.filter(DoorStrike.id == id)

        if type:
            door_strike_query = door_strike_query.filter(DoorStrike.type == type)

        if version:
            door_strike_query = door_strike_query.filter(DoorStrike.version == version)

        return door_strike_query


class DoorExitDevice(Base):
    __tablename__ = "door_exit_devices"

    id = Column(Integer, primary_key=True)
    name = Column(String(5000), nullable=False)
    version = Column(String(500), default="v1")
    dt_created = Column(DateTime, default=datetime.datetime.utcnow)
    dt_updated = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    doors = relationship("Door", back_populates="exit_device")

    def sanitize(self):
        return {
            "id": self.id,
            "name": self.name,
            "version": self.version,
            "dt_created": self.dt_created,
            "dt_updated": self.dt_updated
        }

    @classmethod
    def create(cls, session, name, version = None):
        door_exit_device = DoorExitDevice(name=name, version=version or "v1")
        session.add(door_exit_device)
        return door_exit_device

    @classmethod
    def get_by_id(cls, session, id):
        return session.query(DoorExitDevice).get(int(id))

    @classmethod
    def query(cls, session, id, name, version):
        door_exit_device_query = session.query(DoorExitDevice)

        if id:
            door_exit_device_query = door_exit_device_query.filter(DoorExitDevice.id == id)

        if name:
            door_exit_device_query = door_exit_device_query.filter(DoorExitDevice.name == name)

        if version:
            door_exit_device_query = door_exit_device_query.filter(DoorExitDevice.version == version)

        return door_exit_device_query


class DoorTrim(Base):
    __tablename__ = "door_trims"

    id = Column(Integer, primary_key=True)
    name = Column(String(5000), nullable=False)
    version = Column(String(500), default="v1")
    dt_created = Column(DateTime, default=datetime.datetime.utcnow)
    dt_updated = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    doors = relationship("Door", back_populates="trim")

    def sanitize(self):
        return {
            "id": self.id,
            "name": self.name,
            "version": self.version,
            "dt_created": self.dt_created,
            "dt_updated": self.dt_updated
        }

    @classmethod
    def create(cls, session, name, version = None):
        door_trim = DoorTrim(name=name, version=version or "v1")
        session.add(door_trim)
        return door_trim

    @classmethod
    def get_by_id(cls, session, id):
        return session.query(DoorTrim).get(int(id))

    @classmethod
    def query(cls, session, id, name, version):
        door_trim_query = session.query(DoorTrim)

        if id:
            door_trim_query = door_trim_query.filter(DoorTrim.id == id)

        if name:
            door_trim_query = door_trim_query.filter(DoorTrim.name == name)

        if version:
            door_trim_query = door_trim_query.filter(DoorTrim.version == version)

        return door_trim_query


class DoorDelayEgress(Base):
    __tablename__ = "door_delay_egress"

    id = Column(Integer, primary_key=True)
    type = Column(String(5000), nullable=False)
    version = Column(String(500), default="v1")
    dt_created = Column(DateTime, default=datetime.datetime.utcnow)
    dt_updated = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    doors = relationship("Door", back_populates="delay_egress")
    def sanitize(self):
        return {
            "id": self.id,
            "type": self.type,
            "version": self.version,
            "dt_created": self.dt_created,
            "dt_updated": self.dt_updated
        }

    @classmethod
    def create(cls, session, type, version = None):
        door_delay_egress = DoorDelayEgress(type=type, version=version or "v1")
        session.add(door_delay_egress)
        return door_delay_egress

    @classmethod
    def get_by_id(cls, session, id):
        return session.query(DoorDelayEgress).get(int(id))

    @classmethod
    def query(cls, session, id, type, version):
        door_delay_egress_query = session.query(DoorDelayEgress)

        if id:
            door_delay_egress_query = door_delay_egress_query.filter(DoorDelayEgress.id == id)

        if type:
            door_delay_egress_query = door_delay_egress_query.filter(DoorDelayEgress.type == type)

        if version:
            door_delay_egress_query = door_delay_egress_query.filter(DoorDelayEgress.version == version)

        return door_delay_egress_query


class DoorCylinder(Base):
    __tablename__ = "door_cylinders"

    id = Column(Integer, primary_key=True)
    name = Column(String(5000), nullable=False)
    version = Column(String(500), default="v1")
    dt_created = Column(DateTime, default=datetime.datetime.utcnow)
    dt_updated = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    def sanitize(self):
        return {
            "id": self.id,
            "name": self.name,
            "version": self.version,
            "dt_created": self.dt_created,
            "dt_updated": self.dt_updated
        }

    @classmethod
    def create(cls, session, name, version = None):
        door_cylinder = DoorCylinder(name=name, version=version or "v1")
        session.add(door_cylinder)
        return door_cylinder

    @classmethod
    def get_by_id(cls, session, id):
        return session.query(DoorCylinder).get(int(id))

    @classmethod
    def query(cls, session, id, name, version):
        door_cylinder_query = session.query(DoorCylinder)

        if id:
            door_cylinder_query = door_cylinder_query.filter(DoorCylinder.id == id)

        if name:
            door_cylinder_query = door_cylinder_query.filter(DoorCylinder.name == name)

        if version:
            door_cylinder_query = door_cylinder_query.filter(DoorCylinder.version == version)

        return door_cylinder_query


class DoorCloser(Base):
    __tablename__ = "door_closers"

    id = Column(Integer, primary_key=True)
    name = Column(String(5000), nullable=False)
    version = Column(String(500), default="v1")
    dt_created = Column(DateTime, default=datetime.datetime.utcnow)
    dt_updated = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    def sanitize(self):
        return {
            "id": self.id,
            "name": self.name,
            "version": self.version,
            "dt_created": self.dt_created,
            "dt_updated": self.dt_updated
        }

    @classmethod
    def create(cls, session, name, version = None):
        door_closer = DoorCloser(name=name, version=version or "v1")
        session.add(door_closer)
        return door_closer

    @classmethod
    def get_by_id(cls, session, id):
        return session.query(DoorCloser).get(int(id))

    @classmethod
    def query(cls, session, id, name, version):
        door_closer_query = session.query(DoorCloser)

        if id:
            door_closer_query = door_closer_query.filter(DoorCloser.id == id)

        if name:
            door_closer_query = door_closer_query.filter(DoorCloser.name == name)

        if version:
            door_closer_query = door_closer_query.filter(DoorCloser.version == version)

        return door_closer_query


class DoorAutoOperator(Base):
    __tablename__ = "door_auto_operators"

    id = Column(Integer, primary_key=True)
    name = Column(String(5000), nullable=False)
    version = Column(String(500), default="v1")
    dt_created = Column(DateTime, default=datetime.datetime.utcnow)
    dt_updated = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    def sanitize(self):
        return {
            "id": self.id,
            "name": self.name,
            "version": self.version,
            "dt_created": self.dt_created,
            "dt_updated": self.dt_updated
        }

    @classmethod
    def create(cls, session, name, version = None):
        door_auto_operator = DoorAutoOperator(name=name, version=version or "v1")
        session.add(door_auto_operator)
        return door_auto_operator

    @classmethod
    def get_by_id(cls, session, id):
        return session.query(DoorAutoOperator).get(int(id))

    @classmethod
    def query(cls, session, id, name, version):
        door_auto_operator_query = session.query(DoorAutoOperator)

        if id:
            door_auto_operator_query = door_auto_operator_query.filter(DoorAutoOperator.id == id)

        if name:
            door_auto_operator_query = door_auto_operator_query.filter(DoorAutoOperator.name == name)

        if version:
            door_auto_operator_query = door_auto_operator_query.filter(DoorAutoOperator.version == version)

        return door_auto_operator_query


class DoorAOWallPlate(Base):
    __tablename__ = "door_ao_wall_plates"

    id = Column(Integer, primary_key=True)
    type = Column(String(5000), nullable=False)
    version = Column(String(500), default="v1")
    dt_created = Column(DateTime, default=datetime.datetime.utcnow)
    dt_updated = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    def sanitize(self):
        return {
            "id": self.id,
            "type": self.type,
            "version": self.version,
            "dt_created": self.dt_created,
            "dt_updated": self.dt_updated
        }

    @classmethod
    def create(cls, session, type, version = None):
        door_ao_wall_plate = DoorAOWallPlate(type=type, version=version or "v1")
        session.add(door_ao_wall_plate)
        return door_ao_wall_plate

    @classmethod
    def get_by_id(cls, session, id):
        return session.query(DoorAOWallPlate).get(int(id))

    @classmethod
    def query(cls, session, id, type, version):
        door_ao_wall_plate_query = session.query(DoorAOWallPlate)

        if id:
            door_ao_wall_plate_query = door_ao_wall_plate_query.filter(DoorAOWallPlate.id == id)

        if type:
            door_ao_wall_plate_query = door_ao_wall_plate_query.filter(DoorAOWallPlate.type == type)

        if version:
            door_ao_wall_plate_query = door_ao_wall_plate_query.filter(DoorAOWallPlate.version == version)

        return door_ao_wall_plate_query


class DoorCoordinator(Base):
    __tablename__ = "door_coordinators"

    id = Column(Integer, primary_key=True)
    type = Column(String(5000), nullable=False)
    version = Column(String(500), default="v1")
    dt_created = Column(DateTime, default=datetime.datetime.utcnow)
    dt_updated = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    def sanitize(self):
        return {
            "id": self.id,
            "type": self.type,
            "version": self.version,
            "dt_created": self.dt_created,
            "dt_updated": self.dt_updated
        }

    @classmethod
    def create(cls, session, type, version = None):
        door_coordinator = DoorCoordinator(type=type, version=version or "v1")
        session.add(door_coordinator)
        return door_coordinator

    @classmethod
    def get_by_id(cls, session, id):
        return session.query(DoorCoordinator).get(int(id))

    @classmethod
    def query(cls, session, id, type, version):
        door_coordinator_query = session.query(DoorCoordinator)

        if id:
            door_coordinator_query = door_coordinator_query.filter(DoorCoordinator.id == id)

        if type:
            door_coordinator_query = door_coordinator_query.filter(DoorCoordinator.type == type)

        if version:
            door_coordinator_query = door_coordinator_query.filter(DoorCoordinator.version == version)

        return door_coordinator_query


class DoorFlushBolt(Base):
    __tablename__ = "door_flush_bolts"

    id = Column(Integer, primary_key=True)
    type = Column(String(5000), nullable=False)
    version = Column(String(500), default="v1")
    dt_created = Column(DateTime, default=datetime.datetime.utcnow)
    dt_updated = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    def sanitize(self):
        return {
            "id": self.id,
            "type": self.type,
            "version": self.version,
            "dt_created": self.dt_created,
            "dt_updated": self.dt_updated
        }

    @classmethod
    def create(cls, session, type, version = None):
        door_flush_bolt = DoorFlushBolt(type=type, version=version or "v1")
        session.add(door_flush_bolt)
        return door_flush_bolt

    @classmethod
    def get_by_id(cls, session, id):
        return session.query(DoorFlushBolt).get(int(id))

    @classmethod
    def query(cls, session, id, type, version):
        door_flush_bolt_query = session.query(DoorFlushBolt)

        if id:
            door_flush_bolt_query = door_flush_bolt_query.filter(DoorFlushBolt.id == id)

        if type:
            door_flush_bolt_query = door_flush_bolt_query.filter(DoorFlushBolt.type == type)

        if version:
            door_flush_bolt_query = door_flush_bolt_query.filter(DoorFlushBolt.version == version)

        return door_flush_bolt_query


class DoorMagHolder(Base):
    __tablename__ = "door_mag_holders"

    id = Column(Integer, primary_key=True)
    type = Column(String(5000), nullable=False)
    version = Column(String(500), default="v1")
    dt_created = Column(DateTime, default=datetime.datetime.utcnow)
    dt_updated = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    def sanitize(self):
        return {
            "id": self.id,
            "type": self.type,
            "version": self.version,
            "dt_created": self.dt_created,
            "dt_updated": self.dt_updated
        }

    @classmethod
    def create(cls, session, type, version = None):
        door_mag_holder = DoorMagHolder(type=type, version=version or "v1")
        session.add(door_mag_holder)
        return door_mag_holder

    @classmethod
    def get_by_id(cls, session, id):
        return session.query(DoorMagHolder).get(int(id))

    @classmethod
    def query(cls, session, id, type, version):
        door_mag_holder_query = session.query(DoorMagHolder)

        if id:
            door_mag_holder_query = door_mag_holder_query.filter(DoorMagHolder.id == id)

        if type:
            door_mag_holder_query = door_mag_holder_query.filter(DoorMagHolder.type == type)

        if version:
            door_mag_holder_query = door_mag_holder_query.filter(DoorMagHolder.version == version)

        return door_mag_holder_query


class DoorStop(Base):
    __tablename__ = "door_stops"

    id = Column(Integer, primary_key=True)
    type = Column(String(5000), nullable=False)
    version = Column(String(500), default="v1")
    dt_created = Column(DateTime, default=datetime.datetime.utcnow)
    dt_updated = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    def sanitize(self):
        return {
            "id": self.id,
            "type": self.type,
            "version": self.version,
            "dt_created": self.dt_created,
            "dt_updated": self.dt_updated
        }

    @classmethod
    def create(cls, session, type, version = None):
        door_stop = DoorStop(type=type, version=version or "v1")
        session.add(door_stop)
        return door_stop

    @classmethod
    def get_by_id(cls, session, id):
        return session.query(DoorStop).get(int(id))

    @classmethod
    def query(cls, session, id, type, version):
        door_stop_query = session.query(DoorStop)

        if id:
            door_stop_query = door_stop_query.filter(DoorStop.id == id)

        if type:
            door_stop_query = door_stop_query.filter(DoorStop.type == type)

        if version:
            door_stop_query = door_stop_query.filter(DoorStop.version == version)

        return door_stop_query


class DoorAstragal(Base):
    __tablename__ = "door_astragals"

    id = Column(Integer, primary_key=True)
    type = Column(String(5000), nullable=False)
    version = Column(String(500), default="v1")
    dt_created = Column(DateTime, default=datetime.datetime.utcnow)
    dt_updated = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    def sanitize(self):
        return {
            "id": self.id,
            "type": self.type,
            "version": self.version,
            "dt_created": self.dt_created,
            "dt_updated": self.dt_updated
        }

    @classmethod
    def create(cls, session, type, version = None):
        door_astragal = DoorAstragal(type=type, version=version or "v1")
        session.add(door_astragal)
        return door_astragal

    @classmethod
    def get_by_id(cls, session, id):
        return session.query(DoorAstragal).get(int(id))

    @classmethod
    def query(cls, session, id, type, version):
        door_astragal_query = session.query(DoorAstragal)

        if id:
            door_astragal_query = door_astragal_query.filter(DoorAstragal.id == id)

        if type:
            door_astragal_query = door_astragal_query.filter(DoorAstragal.type == type)

        if version:
            door_astragal_query = door_astragal_query.filter(DoorAstragal.version == version)

        return door_astragal_query


class DoorSeal(Base):
    __tablename__ = "door_seals"

    id = Column(Integer, primary_key=True)
    type = Column(String(5000), nullable=False)
    version = Column(String(500), default="v1")
    dt_created = Column(DateTime, default=datetime.datetime.utcnow)
    dt_updated = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    def sanitize(self):
        return {
            "id": self.id,
            "type": self.type,
            "version": self.version,
            "dt_created": self.dt_created,
            "dt_updated": self.dt_updated
        }

    @classmethod
    def create(cls, session, type, version = None):
        door_seal = DoorSeal(type=type, version=version or "v1")
        session.add(door_seal)
        return door_seal

    @classmethod
    def get_by_id(cls, session, id):
        return session.query(DoorSeal).get(int(id))

    @classmethod
    def query(cls, session, id, type, version):
        door_seal_query = session.query(DoorSeal)

        if id:
            door_seal_query = door_seal_query.filter(DoorSeal.id == id)

        if type:
            door_seal_query = door_seal_query.filter(DoorSeal.type == type)

        if version:
            door_seal_query = door_seal_query.filter(DoorSeal.version == version)

        return door_seal_query


class DoorSweep(Base):
    __tablename__ = "door_sweeps"

    id = Column(Integer, primary_key=True)
    name = Column(String(5000), nullable=False)
    version = Column(String(500), default="v1")
    dt_created = Column(DateTime, default=datetime.datetime.utcnow)
    dt_updated = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    def sanitize(self):
        return {
            "id": self.id,
            "name": self.name,
            "version": self.version,
            "dt_created": self.dt_created,
            "dt_updated": self.dt_updated
        }

    @classmethod
    def create(cls, session, name, version = None):
        door_sweep = DoorSweep(name=name, version=version or "v1")
        session.add(door_sweep)
        return door_sweep

    @classmethod
    def get_by_id(cls, session, id):
        return session.query(DoorSweep).get(int(id))

    @classmethod
    def query(cls, session, id, name, version):
        door_sweep_query = session.query(DoorSweep)

        if id:
            door_sweep_query = door_sweep_query.filter(DoorSweep.id == id)

        if name:
            door_sweep_query = door_sweep_query.filter(DoorSweep.name == name)

        if version:
            door_sweep_query = door_sweep_query.filter(DoorSweep.version == version)

        return door_sweep_query


class DoorAutoDrBtm(Base):
    __tablename__ = "door_auto_dr_btms"

    id = Column(Integer, primary_key=True)
    type = Column(String(5000), nullable=False)
    version = Column(String(500), default="v1")
    dt_created = Column(DateTime, default=datetime.datetime.utcnow)
    dt_updated = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    def sanitize(self):
        return {
            "id": self.id,
            "type": self.type,
            "version": self.version,
            "dt_created": self.dt_created,
            "dt_updated": self.dt_updated
        }

    @classmethod
    def create(cls, session, type, version = None):
        door_auto_dr_btm = DoorAutoDrBtm(type=type, version=version or "v1")
        session.add(door_auto_dr_btm)
        return door_auto_dr_btm

    @classmethod
    def get_by_id(cls, session, id):
        return session.query(DoorAutoDrBtm).get(int(id))

    @classmethod
    def query(cls, session, id, type, version):
        door_auto_dr_btm_query = session.query(DoorAutoDrBtm)

        if id:
            door_auto_dr_btm_query = door_auto_dr_btm_query.filter(DoorAutoDrBtm.id == id)

        if type:
            door_auto_dr_btm_query = door_auto_dr_btm_query.filter(DoorAutoDrBtm.type == type)

        if version:
            door_auto_dr_btm_query = door_auto_dr_btm_query.filter(DoorAutoDrBtm.version == version)

        return door_auto_dr_btm_query


class DoorThreshold(Base):
    __tablename__ = "door_thresholds"

    id = Column(Integer, primary_key=True)
    type = Column(String(5000), nullable=False)
    version = Column(String(500), default="v1")
    dt_created = Column(DateTime, default=datetime.datetime.utcnow)
    dt_updated = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    def sanitize(self):
        return {
            "id": self.id,
            "type": self.type,
            "version": self.version,
            "dt_created": self.dt_created,
            "dt_updated": self.dt_updated
        }

    @classmethod
    def create(cls, session, type, version = None):
        door_threshold = DoorThreshold(type=type, version=version or "v1")
        session.add(door_threshold)
        return door_threshold

    @classmethod
    def get_by_id(cls, session, id):
        return session.query(DoorThreshold).get(int(id))

    @classmethod
    def query(cls, session, id, type, version):
        door_threshold_query = session.query(DoorThreshold)

        if id:
            door_threshold_query = door_threshold_query.filter(DoorThreshold.id == id)

        if type:
            door_threshold_query = door_threshold_query.filter(DoorThreshold.type == type)

        if version:
            door_threshold_query = door_threshold_query.filter(DoorThreshold.version == version)

        return door_threshold_query

class Door(Base):
    __tablename__ = "doors"

    door_no = Column(Integer, primary_key=True)
    floor_no = Column(Integer, ForeignKey("floors.floor_no"), primary_key=True)
    building_id = Column(Integer, ForeignKey("buildings.id"), primary_key=True)
    door_name = Column(String(5000), nullable=False, unique=True)
    compliance_id = Column(Integer, ForeignKey("compliancies.id"))
    fire_rating_id = Column(Integer, ForeignKey("fire_ratings.id"))
    category_id = Column(Integer, ForeignKey("door_categories.id"))
    frame_id = Column(Integer, ForeignKey("door_frames.id"))
    size = Column(String(5000))
    type_id = Column(Integer, ForeignKey("door_types.id"))
    vision_lite = Column(Boolean, default=False)
    transom_id = Column(Integer, ForeignKey("door_transoms.id"))
    side_lite = Column(Boolean, default=False)
    hinge_id = Column(Integer, ForeignKey("door_hinges.id"))
    hinge_size = Column(String(5000))
    continous_hinge_id = Column(Integer, ForeignKey("door_continous_hinges.id"))
    pivot_id = Column(Integer, ForeignKey("door_pivots.id"))
    power_transfer_id = Column(Integer, ForeignKey("door_power_transfers.id"))
    lockset_id = Column(Integer, ForeignKey("door_locksets.id"))
    electric_lockset_id = Column(Integer, ForeignKey("door_electric_locksets.id"))
    strike_id = Column(Integer, ForeignKey("door_strikes.id"))
    exit_device_id = Column(Integer, ForeignKey("door_exit_devices.id"))
    electric_exit_device = Column(Boolean, default=False)
    mullion = Column(Boolean, default=False)
    trim_id = Column(Integer, ForeignKey("door_trims.id"))
    delay_egress_id = Column(Integer, ForeignKey("door_delay_egress.id"))

    version = Column(String(500), default="v1")
    dt_created = Column(DateTime, default=datetime.datetime.utcnow)
    dt_updated = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    building = relationship("Building", back_populates="doors")
    floor = relationship("Floor", back_populates="doors")
    compliance = relationship("Compliance", back_populates="doors")
    fire_rating = relationship("FireRating", back_populates="doors")
    category = relationship("DoorCategory", back_populates="doors")
    frame = relationship("DoorFrame", back_populates="doors")
    type = relationship("DoorType", back_populates="doors")
    transom = relationship("DoorTransom", back_populates="doors")
    hinge = relationship("DoorHinge", back_populates="doors")
    continous_hinge = relationship("DoorContinousHinge", back_populates="doors")
    pivot = relationship("DoorPivot", back_populates="doors")
    power_transfer = relationship("DoorPowerTransfer", back_populates="doors")
    lockset = relationship("DoorLockset", back_populates="doors")
    electric_lockset = relationship("DoorElectricLockset", back_populates="doors")
    strike = relationship("DoorStrike", back_populates="doors")
    exit_device = relationship("DoorExitDevice", back_populates="doors")
    trim = relationship("DoorTrim", back_populates="doors")
    delay_egress = relationship("DoorDelayEgress", back_populates="doors")

    def sanitize (self):
        return {
            "door_no" : self.door_no,
            "floor_no": self.floor_no,
            "building_id": self.building_id,
            "door_name": self.door_name,
            "compliance_id": self.complaiance_id,
            "fire_rating_id": self.fire_rating_id,
            "category_id": self.category_id,
            "frame_id": self.frame_id,
            "size": self.size,
            "type_id": self.type_id,
            "vision_lite": self.vision_lite,
            "transom_id": self.transom_id,
            "side_lite": self.side_lite,
            "hinge_id": self.hinge_id,
            "hinge_size": self.hinge_size,
            "continous_hinge_id": self.continous_hinge_id,
            "pivot_id": self.pivot_id,
            "power_transfer_id": self.power_transfer_id,
            "lockset_id": self.lockset_id,
            "electric_lockset_id": self.electric_lockset_id,
            "strike_id": self.strike_id,
            "exit_device_id": self.exit_device_id,
            "electric_exit_device": self.electric_exit_device,
            "mullion": self.mullion,
            "trim_id": self.trim_id,
            "delay_egress_id": self.delay_egress_id,

            "version": self.version,
            "dt_created": self.dt_created,
            "dt_updated": self.dt_updated
        }

    @classmethod
    def create (cls, session, data, version = None):
        door_no = data["door_no"]
        floor_no = data["floor_no"]
        building_id = data["building_id"]
        door_name = data["door_name"]
        complaince_id = data["complaince_id"]
        fire_rating_id = data["fire_rating_id"]
        category_id = data["category_id"]
        frame_id = data["frame_id"]
        size =   data["size"]
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
        trim_id= data["trim_id"]
        delay_egress_id = data["delay_egress_id"]

        door = Door (door_no = door_no, floor_no = floor_no, building_id = building_id, door_name = door_name, complaince_id = complaince_id, fire_rating_id = fire_rating_id,
                     category_id = category_id, frame_id = frame_id, size = size, type_id = type_id, vision_lite = vision_lite, transom_id = transom_id, side_lite = side_lite,
                    hinge_id = hinge_id, hinge_size = hinge_size, continous_hinge_id = continous_hinge_id, pivot_id = pivot_id, power_transfer_id = power_transfer_id,
                     lockset_id = lockset_id, electric_lockset_id = electric_lockset_id, strike_id = strike_id, exit_device_id = exit_device_id,
                     electric_exit_device = electric_exit_device, mullion = mullion, trim_id = trim_id, delay_egress_id = delay_egress_id)
        session.add (door)
        return door

