# 拉格朗日插值代码
import pandas as pd  # 导入数据分析库Pandas
from scipy.interpolate import lagrange  # 导入拉格朗日插值函数

inputfile = "../data/catering_sale.xls"  # 销量数据路径
outputfile = "../tmp/sales.xls"  # 输出数据路径

data = pd.read_excel(inputfile)  # 读入数据
data[u"销量"][(data[u"销量"] < 400) | (data[u"销量"] > 5000)] = None  # 过滤异常值，将其变为空值


def ployinterp_column(s, n, k=5):
    """# 自定义列向量插值函数
    
    :param s:  s为列向量
    :param n: n为被插值的位置
    :param k: k为取前后的数据个数，默认为5
    :return:
    """
    y = s[list(range(n - k, n)) + list(range(n + 1, n + 1 + k))]  # 取数
    y = y[y.notnull()]  # 剔除空值
    """
    def lagrange(x, w):
    Return a Lagrange interpolating polynomial.

    Given two 1-D arrays `x` and `w,` returns the Lagrange interpolating
    polynomial through the points ``(x, w)``.

    Warning: This implementation is numerically unstable. Do not expect to
    be able to use more than about 20 points even if they are chosen optimally.

    Parameters
    ----------
    x : array_like
        `x` represents the x-coordinates of a set of datapoints.
    w : array_like
        `w` represents the y-coordinates of a set of datapoints, i.e. f(`x`)."""
    return lagrange(y.index, list(y))(n)  # 插值并返回插值结果


# 逐个元素判断是否需要插值
for i in data.columns:
    for j in range(len(data)):
        if (data[i].isnull())[j]:  # 如果为空即插值。
            data[i][j] = ployinterp_column(data[i], j)

data.to_excel(outputfile)  # 输出结果，写入文件
