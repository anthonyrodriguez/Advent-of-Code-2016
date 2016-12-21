#from __future__ import print_function 
import hashlib
doorID = 'uqwqemis'
password = ['_']*8
print ''.join(password)
index = 0
while '_' in password:
    try:
        curHash = hashlib.md5('{}{}'.format(doorID, index)).hexdigest()
        if (curHash.startswith('00000') 
        and (int)(curHash[5]) in range(8)
        and password[(int)(curHash[5])] == '_'):
            password[(int)(curHash[5])] = curHash[6]
            #print('{}'.format(password), end='')
            #print('\r', end='')
            print ''.join(password)
    except ValueError:
        pass
    index += 1
print ''.join(password)
