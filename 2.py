def read():
    with open('notes.txt', 'r', encoding='utf-8') as file:
        read=file.readlines()
    print(read)   


def add():
    a=input()
    with open('notes.txt', 'a', encoding='utf-8') as file:
        file.write(a + '\n')

def delite():
    zam=[]
    with open('notes.txt', 'r', encoding='utf-8') as file:
        zam=file.readlines()
    dell=int(input())
    del zam[dell-1]
    with open('notes.txt', 'w', encoding='utf-8') as file:
        file.writelines(zam)

def redact():
    zam=[]
    with open('notes.txt', 'r', encoding='utf-8') as file:
        zam=file.readlines()
    dell=int(input())
    zamen=input()
    zam[dell-1] = zamen + '\n'
    with open('notes.txt', 'w', encoding='utf-8') as file:
        file.writelines(zam)
    

while True:
    znach=int(input())
    if znach==1:
        read()
    elif znach==2:
        add()
    elif znach==3:
        delite()
    elif znach==4:
        redact()
    elif znach==0:
        break