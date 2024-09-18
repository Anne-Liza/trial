from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Band, Venue, Concert

# Create the SQLite database and session
engine = create_engine('sqlite:///concerts.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Example to add data and test
if __name__ == "__main__":
    # Add test data
    band = Band(name='Sauti Sol', hometown='Nairobi')
    venue = Venue(title='Ngong Race Course', city='Nairobi')
    session.add(band)
    session.add(venue)
    session.commit()

    # Create a concert using the band's method
    concert = band.play_in_venue(venue, '2024-09-16')  # Date as string
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
