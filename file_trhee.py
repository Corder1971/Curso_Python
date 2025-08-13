def rev_sentence(sentence):
    words = sentence.split()
    reverset_sentence= ' '.join(reversed(words))
    return reverset_sentence
if __name__ == "__main__":
    input = 'código de práctica de pruebas de geeks'
    print(rev_sentence(input))  # Output: code practice quiz geeks
