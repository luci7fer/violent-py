import zipfile
zFile = zipfile.ZipFile('evil.zip')
passFile = open('dictionary')
for line in passFile.readline():
    password = line.strip('\n')
    try:
        zFile.extractall(pwd=password)
        print '[*]Password =' +password+ '\n'
        exit(0)
    except Exception as e:
        pass
