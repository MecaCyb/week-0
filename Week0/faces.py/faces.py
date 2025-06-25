# user's input
def main():
    face = input()
    print(convert(face))

#convert into emoji
def convert(text):
    return text.replace(":(", '🙁').replace(":)", '🙂')

main()
