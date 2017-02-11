
"""
Created on Fri Aug 26 00:03:47 2016

@author: jianwang

research for dynamics of limit order books(lob)

"""


# import related package
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy as sp
from sklearn import linear_model
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn import svm
from sklearn import tree
from sklearn import ensemble
import time
import matplotlib.pyplot as plt
import random
from sklearn.metrics import (precision_score, recall_score,
                                     f1_score)
from sklearn.cross_validation import train_test_split

class LimitOrderBook(object):

    def build_y(self,ask_low,bid_high,no_arbi,option):
        """
        # this function used to build the y
        # ask_low as 1 bad high as -1 and no arbitrage as 0
        # option=1 return ask low, option =2 return bid high, option =3 return no arbi, option =4 return total(ask_low=1,
        # bid_high =-1 and no arbi =0)
        :param ask_low: ask low case, 0 for no ask low, 1 for ask low,type list
        :param bid_high: bid_high case, 0 for no bid high, 1 for bid high,type list
        :param no_arbi: no arbi case, 0 for arbitrage, 1 for no arbi,type list
        :return the ask low, bid high , no arbi and three class result based on option
        """

        if (option==1):
            return ask_low
        elif option==2:
            return bid_high
        elif option==3:
            return no_arbi
        elif option==4:
            return ask_low-bid_high
        else:
            print("option should be 1,2,3,4")

    def random_choice(self,num, key):
        """
        random generate a subset of num, used to choose random subset permutation of a given list
        :param num: is the original list to generate the random subset,type list
        :param key: the numbers of subset that we need to choose, type int
        :return: the new num list, type list
        """
        temp=np.random.choice(num,size=key,replace=False)
        temp_sort=sorted(temp)
        for i in range(len(temp)):
            num[temp_sort[i]]=temp[i]
        return num

    def random_split(self,feature_array_list,response_array_list,ticker_ind,size,test_size):
        """
        used to random split the data set to training adn testing set.
        :param feature_array_list:
        :param response_array_list:
        :param ticker_ind:
        :param size:
        :param test_size: the size ratio of testing sample
        :return: total_array,train_x, train_y,test_x,test_y
        """
        total_array=np.concatenate((feature_array_list[ticker_ind],response_array_list[ticker_ind]),axis=1)[:size,:]

        #split the data to train and test data set
        train_x, test_x, train_y, test_y =train_test_split(\
        total_array[:,:134],total_array[:,134], test_size=0.1, random_state=42)

        # the y data need to reshape to size (n,) not (n,1)
        test_y=test_y.reshape(len(test_y),)
        train_y=train_y.reshape(len(train_y),)
        return total_array,train_x,train_y,test_x,test_y

    def time_series_split(self,feature_array_list,response_array_list,ticker_ind,size,random_ratio,train_split_ratio=0.9):
        """
        split the data in time series method to build the training and testing set
        :param feature_array_list: array list of features
        :param response_array_list: array list of responses
        :param ticker_ind: which security that we need to choose
        :param size: sample size to build the train and test set
        :param random_ratio: the ratio for choosing the random subset
        :param train_split_ratio: the ratio  training data sample to the total data sample
        :return: total_array, train_x, train_y,test_x,test_y
        """
        total_array=np.concatenate((feature_array_list[ticker_ind],response_array_list[ticker_ind]),axis=1)[:size,:]

        total_array=total_array[self.random_choice(list(range(size)),int(size*random_ratio)),:]

        train_num_index=int(len(total_array)*train_split_ratio)

        print("total array shape:",total_array.shape)

        #split the data to train and test data set
        train_x=total_array[:train_num_index,:134]
        test_x=total_array[train_num_index:,:134]
        train_y=total_array[:train_num_index,134]
        test_y=total_array[train_num_index:,134]


        # the y data need to reshape to size (n,) not (n,1)
        test_y=test_y.reshape(len(test_y),)
        train_y=train_y.reshape(len(train_y),)
        return total_array,train_x,train_y,test_x,test_y

    def scale_data(self,train_x,test_x):
        """
        can use the processing.scale function to scale the data
        :param train_x:traing features data,type numpy
        :param test_x:testing features data,type numpy
        :return: train_x_scale,test_x_scale
        """

        from sklearn import preprocessing
        # note that we need to transfer the data type to float
        # remark: should use data_test=data_test.astype('float'),very important !!!!
        # use scale for zero mean and one std
        scaler = preprocessing.StandardScaler().fit(train_x)


        train_x_scale=scaler.transform(train_x)
        test_x_scale=scaler.transform(test_x)
        return train_x_scale,test_x_scale

    def predict_threshold(self,predict_proba, threshold):
        """
        return the logit result based on the probability and threshold
        :param predict_proba:
        :param threshold:
        :return: the predict result
        """
        res=[]
        for i in range(len(predict_proba)):
            res.append(int(predict_proba[i][1]>threshold))
        return res

    def logit_fit(self,C,penalty,tol,random_state,train_x,train_y,test_x,test_y):

        """
        logistic regression fit model, can use l1 or l2 penalty
        :param C:
        :param penalty:
        :param tol:
        :param random_state:
        :param train_x:
        :param train_y:
        :return:  time_logistic,predict_y_logistic,precision,recall,f1
        """

        time_logit_train=time.time()
        clf = linear_model.LogisticRegression(C=C, penalty=penalty, tol=tol,random_state= random_state)
        clf.fit(train_x,train_y)
        time_logit_train=time.time()-time_logit_train


        # test the training error
        predict_y_logistic =np.array(clf.predict(train_x))
        accuracy_train=sum(predict_y_logistic==train_y)/len(train_y)



        time_logit_test=time.time()
        predict_y_test_proba =np.array(clf.predict_proba(test_x))

        predict_y_test=self.predict_threshold(predict_y_test_proba,0.5)
        time_logit_test=time.time()-time_logit_test

        accuracy_test=sum(predict_y_test==test_y)/len(test_y)
        precision= precision_score(predict_y_test,test_y)
        recall = recall_score(predict_y_test,test_y)
        f1=f1_score(predict_y_test,test_y)

        return predict_y_test,time_logit_train,time_logit_test,accuracy_train,accuracy_test,precision,recall,f1

    def svm_fit(self,train_x,train_y,test_x,test_y,C=1.0,kernel='poly',degree=2,max_iter=1000,shrinking=True, tol=0.001, verbose=False):

        svm_time_train=time.time()
        clf = svm.SVC(C=C,kernel=kernel,degree=degree,max_iter=max_iter,shrinking=shrinking, tol=tol, verbose=verbose)

        clf.fit(train_x,train_y)

        svm_time_train=time.time()-svm_time_train

        #testing
        # test the training error
        predict_y =np.array(clf.predict(train_x))
        accuracy_train=sum(predict_y==train_y)/len(train_y)

        predict_y_test=np.array(clf.predict(test_x))


        # test the score for the train data

        accuracy_test=sum(predict_y_test==test_y)/len(test_y)
        precision= precision_score(predict_y_test,test_y)
        recall = recall_score(predict_y_test,test_y)
        f1=f1_score(predict_y_test,test_y)
        return predict_y_test,time_logit_train,time_logit_test,accuracy_train,accuracy_test,precision,recall,f1

    def decision_tree_fit(self,train_x,train_y,test_x,test_y,max_depth=10,random_state= 987612345):

            time_train_dt=time.time()
            clf = tree.DecisionTreeClassifier(max_depth=max_depth,random_state= random_state)

            clf.fit(train_x,train_y)

            time_train_dt=time.time()-time_train_dt

            #testing
            # test the training error
            time_test_dt=time.time()
            predict_y =np.array(clf.predict(train_x))
            time_test_dt=time.time()-time_test_dt

            accuracy_train=sum(predict_y==train_y)/len(train_y)

            predict_y_test=np.array(clf.predict(test_x))


            # test the score for the train data

            accuracy_test=sum(predict_y_test==test_y)/len(test_y)
            precision= precision_score(predict_y_test,test_y)
            recall = recall_score(predict_y_test,test_y)
            f1=f1_score(predict_y_test,test_y)
            return predict_y_test,time_train_dt,time_test_dt,accuracy_train,accuracy_test,precision,recall,f1

    def adaboosting_fit(self,train_x,train_y,test_x,test_y,max_depth=10,n_estimators=100,random_state= 987612345):

            time_train_ada=time.time()
            clf =AdaBoostClassifier(base_estimator=DecisionTreeClassifier(max_depth=max_depth),n_estimators=n_estimators,random_state= random_state)

            clf.fit(train_x,train_y)

            time_train_ada=time.time()-time_train_ada

            #testing
            # test the training error
            predict_y =np.array(clf.predict(train_x))
            accuracy_train=sum(predict_y==train_y)/len(train_y)


            time_test_ada=time.time()
            predict_y_test=np.array(clf.predict(test_x))
            time_test_ada=time.time()- time_test_ada



            # test the score for the train data

            accuracy_test=sum(predict_y_test==test_y)/len(test_y)
            precision= precision_score(predict_y_test,test_y)
            recall = recall_score(predict_y_test,test_y)
            f1=f1_score(predict_y_test,test_y)
            return predict_y_test,time_train_ada,time_test_ada,accuracy_train,accuracy_test,precision,recall,f1

    def plot_confusion_matrix(self,predict_y,test_y,title='Confusion matrix', cmap=plt.cm.Blues,):
        from sklearn.metrics import confusion_matrix
        cm = confusion_matrix(test_y, predict_y)
        np.set_printoptions(precision=2)
        plt.imshow(cm, interpolation='nearest', cmap=cmap)
        plt.title(title)
        plt.colorbar()
        tick_marks = np.arange(2)
        plt.xticks(tick_marks, [0,1])
        plt.yticks(tick_marks, [0,1])
        plt.tight_layout()
        plt.ylabel('True label')
        plt.xlabel('Predicted label')

        plt.show()



