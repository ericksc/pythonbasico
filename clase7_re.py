import re
#
# frase = 'Buenos  $%$%^%^ dias %$$%$#  a &*(*(  todos'
#
# expresion = r'\W+'
#
# resultado = re.split(expresion, frase)
# print(resultado)

# resultado = re.split('[a-f3]+', '0321a321d432e31f3B9', flags=re.IGNORECASE)
# print(resultado)

# m = re.match(r"(\d+)\.(\d+)", "24324354.1632")
# resultado = m.groups()     # The entire match
# print(resultado)

email_address = "Please contact us at: support@python.com, xyz@python.com more text erick@erick.com"

#'addresses' is a list that stores all the possible match
addresses = re.findall(r'[\w\.-]+@[\w\.-]+', email_address)
for address in addresses:
    print(address)

