from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Band(Base):
    __tablename__ = 'bands'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    hometown = Column(String, nullable=False)

    concerts = relationship('Concert', back_populates='band')

    def play_in_venue(self, venue, date):
        concert = Concert(band=self, venue=venue, date=date)
        return concert

    def venues(self):
        return [concert.venue for concert in self.concerts]

    @classmethod
    def most_performances(cls, session):
        return session.query(cls).outerjoin(Concert).group_by(cls.id).order_by(func.count(Concert.id).desc()).first()

class Venue(Base):
    __tablename__ = 'venues'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    city = Column(String, nullable=False)

    concerts = relationship('Concert', back_populates='venue')

    def bands(self):
        return [concert.band for concert in self.concerts]

    @classmethod
    def most_frequent_band(cls, session):
        return session.query(cls).outerjoin(Concert).group_by(cls.id).order_by(func.count(Concert.id).desc()).first()

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
        return f"{self.band.name} is performing at {self.venue.title} on {self.date}."

# Create the SQLite database
engine = create_engine('sqlite:///concerts.db')
Base.metadata.create_all(engine)

# Session setup
Session = sessionmaker(bind=engine)
session = Session()

# Example to add data and test
if __name__ == "__main__":
    # Add test data
    band = Band(name='The Rockers', hometown='Rock City')
    venue = Venue(title='The Big Stage', city='Rock City')
    session.add(band)
    session.add(venue)
    session.commit()

    # Create a concert using the band's method
    concert = band.play_in_venue(venue, '2024-09-16')
    session.add(concert)
    session.commit()

    # Test methods
    print(band.concerts)  # List of concerts for the band
    print([v.title for v in band.venues()])  # List of venue titles for the band
    print(venue.concerts)  # List of concerts at the venue
    print([b.name for b in venue.bands()])  # List of band names that performed at the venue
    print(concert.hometown_show())  # Check if concert is in the band's hometown
    print(concert.introduction())  # Print introduction
    print(Band.most_performances(session))  # Band with most performances
    print(Venue.most_frequent_band(session))  # Band with most concerts at the venue