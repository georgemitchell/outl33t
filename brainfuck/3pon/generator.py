import sys

def get_letters(msg):
    letters = {}
    for letter in msg:
        if not letter in letters:
            letters[letter] = 0
        letters[letter] += 1
    return letters

def set_letter_values(by_frequency):
    buff = []
    for letter, _ in by_frequency:
        val = ord(letter)
        for i in range(val):
            buff.append("+")
        buff.append(">")
    for i in range(len(by_frequency)):
        buff.append("<")
    return buff

def set_output_data(msg, lookups):
    buff = []
    cursor = 0
    for letter in msg:
        position = lookups[letter]
        if cursor > position:
            for i in range(cursor - position):
                buff.append("<")
        else:
            for i in range(position - cursor):
                buff.append(">")
        buff.append(".")
        cursor = position
    return buff

if __name__=="__main__":
    message = sys.argv[1]
    letters = get_letters(message)
    by_frequency = [(letter, letters[letter]) for letter in letters]
    by_frequency.sort(lambda x,y: y[1] - x[1])

    lookups = {}
    for i, val in enumerate(by_frequency):
        letter, frequency = val
        lookups[letter] = i

    letter_values = set_letter_values(by_frequency)
    output_data = set_output_data(message, lookups)

    print "".join(letter_values)
    print "".join(output_data)

