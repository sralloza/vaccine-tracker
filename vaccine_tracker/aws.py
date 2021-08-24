import tempfile
from typing import List

import boto3

from vaccine_tracker.config import settings

LINKS_FILE = "notified-links.txt"


def get_links() -> List[str]:
    s3 = boto3.client("s3")
    with tempfile.TemporaryFile() as fp:
        try:
            s3.download_fileobj(settings.s3_bucket, LINKS_FILE, fp)
        except Exception as exc:
            if "404" in str(exc):
                return []
            raise

        fp.seek(0)
        links = fp.read().decode("utf8").splitlines()

    return links


def save_links(links: List[str]):
    file_content = "\n".join(links)
    s3 = boto3.client("s3")
    with tempfile.TemporaryFile() as fp:
        fp.write(file_content.encode("utf8"))
        fp.seek(0)
        s3.upload_fileobj(fp, settings.s3_bucket, LINKS_FILE)
