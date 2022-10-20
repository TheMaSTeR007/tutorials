'''
   1) write a function that gets a sentence (as a str) and outputs the length of the last word and the count of the characters in the sentence. 
   
   e.g.: input_sentence = 'Hello World!' --> output = [ 5 , 12 ]       
   e.g.: input_sentence = 'This is a sentence.' --> output = [ 8 , 19]
   

'''
import re
def lengthOfLastWordAndCountOfCharacters(a):
    l = 0
    y=a.strip()
    stringWithoutSpecialCharacter=re.sub('[^a-zA-Z0-9 \n]', '',y)
    print(stringWithoutSpecialCharacter)
    

    for i in range(len(stringWithoutSpecialCharacter)):
        if stringWithoutSpecialCharacter[i] == " ":
            l = 0
        else:
            l += 1
    return l, len(y)


if __name__ == "__main__":
    inp = "Hello World!"
    print(lengthOfLastWordAndCountOfCharacters(inp))

'''
    2)  write a function that gets two lists of numbers and merges them and outputs the sorted merged list.
   
   e.g.: input_list1 = [0,1,2,8,-1, 9] , input_list2 = [-11,9]--> output = [-11, -1, 0, 1, 2, 8, 9, 9]
   
'''
def mergedSortedList(a,b):
    c=a+b
    c.sort()

    return c
    


if __name__ == "__main__":
    input_list1 = [0,1,2,8,-1, 9]
    input_list2 = [-11,9]
    print(mergedSortedList(input_list1,input_list2))

'''
    3)  write a function that get a list of numbers and outputs the second largest number in it.
   
   e.g.: input_list = [0,1,2,8,-1] --> output = 2
   e.g.: input_list = [-11, 1.2, 9.9,9] --> output = 9
'''
def secondLargestNumber(a):
    
    a.sort()
    
    return a[len(a)-2]
    


if __name__ == "__main__":
    input_list = [-11, 1.2, 9.9,9]
    print(secondLargestNumber(input_list))


'''
    4)  write a function that get a string as an input and outputs the reverse of that (only letters!)
   
   e.g.: input_str = 'hel-lo,wo.rld' --> output = 'dlr-ow,ol.leh'
   e.g.: input_str = '12311!hm' --> output = '12311!mh'
'''
def reverseOnlyLetters(S):
    if not S:
        return S
    str_ = ""
    index1 = 0
    index2 = len(S)-1
    while index1 < len(S):
        if index2 >= 0 and S[index1].isalpha() and S[index2].isalpha():
            str_ += S[index2]
            index2 -= 1
            index1 += 1
        elif S[index1].isalpha():
            index2 -= 1
        elif not S[index1].isalpha():
            str_ += S[index1]
            index1 += 1
        else:
            index2 -= 1
            index1 += 1
    return str_


if __name__ == "__main__":
    input_str = '12311!hm'
    print(reverseOnlyLetters(input_str))


'''
    5)  write a function that gets a sentence (as a str) and outputs the reverse of that.
   
   e.g.: input_sentence = 'Hello World' --> output = 'World Hello'
   e.g.: input_sentence = 'this is a sentence' --> output = 'sentence a is this'
'''
def rev_sentence(sentence):
 
    words = sentence.split(' ')
 
    reverse_sentence = ' '.join(reversed(words))
 
    return reverse_sentence
 
if __name__ == "__main__":
    input = 'Hello World'
    print (rev_sentence(input))



'''
    6)  write a function that gets two numbers as strings and outputs the sum of them. 
   
   e.g.: str1 = '96' , sr2 = '21'--> output = 117
   e.g.: str1 = '28' , sr2 = '2'--> output = 30
'''
def sumOfString(a,b):
  
    return int(a)+int(b)
 
if __name__ == "__main__":
    str1 = '28'
    str2 = '2'
    print (sumOfString(str1,str2))

'''
    7)  write a function that gets two binary numbers from the user and outputs the sum of them in binary. 
   
   e.g.: input1 = 101 , input2 = 10 --> output = 111
   e.g.: input1 = 11 , input2 = 1 --> output = 100
'''
def sumOfBinary(a, b):

    sum = bin(int(a, 2) + int(b, 2))

    return sum[2:]


if __name__ == "__main__":
    num1 = input()
    num2 = input()
    print(sumOfBinary(num1, num2))


'''
    8)  write a function:
    
        5-1) thats gets a list of numbers and counts the occurrences of all items in it. 
              e.g.: list1 = [9,9,1,0,1,9] --> output = [(9,3) , (1,2), (0,1)]
              
        5-2) that gets two lists and outputs their common elements. 
             e.g.: list1 = [66,23,1,0,1,9] , list2 = [5,55,1,12] --> output = [1]         

'''
(8-1)
def countOccurrence(a):
    k = {}
    for j in a:
        if j in k:
            k[j] += 1
        else:
            k[j] = 1
    return k

if __name__ == "__main__":
    list1 = [9, 9, 1, 0, 1, 9]
    print(countOccurrence(list1))    

(8-2)
def commonElement(a, b):
    a_set = set(a)
    b_set = set(b)

    if len(a_set.intersection(b_set)) > 0:
        return (a_set.intersection(b_set))
    else:
        return ("no common elements")


if __name__ == "__main__":
    list1 = [66, 23, 1, 0, 1, 9]
    list2 = [5, 55, 1, 12]
    print(commonElement(list1, list2))

'''
    9)  write a function that gets a string from the user and returns the most frequent character in it. 
   
   e.g.: str1 = 'hello world'--> output = 'l'
   e.g.: str1 = 'cs_comp478'--> output = 'c'
'''
from collections import Counter


def mostFrequentChar(a):

    res = Counter(a)
    res = max(res, key=res.get)

    return res


if __name__ == "__main__":
    str1 = 'cs_comp478'
    print(mostFrequentChar(str1))



'''
    10) write a function that gets a list of numbers and returns the compnents of the list that are perfect square numbers. 
   
   e.g.: input1 = [1, 5, 8, 9] --> output = [1,9]
   e.g.: input1 = [3, 7, 5, 55 ]--> output = []

'''

import math


def findPerfectSquare(a):
    b = []

    for i in a:
        root = math.sqrt(i)
        if int(root + 0.5) ** 2 == i:
            b.append(i)
    return b


if __name__ == "__main__":
    input1 = [3, 7, 5, 55 ]
    print(findPerfectSquare(input1))





    

