# show_batch

make label description dictionary for ImageNet datasets

visualize batch images along with corresponding labels and discription for debugging or other purpose

# example usage:

    from show_batch import show_batch_part
    batch_size=256
    
    # batch_img should be in c01b shape
    batch_img = np.zeros(shape=(3,256,256,batch_size))   
    
    # batch_label is 1-d array, batch_size long
    batch_label = np.zeros(shape=(batch_size,)) 
    
    label_dict = np.load('./label_dict.npy').tolist()
    
    # show_range is an integer number indicating which 40 images to show in the batch
    show_batch_part(batch_img, batch_label,show_range=0, label_dict)  
