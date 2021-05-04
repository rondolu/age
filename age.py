driving = input('請問你有沒有開過車?')
if driving != '有' and driving != '沒有':
    print('給我好好回答')

age = input('你幾歲?')
age = int(age)
if driving == '有':
    if age >= 18:
        print('水喔')
    else:
        print('抓到你囉~')
elif driving == '沒有':
    if age >= 18:
        print('快去學阿')
    else:
        print('你很乖')
else: 
    print('再填一次')
