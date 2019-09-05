from random import randint
#三个数求最大值
def zuidazhi():
    a = input('a=')
    b = input('b=')
    c = input('c=')
    print('the max = ',max(a,b,c))
#  12//2为整除=6，12/2保留一位小数=6.0    3*3=9 乘  3**3=27 乘方
face = randint(1, 6)    #在1到6中随机整数

#输入三条边长如果能构成三角形就计算周长和面积使用海伦公式
#99乘法表
def chengfabiao():
    for i in range(1, 10):
        for j in range(1, i + 1):
            print('%d*%d=%d' % (i, j, i * j), end='\t')
        print()
#三角形
def sanjiaoxing():
    row = int(input('请输入行数: '))
    for i in range(row):
        for _ in range(i + 1):
            print('*', end='')
        print()
    for i in range(row):
        for j in range(row):
            if j < row - i - 1:
                print(' ', end='')
            else:
                print('*', end='')
        print()

    for i in range(row):
        for _ in range(row - i - 1):
            print(' ', end='')
        for _ in range(2 * i + 1):
            print('*', end='')
        print()
#水仙花数
def shuixianhuashu():
    print('三位数的水仙花数：')
    for i in range(100,1000):
        b = i // 100  # 百位
        s = (i - b *100) //10
        g = i % 10      # 个位
        if  g*g*g + s*s*s + b*b*b == i:
            print(b,s,g)
#一行代码实现1--100之和
def yihang():
    print(sum(range(1,101)))
shuixianhuashu()

def suiji():
    for i in range(1,21):
        print(i)
suiji()