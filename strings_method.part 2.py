# print(isinstance('hello',int))  # false    # isinstance
# print(isinstance('hello',float))  # false
# print(isinstance('hello',str))   #  ture     # bcoz hello is in str 

# print('agra'.isalpha())   # true    # isalpha bcoz here contains only alphabets 
# print('ag_raa'.isalpha())    # false 
# print('ag  raa'.isalpha())   #  false 
# print('ag23ra'.isalpha())    # false  

# print('2322'.isalnum())  # true   # isalnum  is combination of alphabets & number 
# print('43242dasdafsdf'.isalnum())   # true 
# print('23_54'.isalnum())    # false 
# print('23 45'.isalpha())   #   false 

# print('pythonprogram'.find('p'))   # 0 bcoz p is start from 0          #  find 
# print('pythonprogram'.rfind('h'))  #  3       # rfind
# print('pythonpropgram'.find('p',7))   # 9
