import random

class Volume:
    def add_new_list_type(self, input_list):
        if isinstance(input_list, list):
            new_massive = list(input_list)
            random.shuffle(new_massive)

            return new_massive
        else:
            print("Входные данные должны быть списком.")
            return None

class RandomData:
    def add_random_data(self, input_list):
        number_of_items_to_add = random.randrange(1, 10)
        data_pool = (True, False, "Bool", "Souse", "Dist", "GACT", "AIM-0", 43, 56, 71.2, None)
        list_copy = input_list.copy()
        list_variable_copy = random.sample(data_pool, k = number_of_items_to_add)
        
        for item_to_add in list_variable_copy: 
            list_copy.append(item_to_add)
            
        return list_copy

