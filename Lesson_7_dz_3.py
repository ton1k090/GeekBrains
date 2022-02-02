import os
import shutil

ROOT = r"G:\DZ PYTHON\pythonGeekBrains\my_project"
project = "/templates"

# if not os.path.exists(ROOT+project):
#     os.mkdir(ROOT+project)
for root, dirs, files in os.walk(ROOT):
    for file in files:
        if file.endswith(".html"):
            path_file = os.path.split(root)[1]
            new_path = os.path.join(ROOT, "template", path_file)
            st_ad = f"{root}/{file}"
            if not os.path.exists(new_path):
                os.makedirs(new_path)
                shutil.copy2(st_ad, new_path)