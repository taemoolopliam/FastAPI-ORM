from ast import Str
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ..database import Base


class User(Base):
    __tablename__ = "DimCustomer"

    CustomerKey = Column(Integer, primary_key=True, index=True, autoincrement=True)
    GeographyKey = Column(Integer)
    CustomerAlternateKey = Column(String)
    Title =  Column(String)
    FirstName =  Column(String)
    MiddleName = Column(String)
    LastName = Column(String)
    #   NameStyle
    #   BirthDate
    #   MaritalStatus
    #   Suffix
    #   Gender
    #   EmailAddress
    #   YearlyIncome
    #   TotalChildren
    #   NumberChildrenAtHome
    #   EnglishEducation
    #   SpanishEducation
    #   FrenchEducation
    #   EnglishOccupation
    #   SpanishOccupation
    #   FrenchOccupation
    #   HouseOwnerFlag
    #   NumberCarsOwned
    #   AddressLine1
    #   AddressLine2
    #   Phone
    #   DateFirstPurchase
    #   CommuteDistance
