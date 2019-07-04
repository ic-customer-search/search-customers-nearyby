import json


def parse_json_from_string(stringified_json: str) -> dict:
    return json.loads(stringified_json)


def parse_customer_record(customer_record_text: str) -> list:
    return []