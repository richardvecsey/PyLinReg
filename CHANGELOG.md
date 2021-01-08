# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
## [1.0.0] - 2021-01-03

### Added
- LinearModel class calculates the slope and intercept values based on predictors and targets values
- Paired values can be used to create linear regression model `linear_model.LinearModel.frompairs()`
- None values of predictors or targets can be replaced with the mean value. Default parameter: *True* as enabled
- Making prediction manually after calculation based on one predictor value `LinearModel.make_prediction()`
- Variables of model can be reset `LinearModel.reset()`
- Possibility of adding predictor values after instantiation `LinearModel.add_predictors()`
- Possibility of adding target values after instantiation `LinearModel.add_targets()`
- Linear regression calculation can be calcualte after instantiation `LinearModel.recalculate()`
- Check if it used as module or script and throw an error when using as script
- @property decorator is used to get values of variables easily
- Add verbose mode to the followng function: add_predictors, add_targets, reset, Default parameter: *False* as disabled
- Start using CHANGELOG as CHANGELOG.md
- Start using README as README.md
- Start using REQUIREMENTS as requirements.txt
- Set license as MIT