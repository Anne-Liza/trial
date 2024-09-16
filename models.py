# models.py

from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Band(Base):
    __tablename__ = 'bands'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    hometown = Column(String)
    
    # Relationship to Concerts
    concerts = relationship("Concert", back_populates="band")

    def concerts(self):
        # Method to return all concerts for this band
        pass

    def venues(self):
        # Method to return all venues this band has performed at
        pass

class Venue(Base):
    __tablename__ = 'venues'
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    city = Column(String)
    
    # Relationship to Concerts
    concerts = relationship("Concert", back_populates="venue")

    def concerts(self):
        # Method to return all concerts at this venue
        pass

    def bands(self):
        # Method to return all bands that performed at this venue
        pass

class Concert(Base):
    __tablename__ = 'concerts'
    
    id = Column(Integer, primary_key=True, index=True)
    band_id = Column(Integer, ForeignKey('bands.id'))
    venue_id = Column(Integer, ForeignKey('venues.id'))
    date = Column(String)
    
    # Relationships
    band = relationship("Band", back_populates="concerts")
    venue = relationship("Venue", back_populates="concerts")

    def band(self):
        # Method to return the band for this concert
        pass

    def venue(self):
        # Method to return the venue for this concert
        pass

    def hometown_show(self):
        # Method to check if the concert is in the band's hometown
        pass

    def introduction(self):
        # Method to return the concert introduction string
        pass
