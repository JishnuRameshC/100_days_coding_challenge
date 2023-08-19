from art import logo


print(logo)
alphabet = []
for letter in range(ord('a'), ord('z') + 1):
    alphabet.append(chr(letter))
for letter in range(ord('a'), ord('z') + 1):
    alphabet.append(chr(letter))
print(alphabet)
diretion = input("type 'encode' to encrypt and 'decode' to decrypt :")
shift = int(input('enter how many shift:'))
text = input("enter the text :")


def cipher(cipher_text, shift_amount,cipher_type):
    new_text = ''
    if cipher_type == 'decode':
        shift_amount *= -1
    for i in cipher_text:
        position = alphabet.index(i)
        new_positon = position + shift_amount
        new_text += alphabet[new_positon]
    print(new_text)


cipher(cyfer_text=text, shift_amount=shift, cyfer_type=diretion)

# def encrypt(pane_text, shift_amount):
#     new_text = ''
#     for i in pane_text:
#         position = alphabet.index(i)
#         new_positon = position + shift_amount
#         new_text += alphabet[new_positon]
#     print(new_text)

# def decrypt(pane_text, shift_amount):
#     new_text = ''
#     for i in pane_text:
#         position = alphabet.index(i)
#         new_positon = position - shift_amount
#         new_text += alphabet[new_positon]
#     print(new_text)

# if diretion == 'encode':
#     encrypt(pane_text=text,shift_amount=shift)
# if diretion == 'decode':
#     decrypt(pane_text=text,shift_amount=shift)

    

