import statistics
def pali():
    try:
        list = []

        for i in text:
            text = int(input('text->'))
            list.append(i)

        summary = sum(list)
        length = len(list)
        avr = summary / length
        print(avr)


    except Exception as ex:
        print(f'Error: {ex}')
pali()