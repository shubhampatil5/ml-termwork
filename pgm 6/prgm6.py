"""
6. Assuming a set of documents that need to be classified, use the naïve Bayesian
Classifier model to perform this task. Built-in Java classes/API can be used to write
the program. Calculate the accuracy, precision, and recall for your data set.
"""
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn import metrics
import numpy as np

categories = ['alt.atheism', 'soc.religion.christian', 'comp.graphics', 'sci.med']
X_train = fetch_20newsgroups(subset='train', categories=categories, shuffle=True, random_state=42)
text_clf = Pipeline([('vect', CountVectorizer()),
                     ('tfidf', TfidfTransformer()),
                     ('clf', MultinomialNB())
                     ])
text_clf.fit(X_train.data, X_train.target)
X_test = fetch_20newsgroups(subset='test', categories=categories, shuffle=True, random_state=42)

predicted = text_clf.predict(X_test.data)

print(np.mean(predicted == X_test.target))

print(metrics.classification_report(X_test.target, predicted, target_names=X_test.target_names))

print(metrics.confusion_matrix(X_test.target, predicted))

"""
Output

 0.8348868175765646
                        precision    recall  f1-score   support

           alt.atheism       0.97      0.60      0.74       319
         comp.graphics       0.96      0.89      0.92       389
               sci.med       0.97      0.81      0.88       396
soc.religion.christian       0.65      0.99      0.78       398

             micro avg       0.83      0.83      0.83      1502
             macro avg       0.89      0.82      0.83      1502
          weighted avg       0.88      0.83      0.84      1502

[[192   2   6 119]
 [  2 347   4  36]
 [  2  11 322  61]
 [  2   2   1 393]]
"""
