import re
import string 
import collections


# opening and reading the file :



# initializing string  
text = ''
f = open("random_text.txt", "r")
if f.mode == 'r':
    text = f.read()
 

text = re.sub(r"[^a-zA-Z0-9]+", ' ', text) # removing punctuations
text = text.replace("the","")


# dictionary keeps the track of each word and its reapitition in the text


dictionary = dict()
words = text.split()

for word in words: 
    if word in dictionary:
        dictionary[word]= dictionary[word]+1
    else:
        dictionary[word] = 1




# Then I removed the words 'a' 'an' 'be' from the dictionary
if 'an' in dictionary:    
    del dictionary['an']
if 'a' in dictionary:
    del dictionary['a']
if 'be' in dictionary:
    del dictionary['be']


# The number of unique words : 

for k,v in dictionary.items():
     print(k, ":",v)


i=0
for k in sorted(dictionary, key=dictionary.get, reverse=True):
    if (i>4):
        break
    print(k,dictionary[k])
    i+=1
       

