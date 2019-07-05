from config import CUSTOMER_RECORDS_FILE_URL, SEARCH_CENTER_LAT, SEARCH_CENTER_LONG, SEARCH_RADIUS
from search_service import SearchService
from utils import exception_to_str
from utils.logging import get_logger

logger = get_logger(__name__)

if __name__ == '__main__':
    try:
        file_url = CUSTOMER_RECORDS_FILE_URL
        center = [SEARCH_CENTER_LAT, SEARCH_CENTER_LONG]

        service = SearchService(SEARCH_RADIUS, center)
        service.populate_customer_from_file(file_url)

        service.print_nearby_customers()
        exit(0)
    except Exception as e:
        logger.error("Search service failed due to an error")
        logger.error(exception_to_str(e))
        exit(1)
