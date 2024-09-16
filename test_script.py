from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Band, Venue, Concert

engine = create_engine('sqlite:///test.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Add test data
band = Band(name='The Rockers', hometown='Rock City')
venue = Venue(title='The Big Stage', city='Rock City')
session.add(band)
session.add(venue)
session.commit()

# Create a concert
concert = band.play_in_venue(venue, '2024-09-16')
session.add(concert)
session.commit()

# Test methods
print(band.concerts())  # List of concerts for the band
print(band.venues())  # List of venues for the band
print(venue.concerts())  # List of concerts at the venue
print(venue.bands())  # List of bands that performed at the venue
print(concert.hometown_show())  # Check if concert is in the band's hometown
print(concert.introduction())  # Print introduction
print(Band.most_performances(session))  # Band with most performances
print(venue.most_frequent_band(session))  # Band with most concerts at the venue
