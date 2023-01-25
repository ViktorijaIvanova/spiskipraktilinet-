spisok=[] #пустой список
numbers=[1,2,3,4,5]
abc=["abc","B","C"]
slovo="programmeerimine"
slovo_list=list(slovo)
print(slovo)
print(slovo_list)
while True:
    print("1-добавить букву в список")
    print("2-склеить списки\n3-добавить букву на i-позицию")
    valik=int(input())
    if valik==1:
        a=input("введи букву")
        slovo_list.append(a)
        print(f"ДОбавили {a} новый список",slovo_list)
    elif valik==2:
      slovo_list.extend(abc)
      print(slovo_list)
    elif valik==3:
      a=input("введи букву, которую хочешь добавить")
      i=int(input("введи номер позиции, куда хочешь добавить букву"))
      slovo_list.insert(i-1,a) #0,1,2...
      print(slovo_list)
    elif valik==4:
      a=input("введи букву, которую хочешь удалить")
      n=slovo_list.remove(a)
    if n>0:
     for i in range(n):
      slovo_list.remove(a)
    else:
     print("искомой буквы нет")
     print(slovo_list)