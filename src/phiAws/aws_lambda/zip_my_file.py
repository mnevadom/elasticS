import zipfile
import datetime
import os

def print_zip_info(archive_name):
    zf = zipfile.ZipFile(archive_name)
    for info in zf.infolist():
        print info.filename
        print '\tComment:\t', info.comment
        print '\tModified:\t', datetime.datetime(*info.date_time)
        print '\tSystem:\t\t', info.create_system, '(0 = Windows, 3 = Unix)'
        print '\tZIP version:\t', info.create_version
        print '\tCompressed:\t', info.compress_size, 'bytes'
        print '\tUncompressed:\t', info.file_size, 'bytes'
        print


def create_zip_file(file):
    print('creating zip file from file ' + file)
    zipFile = (file.replace('.py', '') + '.zip')
    print('zip to create: ' + file.replace('.py', '') + '.zip')
    zf = zipfile.ZipFile(zipFile, mode='w')
    #hacer un if file exists!!
    try:
        zf.write(file)
        print ('Created zip file: ' + zf)
        #fileOut = os.path.join()
        print_zip_info(zipfile)
    except:
        print ('error reading zip file ' + file)
    finally:
        zf.close()

    return zipFile