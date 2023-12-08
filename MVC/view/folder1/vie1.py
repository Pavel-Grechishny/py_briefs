from pathlib import Path
from sys import path

viewroute = 'model1 -> controller1 -> view1'



def show(data):
    print(f'vie1 _ cnt1 _ mod1: {data}')
    
def get_post_user():
    return input('Введите слово: > ')