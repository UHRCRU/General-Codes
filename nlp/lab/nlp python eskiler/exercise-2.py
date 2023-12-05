import re
text1 = """10 WORK \t lecture
11 PRIV    Breakfast
12   WORK  laboratories"""
#1.1, maks 2 digits
print('#exercise1.1',re.findall("\d+", text1))
#1.2
for match in re.finditer('10', text1, re.IGNORECASE):
    print("#exercise1.2 st match start index", match.start(), "End index", match.end()-1)
#1.3
print('#exercise1.3', " ".join(text1.strip().split()))
#1.4
print('#exercise1.4', re.findall('[A-Z]+[A-Z]', text1))
#1.5
print('#exercise1.5', re.findall('.[a-z]+[a-z]+',text1))
#1.6
print('#exercise1.6', re.findall('((\d+)|([A-Z]+[A-Z])|([a-z]+[a-z]+))',text1))

text2 = """
<body>

 <h1>My First Heading</h1>
 <p>My first paragraph.</p>

</body>
"""
#2.1
print('#exercise2.1', re.findall('<[^>]+>',text2))
#2.2
print('#exercise2.2', re.findall('(</\w+>)', text2))
#2.3
print('#exercise2.3',re.findall('>(.*?)<', text2))

text3 = """
Lady, I know it will hurt you
But it's much harder to ignore
There is a chance and I promise
I won't hurt you anymore
Hollywood nights, we're romancin'
You can trust me anytime
Somewhere, oh babe, there is someone
Oh, you're dancin' in my mind
Oh, oh, oh, little queenie
I'm your fool, come on
Teach me the rules
I will send an S.O.S. for love
Oh, oh, oh, little queenie
I'm your fool, you need love
Like I do
I will send an S.O.S. for love
Atlantis is calling, S.O.S. for love
Atlantis is calling from the stars above
Atlantis is calling, S.O.S. for love
Atlantis is calling, it's too hot to stop
If loving you is wrong, babe
Oh, I don't wanna be right
I've got you under my skin, babe
Oh, baby, hold me tight
I'm ready for our romance
I wait a million years for you
I love you more than I'm sayin'
Baby, that's for me the truth
Oh, oh, oh, little queenie
I'm your fool, come on
Teach me the rules
I will send an S.O.S. for love
Oh, oh, oh, little queenie
I'm your fool, you need love
Like I do
I will send an S.O.S. for love
Atlantis is calling, S.O.S. for love
Atlantis is calling from the stars above
Atlantis is calling, S.O.S. for love
Atlantis is calling, it's too hot to stop
Atlantis is calling, S.O.S. for love
Atlantis is calling from the stars above
Atlantis is calling, S.O.S. for love
Atlantis is calling, it's too hot to stop
"""

#3.1
print('#exercise3.1', re.findall("([a-zA-Z]+)\s+\1\b", text3))
#3.2
print('#exercise3.2', re.findall("^\d+\b.*\b[a-zA-Z]+$", text3))
#3.3
print('#exercise3.3', re.findall('^[^a-zA-Z]*([a-zA-Z]+)', text3))
