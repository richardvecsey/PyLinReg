[![Generic badge](https://img.shields.io/badge/Version-1.0.0-blue)](https://shields.io/)
[![Generic badge](https://img.shields.io/badge/Python-%3E%3D3.6-blue)](https://shields.io/)

# PyLinReg

Linear Regression Model with only Python Standard Library based on
Ordinary Least Squares (OLS) Method

## Quickstart

### Requirements

This module use Python Standard Library only. Python version should be higher than *3.6*

### Install

```
pip install pylinreg
```


### How to Use

This code works as module not a script.

#### Import

```
import pylinreg
```

#### Create linear regression model object

```
predictors = [1, 2, 3, 4, 5]
targets = [15, 25, 35, 45, 55]
Model = pylinreg.LinearModel(predictors, targets)
```

#### Get values of slope and intercept

```
slope = Model.slope
intercept = Model.intercept
```

#### Get prediction

```
predictor = 6
prediction = Model.make_prediction(predictor)
```
The prediction is *65*.

#### Help

```
help(pylinreg)
```

### Examples

Examples are available in the [test.py](https://github.com/richardvecsey/PyLinReg/blob/main/test.py)

## License

The content of this repository is licensed under *MIT license*. For more details, check [LICENSE](https://github.com/richardvecsey/PyLinReg/blob/main/LICENSE)
