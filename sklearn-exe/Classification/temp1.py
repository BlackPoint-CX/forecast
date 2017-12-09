#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author(s) : BlackPoint-CX
# CreateTime : 2017/12/8 11:24


from sklearn import linear_model

reg = linear_model.LinearRegression()

reg.fit([[0, 0], [1, 1], [2, 2]], [0, 1, 2])

reg.coef_




