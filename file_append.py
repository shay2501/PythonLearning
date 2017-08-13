import os

# os.listdir('C:/Users/spisarsky.CTI/Music/iTunes/iTunes Media/Music')
for dirname, dirnames, filenames in os.walk('C:/Users/spisarsky.CTI/Music/iTunes/iTunes Media/Music/Unknown Artist/Unknown Album/DefyGravity/Disc1'):
    # rename  all files in directory
    for i,filename in enumerate(filenames):
        #if filename.find('1 - ') == -1:
            print(filename)
            os.rename(os.path.join(dirname,filename), os.path.join(dirname, '1-0' + str(i+1)+' CD1 Track ' + str(i+1) + '.mp3'))

   # print all files in directory, still keeps the old names from original walk, would need to walk again to see new names
    # for i,filename in enumerate(filenames):
    #     print(str(i) + ' - ' + filename)
