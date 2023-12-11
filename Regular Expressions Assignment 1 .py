#!/usr/bin/env python
# coding: utf-8

# In[1]:


import regex as re 
import pandas as pd 
import numpy as np
from datetime import datetime
import ipaddress


# In[2]:


# Q . 1 Write Python Program to replace all occurrences of a space ,comma or dot with a colon.
text = 'Python Exercises, PHP exercises'

new_text = text.replace(" ",":")

new_txt = new_text.replace(",",":")

print(new_txt)


# In[3]:


#Q.2 Create a dataframe using the dictionary below and remove everything (commas (,), !, XXXX, ;, etc.) 
# from the columns except words.


dict = {'SUMMARY': ['hello, world!', 'XXXXX test', '123four, five:; six...']}

df = pd.DataFrame(dict)

df['SUMMARY'] = df['SUMMARY'].str.replace('XXXXX', '     ')

df['SUMMARY'] = df['SUMMARY'].str.replace('[^a-zA-Z\s]', '', regex=True)

print(df)


# In[4]:


# Q.3Create a function in python to find all words that are at least 4 characters long in a string. 
# The use of the re.compile() method is mandatory.



def words (str):
    
    str_pattern = r'\b\w{4,}\b'
    
    X = re.compile(str_pattern)
  
    matches = X.findall(str)
    
    return matches

str = "Chandrayaan-3 is a follow-on mission to Chandrayaan-2 to demonstrate end-to-end capability in safe landing"

results = words(str)

if results:
    print("Yes at least 4 characters Match!",results)
    
else:
    print("No match found.")


# In[5]:


# Q 4 Create a function in python to find all three, four, and five character words in a string. 
# The use of the re.compile() method is mandatory.

str = "Chandrayaan-3 is a follow-on mission to Chandrayaan-2 to demonstrate end-to-end capability in safe nice landing"


def words (str):
    
    str_pattern = r'\b\w{3,5}\b'
    
    X = re.compile(str_pattern)
    
    matches = X.findall(str)
    
    return matches


results = words(str)

if results:
    print("Yes at least characters Match!",results)
    
else:
    print("No match found.")


# In[6]:


# Q.5 Create a function in Python to remove the parenthesis in a list of strings.
# The use of the re.compile() method is mandatory.

