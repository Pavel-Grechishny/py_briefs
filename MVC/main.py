"""
Controller MVC: Управляющий модуль. Точка входа.
"""
from sys import argv

def connect(view_name):
    pass

if 'tk' in argv:
    import view_tk as view 
else:
    import view_cli as view
    import view.folder1.vie1 as vie1
    import view.folder2.vie2 as vie2
    import view.folder3.vie3 as vie3
    

  
while True:
    command = input('Введите команду: > ')
    if command == 'humans':
        print(view.VIE)
    elif command == 'v1':
        print(vie1.viewroute)
    elif command == 'v2':
        print(vie2.viewroute)
    elif command == 'v3':
        print(vie3.viewroute)
    elif command == 'quit':
        print('quit')
        break

















# def mainloop():
    # while True:
        # if input('Сделать шаг? ') == 'да':
            # controller.folder1.cnt1.add_mod1_for_cnt1()
        # else:
            # break



if __name__ == '__main__':
    pass


    
