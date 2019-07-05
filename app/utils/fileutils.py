import requests
import validators

from exceptions import InvalidFormatException, InvalidResponseException
from utils import exception_to_str
from utils.logging import get_logger

logger = get_logger(__name__)


def download_file(url: str) -> str:
    """
    Given a valid URL, return it's content as string
    """
    if not is_url_valid(url):
        raise InvalidFormatException("Download file url is not valid")
    try:
        logger.debug("Downloading file: %s" % (url,))
        response = requests.get(url)
        if not response.ok:
            raise (InvalidResponseException(response.status_code, "File download returned bad status_code"))
        return str(response.content, "utf-8")
    except Exception as e:
        exception_to_str(e)
        raise e


def is_url_valid(url: str) -> bool:
    return validators.url(url)
