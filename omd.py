def step2_umbrella():
    print(
        'А вот это зря!'
        'Утка Маляр не может быть с зонтиком.\nЭто не ее стиль, не ее масштаб. ' 
    )
def step2_no_umbrella():
    print(
        'С тех пор ее никто не видел... '
    )
def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()
    
    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()

if __name__ == '__main__':
    step1()