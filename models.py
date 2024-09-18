from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.sql import func
from datetime import datetime

Base = declarative_base()

class Band(Base):
    __tablename__ = 'bands'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    hometown = Column(String, nullable=False)

    concerts = relationship('Concert', back_populates='band')

    def play_in_venue(self, venue, date_str):
        date = datetime.strptime(date_str, '%Y-%m-%d').date()
        concert = Concert(band=self, venue=venue, date=date)
        return concert

    def venues(self):
        return [concert.venue for concert in self.concerts]

    @classmethod
    def most_performances(cls, session):
        return session.query(cls).outerjoin(Concert).group_by(cls.id).order_by(func.count(Concert.id).desc()).first()

    def __repr__(self):
        return f"<Band(name={self.name}, hometown={self.hometown})>"

class Venue(Base):
    __tablename__ = 'venues'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    city = Column(String, nullable=False)

    concerts = relationship('Concert', back_populates='venue')

    def bands(self):
        return list({concert.band for concert in self.concerts}) 

    @classmethod
    def most_frequent_band(cls, session):
        return session.query(Band).join(Concert).filter(Concert.venue_id == cls.id).group_by(Band.id).order_by(func.count(Concert.id).desc()).first()

    def __repr__(self):
        return f"<Venue(title={self.title}, city={self.city})>"

class Concert(Base):
    __tablename__ = 'concerts'

    id = Column(Integer, primary_key=True)
    band_id = Column(Integer, ForeignKey('bands.id'), nullable=False)
    venue_id = Column(Integer, ForeignKey('venues.id'), nullable=False)
    date = Column(Date, nullable=False)

    band = relationship('Band', back_populates='concerts')
    venue = relationship('Venue', back_populates='concerts')

    def hometown_show(self):
        return self.venue.city == self.band.hometown

    def introduction(self):
        return f"Another one for {self.venue.city}!!!!! {self.band.name}. Are you ready {self.band.hometown}."

    def __repr__(self):
        return f"<Concert(band={self.band.name}, venue={self.venue.title}, date={self.date})>"

# Create the SQLite database
engine = create_engine('sqlite:///concerts.db')
Base.metadata.create_all(engine)
