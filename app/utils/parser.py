import json

from exceptions import InvalidFormatException
from utils import exception_to_str
from utils.logging import get_logger

logger = get_logger(__name__)


def parse_customer_records(customer_records_text: str) -> list:
    """
    Parse a blob of string for customer records. Customer records are expected to be delimited by new line character
    """
    records = customer_records_text.strip().split("\n")
    parsed = []
    try:
        for record in records:
            if record.strip() != "" or record.strip() == "\n":
                parsed.append(parse_json_from_string(record))
            else:
                raise InvalidFormatException("Record is empty")
        return parsed
    except json.decoder.JSONDecodeError as e:
        raise InvalidFormatException(exception_to_str(e))


def parse_json_from_string(stringified_json: str) -> dict:
    if not stringified_json or stringified_json.strip() == "":
        raise InvalidFormatException("String is null")

    return json.loads(stringified_json)
