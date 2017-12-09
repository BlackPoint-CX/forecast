#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author(s) : BlackPoint-CX
# CreateTime : 2017/12/8 14:14
import numpy as np

from sklearn.preprocessing import PolynomialFeatures
X = np.arange(6).reshape(3, 2)
poly = PolynomialFeatures(degree=2)
poly.fit_transform(X)
