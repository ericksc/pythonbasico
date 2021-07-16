
import re

# vamos a obtener la lista de palabras desde
# una frase o texto

re.split( r'\W+', 'Words, words, words.' )

m = re.match(r"(\w+) (\w+)", "Isaac Newton, physicist")
m.group(0)       # The entire match


pattern = r"Cookie"
sequence = "Cake is delicious"
if re.match(pattern, sequence):
  print("Match!")
else: print("Not a match!")


email_address = "Please contact us at: xyz@python.com"
new_email_address = re.sub(r'([\w\.-]+)@([\w\.-]+)', r'erick@python-class.com', email_address)
new_email_address
