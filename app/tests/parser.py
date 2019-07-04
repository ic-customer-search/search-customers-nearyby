import json
import unittest

from utils.logging import get_logger
from utils.parser import parse_json_from_string, parse_customer_record

logger = get_logger(__name__)


class ParserTest(unittest.TestCase):

    def test_parse_json_for_malformed_string(self):
        malformed_string = "{x: 1}"
        self.assertRaises(json.decoder.JSONDecodeError, parse_json_from_string, malformed_string)

    def test_parse_json_for_valid_satring(self):
        json_string = '{"x": 2}'
        parsed = parse_json_from_string(json_string)
        self.assertEqual(type(parsed), dict)

    def test_parse_customer_records(self):
        customer_records = '{"latitude": "53.74452", "user_id": 29, "name": "Oliver Ahearn", "longitude": "-7.11167"}\n' \
                            '{"latitude": "53.761389", "user_id": 30, "name": "Nick Enright", "longitude": "-7.2875"}\n' \
                            '{"latitude": "54.080556", "user_id": 23, "name": "Eoin Gallagher", "longitude": ' \
                            '"-6.361944"}\n' \
                            '{"latitude": "52.833502", "user_id": 25, "name": "David Behan", "longitude": ' \
                           '"-8.522366"}\n '
        parsed_customer_record = parse_customer_record(customer_records)
        self.assertEqual(type(parsed_customer_record), list)
        self.assertEqual(len(parsed_customer_record), 4)
        self.assertEqual(parsed_customer_record[2]["user_id"], 30)

