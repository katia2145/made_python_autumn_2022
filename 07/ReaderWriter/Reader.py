from abc import abstractmethod
import csv
import json
import io


class BaseReader:
    @classmethod
    @abstractmethod
    def read(self):
        raise NotImplementedError("Необходимо переопределить метод")

    @classmethod
    def check_file_mode(self, fileobj):
        if 'r' not in fileobj.mode:
            fileobj.close()
            raise io.UnsupportedOperation("файл должен быть доступен \
                                           для чтения")


class TxtReader(BaseReader):
    def read(fileobj):
        BaseReader.check_file_mode(fileobj)
        lines = fileobj.readlines()
        fileobj.close()
        return lines


class CsvReader(BaseReader):
    def read(fileobj):
        BaseReader.check_file_mode(fileobj)
        lines = []
        spamreader = csv.reader(fileobj, delimiter=' ')
        for row in spamreader:
            lines.append(' '.join(row))
        fileobj.close()
        return lines


class JsonReader(BaseReader):
    def read(fileobj):
        BaseReader.check_file_mode(fileobj)
        json_dict = json.load(fileobj)
        fileobj.close()
        return json_dict
