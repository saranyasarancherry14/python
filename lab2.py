from collections import Counter 
  
data=open("/home/cs2016a221/hi.txt","r")
data1=data.read()
  
# split() returns list of all the words in the string 
split_it = data1.split() 
  
# Pass the split_it list to instance of Counter class. 
Counter = Counter(split_it) 
  
# most_common() produces k frequently encountered 
# input values and their respective counts. 
most_occur = Counter.most_common(10) 
  
print(most_occur) 
