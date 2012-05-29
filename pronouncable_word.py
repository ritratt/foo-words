import hashlib
import string
allowed='aeiouy01234567890'
alphabet='abcdefghijklmnopqrstuvwxyz'
consonants='bcdfghjklmnpqrstvwxz'
vowels='aeiouy'
pr=[]
def hashtoword(hash):
  pr.append(alphabet[int(hash[-2:],16)%26])
  for i in range(0,len(hash),2):
    if(i%3==0):
     pr.append(vowels[int(hash[i:i+2],16)%6])
    else:
     pr.append(consonants[int(hash[i:i+2],16)%19])
  print ''.join(pr)
  print str(wordtest(pr))
word=raw_input("give ")
hash=hashlib.md5(word).hexdigest()
print hash
hashtoword(hash)
#print str(wordtest(hash))
