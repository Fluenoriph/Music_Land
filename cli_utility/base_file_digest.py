import abc


class BaseFileDigest(abc.ABC):

    @staticmethod
    @abc.abstractmethod
    def compute_digest(file):
        pass

    @staticmethod
    @abc.abstractmethod
    def get_buffer_size():
        pass
