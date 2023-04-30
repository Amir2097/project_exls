str_d = ['22.04.23', '2023-04-24 12:52:58']

for i in str_d:
    ii = i.split('.')
    if len(i) > 9:
        ii = i.split(' ')[0].split('-')
        form_ii = f'{ii[2]}.{ii[1]}.{ii[0]}'
        print(form_ii)

    if len(i) == 8:
        ii = i.split('.')
        form_ii = f'{ii[0]}.{ii[1]}.20{ii[2]}'
        print(form_ii)
