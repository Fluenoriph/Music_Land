import hashlib


class FileDigest:
    BUFFER_SIZE = 4096

    @staticmethod
    def md5(file):
        hash_md5 = hashlib.md5()

        with open(file, "rb") as f:
            for chunk in iter(lambda: f.read(FileDigest.BUFFER_SIZE), b""):
                hash_md5.update(chunk)

        return hash_md5.hexdigest()
