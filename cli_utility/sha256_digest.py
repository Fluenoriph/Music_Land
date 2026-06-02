import hashlib
from cli_utility.base_file_digest import BaseFileDigest


class SHA256Digest(BaseFileDigest):

    @staticmethod
    def compute_digest(file):
        sha256_hash = hashlib.sha256()

        with open(file, "rb") as f:
            for chunk in iter(lambda: f.read(SHA256Digest.get_buffer_size()), b""):
                sha256_hash.update(chunk)

        return sha256_hash.hexdigest()

    @staticmethod
    def get_buffer_size():
        return 65536
