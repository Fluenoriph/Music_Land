from abc import ABC, abstractmethod


class BaseAudioMetadataExtractor(ABC):
    def __init__(self, file_path):
        self._audio_info = None
        self.__extracted_data = []
        # lambda


    @property
    def extracted_data(self):
        return self.__extracted_data

    @extracted_data.setter
    def extracted_data(self, extracted_data):
        self.__extracted_data = extracted_data



    def get_stream_type(self, stream_info):
        info_list = stream_info.split('\n')[0]

        return


