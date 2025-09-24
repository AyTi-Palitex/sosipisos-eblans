from typers import Volume, RandomData

type_1 = input("Введи слово: ")
type_2 = input("Введи слово: ")
type_3 = input("Введи слово: ")

print("-" * 20) # Просто разделитель для красоты

massive_one = [type_1, type_2, type_3]

print(massive_one)

massive_one.append("lmaoooo")
massive_one.append("lol")

print(massive_one)

del massive_one[2]
print(massive_one)

print("-" * 20)

massive_two = list(massive_one)

shuffler = Volume()
shuffled_list = shuffler.add_new_list_type(massive_one)
print(f"Перемешанный список: {shuffled_list}")
print(f"Оригинал не изменился: {massive_one}") 

print("-" * 20) 

data_adder = RandomData()
final_list = data_adder.add_random_data(shuffled_list)
print(f"Список с добавленными случайными данными: {final_list}")