import unittest

from customer import Customer
from exceptions import InvalidFormatException


class CustomerTest(unittest.TestCase):

    def test_customer_object_with_valid_record_dict(self):
        record = {"latitude": "52.833502", "user_id": 29, "name": "Oliver Ahearn", "longitude": "-8.522366"}
        customer = Customer(record)
        self.assertEqual(customer.lat, record["latitude"])
        self.assertEqual(customer.long, record["longitude"])
        self.assertEqual(customer.user_id, record["user_id"])
        self.assertEqual(customer.name, record["name"])

    def test_customer_object_with_invalid_record_dict(self):
        with self.assertRaises(InvalidFormatException):
            invalid_record = {}
            Customer(invalid_record)

        with self.assertRaises(InvalidFormatException):
            invalid_record = {"latitude": "53.22"}
            Customer(invalid_record)

        with self.assertRaises(InvalidFormatException):
            invalid_record = {"latitude": "", "longitude": ""}
            Customer(invalid_record)

        with self.assertRaises(InvalidFormatException):
            invalid_record = {"latitude": "50"}
            Customer(invalid_record)

        with self.assertRaises(InvalidFormatException):
            invalid_record = {"longitude": "50"}
            Customer(invalid_record)

        with self.assertRaises(InvalidFormatException):
            invalid_record = {"name": "Oliver Ahearn"}
            Customer(invalid_record)

        with self.assertRaises(InvalidFormatException):
            invalid_record = {"latitude": "52.833502", "name": "Oliver Ahearn", "longitude": "-8.522366"}
            Customer(invalid_record)

