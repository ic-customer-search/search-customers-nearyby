import requests
import validators

from exceptions import InvalidFormatException, InvalidResponseException
from utils import exception_to_str
from utils.logging import get_logger

logger = get_logger(__name__)


def download_file(url: str) -> str:
    if not is_url_valid(url):
        raise InvalidFormatException("URL is not valid")
    try:
        logger.debug("Downloading file: %s" % (url,))
        response = requests.get(url)
        if not response.ok:
            raise (InvalidResponseException(response.status_code, "File download returned bad status_code"))
        return str(response.content)
    except Exception as e:
        logger.error("Error downloading file.")
        logger.error(exception_to_str(e))
        raise e


def is_url_valid(url: str) -> bool:
    return validators.url(url)
