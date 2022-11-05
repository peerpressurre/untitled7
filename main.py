def pali():
    try:
        text = (input('text->'))
        digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
        counter = []
        for i in text:
            if i.isdigit():
                counter = [i]
                print(counter)

    except Exception as ex:
        print(f'Error: {ex}')
pali()