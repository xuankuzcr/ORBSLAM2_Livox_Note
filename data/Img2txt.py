#!/usr/bin/env python3
#-*- coding:utf-8-*-
import os
 
data_path1 = 'rgb'
data_path2 = 'depth'
img_names1 = os.listdir(data_path1)
img_names2 = os.listdir(data_path2) 
list_file1 = open('rgb.txt', 'w')
list_file2 = open('depth.txt', 'w')

list_file1.write('# color images\n')
list_file1.write("# file: 'SUSTech-ORB-SLAM2.bag'\n")
list_file1.write('# timestamp filename\n')

img_names1=sorted(img_names1)  #图片顺序
img_names2=sorted(img_names2)  #图片顺序

for img_name1 in img_names1:
    if os.path.splitext(img_name1)[1] == '.png':
	imgName1 = os.path.splitext(img_name1)[0]
    list_file1.write(imgName1+' '+'rgb/%s\n'%img_name1)    

list_file1.close()

list_file2.write('# depth maps\n')
list_file2.write("# file: 'SUSTech-ORB-SLAM2.bag'\n")
list_file2.write('# timestamp filename\n')

for img_name2 in img_names2:
    if os.path.splitext(img_name2)[1] == '.png':
	imgName2 = os.path.splitext(img_name2)[0]
    list_file2.write(imgName2+' '+'depth/%s\n'%img_name2)    

list_file2.close()
