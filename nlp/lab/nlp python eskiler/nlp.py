
#re.search()
#re.finadll()
#re.split()
#re.sub(r'\s+','', text_txt1)
       


import re
text1 = """10 WORK \t lecture
11 PRIV    Breakfast
12   WORK  laboratories"""

for line in text1:
    if line.isdigit() == True:
        print(line)
"result=re.search(r'[int]', text1)"
result1=re.search(r'the', text1)
result2=re.findall(r'^[Tt]', text1) # ^ ilk kelimeyi arastiriyor//
result3=re.findall(r'[Tt][a-z A-Z]*', text1)

text2 = """
<body>

 <h1>My First Heading</h1>
 <p>My first paragraph.</p>

 </body>
"""

result4=re.split(r'\s', text2) #split ayri ayri bakiyor kelimelere
result5=re.split(r'\s+', text2)
result6=re.split(r'\n', text2)
result7=re.split(r'\W', text2)
result8=re.findall(r'\w', text2) #findall hepsine bakiyor/ kucuk w
result9=re.sub(r'\s+','', text2) #bosluklari iptal ediyor           v )


print(result)

print (result.start())
print(result1)
print(result2)
print(len(result2))
print(len(result3))

print("________________________________")


print(result4)
print(result5)
print(result6)
print(result7)
print(result8)
print(result9)
