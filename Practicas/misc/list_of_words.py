def list_of_words(text: str, sep: str = " ") -> list:
    return text.split(sep)

list_of_words("María tenía un pequeño cordero", sep="a")
print("Hola de parte de list_of_words.py")
