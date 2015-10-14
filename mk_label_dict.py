import sys
import os
import yaml
import numpy as np

import glob


def remove_quote(key):
    
    if key[0]=='\'':
        key = key[1:]
    if key[-1] =='\'':
        key = key[:-1]
        
    return key

    
    
if __name__ == '__main__':

    import csv
    from collections import OrderedDict

    sortedID2WNID = []
    # sortedID.csv contains the 1000 catagory WNID and its corresponding sortedID label number. 
    # Extracted from meta_clsloc.mat file in ILSVRC_2014 datasets 
    # http://image-net.org/download-images
    with open('./sortedID.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        
        for row in reader:          
            sortedID2WNID.append(row['WNID'])
                
    print '---------------'
    
    dict_WNID2words={}
    # words.csv contains the 1860 catagory WNID and its corresponding word discription. 
    # Extracted from meta_clsloc.mat file in ILSVRC_2014 datasets 
    # http://image-net.org/download-images    
    with open('./words.csv') as csvfile:
        r = csv.DictReader(csvfile)
        
        for row in r:
            key = row['WNID']                            
            field1 = row['words']
            field2 = row['gloss']
            key = remove_quote(key)
            field1 = remove_quote(field1)
            field2 = remove_quote(field2)
            dict_WNID2words[key]=field1+' = '+field2
            
        dict_WNID2words = OrderedDict(sorted(dict_WNID2words.items()))
    
    #for key, value in dict_WNID2words.iteritems():
        #print key
        
    sortedID2words = []
    
    for WNID in sortedID2WNID:
        #print WNID
        sortedID2words.append(dict_WNID2words[WNID])
        
    #print sortedID2words
    #print len(sortedID2words)
    np.save('./label_dict.npy', sortedID2words)
    
       
            
    
        
        
            
        
        
        
        
        
