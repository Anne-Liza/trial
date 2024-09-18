import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Band, Venue, Concert

class TestConcertModels(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.engine = create_engine('sqlite:///:memory:')  # Use in-memory database for testing
        Base.metadata.create_all(cls.engine)
        cls.Session = sessionmaker(bind=cls.engine)

    def setUp(self):
        self.session = self.Session()

        # Setup test data
        self.band = Band(name='The Rockers', hometown='Rock City')
        self.venue = Venue(title='The Big Stage', city='Rock City')
        self.session.add(self.band)
        self.session.add(self.venue)
        self.session.commit()

        self.concert = self.band.play_in_venue(self.venue, '2024-09-16')
        self.session.add(self.concert)
        self.session.commit()

    def test_bands_concerts(self):
        self.assertIn(self.concert, self.band.concerts)

    def test_venues(self):
        self.assertIn(self.venue, self.band.venues())

    def test_hometown_show(self):
        self.assertTrue(self.concert.hometown_show())

    def test_introduction(self):
        self.assertEqual(self.concert.introduction(), "The Rockers is performing at The Big Stage on 2024-09-16.")

    @classmethod
    def tearDownClass(cls):
        cls.session.query(Band).delete()
        cls.session.query(Venue).delete()
        cls.session.query(Concert).delete()
        cls.session.commit()

if __name__ == '__main__':
    unittest.main()
