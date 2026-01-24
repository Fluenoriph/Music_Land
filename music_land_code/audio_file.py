import hashlib


class AudioFile:
    BUFFER_SIZE = 4096

    def __init__(self, file, audio_type):
        self.__file = file
        self.__audio_data = audio_type
        self.__hash_sum = self.md5_digest()

    @property
    def file(self):
        return self.__file

    @property
    def audio_data(self):
        return self.__audio_data

    @property
    def hash_sum(self):
        return self.__hash_sum

    def md5_digest(self):
        hash_md5 = hashlib.md5()

        with open(self.file, "rb") as f:
            for chunk in iter(lambda: f.read(AudioFile.BUFFER_SIZE), b""):
                hash_md5.update(chunk)

        return hash_md5.hexdigest()
