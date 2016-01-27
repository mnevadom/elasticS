import zipfile
import datetime


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
    print('creating archive ' + file)
    print(file.replace('.py', '') + '.zip')
    zf = zipfile.ZipFile(file.replace('.py', '') + '.zip', mode='w')
    #hacer un if file exists!!
    try:
        zf.write(file)
        print ('Created zip file: ')
        print_zip_info('get_container_func.zip')
    except:
        print ('error reading zip file ' + file)
    finally:
        zf.close()
