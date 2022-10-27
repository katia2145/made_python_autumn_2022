from pathlib import Path
import io
import re


def parser(file_to_read, keywords=[]):
    if keywords == []:
        return []

    if not isinstance(keywords, list):
        raise TypeError("keywords must be list type")

    if isinstance(file_to_read, str):
        path_to_file = Path(file_to_read)
        if not path_to_file.is_file():
            raise FileNotFoundError("No such file")
        fileobj = open(file_to_read, "r", encoding="utf-8")

    elif isinstance(file_to_read, io.TextIOWrapper):
        fileobj = file_to_read
        if "r" not in fileobj.mode:
            raise io.UnsupportedOperation("file is not avelliabel to reading")

    else:
        raise TypeError("keywords must be str or fileobject type")

    result = []
    while True:
        line = fileobj.readline()
        if not line:
            break
        line = line.strip().lower()
        for keyword in keywords:
            if len(re.findall("\W(" + keyword + ")\W", line)) > 0:
                result.append(line)

    fileobj.close()

    return result
