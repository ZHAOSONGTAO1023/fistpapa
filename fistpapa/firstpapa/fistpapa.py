import urllib.request
import chardet

response1 = urllib.request.urlopen('http://116.236.152.83:38101/admin/index.htm')####获取页面的源代码
htmlcode1 = response1.read().decode('utf-8')  #明确知道代码是utf-8，用utf-8转码
print('utf-8=========================================================\n\r',htmlcode1)

response2 = urllib.request.urlopen('http://116.236.152.83:38101/admin/index.htm')
htmlcode2 = response2.read()
chardit1 = chardet.detect(htmlcode2)#若事先不知道程序编码格式，需先获取代码格式
print(chardit1)
print('donnot konw============================\n\r',htmlcode2.decode(chardit1['encoding']))#再转换成程序的代码格式输出




