from pathlib import Path
from sys import path

import model.folder1.mod1
import view.folder1.vie1


print(f'-------------------------------------------')


def add_mod1_for_cnt1():
    data = view.folder1.vie1.get_post_user()
    model.folder1.mod1.data.append(data)
    view.folder1.vie1.show(model.folder1.mod1.data)
