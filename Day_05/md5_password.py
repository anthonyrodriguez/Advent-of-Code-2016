import hashlib
doorID = 'uqwqemis'
password = ''
index = 0
while len(password) < 8:
    if hashlib.md5('{}{}'.format(doorID, index)).hexdigest()[:5] == '00000':
        password += hashlib.md5('{}{}'.format(doorID, index)).hexdigest()[5]
    index += 1
print password
