import numpy as np
import matplotlib.pylab as plt
import numpy as np
import cv2
import time

class ComputerVision(object):
    # size is the image shape.
    def img_write(image,name,path_save,size):
        """
        divide the image into small part of image with the given size
        :param image: original image
        :param size: the size of small image that we want to divide from the original image
        :return: no return
        """

        image = cv2.pyrDown(image)
        image = cv2.pyrDown(image)
        i=0
        for m in range(int(image.shape[0]/size[0])):
            for n in range(int(image.shape[1]/size[1])):
                crop_img = image[m*size[0]:(m+1)*size[0], n*size[1]:(n+1)*size[1]]
                cv2.imwrite(path_save+name+str(i) + ".jpg", crop_img)
                i+=1

    def integral_image(img):

        """

        :param img:original image
        :return: the integral_image
        """
        height, width = img.shape[0],img.shape[1]
        blank_image1 = np.zeros((height, width), int)
        blank_image2 = np.zeros((height, width), int)

        for m in range(height):
            for n in range(width):
                for z in range(m+1):
                    blank_image1[m][n] += img[z][n]

        for m in range(height):
            for n in range(width):
                for z in range(n+1):
                    blank_image2[m][n] += blank_image1[m][z]

        return blank_image2

    def haar_feature(size):
        """
        Given a size of image, generate all its haar features based on the five basic unit features
        :param size: the size to generate haar features
        :return: total haar features
        """
        # image_x and image_y represent the dimension of the image, which is the first and second index of size.
        image_x=size[0]
        image_y=size[1]
        # use the following five kind of basic feature types
        features_num=5
        features_type=[[2,1],[1,2],[3,1],[1,3],[2,2]]
        # haar_feature is to store all the features of the image
        haar_feature=[]
        count=0

        for i in range(features_num):
            size_x=features_type[i][0]
            size_y=features_type[i][1]

            for width in np.arange(size_x,image_x+1,size_x):
                for height in np.arange(size_y,image_y+1,size_y):
                     for x in range(image_x-width+1):
                         for y in range(image_y-height+1):
                             haar_feature.append([i,x,y,width,height])
                             count=count+1
        print("the total number of haar feature is:",count)
        return haar_feature

    def feature_value(integral_image, feature):
        """
        Given integral_image and a specific Haar feature, returns the difference of the corresponding squares
        indicated by this Haar feature in original image

        """
        # read the the type, location, scale of Haar feature
        t=feature[0]
        x=feature[1]
        y=feature[2]
        w=feature[3]
        h=feature[4]

        if t==0:
            a_11=a_12=a_13=a_21=0
            a_22=integral_image[x-1+w/2][y-1+h]
            a_23=integral_image[x-1+w][y-1+h]
            if (x-1>0):
                a_21=integral_image[x-1][y-1+h]
                if y-1>0:
                    a_11=integral_image[x-1][y-1]
                    a_12=integral_image[x-1+w/2][y-1]
                    a_13=integral_image[x-1+w][y-1]
            elif y-1>0:
                a_12=integral_image[x-1+w/2][y-1]
                a_13=integral_image[x-1+w][y-1]

            return a_11-2*a_12+a_13-a_21+2*a_22-a_23
        elif t==1:
            a_11=a_12=a_21=a_31=0
            a_22=integral_image[x-1+w][y-1+h/2]
            a_32=integral_image[x-1+w][y-1+h]
            if x-1>0:
                a_21=integral_image[x-1][y-1+h/2]
                a_31=integral_image[x-1][y-1+h]
                if y-1>0:
                    a_11=integral_image[x-1][y-1]
                    a_12=integral_image[x-1+w][y-1]
            elif y-1>0:
                a_12=integral_image[x-1+w][y-1]

            return -a_11+a_12+2*a_21-2*a_22-a_31+a_32
        elif t==2:
            a_11=a_12=a_13=a_14=a_21=0
            a_22=integral_image[x-1+w/3][y-1+h]
            a_23=integral_image[x-1+w/3+w/3][y-1+h]
            a_24=integral_image[x-1+w][y-1+h]
            if x-1>0:
                a_21=integral_image[x-1][y-1+h]
                if y-1>0:
                    a_11=integral_image[x-1][y-1]
                    a_12=integral_image[x-1+w/3][y-1]
                    a_13=integral_image[x-1+w/3+w/3][y-1]
                    a_14=integral_image[x-1+w][y-1]
            elif y-1>0:
                a_12=integral_image[x-1+w/3][y-1]
                a_13=integral_image[x-1+w/3+w/3][y-1]
                a_14=integral_image[x-1+w][y-1]

            return a_11-2*a_12+2*a_13-a_14-a_21+2*a_22-2*a_23+a_24
        elif t==3:
            a_11=a_12=a_21=a_31=a_41=0
            a_22=integral_image[x-1+w][y-1+h/3]
            a_32=integral_image[x-1+w][y-1+h/3+h/3]
            a_42=integral_image[x-1+w][y-1+h]
            if x-1>0:
                a_21=integral_image[x-1][y-1+h/3]
                a_31=integral_image[x-1][y-1+h/3+h/3]
                a_41=integral_image[x-1][y-1+h]
                if y-1>0:
                    a_11=integral_image[x-1][y-1]
                    a_12=integral_image[x-1+w][y-1]
            elif y-1>0:
                a_12=integral_image[x-1+w][y-1]

            return a_11-a_12-2*a_21+2*a_22+2*a_31-2*a_32-a_41+a_42
        else:
            a_11=a_12=a_13=a_21=a_31=a_41=0
            a_22=integral_image[x-1+w/2][y-1+h/2]
            a_23=integral_image[x-1+w][y-1+h/2]
            a_32=integral_image[x-1+w][y-1+h]
            a_33=integral_image[x-1+w][y-1+h]
            if x-1>0:
                a_21=integral_image[x-1][y-1+h/2]
                a_31=integral_image[x-1][y-1+h]
                if y-1>0:
                    a_11=integral_image[x-1][y-1]
                    a_12=integral_image[x-1+w/2][y-1]
                    a_13=integral_image[x-1+w][y-1]
            elif y-1>0:
                a_12=integral_image[x-1+w/2][y-1]
                a_13=integral_image[x-1+w][y-1]

            return a_11-2*a_12+a_13-2*a_21+4*a_22-2*a_23+a_31-2*a_32+a_33


    def weak_classifier(features,weights,classes):
        """
        this function is to realize the weak classifier in the paper " Robust
        features:input of haar features value array, list or n*1 ndarray
        weights:the weights of input haar features, list or n*1 array
        classes: the classes of each input feature,list or n*1 array
        return: the minimum error of the classifier, and the corresponding threshold
        """
        features=np.array(features)
        weights=np.array(weights)
        classes=np.array(classes)

        #feature_matrix combines the haar features, weights and classes together.
        feature_matrix=np.concatenate((features.reshape(features.shape[0],1),weights.reshape(weights.shape[0],1),classes.reshape(classes.shape[0],1)),1)
        # sorted the feature matrix by the haar features
        feature_matrix=feature_matrix[np.argsort(feature_matrix[:,0])]
        T_p=np.sum(feature_matrix[feature_matrix[:,2]==1][:,1])
        T_n=np.sum(feature_matrix[feature_matrix[:,2]==0][:,1])
        _error=[]
        for i in range(1,feature_matrix.shape[0]-1):
            S_p=np.sum(feature_matrix[:i,:][feature_matrix[:i,2]==1][:,1])
            S_n=np.sum(feature_matrix[:i,:][feature_matrix[:i,2]==0][:,1])
            _error.append(min(S_p+(T_n-S_n),S_n+(T_p-S_p)))

        return min(_error),feature_matrix[_error.index(min(_error)),0]

    def ada_boost(features,weights,classes,iter_num):
        """
        :param: features:input of haar features array, can be nxm np array matrix
        :param weights: the weights of input haar features
        :param classes: the classes of each input feature
        :param iter_num: total number of iterations, that is the number of classifiers
        :return: alpha,index of features and threshold for each classifier
        """

        # normalize the weights
        weights=np.array(weights)/sum(weights)
        features=np.array(features)
        classes=np.array(classes)

        feature_matrix=np.concatenate((features,weights.reshape(weights.shape[0],1),classes.reshape(classes.shape[0],1)),1)


        # loop to find iter_num classifiers
        _alpha_list,_feature_index_list,_error_classifer_list,_threshold_classifier_list=[],[],[],[]
        for i in range(0,iter_num):
            print("the model number",i)

            # loop for all the features
            _error_list,_threshold_list,_class_predict_list=[],[],[]
            for j in range(features.shape[1]):
                # sort the feature_matrix by the j feature
                #feature_matrix=feature_matrix[np.argsort(feature_matrix[:,j])]

                _threshold=ComputerVision.weak_classifier(feature_matrix[:,j],feature_matrix[:,-2],feature_matrix[:,-1])[1]
                _threshold_list.append(_threshold)
                _class_predict=[0 if x <=_threshold else 1 for x in feature_matrix[:,j]]
                _class_predict_list.append(_class_predict)

                _error=np.sum(feature_matrix[:,-2][_class_predict!=feature_matrix[:,-1]])
                _error_list.append(_error)

            _error_min=min(_error_list)
            _feature_index=_error_list.index(_error_min)
            _threshold_choose=_threshold_list[_feature_index]
            _class_choose=_class_predict_list[_feature_index]
            
            if _error_min==0:
                return [1],[_feature_index],[_threshold_choose]

            # update the weights
            _beta=_error_min/(1+_error_min)
            _alpha=np.log(1/(_beta))

            for i in range(feature_matrix[:,_feature_index].shape[0]):
                if _class_choose[i]==feature_matrix[i,-1]:
                    feature_matrix[i,-2]=feature_matrix[i,-2]*_beta
            feature_matrix[:,-2]=feature_matrix[:,-2]/sum(feature_matrix[:,-2])

            _feature_index_list.append(_feature_index)
            _error_classifer_list.append(_error_min)
            _threshold_classifier_list.append(_threshold_choose)
            _alpha_list.append(_alpha)

        return _alpha_list,_feature_index_list,_threshold_classifier_list

