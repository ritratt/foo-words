import hashlib
import string
allowed='aeiouy01234567890'
alphabet='abcdefghijklmnopqrstuvwxyz'
consonants='bcdfghjklmnpqrstvwxz'
vowels='aeiouy'
f=open("words.txt")
words=f.read()
words=words.split('\n')
print len(words)
f.close()
def hashtoword(hash):
  pr=[]
  pr.append(alphabet[int(hash[-2:],16)%26])
  for i in range(0,len(hash),2):
    if(i%3==0):
     pr.append(vowels[int(hash[i:i+2],16)%6])
    else:
     pr.append(consonants[int(hash[i:i+2],16)%19])
  print 'Pronouncable but unrememberable password is '+''.join(pr[:8])

def passphrase(pwd):
  pph=[]
  pwd_hash=hashlib.md5(pwd).hexdigest()
  for i in range(0,len(pwd_hash),4):
    pph.append(words[int(str(pwd_hash[i:i+4]),16)])
    pph.append(' ')
  print 'Makes-total-sense passphrase is '+''.join(pph)
word=raw_input("give ")
print(words.count(word))
hash=hashlib.md5(word).hexdigest()
print 'Hash of passwords is='+hash
hashtoword(hash)
passphrase(word)

