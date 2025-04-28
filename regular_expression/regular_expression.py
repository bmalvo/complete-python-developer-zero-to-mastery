import re

pattern = re.compile(r"/^[a-zA-Z0–9._%+-]+@[a-zA-Z0–9.-]+\.[a-zA-Z]{2,}$/")

# pattern = re.compile(cheker)

text = 'search inside of this text, please!'
email = 'boydmalvo@gmail.com'
a = pattern.fullmatch(email)



print(a)
