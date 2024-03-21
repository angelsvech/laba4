def zadacha1():
    a=int(input("введите число"))
    if a % 3 == 0:
        print("делится")
    else:
        print("не делится")

def zadacha2():
    try:
        a = int(input("введите число"))
        s=100/a
        print(s)
    except ValueError:
        print("введите пожалйсто число")
    except ZeroDivisionError:
        print("введите пожалйсто не 0 ")


from datetime import datetime
def zadacha3():
    data=input("ввелите дату дд.мм.гггг:")
    da=datetime.strptime(data,'%d.%m.%Y')
    day=da.day
    month=da.month
    year=da.year

    if day*month==year%100:
        print("магическая дата")
    else:
        print("не магическая дата")

def zadacha4():
    a = input("введите четный билет")
    bilet=list(map(int,a))
    delim=len(a)//2
    first=bilet[:delim]
    second=bilet[delim:]

    sf=sum(first)
    ss=sum(second)

    if sf == ss:
        print("счастливый билет")
    else:
        print("не счастливый билет")
zadacha4()
