random_list = [105, 3.1, "Hello", 737, "Python", 2.7, "World", 412, 5.5, "AI"]

tuple_float = ()
for item in random_list:
  if type(item) == float:
    tuple_float = tuple_float + (item,)

list_string = []
for item in random_list:
  if type(item) == str:
    list_string.append(item,)

list_dict = {'satuan' : [], 'puluhan' : [], 'ratusan' : []}
for item in random_list:
    if type(item) == int:
        if 0 <= item < 10:
            list_dict['satuan'].append(item)
        elif 10 <= item < 100:
            list_dict['puluhan'].append(item)
        elif 100 <= item < 1000:
            list_dict['ratusan'].append(item)

print("Data Float  :", list_float)
print("Data String :", list_string)
print("Data satuan :", list_dict['satuan'])
print("Data puluhan :", list_dict['puluhan'])
print("Data ratusan:", list_dict['ratusan'])