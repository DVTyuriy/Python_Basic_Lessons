



if __name__ == '__main__':
    contain_list = list()
    while True:
        input_string = input('Введіть текст для збереження в нотатки\n'
                           'Або \n'
                           'earliest - щоб вивести нотатки на экран від найранішої до найпізнішої:\n'
                           'latest -   щоб вивести нотатки на экран від найпізнішої до найранішої:\n'
                           'longest -  щоб вивести нотатки на экран від найдовшої до найкоротшої:\n'
                           'shortest - щоб вивести нотатки на экран від найкоротшої до найдовшої:\n'
                           'exit -     для завершення\n'
                           )
        contain_list = ['this is note', 'this is notissimo', 'note', 'this is a huge long, insanely long note', 'well, anyways']
        if input_string.lower() == 'exit':
            exit()
        if input_string.lower() == 'earliest':
             for i in range(len(contain_list)):
                print(contain_list[i])
             print()

        elif input_string.lower() == 'latest':
            contain_list.reverse()
            for i in range(len(contain_list)):
                print(contain_list[i])
            print()
        elif input_string.lower() == 'longest':

            print()
        elif input_string.lower() == 'shortest':
            print()
        elif input_string == '':
            print('Ви нічого не ввели, а ми нічого і не записали')
            print()
        else:
                contain_list.append(input_string)
                print('Так, це ми записали до нотатків')



