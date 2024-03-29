import json
from typing import Dict

from exceptions import InvalidFormatException


class Customer:
    required_attrs = ("user_id", "latitude", "longitude")

    def __init__(self, record: Dict):
        if not self.validate(record):
            raise InvalidFormatException("Customer record is not valid")
        self.user_id = record["user_id"]
        self.lat = record["latitude"]
        self.long = record["longitude"]
        self.name = record["name"]

    def __lt__(self, other):
        return self.user_id < other.user_id

    def __str__(self):
        record = {
            "latitude": self.lat,
            "longitude": self.long,
            "name": self.name,
            "user_id": self.user_id
        }
        return json.dumps(record)

    @classmethod
    def validate(cls, record: Dict) -> bool:
        is_record_valid = bool(record) and all(attr in record for attr in Customer.required_attrs)
        if not is_record_valid:
            return False
        is_record_not_empty = all(record[attr].strip() != "" for attr in ("latitude", "longitude"))
        return is_record_not_empty