if __name__ == "__main__":
    #Set default parameters
    ticker_list=["AAPL","AMZN","GOOG","INTC","MSFT"]
    # start at 10am and end at 3:30 PM
    start_ind=10*3600
    end_ind=15.5*3600
    data_order_list=[]
    data_mess_list=[]
    time_index_list=[]
    path_save='/media/jianwang/Study/Research/order_book/'
    path_load="/media/jianwang/Study/Research/order_book/"

    ## set random seed to produce the same results

    np.random.seed(987612345)

    #read the stock ticker,totally 5 dataset

    for i in range(len(ticker_list)):
            #get the path for the csv files
            # name_order is for the order book and name_mess for the message book
            name_order='_2012-06-21_34200000_57600000_orderbook_10.csv'
            name_mess='_2012-06-21_34200000_57600000_message_10.csv'
            # calculate the cputime for reading the data
            t=time.time()
            # header =-1 means that the first line is not the header, otherwise, the first line will be header
            # data_order is for order book and data mess is for message book
            data_order_list.append(np.array(pd.read_csv(path_load+ticker_list[i]+name_order,header=-1),dtype="float64"))
            data_mess_list.append(np.array(pd.read_csv(path_load+ticker_list[i]+name_mess,header=-1),dtype="float64"))
            print("Time for importing the "+ticker_list[i]+" data is:",time.time()-t)
            print("The shape of the order data is: ",data_order_list[i].shape, " of message data is: ", data_mess_list[i].shape)
            # get the time index
            time_index_list.append(data_mess_list[i][:,0])

    # print the sample of data
    print("Check the original data:")

    for i in range(len(ticker_list)):
        print()
        print("The first five sampe of "+ticker_list[i]+" is: ",data_order_list[i][:3])

    # load the features
    t=time.time()
    feature_array_list=[]
    for ticker_ind in range(len(ticker_list)):
        feature_array_list.append(np.array(pd.read_csv(path_save+ticker_list[ticker_ind]+'_feature_array.txt',\
                                                       sep=' ',header=-1)))
    print(time.time()-t)

    # load the response data

    response_list=[]
    for ticker_ind in range(len(ticker_list)):
        response_list.append((np.array(pd.read_csv(path_save+ticker_list[ticker_ind]+'_response.txt',header=-1))))


    # print the shape of the response,note it is the total response
    print("The shape of the total response is:\n")

    for ticker_ind in range(len(ticker_list)):
        print(response_list[ticker_ind].shape)

    # need to get the response from 10 to 15:30, the shape of the response and the feature array should be equal
    response_reduced_list=[]
    for ticker_ind in range(len(ticker_list)):
        first_ind = np.where(time_index_list[ticker_ind]>=start_ind)[0][0]
        last_ind=np.where(time_index_list[ticker_ind]<=end_ind)[0][-1]
        response_reduced_list.append(response_list[ticker_ind][first_ind:last_ind+1])

    print("The shape of the reduced response is:\n")

    # print the shape of reduced response, response reduced is used for testing and training the model
    for ticker_ind in range(len(ticker_list)):
        print(response_reduced_list[ticker_ind].shape)

    # split data in time series way
    total_array,train_x,train_y,test_x,test_y=LimitOrderBook().time_series_split(feature_array_list,
                response_reduced_list,ticker_ind=0,size=100000,random_ratio=0.5,train_split_ratio=0.9)

    # scale the data
    train_x_scale,test_x_scale=LimitOrderBook().scale_data(train_x,test_x)

    #fit the logit model
    predict_y_test_logit,time_logit_train,time_logit_test,accuracy_train,accuracy_test,precision_logit,recall_logit,f1_logit=\
        LimitOrderBook().logit_fit(1,penalty="l1",tol=10**(-6),random_state=987612345,train_x=train_x_scale,train_y=train_y,\
                                   test_x=test_x_scale,test_y=test_y)

    print("time_train:",time_logit_train,"time_test:",time_logit_test,"accuracy_train:",accuracy_train,"accuracy_test:",accuracy_test,\
          "precision:",precision_logit,"recall:",recall_logit,"f1:",f1_logit)

    # fit the svm model
    predict_y_test_svm,time_train_svm,time_test_svm,accuracy_train_svm,accuracy_test_svm,precision_svm,recall_svm,f1_svm=\
    LimitOrderBook().svm(train_x=train_x_scale,train_y=train_y,\
                               test_x=test_x_scale,test_y=test_y,C=1.0,kernel='poly',degree=2,max_iter=5000,shrinking=True, tol=0.001, verbose=False)

    print("time_train:",time_train_svm,"time_test:",time_test_svm,"accuracy_train:",accuracy_train_svm,"accuracy_test:",accuracy_test_svm,\
          "precision:",precision_svm,"recall:",recall_svm,"f1:",f1_svm)

    # fit the decision tree model
    predict_y_test_dt,time_train_dt,time_test_dt,accuracy_train_dt,accuracy_test_dt,precision_dt,recall_dt,f1_dt=\
        LimitOrderBook().decision_tree(train_x=train_x_scale,train_y=train_y,\
                                   test_x=test_x_scale,test_y=test_y,max_depth=10,random_state= 987612345)

    print("time_train:",time_train_dt,"time_test:",time_test_dt,"accuracy_train:",accuracy_train_dt,"accuracy_test:",accuracy_test_dt,\
          "precision:",precision_dt,"recall:",recall_dt,"f1:",f1_dt)

    # fit the adaboosting model
    predict_y_test_ada,time_train_ada,time_test_ada,accuracy_train_ada,accuracy_test_ada,precision_ada,recall_ada,f1_ada=\
        LimitOrderBook().adaboosting_fit(train_x=train_x_scale,train_y=train_y,\
                                   test_x=test_x_scale,test_y=test_y,max_depth=10,n_estimators=100,random_state= 987612345)

    print("time_train:",time_train_ada,"time_test:",time_test_ada,"accuracy_train:",accuracy_train_ada,"accuracy_test:",accuracy_test_ada,\
          "precision:",precision_ada,"recall:",recall_ada,"f1:",f1_ada)

    # plot confusion matrix
    LimitOrderBook().plot_confusion_matrix(predict_y_test_ada,test_y)

    #------------------------------------------------------------------------------------------------------------------
    #multi-class
    #------------------------------------------------------------------------------------------------------------------

    #load arbitrage data for multi-class
    ask_low_time_list=[]
    bid_high_time_list=[]
    no_arbi_time_list=[]
    time_list=[1,5,10,15,20]
    t = time.time()
    for ticker_ind in range(5):
        ask_low_time_list.append([])
        bid_high_time_list.append([])
        no_arbi_time_list.append([])
        for time_ind in range(len(time_list)):
            ask_low_time_list[ticker_ind].append(
                np.array(pd.read_csv(path_save+ticker_list[ticker_ind]+'_ask_low_time_'+str(time_list[time_ind])+'.txt',header=-1)))
            bid_high_time_list[ticker_ind].append(
                np.array(pd.read_csv(path_save+ticker_list[ticker_ind]+'_bid_high_time_'+str(time_list[time_ind])+'.txt',header=-1)))
            no_arbi_time_list[ticker_ind].append(
                np.array(pd.read_csv(path_save+ticker_list[ticker_ind]+'_no_arbi_time_'+str(time_list[time_ind])+'.txt',header=-1)))

    print(time.time()-t)

    # load the response data

    for ticker_ind in range(len(ticker_list)):
        response_list.append((np.array(pd.read_csv(path_save+ticker_list[ticker_ind]+'_multiresponse.txt',header=-1))))

        ## print the shape of the response
    ## note it is the total response
    print("The shape of the total response is:\n")

    for ticker_ind in range(len(ticker_list)):
        print(response_list[ticker_ind].shape)

    # need to get the response from 10 to 15:30
    # the shape of the response and the feature array should be equal
    response_reduced_list=[]
    for ticker_ind in range(len(ticker_list)):
        first_ind = np.where(time_index_list[ticker_ind]>=start_ind)[0][0]
        last_ind=np.where(time_index_list[ticker_ind]<=end_ind)[0][-1]
        response_reduced_list.append(response_list[ticker_ind][first_ind:last_ind+1])

    print("The shape of the reduced response is:\n")

    ## print the shape of reduced response
    ## response reduced is used for testing and training the model
    for ticker_ind in range(len(ticker_list)):
        print(response_reduced_list[ticker_ind].shape)



