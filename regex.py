import re

txt='''Pikachu! is an electric type pokemon!!! 
      Ash Ketchum is its trainer!!, element his number is 8657448214 Pikachu'''

print(re.findall("!+",txt))
print(re.findall("!",txt))

print(re.findall("[A-Z]",txt))
print(re.findall("[a-z]",txt))
print(re.findall("[A-Za-z]",txt))

print(re.findall("\d",txt))
print(re.findall("\D",txt))

print(re.findall("\APikachu",txt))
print(re.findall("^Pikachu",txt))

print(re.findall("Pikachu\Z",txt))
print(re.findall("Pikachu$",txt))

print(re.findall(r"\bPik",txt))
print(re.findall(r"Pik\b",txt))
print(re.findall(r"achu\b",txt))
print(re.findall(r"\bPikachu\b",txt))

print(re.findall(r"\Bachu",txt))
print(re.findall(r"Pik\B",txt))
print(re.findall(r"achu\B",txt))
print(re.findall(r"\Buhcakip\B",txt))

print(re.findall("\s",txt))
print(re.findall("\S",txt))

print(re.findall("Pika.*u",txt))

print(re.search("Pika.*u",txt))
print(re.search(r"\bPik",txt))
print(re.search(r"\Bachu",txt))

match_obj = re.search(r"\Bachu",txt)
print(match_obj.span())
print(match_obj.start())
print(match_obj.end())
print(match_obj.string)

print(re.sub("\s","9",txt,2))

print(re.findall("Pika.*u|8657448214",txt))
print(re.findall("Pika.*u&8657448214",txt))

k = "color, colour, colouur"
print(re.findall("u?",k))

print(re.search("^p",txt))

print(re.search("[ika]",k))

print(re.search("[ika]",k))

