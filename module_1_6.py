# Словари и множества



# 2 Создание переменой
my_dict={"Pasha" : 1998 , "Olia" : 1997, "Maksim" : 1999} # Создания ключей и значений.
print (my_dict) # вывод словаря на консоле

# 2.1 вывод сушествуешего словаря
print(my_dict["Pasha"]) # запрос индекса словаря
print(my_dict.get("Pasha")) # запрос на получения значения метод 2

print (my_dict)  # вывод словаря на консоле
# 2.1 вывод не сушествуешегося словаря без ошибки
my_dict["Atomic"]=2050 # создания ключа
print (my_dict)  # вывод словаря на консоле
# 2.2 Добавить ключи и значения
my_dict.update({"Chats": 9999, "Maria" : 1867 }) # Добавить к словарю двух Users
print (my_dict) # вывод словаря на консоле
# 2.3 удалением из словаря спомщью метода .pop
a=my_dict.pop('Pasha') #сохраняю значения ключа
b=my_dict.pop('Maria') #сохраняю значения ключа
print (a) # вывод словаря на консоле
print (b) # вывод словаря на консоле

# 3 работа с множеством
my_set= {1,2,3,4,5,6,False,True, "Привет",3.14,1,2,3,4,5,6,False,True, "Привет",3.14} # множество
print(my_set) # вывод множества на консоле

# 3.1 добавить значения в множество
my_set.add(600) #Первое значение.
my_set.add(900) # Второе значение.
print(my_set) # вывод словаря на консоле

# 3.2 удалить обьекты
print(my_set.discard(True))
print(my_set) # вывод множества на консоле изменино
