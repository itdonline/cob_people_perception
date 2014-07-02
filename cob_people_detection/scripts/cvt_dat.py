#!/usr/bin/env python
import cv
import os
import sys
import numpy
import shutil


def convert_dat(path):
  os.chdir(path)

  dir_list=os.listdir(".")
  print dir_list
  #get all dat files in directory
  folder_ctr=0
  for dir in dir_list:
    dat_list=list()
    os.chdir(path+"/"+str(dir))
    subdir_list=os.listdir(".")
    #print subdir_list
    for file in subdir_list:
      if os.path.splitext(file)[1]==".dat":
        dat_list.append(file)
      #training_set_file_stream = open(training_set_list_path,"w")
    #convert dat files one by one
    print "number of dat files: " + str(len(dat_list))
    filerange=len(dat_list)
    file_ctr=0
    for file in dat_list:
      f = open(file,"r")
      file_content = f.read().strip()
      file_content = file_content.replace('\n', ';')
      mat=numpy.matrix(file_content)
      mat=mat.astype(numpy.float32)
      for(r,c),value in numpy.ndenumerate(mat):
        if mat[r,c]==-1:
          mat[r,c]=0;
        else:
          mat[r,c]/=1000
      cv_mat=cv.fromarray(mat)
      o_path1=path+"/"+str(dir)+"/"+os.path.splitext(file)[0]+".xml"
      cv.Save(o_path1,cv_mat,"depth")
      o_str= "processed file "+str(file_ctr+1) + " of "+ str(filerange)
      print o_str
      file_ctr+=1
    folder_ctr+=1
    o_str = "processed folder " + str(folder_ctr) + " of " + str(len(dir_list))
    print o_str

if __name__=="__main__":
  #path="/share/goa-tz/people_detection/eval/Kinect3D/"
  path="/home/stefan/rgbd_db"

  #folder=sys.argv[1]
  i_path=path#+folder
  print i_path
  #src_dir="/share/goa-tz/people_detection/eval/Kinect3D_tar/"
  #os.chdir(path)
  #src_list=os.listdir(src_dir)
  #dir_ctr=0
  #for src in src_list:
  #  dir_str=path+str(dir_ctr)
  #  #os.mkdir(dir_str)
  #  #os.chdir(dir_str)
  #  src_mod=src.replace("(","\(")
  #  src_mod=src_mod.replace(")","\)")
  #  src_path_mod=src_dir+src_mod
  #  tarext_str="unzip "+src_path_mod+" -d ."
  #  os.system(tarext_str)
  #  tmppath=path+src
  #  tmppath= os.path.splitext(tmppath)[0]
  #  os.rename(str(tmppath),path+str(dir_ctr))
  #  dir_ctr+=1


  convert_dat(i_path)

  #os.system("gnome-session-save --force-logout")

