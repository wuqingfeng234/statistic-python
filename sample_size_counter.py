import math

from statsmodels.stats.power import NormalIndPower
import matplotlib


#Python统计包statsmodels.stats.power中，有一个NormalIndPower工具，可以用其中的solve_power函数实现。


effect_size = 0.03 / math.sqrt(0.3 * (1 - 0.3))
ztest = NormalIndPower()
num = ztest.solve_power(
    effect_size,
    alpha=0.05,
    power=0.8,
    ratio=1,
    alternative="two-sided"
)
print(num)
