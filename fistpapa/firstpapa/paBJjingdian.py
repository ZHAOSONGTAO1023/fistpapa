import urllib.request

from bs4 import BeautifulSoup
final = []
#先获取页数
res = urllib.request.urlopen('https://beijing.cncn.com/jingdian/')  ####获取页面的源代码

b = BeautifulSoup(res, 'html.parser')  # 创建BeautifulSoup对象
span = b.body.find('div', {'class': 'page_con'}).find_all('span')#定位到页数对应的上层位置
num = str(span[len(span)-1].string)
NUM = num[1:-1]  #得到页数的字符串    截取字符串第二个到倒数第二个字符

for i in range(1,int(NUM)+1):
    response1 = urllib.request.urlopen('https://beijing.cncn.com/jingdian/1-'+ str(i) +'-0-0.html')  ####获取页面的源代码


    bs = BeautifulSoup(response1, 'html.parser')  # 创建BeautifulSoup对象
    body = bs.body
    div = body.find('div',{'class':'city_spots_list'})#找body中div标签下，class属性为city_spots_list的div
    ul = div.find('ul')
    li = ul.find_all('li')

    for place in li:
        temp = []
        a = place.find('a')
        img = a.find('img')['alt']
        # print(img)
        temp.append(img)
        final.append(temp)
print(len(final))
for i in range(1,len(final)):
    print(final[i])


