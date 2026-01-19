# Класс для извлечения аудио-метаданных.

class AudioFileMetadataExtractor:
    def __init__(self, audio_info, tag_keys=None):
        self.audio_info = audio_info
        self.tag_keys = tag_keys
        self.__extracted_tags_data = []

        is_tags_exist = (self.tag_keys is not None) and (self.audio_info.tags is not None)

        if is_tags_exist:
            for tag in self.tag_keys:
                if tag in self.audio_info.tags:
                    tag_value = str(self.audio_info[tag])

                    self.extracted_tags_data.append(tag_value.strip("[']"))
                else:
                    self.extracted_tags_data.append(None)

    @property
    def extracted_tags_data(self):
        return self.__extracted_tags_data

    @extracted_tags_data.setter
    def extracted_tags_data(self, value):
        self.__extracted_tags_data = value