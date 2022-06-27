# 卡方分布——画图
# 导入需要的包
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import matplotlib.style as style
from IPython.core.display import HTML

# PLOTTING CONFIG 绘图配置
# %matplotlib inline
style.use('fivethirtyeight')
plt.rcParams['figure.figsize'] = (20, 7)
plt.figure(dpi=100)

# 探究自由度K大小对结果的影响：
plt.figure(dpi=100)

# PDF    K=1
plt.plot(np.linspace(0, 15, 100), stats.chi2.pdf(np.linspace(0, 15, 100), df=1))
plt.fill_between(np.linspace(0, 15, 100), stats.chi2.pdf(np.linspace(0, 15, 100), df=1), alpha=0.15)

# PDF    K=3
plt.plot(np.linspace(0, 15, 100), stats.chi2.pdf(np.linspace(0, 15, 100), df=3))
plt.fill_between(np.linspace(0, 15, 100), stats.chi2.pdf(np.linspace(0, 15, 100), df=3), alpha=0.15)

# PDF    K=6
plt.plot(np.linspace(0, 15, 100), stats.chi2.pdf(np.linspace(0, 15, 100), df=6))
plt.fill_between(np.linspace(0, 15, 100), stats.chi2.pdf(np.linspace(0, 15, 100), df=6), alpha=0.15)

# PDF    K=11
plt.plot(np.linspace(0, 15, 100), stats.chi2.pdf(np.linspace(0, 15, 100), df=11))
plt.fill_between(np.linspace(0, 15, 100), stats.chi2.pdf(np.linspace(0, 15, 100), df=11), alpha=0.15)

# LEGEND 图例
plt.text(x=0.5, y=0.7, s="$ k=1$", rotation=-65, alpha=.75, weight="bold", color="#008fd5")
plt.text(x=1.5, y=.35, s="$ k=3$", alpha=.75, weight="bold", color="#fc4f30")
plt.text(x=5, y=.2, s="$ k=6$", alpha=.75, weight="bold", color="#e5ae38")

# Ticks 坐标轴
plt.tick_params(axis="both", which="major", labelsize=18)
plt.axhline(y=0, color="black", linewidth=1.3, alpha=.7)
