import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

def main():

    plt.rcdefaults()

    info_list = [("C1", 35, 20.5), ("C2", 35, 20.2), ("C3", 35, 19.8), ("C4", 35, 19.5), ("C5", 35, 20.0)]
    info_list = [("C1", 116, 19.4), ("C2", 231, 21.1), ("C3", 37, 20.0), ("C4", 55, 20.0), ("C5", 34, 19.5)]
    info_list = [("C1", 36, 19.0), ("C2", 116, 21.1), ("C3", 231, 19.1), ("C4", 72, 20.6), ("C5", 44, 20.2)]
    info_list = [("C1", 66, 20.4), ("C2", 36, 19.9), ("C3", 44, 19.5), ("C4", 39, 20.6), ("C5", 37, 19.6)]
    positions = np.arange(len(info_list))
    names = [row[0] for row in info_list]
    scores = [row[1] for row in info_list]
    proges = [row[2] for row in info_list]

    fig, ax1 = plt.subplots()
    ax = plt.gca()
    ax.spines['left'].set_linewidth(2)
    ax.spines['right'].set_linewidth(2)
    ax.spines['top'].set_linewidth(2)
    ax.spines['bottom'].set_linewidth(2)
    #ax1.linewidth(4)
    #Dataset Bar
    ax1.bar(positions, scores, width=0.4, align='center', color='chocolate', label="Dataset")
    ax1.set_xticks(positions)
    ax1.set_xticklabels(names)
    ax1.tick_params(labelsize=14)

    ax1.set_xlabel("Classification", fontsize = 16)

    ax1.set_ylabel("Dataset Capacity", fontsize = 14)
    max_score = max(scores)
    ax1.set_ylim(0, int(max_score * 1.2))
    #Dataset labels
    for x,y in zip(positions, scores):
        ax1.text(x, y - max_score * 0.05, y, ha='center', va='center', fontsize=16)

    #Feature proportion
    ax2 = ax1.twinx()
    ax2.plot(positions, proges, 'o-', color='darkblue', label="Feature")
    max_proges = max(proges)
    #ax1.spines.set_linewidth('2.0')
    #Feature proportion label
    for x,y in zip(positions, proges):
        ax2.text(x, y + max_proges * 0.01, ('%.1f%%' %y), ha='center', va= 'bottom', fontsize=16)

    fmt = '%.1f%%'
    yticks = mtick.FormatStrFormatter(fmt)
    ax2.yaxis.set_major_formatter(yticks)
    ax2.set_ylim(0, int(max_proges * 1.2))
    ax2.set_ylabel("Feature Proportion", fontsize = 14)
    ax2.tick_params(labelsize=14)

    handles1, labels1 = ax1.get_legend_handles_labels()
    handles2, labels2 = ax2.get_legend_handles_labels()
    plt.legend(handles1+handles2, labels1+labels2, loc='lower right', fontsize=14)


    plt.savefig("Unbalanced-3.jpg", dpi=1800, bbox_inches='tight')
    plt.show()



if __name__ == '__main__':
    main()