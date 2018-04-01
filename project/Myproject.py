# coding=UTF-8
"""
def my_LuckDay():
    print("一定要好好努力!")


my_LuckDay()
"""


def todayis_Goodday():
    print("hi")


todayis_Goodday()


def input_word():
    # words = input('Enter a word:')
    print('cheese' + 'shop')


input_word()

sum = 0
x = 1
n = 1
while True:
    sum += x
    x *= 2
    n += 1
    if n > 20:
        break
print sum

sum1 = 0
x = 0
while True:
    x = x + 1
    if x > 100:
        break
    # if x % 2 == 0:
    if x % 2 != 1:
        continue
    sum1 += x
print sum1

for x in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    for y in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        if x < y:
            print str(x) + str(y)

for x in range(1, 9):
    for y in range(x + 1, 10):
        print str(x) + str(y)

d = {
    95: 'Adam',
    85: 'Lisa',
    59: 'Bart',
    69: 'Tom',
    85: 'Jam'
}
score = input('please enter your score:')
print d.get(score)
# for score in d:
# print d.get(85)

