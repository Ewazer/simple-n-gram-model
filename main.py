import random

def clean_word(word):
  word = word.strip('.;,-“’”:?—‘!()_').lower()
  return word

def disct_count(text):
   dictionnaire = {}
   for word in text.split():
      word_clean = clean_word(word)
      if word_clean not in dictionnaire :
       dictionnaire[word_clean] = 1
      else:
       dictionnaire[word_clean] += 1
      
   return dictionnaire

def by_gram_dic_count(text):
   dict = {}
   list = []
   for word in text.split():
      word_clean = clean_word(word)
      if len(list) >= 2:
         if f"{list[0]},{list[1]}" in dict:
            dict[f"{list[0]} , {list[1]}"] += 1
         else:
            dict[f"{list[0]} , {list[1]}"] = 1
         list.pop(0)
         list.append(word_clean)  
      else:
         list.append(word_clean)   
   if f"{list[0]},{list[1]}" in dict:
      dict[f"{list[0]} , {list[1]}"] += 1
   else:
      dict[f"{list[0]} , {list[1]}"] = 1
      
   return(dict)

def by_gram(text):
  successor_map = {}
  window = []
  
  for line in text:
    for word in line.split():
      clean_word = word.strip('.;,-“’”:?—‘!()_').lower()
      window.append(clean_word)
  
      if len(window) == 2:
        key = window[0]
        value = window[1]
        if key in successor_map:
          successor_map[key].append(value)
        else:
          successor_map[key] = [value]
        window.pop(0)
  
  return(successor_map)

def three_gram(text):
  successor_map = {}
  window = []

  for line in text:
    for word in line.split():
      clean_word = word.strip('.;,-“’”:?—‘!()_').lower()
      window.append(clean_word)

      if len(window) == 3:
        key = (window[0], window[1])
        value = window[2]
        if key not in successor_map:
          successor_map[key] = [value]
        else:
          successor_map[key].append(value) 
        window.pop(0)
  
  return(successor_map)

def four_gram(text):
  successor_map = {}
  window = []

  for line in text:
    for word in line.split():
      clean_word = word.strip('.;,-“’”:?—‘!()_').lower()
      window.append(clean_word)

      if len(window) == 4:
        key = (window[0], window[1],window[2])
        value = window[3]
        if key not in successor_map:
          successor_map[key] = [value]
        else:
          successor_map[key].append(value) 
        window.pop(0)

  return(successor_map)

reader = open('text.txt')

print("by-gram")
print()

bygram_dict = by_gram(reader)

word1 = "for"

for i in range(10):
    print(word1, end=" ")
    successors = bygram_dict[word1]
    word1 = random.choice(successors)

print()
print("three-gram")
print()

reader = open('text.txt')

three_dict = three_gram(reader)

word1 = "for"
word2 = "god"

for i in range(10):
  print (word1, end=" ")
  successors = three_dict[(word1, word2)]
  word3 = random.choice(successors)
  word1, word2 = word2, word3

reader = open('text.txt')

four_dict = four_gram(reader)

word1 = "for"
word2 = "god"
word3 = "his"

for i in range(10):
  print (word1, end=" ")
  successors = four_dict[(word1, word2, word3)]
  word4 = random.choice(successors)
  word1, word2, word3 = word2, word3, word4
