# Concert Domain Management

This project implements a simple concert management system using SQLAlchemy ORM with SQLite as the database. It allows users to manage bands, venues, and concerts, capturing relationships and providing functionality to query relevant data.

## Models

### Band
- **Attributes**:
  - `id`: Unique identifier for the band.
  - `name`: Name of the band.
  - `hometown`: Hometown of the band.
- **Methods**:
  - `play_in_venue(venue, date)`: Creates a concert for the band in a specified venue on a given date.
  - `venues()`: Returns a list of venues where the band has performed.
  - `most_performances(session)`: Class method that returns the band with the most concerts.

### Venue
- **Attributes**:
  - `id`: Unique identifier for the venue.
  - `title`: Title of the venue.
  - `city`: City where the venue is located.
- **Methods**:
  - `bands()`: Returns a list of bands that have performed at the venue.
  - `most_frequent_band(session)`: Class method that returns the band that has performed the most concerts at the venue.

### Concert
- **Attributes**:
  - `id`: Unique identifier for the concert.
  - `band_id`: Foreign key referencing the band.
  - `venue_id`: Foreign key referencing the venue.
  - `date`: Date of the concert.
- **Methods**:
  - `hometown_show()`: Checks if the concert is in the band's hometown.
  - `introduction()`: Returns a formatted introduction message for the concert.

## Setup

1. Clone the repository.
2. Install the required packages:
   ```bash
   pip install sqlalchemy
