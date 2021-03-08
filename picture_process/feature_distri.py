import matplotlib
import matplotlib.pyplot as plt
import numpy as np


labels = ['C1', 'C2', 'C3', 'C4', 'C5']
men_means = [0.200, 0.200, 0.200, 0.200, 0.200]
women_means = [0.205, 0.202,0.198, 0.194, 0.201]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, men_means, width, label='Data Proportion')
rects2 = ax.bar(x + width/2, women_means, width, label='Feature Proportion')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Ratio')
ax.set_title('Data and Feature Proportion')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend(loc='lower right')


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)
autolabel(rects2)

fig.tight_layout()

plt.savefig("proportion.jpg", dpi=1800, bbox_inches='tight')

plt.show()