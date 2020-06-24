import datetime

from flask_appbuilder import Model
from sqlalchemy import Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

mindate = datetime.date(datetime.MINYEAR, 1, 1)


class ContactGroup(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name


class Gender(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name


class Contact(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(150), unique=True, nullable=False)
    address = Column(String(564))
    birthday = Column(Date, nullable=True)
    personal_phone = Column(String(20))
    personal_celphone = Column(String(20))
    contact_group_id = Column(Integer, ForeignKey("contact_group.id"), nullable=False)
    contact_group = relationship("ContactGroup")
    gender_id = Column(Integer, ForeignKey("gender.id"), nullable=False)
    gender = relationship("Gender")

    def __repr__(self):
        return self.name

    def month_year(self):
        date = self.birthday or mindate
        return datetime.datetime(date.year, date.month, 1) or mindate

    def year(self):
        date = self.birthday or mindate
        return datetime.datetime(date.year, 1, 1)


class Test(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(150), unique=False, nullable=False)
    socials = Column(String(5), nullable=False)
    twitter = Column(String(100))
    instagram = Column(String(100))
    facebook = Column(String(100),)

    def __repr__(self):
        return self.name


class Socials(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(20), unique=True, nullable=False)

    def __repr__(self):
        return self.name


class Try(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=False, nullable=False)
    socials_id = Column(Integer, ForeignKey("socials.id"), nullable=False)
    socials = relationship("Socials")
            
    def __repr__(self):
        return self.name