import os, sys

def main():
    search_window_size=[28,23]
    folder_face="/media/jianwang/Study/load/computer-vision/face/"
    folder_nonface="/media/jianwang/Study/load/computer-vision/nonface/"
    path_save='/media/jianwang/Study/load/computer-vision/result/'
    path_load="/media/jianwang/Study/load/computer-vision/testing/"

    # haar_feature_type=ComputerVision.haar_feature(search_window_size)
    # np.savetxt(path_save+'haar_feature_type.txt', np.array(haar_feature_type), delimiter=',')
    # haar_feature_value_list=[]
    #
    # for image_name in os.listdir(folder_face):
    #     print(image_name)
    #     img=cv2.imread(folder_face+image_name,cv2.IMREAD_GRAYSCALE)
    #     integral_img=ComputerVision.integral_image(img)
    #     haar_feature_value=[]
    #     for t in haar_feature_type:
    #         haar_feature_value.append(ComputerVision.feature_value(integral_img,t))
    #     haar_feature_value_list.append(haar_feature_value)
    # for image_name in os.listdir(folder_nonface):
    #     print(image_name)
    #     img=cv2.imread(folder_nonface+image_name,cv2.IMREAD_GRAYSCALE)
    #     integral_img=ComputerVision.integral_image(img)
    #     haar_feature_value=[]
    #     for t in haar_feature_type:
    #         haar_feature_value.append(ComputerVision.feature_value(integral_img,t))
    #     haar_feature_value_list.append(haar_feature_value)
    #
    # haar_feature_value_array=np.array(haar_feature_value_list)
    #
    # np.savetxt(path_save+'haar_feature_value_array.txt', np.array(haar_feature_value_array), delimiter=',')
    #
    # weights=[1.0/200]*100+[1.0/560]*280
    # classes=[1]*100+[0]*280
    # iter_num=10
    #
    # time_t=time.time()
    # alpha_weight,feature_index,threshold=ComputerVision.ada_boost(haar_feature_value_array,weights,classes,iter_num)
    #
    # np.savetxt(path_save+'alpha_weight.txt', np.array(alpha_weight), delimiter=',')
    # np.savetxt(path_save+'feature_index.txt', np.array(feature_index), delimiter=',')
    # np.savetxt(path_save+'threshold.txt', np.array(threshold), delimiter=',')
    #
    # print(time.time()-time_t)
    haar_feature_type=np.loadtxt(path_save+'haar_feature_type.txt',delimiter=',')
    alpha_weight=np.loadtxt(path_save+'alpha_weight.txt',delimiter=',')
    feature_index=np.loadtxt(path_save+'feature_index.txt',delimiter=',')
    threshold=np.loadtxt(path_save+'threshold.txt',delimiter=',')

    test_image=cv2.imread(path_load+"background_1.pgm",cv2.IMREAD_GRAYSCALE)
    #test_image_1=cv2.pyrDown(test_image)
    #test_image_2=cv2.pyrDown(test_image_1)
    print("start test")
    for i in range(test_image.shape[0]-search_window_size[0]+1):
        print(i)
        for j in range(test_image.shape[1]-search_window_size[1]+1):
            value_of_classifier=0
            sum_of_alpha_weight=0
            sub_img = test_image[i:i+search_window_size[0], j:j+search_window_size[1]]
            integral_img=ComputerVision.integral_image(sub_img)
            for l in range(len(feature_index)):
                mark=0
                haar_feature_value=ComputerVision.feature_value(integral_img,haar_feature_type[feature_index[l]])
                if haar_feature_value>threshold[l]:
                    mark+=1
            if mark>=len(feature_index):
                cv2.imwrite(path_save+"face-" + str(i)+str(j) + ".jpg", sub_img)





if __name__ == "__main__":
    main()