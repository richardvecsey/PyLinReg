# -*- coding: utf-8 -*-
"""
Test file for 'PyLinReg' project
==============================================================================
MIT License
Copyright (c) 2021 Richárd Ádám Vécsey Dr.
See accompanying file LICENSE.
"""

# constants
__author__ = 'Richárd Ádám Vécsey Dr.'
__copyright__ = "Copyright 2021, PyLinReg"
__credits__ = ['Richárd Ádám Vécsey Dr.']
__license__ = 'MIT'
__version__ = '1.0.0'
__status__ = 'Alpha'


# import
import pylinreg



# print help
help(pylinreg)



# create dummy data for 'targets'
# dependent variable
# eg: height in meter
dummy_targets = [52.21, 53.12, 54.48, 55.84, 57.20, 58.57, 59.93, 61.29, 63.11,
                 64.47, 66.28, 68.10, 69.92, 72.19, 74.46]

# create dummy data for 'predictors'
# independent variable
# eg: mass in kg
dummy_predictors = [1.47, 1.50, 1.52, 1.55, 1.57, 1.60, 1.63, 1.65, 1.68, 1.70, 
                    1.73, 1.75, 1.78, 1.80, 1.83]

# create list with dummy pairs for Example 2
dummy_pairs = []
for pair in zip(dummy_predictors, dummy_targets):
    dummy_pairs.append([pair[0], pair[1]])



# Example 1
print('Example 1')
# instantiate the linear regression model
Model = pylinreg.LinearModel(dummy_predictors, dummy_targets)
# get slope and intercept values
print('{:>10}: {:8.4f}'.format('slope', Model.slope))
print('{:>10}: {:8.4f}'.format('intercept', Model.intercept))

# make prediction for 1.92 m height
predictor = 1.92
prediction = Model.make_prediction(predictor)
print('\n{:>10}: {:8.4f}'.format('prediction', prediction))



# Example 2
print('\nExample 2')
# create the linear regression model from pairs
Model2 = pylinreg.LinearModel.frompairs(dummy_pairs)
# get slope and intercept values
print('{:>10}: {:8.4f}'.format('slope', Model2.slope))
print('{:>10}: {:8.4f}'.format('intercept', Model2.intercept))

# make prediction for 1.92 m height
predictor = 1.92
prediction = Model2.make_prediction(predictor)
print('\n{:>10}: {:8.4f}'.format('prediction', prediction))



# Example 3
print('\nExample 3')
# reset the variables of Model2 and set them again with verbose mode
Model2.reset()
Model2.add_predictors(dummy_predictors, verbose=True)
Model2.add_targets(dummy_targets, verbose=True)
# make the calculations again
Model2.recalculate()
# make prediction for 1.92 m height
predictor = 1.92
prediction = Model2.make_prediction(predictor)
print('\n{:>10}: {:8.4f}'.format('prediction', prediction))



# Example 4
print('\nExample 4')
# get details of variables
Model2.details



# Example 5
print('\nExample 5')
# working with NaN or None values
# create dummy data for 'targets'
# dependent variable
# eg: height in meter
dummy_targets_3 = [62.07, 52.21, 53.12, 54.48, 55.84, 57.20, 58.57, 59.93,
                   61.29, 63.11, 64.47, 66.28, 68.10, 69.92, 72.19, 74.46]

# create dummy data for 'predictors'
# independent variable
# eg: mass in kg
dummy_predictors_3 = [None, 1.47, 1.50, 1.52, 1.55, 1.57, 1.60, 1.63, 1.65,
                      1.68, 1.70, 1.73, 1.75, 1.78, 1.80, 1.83]

Model3 = pylinreg.LinearModel(dummy_predictors_3, dummy_targets_3)
# get slope and intercept values
Model3.details


"""
Source:
Example comes from the 'Simple linear regression' Wikipedia article:
https://en.wikipedia.org/wiki/Simple_linear_regression
"""