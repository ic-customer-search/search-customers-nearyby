import os

SEARCH_RADIUS = os.getenv("SEARCH_RADIUS", 100)
SEARCH_CENTER_LAT = os.getenv("SEARCH_CENTER_LAT", 53.339428)
SEARCH_CENTER_LONG = os.getenv("SEARCH_CENTER_LONG", -6.257664)

CUSTOMER_RECORDS_FILE_URL = os.getenv("CUSTOMER_RECORDS_FILE_URL",
                                      "https://s3.amazonaws.com/intercom-take-home-test/customers.txt")
