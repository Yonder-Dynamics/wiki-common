import os
import sys
from shutil import copyfile


def ensure_dirs(path):
    try:
        os.makedirs(path)
    except OSError:
        pass  # ignore path creation errors


def traverse(path, src, base):
    for file in os.listdir(path):
        if file == base:
            continue
        full_path = path + "/" + file
        if os.path.isdir(file):
            ensure_dirs(base + "/" + full_path)
            traverse(full_path, src, base)
        else:
            if file.lower() == src:
                copyfile(full_path, base + "/" + full_path)


# step back into the
build_target = sys.argv[1]
build_src = sys.argv[2].lower()

ensure_dirs(build_target)

traverse(".", build_src, build_target)
