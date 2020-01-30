# encoding: utf-8

"""
@version: v1.0
@author: Richard
@license: Apache Licence
@contact: billions.richard@qq.com
@site:https://github.com/BillionsRichard
@software: PyCharm
@time: 2020/1/25 17:42
"""
from statsmodels.tsa.stattools import adfuller as ADF
import numpy as np

print(ADF(np.random.rand(100))) # 均匀分布

