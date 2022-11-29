import re
ver ='107.0.5304.122'
text = 'ChromeDriver 107.0.5304.62'
print((re.split('\.',ver))[0])  

print(re.split(' ',text)[1])