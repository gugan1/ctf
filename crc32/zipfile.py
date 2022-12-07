import zipfile


        
files = zipfile.ZipFile(".\\1.zip", 'r')

for file in files.infolist():

    with open(".\\crc32.txt",'a') as f:
        f.write(hex(file.CRC)+',')
            
    print(hex(file.CRC)+',')
        