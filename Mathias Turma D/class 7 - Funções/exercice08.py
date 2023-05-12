def text(text: str)->tuple:
    text_reserve= ''
    text= ''.join(text.split())
    amount = len(text)
    for letter in text[::-1]:
        text_reserve+=letter
    return amount, text_reserve
words= text("Sport Club do Recife")

print(f'A quantidade de palvras são {words[0]} letras e ao contrário fica: {words[1]}')