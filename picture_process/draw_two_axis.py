import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

def main():

    plt.rcdefaults()

    info_list = [("Donald", 35, 20.5), ("Calin", 35, 19.8), ("Gerhard", 35, 20.2), ("Tony", 35, 19.5), ("Serena", 35, 20.0)]
    info_list = [("Donald", 116, 19.4), ("Calin", 37, 20.0), ("Gerhard", 231, 21.1), ("Tony", 55, 20.0), ("Serena", 34, 19.5)]
    info_list = [("Donald", 36, 19.0), ("Calin", 231, 19.1), ("Gerhard", 116, 21.1), ("Tony", 72, 20.6), ("Serena", 44, 20.2)]
    info_list = [("Donald", 66, 20.4), ("Calin", 44, 19.5), ("Gerhard", 36, 19.9), ("Tony", 39, 20.6), ("Serena", 37, 19.6)]
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
    ax1.bar(positions, scores, width=0.5, align='center', color='chocolate', label="Capacity")
    ax1.set_xticks(positions)
    ax1.set_xticklabels(names)
    ax1.tick_params(labelsize=16)

    ax1.set_xlabel("Category", fontsize = 16)

    ax1.set_ylabel("Sample Capacity", fontsize = 16)
    max_score = max(scores)
    ax1.set_ylim(0, int(max_score * 1.2))
    #Dataset labels
    for x,y in zip(positions, scores):
        ax1.text(x, y - max_score * 0.05, y, ha='center', va='center', fontsize=16)

    #Feature proportion
    ax2 = ax1.twinx()
    ax2.plot(positions, proges, 'o-', color='darkblue', label="Proportion")
    max_proges = max(proges)
    #ax1.spines.set_linewidth('2.0')
    #Feature proportion label
    for x,y in zip(positions, proges):
        ax2.text(x, y + max_proges * 0.02, ('%.1f%%' %y), ha='center', va= 'bottom', fontsize=16)

    fmt = '%.1f%%'
    yticks = mtick.FormatStrFormatter(fmt)
    ax2.yaxis.set_major_formatter(yticks)
    ax2.set_ylim(0, int(max_proges * 1.2))
    ax2.set_ylabel("Neuron Proportion", fontsize = 16)
    ax2.tick_params(labelsize=16)

    handles1, labels1 = ax1.get_legend_handles_labels()
    handles2, labels2 = ax2.get_legend_handles_labels()
    plt.legend(handles1+handles2, labels1+labels2, loc='lower right', fontsize=16)


    plt.savefig("proportion-4.png", dpi=1800, bbox_inches='tight')
    plt.show()



if __name__ == '__main__':
    main()