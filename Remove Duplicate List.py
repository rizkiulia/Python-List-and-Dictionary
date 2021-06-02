#Contoh sebuah fungsi, yang menerima suatu argument objek list, dan return sebuah objek list baru, dimana objek list baru ini berisi list sebelumnya dikurangi dengan data yang duplikat, sehingga setiap element di dalam list adalah unik.





# solusi tanpa menggunakan set
def remove_duplicate(obj_list):
    new_list = []
    for element in obj_list:
      if element not in new_list:
       new_list.append(element)
    return new_list

  # solusi dengan menggunakan set
def remove_duplicate_with_set(obj_list):
    new_list = list(set(obj_list))
    return new_list

obj_list = [1, 2, 4, 6, 2, 1, 4, 5, 7, 8, 6]
print(remove_duplicate(obj_list))
print(remove_duplicate_with_set(obj_list))
