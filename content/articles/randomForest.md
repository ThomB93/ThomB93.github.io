Title: Random Forest Classifier
Date: 2020-06-04
Category: Article
Tags: random forest, trees, decision trees, machine learning, ml
Slug: randomforest
Author: Thomas Brunbjerg
Summary: Describes the Random Forest Classifier and how you can use it with python
report: article

- Random Forests are built from decision trees.
- Combines the simplicity of decision trees with some flexibility to achieve a better accuracy.

**How to create a Random Forest:**

1. Create a bootstrapped dataset
    * Randomly select samples from the original dataset
        * You may pick the same sample more than once
2. Create a decision tree using the bootstrapped dataset
    * At each step, select a random number of columns (variables)
        * E.g. we select 2 out of 4 columns to use.
        * A good starting point is the square of the number of variables
    * Select the best column to use as the root node (first step)
    * Select 2 new random columns from the remaining as candidates
3. Repeat step 2 so as to create multiple decision trees from a bootstrapped dataset
4. The resulting trees will look different from one another. The variety of trees is what makes Random Forest effective.
5. Run the out-of-bag dataset through all the trees.
6. Accuracy can be measured by the proportion of out-of-bag samples that were correctly classified.
7. You can now create Random Forest Trees using a different number of columns at each step, and check which one has the best accuracy. 
8. To predict from new data, run the data through all the trees and see which category got the most votes.

[![small]({static}/img/article/randomforest_01.png)]({static}/img/article/randomforest_01.png)

**Keywords:**

* Bagging: Bootstrapping the data using the aggregate to make a decision
* Out-of-bag Dataset: The data that is left over after bootstrapping the dataset
* Out-of-bag Error: The proportion of out-of-bag samples that were incorrectly classified.

**How to deal with missing data?**

Data can be missing either in the original dataset (training data), or in the new data you want to categorize.

1. Make an initial guess based on the most common values in the column.
2. Refine your guesses by determining which samples (rows) are similar
    * Build a Random Forest
    * Run all data through all the trees
        * If two or more samples end up in the same leaf node, that means they are similar.
        * Use a proximity matrix to keep track of the similar samples. Each numbered column/row corresponds to a sample. A value of 1 says that they are similar.
        * Add to the proximity matrix for each tree the data is run through.
        * If the same samples are similar in other trees, increment the value by 1 for each tree.
        * After all the trees have been run through, divide each value by the total number of trees.
        * Use the proximity values for the sample with missing data (4) to make a better guess.

[![tiny]({static}/img/article/randomforest_04.png)]({static}/img/article/randomforest_04.png)
[![tiny]({static}/img/article/randomforest_03.png)]({static}/img/article/randomforest_03.png)
[![tiny]({static}/img/article/randomforest_02.png)]({static}/img/article/randomforest_02.png)

**How to make a better guess using proximity matrix?**

1. Find the weighted frequency that each other value in the column have
    * Frequency = (Number of time value occurs) / (Total number of values in column)
    * Weight = (Proximity of the value)  / (All proximities)
        * Proximity of the value: The number given in the proximity matrix for that value. E.g. The third column in sample 2 will have a proximity value of 0.1. If more samples have the same value, sum the proximites.
        * All proximities: Sum all the proximity values for the sample that we are making a guess for.
2. Use the value that had the highest weighted frequency as the new guess.

**How to make a better guess for continuous data using proximity matrix?**

1. Use the weighted average as the refined guess.
    * Weighted average = Value of the column * Weight (same as previously described)
    * Take the weighted average for each value in the column and sum them.
    * Use the result of the equation as the new refined guess.

**Repeat** each of these steps for making a more refined guess, by building a new Random Forest and running the data through them and making a proximity matrix. Do this until there is no change made in the guess.

**How to make a guess for missing data in a new sample?**

1. Create several copies of the sample - each one with a different category.
2. Use the same iterative method as for the original samples for each of these new samples. You now have a guess for the missing data in each sample.
3. Check which one of the samples is being correctly labeled the most times with the new guess. 
4. The sample which is being correctly labeled the most times is the winner and the category for the new sample can be determined.

[![tiny]({static}/img/article/randomforest_06.png)]({static}/img/article/randomforest_06.png)
[![tiny]({static}/img/article/randomforest_05.png)]({static}/img/article/randomforest_05.png)

**How to measure distance using proximity matrix?**

1. Distance = 1 - proximity values.
    * For each proximity value, subtract it from 1 and input the new value into the matrix.
    * The higher the number, the more far away the samples are.
    * From the matrix we can create an MDS plot (Multidimensional Scaling) that better shows the distances.

**Fact:** If we can make a tree from some data, we can show how the samples are related using an MDS plot. 

**How to use a Random Forest Classifier in python?**

```python
#Import Random Forest Model
from sklearn.ensemble import RandomForestClassifier

#Create a Gaussian Classifier
clf=RandomForestClassifier(n_estimators=100)

#Train the model using the training sets
y_pred =clf.predict(X_test)
clf.fit(X_train,y_train)

y_pred=clf.predict(X_test)

#Import scikit-learn metrics module for accuracy calculation
from sklearn import metrics
# Model Accuracy, how often is the classifier correct?
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
#Use the model to make predictions on new data
clf.predict([[3, 5, 4, 2]])
```
**Important Hyperparameters:**

* n_estimators: The total number of trees to build.
* Criterion: Can be "gini" or “entropy”. Determines what function to use when making splits in the tree.
* Max_Depth: The maximum number of nodes from the root to the leaf nodes.
* Max Features: How to determine the best number of features when building the trees. 
