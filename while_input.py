selected = None
while selected not in ['가위', '바위', '보']:
    selected = input('가위, 바위, 보 중에서 선택하세요> ')
    if(selected == '바위'):
        print('win')
        selected = selected
    else:
        print('선택한 값은',selected)
        selected = None