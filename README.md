String methods:
- lower() 
    For converting the string to the lowercase filled characters as a result of the operation
- upper()
    For converting the string to the uppercase filled characters as a result of the operation
- count('')
    For counting the characters in the string .
- capitalize()
    For capitalizing only first character in the string .
- index()
    This is the used for returnign the index at which the character sits.
```
   a = "asfdfsa"
   a.index("s")
   output:
   1


   But there exists one problem with the index() method and that is it throws back the error if it could not find the substring in the mainstring 
   a = "hello World"
   a.index("asdfs")
   output:

    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    ValueError: substring not found
```
- strip()
  * this is used to strip of the white spaces in that string
      - to strip the white spaces
  * strip('a')
      - this is used to strip a at any position in the string
  This method is used to strip the characters from either side in the string
  example:
  - lstrip('a')
    * This is used to strip all the characters with 'a' from the zero index to the place where a's end continuously in the string 
    ```
      sample_str = "akjksfk232323akfsfk"
      sample_str.lstrip("a")
      'kjksfk232323akfsfk'
    ```

  - rstrip
  ```
    sample_str.rstrip("k")
    'akjksfk232323akfsf'
  ```
- find()
  the method is being performed on top of the string objects
  ```
    a = "afsfkjskfjk"
    a.find('a') //outputs 0
  ```
- slicing the strings:
  ```
    # this could be querky concept to understand
    a = "helloramaraju"
    a[1:upto:steps]
    print(a[1:6])# this is used to print the string that is held in the variable a from 1 to 5th index
  ```



A Very Good Blog of explaining of the key word self in python
[https://medium.com/quick-code/understanding-self-in-python-a3704319e5f0]




# How to load python3 scripts in a PYTHON Shell
```
  python3 
  > the above command does the process of taking the python into a python3 shell
  now that we are into the python3 shell we have something called

  `exec`
    - The exec does the operation of the file loading .
    - exec('<filenametoload.py>') in the python shell makes the loading of the python script .
```