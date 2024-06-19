sample_dict = {
    "mouth": "Mund",
    "finger": "Finger",
    "leg": "Bein",
    "hand": "Hand",
    "face": "Gesicht",
    "nose": "Nase"
}

while True:
    user_data=input('Enter a word in English or EXIT: ')
    if user_data=='EXIT':
        print('Bye!')
        break
    
    else:   
        if user_data in sample_dict:
            print('Translation:',sample_dict[user_data])
        else:
            print('no match!')