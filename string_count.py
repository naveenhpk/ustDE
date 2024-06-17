msg='Learning Python for Data Engineering'
msg.casefold()
vowels=1
con=1
# words=0
# spaces=0
vow='aeiou'
# for i in msg:
#     if i=='a' or i=='e' or i=='i' or i=='o'or i=='u':
#         vowels+=1
#     else:
#         con+=1
#     if i==" ":
#         spaces+=1
#     else:
#         words+=1
msg1=msg.split(" ")
spaces=msg.count(" ")
words=len(msg1)
for i in msg:
    if i in vow:
        vowels+=1
    else:
        con+=1

print('vowels',vowels)
print('consonets',con)
print('spaces',spaces)
print('words',words)