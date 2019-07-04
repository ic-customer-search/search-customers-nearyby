import unittest

from config import CUSTOMER_RECORDS_FILE_URL
from utils.fileutils import download_file
from utils.logging import get_logger

logger = get_logger(__name__)


class FileUtilsTest(unittest.TestCase):

    def test_download_file_with_valid_link(self):
        file_link = CUSTOMER_RECORDS_FILE_URL
        downloaded_file = download_file(file_link)
        self.assertEqual(type(downloaded_file), str)

    def test_download_file_with_invalid_link(self):
        file_link = "https://broken-link"
        self.assertRaises(Exception, download_file, file_link)
