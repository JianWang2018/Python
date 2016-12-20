import numpy as np
import matplotlib.pylab as plt
import pandas as pd

# the threshold function is used to return the optimal threshold for classifying the samples
def Threshold(feature_list):
    # first sorted the feature_list by the first element
    feature_list=sorted(feature_list)
    threshold_idx=0
    for i in range(len(feature_list)):






def main():
    #for problem 2:
    # buid a tuple list to store the x,y values, we call it haar_feature_list
    haar_feature_list=[(0.48,1),(0.67,1),(0.60,1),(0.64,1),(0.64,1),(0.88,1),(0.74,1),(0.35,1),(-0.09,-1),(0.31,-1),(0.15,-1),(0.38,-1),(0.27,-1),\
                       (0.45,-1),(0.10,-1),(0.28,-1),(0.29,-1),(0.37,-1),(0.58,-1),(0.15,-1)]
    #print("The haar feature list is:" , haar_feature_list)
    #print("The length of haar feature list is:", len(haar_feature_list))
    # sort the haar_feature_list by first element
    haar_feature_list=sorted(haar_feature_list)
    #print(haar_feature_list)







if __name__ == "__main__":

    main()