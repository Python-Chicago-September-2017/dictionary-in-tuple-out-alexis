my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

def tuple_out_of_dictionary(a_dictionary):
    new_tuple = a_dictionary.items()
    return new_tuple

print tuple_out_of_dictionary(my_dict)
