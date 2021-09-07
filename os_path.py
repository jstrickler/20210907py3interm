import os
from datetime import datetime

FOLDER = "DATA"
FILE_NAME = "alice.txt"


def main():
    file_path = os.path.join(FOLDER, FILE_NAME)
    print("file_path: {}\n".format(file_path))

    print("os.path.abspath(file_path): {}\n".format(os.path.abspath(file_path)))
    print("os.path.dirname(file_path): {}\n".format(os.path.dirname(file_path)))
    print("os.path.basename(file_path): {}\n".format(os.path.basename(file_path)))

    file_size = os.path.getsize(file_path)
    print("file_size: {}\n".format(file_size))

    print("os.path.isfile(file_path): {}\n".format(os.path.isfile(file_path)))
    print("os.path.isdir(file_path): {}\n".format(os.path.isdir(file_path)))

    print("os.path.exists(file_path): {}\n".format(os.path.exists(file_path)))
    print("os.path.exists('wombats.txt'): {}\n".format(os.path.exists('wombats.txt')))

    print("os.path.getmtime(file_path): {}\n".format(os.path.getmtime(file_path)))

    timestamp = os.path.getmtime(file_path)
    #  .getatime() access
    #  .getctime() metadata changed

    print("datetime.fromtimestamp(timestamp): {}\n".format(datetime.fromtimestamp(timestamp)))















if __name__ == '__main__':
    main()
