import matplotlib.pylab as plt
import numpy as np
import time
import scipy.io

class NeuralNetwork(object):
    def eval_perceptron(self,neg_examples, pos_examples, w):
        """
        % Evaluates the perceptron using a given weight vector. Here, evaluation
        % refers to finding the data points that the perceptron incorrectly classifies.
        :param neg_examples:The num_neg_examples x 3 matrix for the examples with target 0.
        num_neg_examples is the number of examples for the negative class.
        :param pos_examples:The num_pos_examples x 3 matrix for the examples with target 1.
        num_pos_examples is the number of examples for the positive class.
        :param w:A 3-dimensional weight vector, the last element is the bias.
        :return:
        mistakes0:A vector containing the indices of the negative examples that have been
        incorrectly classified as positive.
        mistakes1:A vector containing the indices of the positive examples that have been
        incorrectly classified as negative.
        """

        num_neg_examples = neg_examples.shape[0]
        num_pos_examples = pos_examples.shape[0]
        mistakes0 = []
        mistakes1 = []
        for i in range(num_neg_examples):
            x = neg_examples[i,:]
            activation = np.dot(x,w)
            if (activation >= 0):
                mistakes0.append(i)


        for i in range(num_pos_examples):
            x = pos_examples[i,:]
            activation = np.dot(x,w)
            if (activation < 0):
                mistakes1.append(i)
        return mistakes0,mistakes1

    def update_weights(self,neg_examples, pos_examples, w_current):
        """
        Updates the weights of the perceptron for incorrectly classified points
        using the perceptron update algorithm. This function makes one sweep
        over the dataset.
        :param neg_examples: The num_neg_examples x 3 matrix for the examples with target 0.
               num_neg_examples is the number of examples for the negative class.
        :param pos_examples: The num_pos_examples x 3 matrix for the examples with target 1.
               num_pos_examples is the number of examples for the positive class.
        :param w_current:  A 3-dimensional weight vector, the last element is the bias.
        :return: w :The weight vector after one pass through the dataset using the perceptron
              learning rule.
        """

        w = np.array(w_current).reshape(np.size(w_current),)
        num_neg_examples = np.array(neg_examples).shape[0]
        num_pos_examples = np.array(pos_examples).shape[0]
        for i in range(num_neg_examples):
            this_case = neg_examples[i,:]
            activation = np.dot(this_case,w)
            if (activation >= 0):

                # update the weights,(0-1) so minus
                w=w-this_case


        for i in range(num_pos_examples):
            this_case = pos_examples[i,:]
            activation = np.dot(this_case,w)
            if (activation < 0):

                #update the weights, (1-0) so +
                w=w+this_case

        return w

    def learn_perceptron(self,neg_examples_nobias,pos_examples_nobias,w_init,w_gen_feas,iter_max=100):
        """
        Learns the weights of a perceptron for a 2-dimensional dataset and plots
        the perceptron at each iteration where an iteration is defined as one
        full pass through the data. If a generously feasible weight vector
        is provided then the visualization will also show the distance
        of the learned weight vectors to the generously feasible weight vector.
        :param neg_examples_nobias:The num_neg_examples x 2 matrix for the examples with target 0
                                   num_neg_examples is the number of examples for the negative class.
        :param pos_examples_nobias:The num_pos_examples x 2 matrix for the examples with target 1.
                                   num_pos_examples is the number of examples for the positive class.
        :param w_init:A 3-dimensional initial weight vector. The last element is the bias.
        :param w_gen_feas:A generously feasible weight vector.
        :return:w - The learned weight vector.
        """

        #bookkeeping
        num_neg_examples=neg_examples_nobias.shape[0]
        num_pos_examples=pos_examples_nobias.shape[0]
        num_err_history=[]
        w_dist_history=[]

        # we add a column of ones to the examples in order to allow us to learn bias parameters
        neg_examples=np.append(neg_examples_nobias,np.ones([num_neg_examples,1]),axis=1)
        pos_examples=np.append(pos_examples_nobias,np.ones([num_pos_examples,1]),axis=1)

        # if weight vectors have not been provided, initialize them appropriately
        if not np.size(w_init):
            w=np.random.randn(3,1)
        else:
            w=w_init

        #find the data points that the perceptron has incorrectly classified and record the number of errors
        #it makes
        iter=0
        mistake0,mistake1=self.eval_perceptron(neg_examples,pos_examples,w)
        num_errs=np.array(mistake0).shape[0]+np.array(mistake1).shape[0]
        num_err_history.append(num_errs)

        #If a generously feasible weight vector exists, record the distance
        #to it from the initial weight vector.
        if (len(w_gen_feas) != 0):
            w_dist_history.append(np.linalg.norm(w - w_gen_feas))

        #Iterate until the perceptron has correctly classified all points.
        while (num_errs > 0 and iter<iter_max):
            iter = iter + 1

            #Update the weights of the perceptron.
            w = self.update_weights(neg_examples, pos_examples, w)

            #If a generously feasible weight vector exists, record the distance
            #to it from the current weight vector.
            if (len(w_gen_feas) != 0):
                w_dist_history.append(np.linalg.norm(w - w_gen_feas))


            #Find the data points that the perceptron has incorrectly classified.
            #and record the number of errors it makes.
            mistakes0, mistakes1 = self.eval_perceptron(neg_examples,pos_examples,w)
            num_errs=np.array(mistakes0).shape[0]+np.array(mistakes1).shape[0]
            num_err_history.append(num_errs)
            print('Number of errors in iteration %d:\t%d\n'%(iter,num_errs))
            print('weights:\t', w, '\n')

        if iter == iter_max:
            print("iteration reaches the maximum numbers and stop loop")
        return w

path_load="/media/jianwang/Study/data/load/neural_network"
np.random.seed(987612345)

def main():
    #data is in dict form
    data = scipy.io.loadmat(path_load+'/dataset3.mat')
    w=NeuralNetwork().learn_perceptron(data['neg_examples_nobias'],data['pos_examples_nobias'],data['w_init'],data['w_gen_feas'])
    print(w)

if __name__=="__main__":
    main()
