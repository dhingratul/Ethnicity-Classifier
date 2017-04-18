#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 16:31:53 2017

@author: dhingratul
"""
import numpy as np
my_data = np.genfromtxt('census_2000.csv', delimiter=',', dtype= str) 
eth=[0,1,2,3,4,5]
k=3
dic={}
np.delete(my_data,0,0) # Remove Headers
# Random data split into Train and Test 
np.random.shuffle(my_data)
split=round(0.9*len(my_data))
train=my_data[:split,:]
test=my_data[split:,:]
#print(my_data)    
names=train[:,0]    
for i in range(len(names)):
    #print(names[i])
    for j in range(len(names[i])-k+1):
        #print(j)
        try:
            ctr=int(train[i,2])
            if names[i][j:j+k] not in dic:
                dic[names[i][j:j+k]]=[ctr,ctr*float(train[i,5]),
                ctr*float(train[i,6]),ctr*float(train[i,7]),
                ctr*float(train[i,8]),ctr*float(train[i,9]),
                         ctr*float(train[i,10])]
            else:
                #print(i,j)
                temp=dic[names[i][j:j+k]]
                dic[names[i][j:j+k]]=[temp[0]+ctr,temp[1]+ctr*float(train[i,5]),
                    temp[2]+ctr*float(train[i,6]),temp[3]+ctr*float(train[i,7]),
                temp[4]+ctr*float(train[i,8]),temp[5]+ctr*float(train[i,9]),
                         temp[6]+ctr*float(train[i,10])]
        except:
            pass
names_test=test[:,0]   
percent=test[:,5:]   
ctr=0 
ctr2=0
for i in range(len(names_test)):
    #print(i)
    te=names_test[i]
    l=[]
    try:
        for j in range(len(te)-k+1):
            l.append(dic[te[j:j+k]])
    except:
        pass        
    
    if not l:
        #print("NA")
        pass
    else:
        ctr+=1
        l=np.array(l)  
        l2=np.prod(l,axis=0)
        try:
            out=np.array(percent[i,:],dtype='|S4')
            out = out.astype(np.float)
        except: 
            pass
        tr_label=np.argmax(out)
        pr_label=np.argmax(l2[1:])
        #print(i,pr_label)
        if pr_label==tr_label:
            ctr2+=1
            
print(ctr2/ctr)
  