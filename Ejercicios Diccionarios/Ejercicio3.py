# Continuar el programa: ahora nos pide un cóigo morse donde cada letra esta 
# separada por espacios y nos da la cadena correspondiente.

codigo = {
  'A': '.-',     'B': '-...',    'C': '-.-.',
  'D': '-..',    'E': '.',       'F': '..-.',
  'G': '--.',    'H': '....',    'I': '..',
  'J': '.---',   'K': '-.-',     'L': '.-..',
  'M': '--',     'N': '-.',      'O': '---',
  'P': '.--.',   'Q': '--.-',    'R': '.-.',
  'S': '...',    'T': '-',       'U': '..-',
  'V': '...-',   'W': '.--',     'X': '-..-',
  'Y': '-.--',   'Z': '--..',    '1': '.----',
  '2': '..---',  '3': '...--',   '4': '....-',
  '5': '.....',  '6': '-....',   '7': '--...',
  '8': '---..',  '9': '----.',   '0': '-----',
  '.': '.-.-.-', ',': '--..--',  ':': '---...',
  ';': '-.-.-.', '?': '..--..',  '!': '-.-.--',
  '"': '.-..-.', "'": '.----.',  '+': '.-.-.',
  '-': '-....-', '/': '-..-.',   '=': '-...-',
  '_': '..--.-', '$': '...-..-', '@': '.--.-.',
  '&': '.-...',  '(': '-.--.',   ')': '-.--.-'
}

morse=input("Morse:")
lista_morse=morse.split(" ")
palabra = ""
for cod in lista_morse:
    letra=[key for key,valor in codigo.items() if valor==cod][0]
    palabra=palabra+letra
print (palabra)