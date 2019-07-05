import unittest

from search_service import SearchService
from utils.logging import get_logger

logger = get_logger(__name__)


class SearchServiceTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.customers_within_100 = [{'latitude': '53.2451022', 'user_id': 4, 'name': 'Ian Kehoe', 'longitude': '-6.238335'},
                                    {'latitude': '53.1229599', 'user_id': 6, 'name': 'Theresa Enright','longitude': '-6.2705202'},
                                {'latitude': '53.1302756', 'user_id': 5, 'name': 'Nora Dempsey','longitude': '-6.2397222'}]
        cls.distant_customers = [
            {'latitude': '52.228056', 'user_id': 18, 'name': 'Bob Larkin', 'longitude': '-7.915833', 'distance': 166.0},
            {'latitude': '55.033', 'user_id': 19, 'name': 'Enid Cahill', 'longitude': '-8.112', 'distance': 224.0},
            {'latitude': '53.521111', 'user_id': 20, 'name': 'Enid Enright', 'longitude': '-9.831111',
             'distance': 238.0},
            {'latitude': '51.802', 'user_id': 21, 'name': 'David Ahearn', 'longitude': '-9.442', 'distance': 275.0},
            {'latitude': '54.374208', 'user_id': 22, 'name': 'Charlie McArdle', 'longitude': '-8.371639',
             'distance': 180.0},
            {'latitude': '52.833502', 'user_id': 25, 'name': 'David Behan', 'longitude': '-8.522366',
             'distance': 161.0},
            {'latitude': '54.1225', 'user_id': 27, 'name': 'Enid Gallagher', 'longitude': '-8.143333',
             'distance': 152.0},
            {'latitude': '53.807778', 'user_id': 28, 'name': 'Charlie Halligan', 'longitude': '-7.714444',
             'distance': 109.0}
        ]

    def test_search_service(self):
        center = [53.339428, -6.257664]
        customers = [*self.customers_within_100, *self.distant_customers]
        service = SearchService(100, center)
        for customer in customers:
            service.add_customer(customer)
        all_nearby_customers = service.get_sorted_customers()

        self.assertTrue(len(all_nearby_customers) == 3)

        sorted_customers_within_100 = sorted(self.customers_within_100, key=lambda x: x["user_id"])
        all_nearby_customers_user_id = [customer.user_id for customer in all_nearby_customers]
        for i, record in enumerate(sorted_customers_within_100):
            self.assertEqual(all_nearby_customers_user_id[i], record["user_id"])

    def test_search_service_using_file(self):
        # The below file is being treated as test data. It should never change or else, it will break the tests.
        # For running in production, we should use a different file url or
        # swap the below url with a test url that will not change.
        file_url = "https://s3.amazonaws.com/intercom-take-home-test/customers.txt"
        center = [53.339428, -6.257664]
        service = SearchService(100, center)
        service.populate_customer_from_file(file_url)
        all_nearby_customers = service.get_sorted_customers()
        total_nearby_customers = len(all_nearby_customers)
        self.assertTrue(total_nearby_customers == 16)

        for i in range(1, total_nearby_customers):
            self.assertTrue(all_nearby_customers[i-1].user_id < all_nearby_customers[i].user_id)
