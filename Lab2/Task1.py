predl = input("\t\t\tЗАДАНИЕ:\n Пусть дана строка, состоящая из слов, пробелов и знаков препинания. На основании этой строки создайте новую (и выведите ее на консоль)\n Введите строку:\n")
new_predl = list(filter(lambda x: len(x)>=5 and len(x)<=10, predl.translate(str.maketrans({x: None for x in [',', '.', ':', ';', '!', '?', ')', '(']})).split()))
print(new_predl)


