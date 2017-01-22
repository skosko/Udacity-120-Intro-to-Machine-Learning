#!/usr/bin/python 

""" 
    Skeleton code for k-means clustering mini-project.
"""


import pickle
import numpy
import matplotlib.pyplot as plt
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

def Draw(pred, features, poi, mark_poi=False, name="image.png", f1_name="feature 1", f2_name="feature 2"):
    """ some plotting code designed to help you visualize your clusters """

    ### plot each cluster with a different color--add more colors for
    ### drawing more than five clusters
    colors = ["b", "c", "k", "m", "g"]
    for ii, pp in enumerate(pred):
        plt.scatter(features[ii][0], features[ii][1], color = colors[pred[ii]])

    ### if you like, place red stars over points that are POIs (just for funsies)
    if mark_poi:
        for ii, pp in enumerate(pred):
            if poi[ii]:
                plt.scatter(features[ii][0], features[ii][1], color="r", marker="*")
    plt.xlabel(f1_name)
    plt.ylabel(f2_name)
    plt.savefig(name)
    plt.show()

### load in the dict of dicts containing all the data on each person in the dataset
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )

### there's an outlier--remove it! 
data_dict.pop("TOTAL", 0)


### Quiz: Feature scaling using MinMaxScaler

## Salary Range
salary = []

for users in data_dict:
    value = data_dict[users]["salary"]
    if value == 'NaN':
        continue
    salary.append(float(value))

min_salary = min(salary)
max_salary = max(salary)

## Excercised Stock Options Range
eso = []

for users in data_dict:
    value = data_dict[users]["exercised_stock_options"]
    if value == 'NaN':
        continue
    eso.append(float(value))

min_eso = min(eso)
max_eso = max(eso)

## Scaling of the Features (to get scaled values for Salary of 200.000 & ESO of 1.000.000)
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()

salaries = numpy.array([[float(min_salary)], [200000.0], [float(max_salary)]])
salaries_scaled = scaler.fit_transform(salaries)
print salaries_scaled

ex_stock_options = numpy.array([[float(min_eso)], [1000000.0], [float(max_eso)]])
ex_stock_options_scaled = scaler.fit_transform(ex_stock_options)
print ex_stock_options_scaled

