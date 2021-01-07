from time import process_time   #TO CALCULATE TIME TAKEN TO PROCESS
Time_start = process_time()    #START THE PROCESS TIME

# TO READ FIND_WORDS.TXT FILE AS A LIST
Find_Words = open("find_words.txt","r")
Find_Words_String = Find_Words.read()
Find_Words_List = Find_Words_String.split("\n")

# TO READ T8.SHAKESPEARE.TXT AS A STRING
Shakespeare = open("t8.shakespeare.txt","r")
Shakespeare_String = Shakespeare.read()
"""
    Shakespeare_List = Shakespeare_String.split("\n")
    print(Shakespeare_List)
"""
"""
    Line_Count = 0
    Shakespeare_List = Shakespeare_String.split("\n")
    for i in Shakespeare_List:
        if i:
            Line_Count += 1
    print("Line Count =",Line_Count,"\n")
"""

# TO READ FRENCH_DICTIONARY.CSV AND MAKE IT AS A DICTIONARY
import csv
French_Dictionary = csv.reader(open("french_dictionary.csv","r"))
Dictionary={}
for Row in French_Dictionary:
    Key,Value = Row
    Dictionary[Key] = Value

# TO TRANSATE WORDS TO FRENCH 
# TO FIND UNIQUE WORDS REPLACED
# TO FIND NUMBER OF TIMES WORD WAS REPLACED
# TO FIND FREQUENCY OF EACH WORD REPLACED
import re
Unique_Words = []
Frequency_Of_Word_Replaced = {}
Number_Of_Time_Words_Replaced = 0
for i in Find_Words_List:
    Frequency_Of_Word_Replaced[i] = Shakespeare_String.count(i)
    if i in Shakespeare_String:
        Replace_Word=Dictionary[i]
        Shakespeare_String = re.sub(i,Replace_Word,Shakespeare_String)
        Unique_Words.append(i)
        Number_Of_Time_Words_Replaced += 1
print("1. UNIQUE LIST OF WORDS REPLACED:\n",Unique_Words,"\n")
print("2. NUMBER OF TIME WORDS REPLACED:\n",Number_Of_Time_Words_Replaced,"\n")
print("3. FREQUENCY OF EACH WORD REPLACED:\n",Frequency_Of_Word_Replaced,"\n")


# TO WRITE TRANSLATED WORD INTO A FILE OUTPUT.TXT
t=open("output.txt","w")
t.write(Shakespeare_String)

# TO PRINT TIME TAKEN FOR ENTIRE PROCESS
Time_Stop = process_time()
print("4. TIME TAKE TO PROCESS [IN SECONDS]:\n",Time_Stop - Time_start,"\n")

#TO PRINT MEMORY TAKEN FOR ENTIRE PROCESS
import os, psutil
process = psutil.Process(os.getpid())
print("5. MEMORY TAKEN TO PROCESS:\n",process.memory_info().rss,"Bytes")

