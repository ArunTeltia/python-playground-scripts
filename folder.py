import os

import re
basedir = "E:\Please don't bully me, Nagatoro"
# for fn in os.listdir(basedir):
#   if not os.path.isdir(os.path.join(basedir, fn)):
#     continue # Not a directory
#   if ',' in fn:
#     continue # Already in the correct form
#   if ' ' not in fn:
#     continue # Invalid format
#   firstname,_,surname = fn.rpartition(' ')
#   os.rename(os.path.join(basedir, fn),
#             os.path.join(basedir, surname + ', ' + firstname))
# print( os.listdir(basedir))
for folder in os.listdir(basedir):
    res = re.split(', |_|-|! ', folder)
    
    # print(res)
    
    
    split =res[0].split(" ")
    if split[0]=='Chapter':
        res[0]=split[1]
        # print(split)
    s=" "
    s = s.join(res)
    print(s) 
    # if(mangakakalot[0])
    # s = " "
    # s = s.join(mangakakalot)
    os.rename(os.path.join(basedir, folder), os.path.join(basedir, s))
