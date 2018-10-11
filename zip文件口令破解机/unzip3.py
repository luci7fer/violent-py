import zipfile
import optparse
from threading import Thread


def extractFile(zFile, password):
    try:
        zFile.extractall(pwd=password)
        print('[+] Found password ' + password + '\n')
    except:
        pass


def main():
    usage = "usage: %prog [options] -f <zipfilename> -d <dictionary>"
    parser = optparse.OptionParser(usage=usage)
    parser.add_option("-f", dest="zname", type="string",
                      help="specify zip file")
    parser.add_option("-d", dest='dname', type='string',
                      help="specify dictionary name")
    (options, args) = parser.parse_args()
    if(options.zname==None) | (options.dname==None):
        print(parser.usage)
        exit(0)
    else:
        zFile = zipfile.ZipFile(options.zname)
        passfile = open(options.dname)
    for line in passfile.readlines():
        password = line.strip('\n')
        t = Thread(target=extractFile, args=(zfiel, password))
        t.start()


if __name__ == '__main__':
    main()
