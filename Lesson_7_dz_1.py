import os
import shutil


ROOT = os.path.dirname(__file__)
dir_name = "my_project"
subfolder = ["settings", "mainapp", "adminapp", "authapp"]
if not os.path.exists(dir_name):
    dir_path = [os.makedirs(os.path.join(dir_name, i)) for i in subfolder]
else:
    shutil.rmtree(dir_name)

