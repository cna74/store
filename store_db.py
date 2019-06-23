from sqlalchemy import create_engine, Column, String, Integer, Text, Time, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from khayyam3 import JalaliDatetime

Base = declarative_base()


class Rent(Base):
    def __init__(self, _id=None, date=None, time=None, who="", first_name="", last_name="", product="",
                 address="", pre_paid=0, post_paid=0, paid=0, others="", img_path=""):
        self.id = _id
        self.date = date
        self.time = time
        self.who = who
        self.first_name = first_name
        self.last_name = last_name
        self.product = product
        self.address = address
        self.pre_paid = pre_paid
        self.post_paid = post_paid
        self.paid = paid
        self.others = others
        self.img_path = img_path

    def __str__(self):
        return f"""id: {self.id}, date: {self.date}, time: {self.time}, who: {self.who}, first_name: {self.first_name},
last_name: {self.last_name}, product: {self.product}, address: {self.address}, pre_paid: {self.pre_paid},
post_paid: {self.post_paid}, paid: {self.paid}, others: {self.others}, img_path: {self.img_path}"""

    __tablename__ = "rent"

    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(Date)
    time = Column(Time)
    who = Column(String, default="")
    first_name = Column(String, default="")
    last_name = Column(String, default="")
    product = Column(Text, default="")
    address = Column(Text, default="")
    pre_paid = Column(Integer, default=0)
    post_paid = Column(Integer, default=0)
    paid = Column(Integer, default=0)
    others = Column(Text, default="")
    img_path = Column(Text, default="")


# region create
engine = create_engine('sqlite:///store_db.db', connect_args={"check_same_thread": False})
Base.metadata.create_all(bind=engine)
session = Session(bind=engine)
# endregion


def add(obj):
    if isinstance(obj, Rent):
        session.add(obj)
        session.commit()


def get_last_row():
    return session.query(Rent).count()


print()
add(Rent(date=JalaliDatetime.now().date().to_date()))
