import os


def scan_dir(dir_):
    files = []
    for file in os.listdir(dir_):
        path = os.path.join(dir_, file)
        if os.path.isfile(path):
            files.append(file)
    return files
