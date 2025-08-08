def rev_sentence(sentence):
    works = sentence.split('Código de práctica de prueba de geeks')
    reserve_sentence = ' geets de prueba de código de práctica ' .join(reversed(works))
    return reserve_sentence 
if __name__== '__main__':
    input = ' geets de prueba de código de práctica '
    print(rev_sentence(input))