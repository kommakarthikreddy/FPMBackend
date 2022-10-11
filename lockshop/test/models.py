import datetime

from email.policy import default
from sqlalchemy import Column, String, DateTime

from lockshop.sql_util.utils import *

class TestTable(Base):
    __tablename__ = "test_table"
    id = Column(Integer, primary_key=True)
    message = Column(String(1000))
    version = Column(String(500), default="v1")
    dt_created = Column(DateTime, default=datetime.datetime.utcnow)
    dt_updated = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    def sanitize(self):
        return {
            "id": self.id,
            "message": self.message or "",
            "version": self.version,
            "dt_created": self.dt_created,
            "dt_updated": self.dt_updated
        }

    @classmethod
    def create(cls, session, message, version="v1"):
        test_record = TestTable(message=message, version=version or "v1")
        session.add(test_record)
        return test_record

    @classmethod
    def get_by_id(cls, session, id):
        return session.query(TestTable).get(int(id))

    @classmethod
    def get_all(cls, session):
        return session.query(TestTable).all()
