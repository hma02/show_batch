import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def show(imgs, n=1):
    fig = plt.figure()
    col_max = 8
    row = math.ceil(n /col_max)
    for i in range(n):
        fig.add_subplot(row, col_max, i+1, xticklabels=[], yticklabels=[])
        if n == 1:
            img = imgs
        else:
            img = imgs[i]
        plt.imshow(img)

def show_batch(filenames,labels,minibatch_index,label_dict, batch_size):

    import hickle as hkl
    batch_img = hkl.load(str(filenames[minibatch_index]))# c01b
    batch_label = labels[(minibatch_index) * batch_size: (minibatch_index + 1) * batch_size]
    print minibatch_index
    for show_range in range(6):
        show_batch_part(batch_img, batch_label,show_range,label_dict)


def show_batch_part(batch_img, batch_label,show_range, label_dict):
    
    print batch_label[show_range*40:(show_range+1)*40] 
    
    for cat in batch_label[show_range*40:(show_range+1)*40]:
        print cat,label_dict[cat]
    
    show(batch_img.transpose(3,1,2,0)[show_range*40:(show_range+1)*40],40) # c01b to bc01
    plt.show()

if __name__ == '__main__': 
    
    # example usage:
    
    batch_size=256
    
    # batch_img should be in c01b shape
    batch_img = np.zeros(shape=(3,256,256,batch_size))   
    
    # batch_label is 1-d array, batch_size long
    batch_label = np.zeros(shape=(batch_size,)) 
    
    label_dict = np.load('./label_dict.npy').tolist()
    
    # import this function only
    # show_range is an integer number indicating which 40 images to show in the batch
    show_batch_part(batch_img, batch_label,show_range=0, label_dict)  