from heapq import heappush, heappop
from typing import Dict, List

from utils.distance_calculator import get_customer_distance
from utils.fileutils import download_file
from utils.logging import get_logger
from utils.parser import parse_customer_records

logger = get_logger(__name__)


class SearchService:

    def __init__(self, search_radius: float, search_center: List[float]):
        self.search_radius = search_radius
        self.search_center = search_center
        self.search_results = []

    def add_customer(self, customer: Dict):
        """
        Add a single customer to our search result if she is within the search radius.
        NOTE: This function can also be used for streaming input
        """
        distance = get_customer_distance(customer, self.search_center)
        # logger.debug("user_id: %, distance: %" % (customer["user_id"], distance))
        if distance < self.search_radius:
            heappush(self.search_results, (customer["user_id"], customer))

    def print_nearby_customers(self):
        """
        Loop over sorted list of customers and print the output
        """
        nearby_customers = self.get_sorted_customers()
        for customer in nearby_customers:
            print(customer)

    def get_sorted_customers(self):
        """
        Return sorted list of customers based on user_id
        """
        result_copy = list(self.search_results)
        sorted_customers = []
        while result_copy:
            (user_id, customer) = heappop(result_copy)
            sorted_customers.append(customer)
        return sorted_customers

    def populate_customer_from_file(self, customer_list_url: str):
        """
        Fetch all customer objects for a remote file and add it to the customer list
        """
        customers = SearchService.fetch_all_customers(customer_list_url)
        for customer in customers:
            self.add_customer(customer)

    @staticmethod
    def fetch_all_customers(customer_list_url: str):
        """
        Download remote file of customer records and return parsed version
        """
        customer_file = download_file(customer_list_url)
        return parse_customer_records(customer_file)
