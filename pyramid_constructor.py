import pdb
original_number = raw_input("Enter the number of the level in pyramid")
duplicate_number = int(original_number)
number_of_hashes_to_be_removed = False
formed_main_array = []
form_hash = "#"
while(duplicate_number != 0):
  if number_of_hashes_to_be_removed:
      prefix_adder = " "
      suffix_adder = " "
      string_formed = prefix_adder + str(form_hash * duplicate_number) + suffix_adder
      formed_main_array.append(string_formed)
  else:
      number_of_hashes_to_be_removed = True
      formed_main_array.append(str(form_hash * duplicate_number))
  duplicate_number -= 1
for ele in reversed(formed_main_array):
    print(ele)
  