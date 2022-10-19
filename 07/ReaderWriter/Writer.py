from abc import abstractmethod
import json
import io
import numpy as np


class BaseWriter:
    @classmethod
    @abstractmethod
    def dump(self):
        raise NotImplementedError("Необходимо переопределить метод")


class TxtWriter(BaseWriter):
    def dump(data, fileobj):
        if 'w' not in fileobj.mode:
            raise io.UnsupportedOperation("файл должен быть доступен \
                                           для записи")

        if isinstance(data, str):
            fileobj.write(data)
            fileobj.close()

        elif isinstance(data, list):
            for line in data:
                fileobj.write(line + '\n')
            fileobj.close()
        else:
            fileobj.close()
            raise TypeError("аргумент должен быть list или str")


class CsvWriter(BaseWriter):
    def dump(data, fileobj):
        if 'w' not in fileobj.mode:
            raise io.UnsupportedOperation("файл должен быть доступен \
                                           для записи")

        if isinstance(data, str):
            data = [data]
            np.savetxt(fileobj, data, delimiter=", ", fmt='% s')
            fileobj.close()

        elif isinstance(data, list):
            np.savetxt(fileobj, data, delimiter=", ", fmt='% s')
        else:
            fileobj.close()
            raise TypeError("аргумент должен быть list или str")


class JsonWriter(BaseWriter):
    def dump(data, fileobj):
        if 'w' not in fileobj.mode:
            raise io.UnsupportedOperation("файл должен быть доступен \
                                           для записи")

        if isinstance(data, str):
            fileobj.write(data)
            fileobj.close()
        elif isinstance(data, dict):
            json.dump(data, fileobj)
            fileobj.close()
        else:
            fileobj.close()
            raise TypeError("аргумент должен быть list или str")
