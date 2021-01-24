count = 1
list2 = []
string = input('Введите строку из нескольких слов, разделенных пробелами. '
               '\nНажите Enter для окончания: ')
list1 = string.split()

for each in list1:
    list2.append(str(count))
    list2.append('.')
    list2.append(' ')
    a = list1[count - 1]
    a = a[:10]
    list2.append(a)
    list2.append('\n')
    count += 1

string = ''.join(list2)
print(string)
