'''
  In python the dictionaries also exist and then dictionaries also exist with the key value pairs as shown 
  key_dict = {
    "anna": "Hazare",
    "viswakam": "heg"  
  }

  when we want to remove the key by the name `anna` in key_dict we can do that by 
  ```
    del key_dict('anna')
  ```
  when we want to add a new key value pair then
  ```
    key_dict['name2'] = "Ya Allah"
  ```

  when we want to update the key in the dictionary then
  ```
    key_dict['name1'] = "Bismillah"
  ```

  .items returns us back with a list of the tuples
  key_dict.items()
'''


cricketers = {
  "sachin": {
     "age": 67,
     "test_played": 456,
     "families": ['sungeli','rangeli','bangeli'] 
  }  
}

print(cricketers['sachin'])#{'test_played': 456, 'age': 67, 'families': ['sungeli', 'rangeli', 'bangeli']}
print(type(cricketers))#type 'dict'
print(cricketers.keys())#['sachin']
print(type(cricketers.keys()))#list
print(cricketers.items())