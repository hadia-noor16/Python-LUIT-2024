

while True:
    year=int(input('When was Python 1.0 released?: '))
    if year==1994:
        break
    elif year<1994:
        print('It was later than that!')
    else:
        print('It was earlier than that!')
print('Correct!')