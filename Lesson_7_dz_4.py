import os

file_size = {}

root_dir = "G:\DZ PYTHON\pythonGeekBrains\Lesson_6"
for root, dirs, files in os.walk(root_dir):
    for file in files:
        size = (os.stat(os.path.realpath(f'{root}/{file}'))).st_size
        key = 10 ** len(str(size))
        file_size[key] = file_size.get(key, 0) + 1

print(file_size)