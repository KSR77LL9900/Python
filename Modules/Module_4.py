#Project Title
#Detection of positive and negative statements using python and machine learning.

#TOPICS
#Introduction, Description of project, steps to follow, python libraries, arrays in python, combining teo different arrays in python, vectorization in python, code and output.

#importing
#pip install scikit-learn 
from sklearn import tree #here tree is a module, present in sklearn library
#tree is basically a decision treat classifier, which will be used to classification of a prediction method.
from sklearn.feature_extraction.text import CountVectorizer #By the term feature extraction is required to extract raw data, images, sample text from the set and CountVectorizer is something that is required to convert the sample text data in the form of vectors or matrix.

#Creating arrays
positive_set=["I'm Good"," I'm Fine"]
negative_set=["I'm feeling low","This cannot be not happen"]

#Labeling
label1=["POSITIVE"]*len(positive_set)
label2=["NEGATIVE"]*len(negative_set)
labelled=label1+label2
print(labelled)

#Now combinig two different arrays
data_set=(positive_set + negative_set)
print(data_set)

#Now Creating a new array, that contains both negative and positive set terms
sample_set=["I'm Good","I'm feeling low"]
print(positive_set,negative_set,sample_set)


#Vectorization is a techinque used in machine learning and data science to speed up computations by performing operations on entire arrays or matrices instead of individual elements. It is a fundamental concept in python programming for machine learning and is essential for efficient data processing. It allows us to process large datasets quickly and efficiently. It is implemented using libraries like sklrean, Numpy, Pandas in oython, and it is essential for building complex machine learning models.

#CountVectorizer is a technique used to transform a collection of text documents into a numerical representation that can be used by machine learning algorithms. It converts a collection of text documents into a matrix.

#fit() is a technique use to fit the CountVectorizer Object to an array and returns a scattered matrix representation. Before we can use our vectorizer, it needs to run once though all the data we have so it can build the mapping from words to indices. This is also referred to as "fitting" the victorizer.

#transform() is a technique use to transform our text data present in (sample_set) and (data_set) in the form of VECTORS.

#We can get the features names(i.e., the unique words/tokens) using the (get_feature_names_out()) method. We can convert the Scattered matrix into an array where most values are non-zero using the (toarray()).

#Writing a small program to understand the working of the above mentioned terms
def Vectorize():
    sample=["CAT DOG MOUSE","DOG COW SHEEP","HORSE COW COW DEER"]
    #NOW VECTORIZATION
    vectorizer=CountVectorizer() # assigining
    vectorizer.fit(sample) # Mapping
    sample_vectors=vectorizer.transform(sample) # Transformed
    feature_name=vectorizer.get_feature_names_out() # To showcase the types of individual unique elements
    print(feature_name) 
    print(sample_vectors.toarray())#Our vectors
#Vectorize() #To exicute the function

# The rough idea of Vectorization
#Now Vectorizatize the started program.
Vectorization=CountVectorizer()
Vectorization.fit(data_set)
data_transorm=Vectorization.transform(data_set)
sample_transform=Vectorization.transform(sample_set)
feature_name=Vectorization.get_feature_names_out()
print(data_transorm.toarray()) #(.toarray() is used to print the result in the form of an array)
print(sample_transform.toarray())
print(feature_name)

#Classification in python
#A classifier is a statistical model that tries to predict a label for a given input. In our case, the input is the text and the output is either "positive" or "negative", depending on whether the classifier thinks that the input is positive or negative. A machine learning classifier can be "trained". We give it labelled data and it tries to learn rules based on that data. Everytime it gets more data, it updates its rules slightly to account for the new information. There are many types of classifiers, but one of the simplest is called a Decision Tree.

#Decision Tree
#Decision tree learns a set of yes/no rules by building decisions iinto a tree structure. Each new input moves down the tree, While various questions are asked one by one. When the  input filters all the way to a leaf node in the tree, it acquires a label.
#Similarly to the vectorizer, we first create a classifier by using the module we imported at start. Then we call fit() on the classifier and pass in our(data_vectors) and their associated labels. Once our classifier is trained, we can call the predict() method and pass in previously unseen data, Here we pass inr (sample_tranform) which is the list of vectorized (sample_data) that the computer didn't look at during training.
classifier=tree.DecisionTreeClassifier()
classifier.fit(data_transorm, labelled)
predictions=classifier.predict(sample_transform)
print(predictions)
print(sample_set)