text = ["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]



def bracket (text):
    
    pattern = re.compile(r'\(([^)]*)\)')
    
    new_text = [pattern.sub(r'\1',s) for s in text]  
    
    return new_text
                         
    
results = bracket(text)

for new_text in results:
    
    print(new_text)
     
                         
if results:
                        
    print("Yes Bracket are removed!")
                         
else:
    print("No Bracket removed")                         
                         
 


# In[7]:


# Q 6 Write a python program to remove the parenthesis area from the text stored in the text file using Regular Expression.
# Sample Text: ["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]
# Expected Output: ["example", "hr@fliprobo", "github", "Hello", "Data"]
# Note- Store given sample text in the text file and then to remove the parenthesis area from the text.

def remove_parentheses_from_text_file(old_file_path, new_file_path):
    
    with open(old_file_path, "r") as file:
        
        lines = file.readlines()

    pattern = re.compile(r"\([^)]*\)")
    
    new_lines = [pattern.sub("", line).strip() for line in lines]

    with open(new_file_path, "w") as output_file:
        
        output_file.write('\n'.join(new_lines))
        
        print(new_lines)


old_file_path = "old_text.txt"

new_file_path = "new_text.txt"


target_string = ["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]

with open(old_file_path, "w") as file:
    
    for line in target_string:
        
        file.write(line + "\n")

remove_parentheses_from_text_file(old_file_path, new_file_path)


# In[8]:


# Q 7 Write a regular expression in Python to split a string into uppercase letters.
# Sample text: “ImportanceOfRegularExpressionsInPython”

txt = "ImportanceOfRegularExpressionsInPython"

results = re.findall(r'[A-Z][a-z]*',txt)

print(results)


# In[9]:


# Q 8 Create a function in python to insert spaces between words starting with capital letters or with numbers.
# Sample Text: “RegularExpression1IsAn2ImportantTopic3InPython"

def insert_spaces(text):
    result = ''
    for char in text:
        if char.isupper() or char.isdigit():
            result += ' ' + char
        else:
            result += char
    return result.strip()

# Sample text
sample_text = "RegularExpression1IsAn2ImportantTopic3InPython"

# Get the expected output
output = insert_spaces(sample_text)

# Display the result
print(output)


# In[10]:


# Q 9 Use the github link below to read the data and create a dataframe. 
# After creating the dataframe extract the first 6 letters of each country 
# and store in the dataframe under a new column called first_five_letters.

# Github Link-  https://raw.githubusercontent.com/dsrscientist/DSData/master/happiness_score_dataset.csv


url = "https://raw.githubusercontent.com/dsrscientist/DSData/master/happiness_score_dataset.csv"


df = pd.read_csv(url)

# Extract the first 6 letters of each country and create a new column
df['first_five_letters'] = df['Country'].str[:6]

# Display the DataFrame
print(df.head())


# In[11]:


# Q 10 Write a Python program to match a string that contains only upper and lowercase letters, numbers, and underscores.


def find_valid_strings(text):

    pattern = r'\b[a-zA-Z0-9_]+\b'

 
    valid_strings = re.findall(pattern, text)

    return valid_strings


sample_text = "This is a Valid_String123 and Another_Valid_123. Invalid@String and spaces not allowed."


result = find_valid_strings(sample_text)


print(result)


# In[12]:


# Q12 Write a Python program to remove leading zeros from an IP address



def remove_leading_zeros(ip_address):
  
    try:
        ip_obj = ipaddress.ip_address(ip_address)
        formatted_ip = str(ip_obj)
        return formatted_ip
    except ValueError:
        print("Invalid IP address")


ip_with_zeros = "192.168.001.001"
ip_without_zeros = remove_leading_zeros(ip_with_zeros)

print(f'Original IP: {ip_with_zeros}')
print(f'IP without leading zeros: {ip_without_zeros}')


# In[13]:


# Q.13 Write a regular expression in python to match a date string in the form of Month 
# name followed by day number and year stored in a text file.


Sample_text = 'On August 15th 1947 that India was declared independent from British colonialism, and the reins of control were handed over to the leaders of the Country'

with open('sample_text.txt', 'r') as file:
    
    text_content = file.read()

date_pattern = re.compile(r'\b(?:August)\s+\d{1,2}(?:st|nd|rd|th)?\s+\d{4}\b')

matches = date_pattern.findall(text_content)


for match in matches:
    print(match)

    


# In[14]:


# Q 15  Write a Python program to search some literals strings in a string. 

sample_text = 'The quick brown fox jumps over the lazy dog.'

searched_words = ['fox', 'dog', 'horse']

def search_literals(input_string, searched_words):
    
    found_words = [word for word in searched_words if word in input_string]
    
    return found_words

found_literals = search_literals(sample_text, searched_words)


print("Found words:")
for word in found_literals:
    print(word)


# In[15]:


# Q16 Write a Python program to search a literals string in a string and also find the location within the original string where the pattern occurs

sample_text = 'The quick brown fox jumps over the lazy dog.'
    
searched_words = 'fox'
    

def search_literal(input_string, searched_words):
    
    position = input_string.find(searched_words)
    
    return position

found_position = search_literal(sample_text, searched_words)


if found_position != -1:
    
    print(f"'{searched_words}' found at position {found_position}")
    
else:
    print(f"'{searched_words}' not found in the sample text.")
    


# In[16]:


# Q 17  Write a Python program to find the substrings within a string.



sample_text = 'Python exercises, PHP exercises, C# exercises'

pattern = 'exercises'


positions = [(match.start(), match.end()) for match in re.finditer(pattern, sample_text)]

if positions:
    
    print(f"Pattern '{pattern}' found at positions:")
    
    for start, end in positions:
        
        print(f"Start: {start}, End: {end}")
else:
    print(f"Pattern '{pattern}' not found in the sample text.")


# In[17]:


# Q 18 Write a Python program to find the occurrence and position of the substrings within a string.


sample_text = 'Python exercises, PHP exercises, C# exercises'

pattern = 'exercises'

matches = list(re.finditer(pattern, sample_text))

if matches:
    
    print(f"Pattern '{pattern}' found {len(matches)} time(s) at positions:")
    
    print("\n".join([f"Start: {match.start()}, End: {match.end()}" for match in matches]))
    
else:
    
    print(f"Pattern '{pattern}' not found in the sample text.")
    


# In[18]:


# Q 19 Write a Python program to convert a date of yyyy-mm-dd format to dd-mm-yyyy format.


def convert_date_format(input_date):

    try:
        
        return datetime.strptime(input_date, '%Y-%m-%d').strftime('%d-%m-%Y')
    
    except ValueError:
        
        return "Invalid date format"

input_date = '2023-12-25'

converted_date = convert_date_format(input_date)


print(f"Original Date: {input_date}")

print(f"Converted Date: {converted_date}")


# In[19]:


# Q 20 Create a function in python to find all decimal numbers with a precision of 1 or 2 in a string.
# The use of the re.compile() method is mandatory.

sample_text = "01.12 0132.123 2.31875 145.8 3.01 27.25 0.25"

def find_decimal_numbers(input_string):
    
    pattern = re.compile(r'\b\d+\.\d{1,2}\b')
    
    return pattern.findall(input_string)

decimal_numbers = find_decimal_numbers(sample_text)

print(decimal_numbers)


# In[20]:


# Q 21 Write a Python program to separate and print the numbers and their position of a given string.

sample_text = 'The price is $25.99 and the quantity is 10.'

def separate_and_print_numbers(input_string):
    
    for match in re.finditer(r'\b\d+\b', input_string):
        
        print(f"{match.group()}, Position: ({match.start()}, {match.end() - 1})")

        
separate_and_print_numbers(sample_text)



# In[21]:


# Q 22 Write a regular expression in python program to extract maximum/largest numeric value from a string.

sample_text = 'My marks in each semester are: 947, 896, 926, 524, 734, 950, 642'

import re

def extract_maximum_numeric_value(input_string):
    
    matches = [int(match) for match in re.findall(r'\b\d+\b', input_string)]
    
    if matches:
       
        return max(matches)
    
    else:
        return None  
    

max_numeric_value = extract_maximum_numeric_value(sample_text)

print(f"Maximum Numeric Value: {max_numeric_value}")


# In[22]:


# Q -23 Create a function in python to insert spaces between words starting with capital letters.

sample_text = "RegularExpressionIsAnImportantTopicInPython"

def insert_spaces(input_string):
    
    spaced_words = []
    
    current_word = ""

    for char in input_string:
        
        if char.isupper() and current_word:
            
            spaced_words.append(current_word)
            
            current_word = char
            
        else:
            current_word += char

    if current_word:
        
        spaced_words.append(current_word)

    return ' '.join(spaced_words)



result = insert_spaces(sample_text)

print(result)


# In[23]:


# Q -23 Create a function in python to insert spaces between words starting with capital letters.

sample_text = "RegularExpressionIsAnImportantTopicInPython"

def insert_spaces(input_string):
    
    spaced_string = re.sub(r'([a-z])([A-Z])', r'\1 \2', input_string)
    
    return spaced_string


result = insert_spaces(sample_text)

print(result)


# In[24]:


# Q 24 - Python regex to find sequences of one upper case letter followed by lower case letters

sample_text = "The Quick Brown Fox Jumps Over The Lazy Dog"

def find_sequences(input_string):
    
    pattern = re.compile(r'\b[A-Z][a-z]*\b')
    
    return pattern.findall(input_string)


result = find_sequences(sample_text)

print(result)


# In[25]:


# Q 25-Write a Python program to remove continuous duplicate words from Sentence using Regular Expression.

sample_text = "Hello hello world world"

def remove_continuous_duplicates(input_sentence):
    
    pattern = re.compile(r'\b(\w+)(\s+\1)+\b', flags=re.IGNORECASE) 
    
    cleaned_sentence = pattern.sub(r'\1', input_sentence)
    
    return cleaned_sentence



result = remove_continuous_duplicates(sample_text)

print(result)


# In[26]:


# Q 26- Write a python program using RegEx to accept string ending with alphanumeric character.

sample_text = "Hello123"

def ends_with_alphanumeric(input_string):
    
    pattern = re.compile(r'\w$')
    
    return bool(pattern.search(input_string))


result = ends_with_alphanumeric(sample_text)

if result:
    
    print ("Yes with alphanumeric character:", result)
    
else: 
    
    print ("No match")


# In[27]:


# Q 27 Write a python program using RegEx to extract the hashtags.

sample_text = """RT @kapil_kausik: #Doltiwal I mean #xyzabc is "hurt" by #Demonetization as the same has rendered USELESS <ed><U+00A0><U+00BD><ed><U+00B1><U+0089> "acquired funds" No wo"""

def extract_hashtags(input_text):
    
    pattern = re.compile(r'#\w+')
    
    hashtags = pattern.findall(input_text)
    
    return hashtags

result = extract_hashtags(sample_text)

print(result)


# In[28]:


# Q 28 Write a python program using RegEx to remove <U+..> like symbols
# Check the below sample text, there are strange symbols something of the sort <U+..> all over the place.
# You need to come up with a general Regex expression that will cover all such symbols.


sample_text = "@Jags123456 Bharat band on 28??<ed><U+00A0><U+00BD><ed><U+00B8><U+0082>Those who are protesting #demonetization are all different party leaders"

def remove_unicode_symbols(input_text):
    
    pattern = re.compile(r'<U\+[0-9A-Fa-f]+>')
    
    cleaned_text = pattern.sub('', input_text)
    
    
    return cleaned_text



result = remove_unicode_symbols(sample_text)

print(result)


# In[29]:


# Q 29 Write a python program to extract dates from the text stored in the text file.

file_path = 'sample_text1.txt'

def extract_dates_from_file(file_path):
    
    with open(file_path, 'r') as file:
        
        text_content = file.read()

    date_pattern = re.compile(r'\b\d{2}-\d{2}-\d{4}\b')
    
    dates = date_pattern.findall(text_content)

    return dates



dates_found = extract_dates_from_file(file_path)


print(dates_found)


# In[30]:


# Q30 Create a function in python to remove all words from a string of length between 2 and 4.
# The use of the re.compile() method is mandatory.


sample_text = "The following example creates an ArrayList with a capacity of 50 elements. 4 elements are then added to the ArrayList and the ArrayList is trimmed accordingly."

def remove_words_between_length(input_string):
    
    pattern = re.compile(r'\b\w{2,4}\b')
    
    cleaned_string = pattern.sub('', input_string)
    
    return cleaned_string



result = remove_words_between_length(sample_text)

print(result)


# In[ ]:




