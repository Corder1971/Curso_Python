str = 'geeks de pruebea de práctica de código'
def rev_sentence(sentence):
    words = sentence.split(' ')
    reverse_sentence = ' '.join(reversed(words))
    return reverse_sentence
if __name__ == "_main_":
    input = 'geeks quiz practice code'
    print (rev_sentence(input))