import requests
import validators

from utils.logging import get_logger

logger = get_logger(__name__)


def download_file(url: str) -> str:
    if not is_url_valid(url):
        raise Exception("URL is not valid")
    try:
        logger.debug("Downloading file: %s" % (url,))
        response = requests.get(url)
        if not response.ok:
            raise (Exception("Response incorrect"))
        return str(response.content)
    except Exception as e:
        logger.error("Error downloading file. %s" % (e,))
        raise e


def is_url_valid(url: str) -> bool:
    return validators.url(url)
