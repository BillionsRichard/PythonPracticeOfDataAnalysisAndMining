# -*- coding: utf-8 -*-
# 真实位置：sklearn.metrics._classification.confusion_matrix
# 受保护成员函数
# 导入混淆矩阵函数
import matplotlib.pyplot as plt  # 导入作图库
# from sklearn.metrics import confusion_matrix # pycharm 无法识别，但是可以运行。
# 实际位置如下
from sklearn.metrics._classification import confusion_matrix


def cm_plot(y, yp):
    # print('y', y)
    # print("yp", yp)
    """
        By definition a confusion matrix :math:`C` is such that :math:`C_{i, j}`
    is equal to the number of observations known to be in group :math:`i` and
    predicted to be in group :math:`j`.

    Thus in binary classification, the count of true negatives is
    :math:`C_{0,0}`, false negatives is :math:`C_{1,0}`, true positives is
    :math:`C_{1,1}` and false positives is :math:`C_{0,1}`.
    
    |-------------------> predicted label
    |C[0][0]  C[0][1]
    |
    |C[1][0]  C[1][1]
    |
    |
   \|/
   
    true Label
     
    """
    cm = confusion_matrix(y, yp)  # 混淆矩阵
    print(cm, type(cm), cm.T)

    # 画混淆矩阵图，配色风格使用cm.Greens，更多风格请参考官网。
    """
    The origin is set at the upper left hand corner and rows (first
    dimension of the array) are displayed horizontally.  The aspect
    ...
    """
    display_cm = cm.T
    plt.matshow(display_cm, cmap=plt.cm.Greens)
    plt.colorbar()  # 颜色标签

    for x in range(len(display_cm)):  # 数据标签
        for y in range(len(display_cm)):
            plt.annotate(
                display_cm[x, y],
                xy=(x, y),
                horizontalalignment="center",
                verticalalignment="center",
            )

    plt.xlabel("Predicted label")  # 坐标轴标签
    plt.ylabel("True label")  # 坐标轴标签
    return plt


if __name__ == '__main__':
    y_true = [1, 0, 1, 0, 1, 1, 1, 0, 1, 1]
    y_pred = [0, 0, 1, 1, 1, 0, 0, 1, 1, 1]
    cm_plot(y_true, y_pred).show()
