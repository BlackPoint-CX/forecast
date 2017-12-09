#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author(s) : BlackPoint-CX
# CreateTime : 2017/12/8 12:05
from sklearn import linear_model

reg = linear_model.Ridge(alpha=0.5)

data = [[0, 0], [0, 0], [1, 1]]
pred = [0, 0.1, 1]

reg.fit(X=data,y=pred)

reg.coef_

reg.intercept_

regCV = linear_model.RidgeCV(alphas=[0.1,1.0,10])
regCV.fit(X=data,y=pred)
regCV.alpha_
regCV.coef_
regCV._estimator_type

