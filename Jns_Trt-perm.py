import re
def do_input_int(message):
    flag = True
    while flag:
        value = input(message)
        if bool(re.match('^[-+]?[0-9]{1,}$', value)):
            flag = False
            value = int(value)
        else:
            print('error')
    return value
def is_int(message,error):
    flag=True
    while flag:
        a=input(message)
        if a.isdecimal() and int(a)>0:
            flag=False
            a=int(a)
        else:
            print(error)
    return a


def getmobile():
    global k, iList
    ret = False
    j = 0
    for i in range(len(iList)):
        pointing_index = i + iList[i][1]
        if 0 <= pointing_index < len(iList):
            if iList[i][0] > iList[pointing_index][0]:
                if not ret:
                    ret = True
                    j = i
                elif iList[i][0] > iList[j][0]:
                    j = i
    k = j
    return ret


def swap():
    global k, iList
    dir = iList[k][1]
    tmp = iList[k + dir]
    iList[k + dir] = iList[k]
    iList[k] = tmp


def reverse():
    global k, iList
    for i in range(len(iList)):
        if iList[i][0] > iList[k][0]:
            iList[i][1] *= -1


def write_list():
    global n, iList
    for i in range(len(iList)):
        print(iList[i][0], end="")
    print("  #", n, sep="", end="\n")
    n += 1

stop = ''
while stop != 'stop':
    sMyList = []
    p=do_input_int("Введіть кількість чисел для перестановки:")
    for i in range(1,p+1):
        sMyList.append(i)
    iList = [[int(item), -1] for item in sMyList]
    k = n = 1
    write_list()
    if getmobile():
        swap()
        write_list()
    while getmobile():
        reverse()
        swap()
        write_list()
    stop = input("\nНапишіть 'stop' для зупинки програми або натисніть Enter для продовження: ")
