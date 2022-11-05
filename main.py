import statistics
def pali():
    try:
        text = (input('text->'))
        text1 = [text.split(' ')]
        summary = sum(text1)
        print(summary)
        length = len(text1)
        avr = summary / length
        print(avr)


    except Exception as ex:
        print(f'Error: {ex}')
pali()