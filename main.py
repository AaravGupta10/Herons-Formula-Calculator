CHARS = ((' ', '▬'), ('a', '$'), ('b', '@'), ('c', '!'), ('d', '#'), ('e', '^'), ('f', '%'), ('g', ')'), ('h', '('), ('i', '*'), ('j', ';'), ('k', '>'),
('l', '?'), ('m', '/'), ('n', ':'), ('o', '~'), ('p', '<'), ('q', '['), ('r', '}'), ('s', '"'), ('t', ']'), ('u', '{'), ('v', '◙'), ('w', '╤'), ('x', '╚'),
('y', '|'), ('z', '-'))



def convertEncode(word):
    for a,b in CHARS:
        word = word.replace(a, b)
    return word

def convertDecode(word):
    for b, a in CHARS:
        word = word.replace(a, b)
    return word



def main():
    if __name__ == "__main__":
        EncodeOrDecode = input("Do you want to encode or decode ? (encode - e, decode - d) ")

        if EncodeOrDecode == "e":
            word = input("Enter the word you want to encode: ")
            word = convertEncode(word)
            print(f"Your encoded word is {word}")
        elif EncodeOrDecode == "d":
            word = input("Enter the word you want to decode: ")
            word = convertDecode(word)
            print(f"Your decoded word is {word}")
        else:
            print("Invalid Input")

        StartOrEnd = input("Do you want to exit ? (y/n) ")
        if StartOrEnd == "y":
            print("Goodbye")
        elif StartOrEnd == "n":
            main()
        else:
            print("Invalid Input")

main()
