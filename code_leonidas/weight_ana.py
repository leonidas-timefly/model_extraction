import os
import numpy as np
import matplotlib.pyplot as plt


ProPath = "pro_value/Vgg16/5"

nb_class = 5

path_list = []

for k in range(1, nb_class + 1):
    temp_path = os.path.join(ProPath, "class" + str(k))
    print(temp_path)
    path_list.append(temp_path)

#print(path_list)

#print(len(path_list))
child_path_set = [[] for _ in range(nb_class)]

#os.listdir(path_list[0])
for k in range(nb_class):
    for child_path in os.listdir(path_list[k]):
        print(child_path)
        child_path_set[k].append(child_path)
print(child_path_set)
print(child_path_set[0], child_path_set[1], child_path_set[2], child_path_set[3], child_path_set[4])

def get_max_min(child_path_set):
    for k in range(nb_class):
        with open("class" + str(k + 1) + "max&min.txt", 'w') as ff:
            for num in range(len(child_path_set[k])):
                file_name = os.path.join(ProPath, os.path.join("class" + str(k + 1), child_path_set[k][num]))
                print(file_name)
                with open(file_name, 'r') as sf:
                    lines = sf.readlines()
                    temp = child_path_set[k][num] + "  "+ str(float(lines[0])) + "  " + str(float(lines[-1]))
                    print(temp)
                    print(float(lines[0]), float(lines[-1]))
                ff.write(temp + "\n")

#get_max_min(child_path_set = child_path_set)


file_list = [
    ["1118.txt", "2894.txt", "2490.txt", "2840.txt", "1507.txt", "684.txt"],
    ["3969.txt", "3248.txt", "3033.txt", "1610.txt", "640.txt", "972.txt"],
    ["3070.txt", "2936.txt", "9.txt", "3227.txt", "1925.txt", "3262.txt"],
    ["1031.txt", "946.txt", "3157.txt", "877.txt", "4081.txt", "517.txt"],
    ["94.txt", "2632.txt", "3564.txt", "4088.txt", "2300.txt", "2984.txt"]
]
def Draw_picture(ProPath, file_list):
    for num in range(len(file_list)):
        y = [[] for _ in range(len(file_list[num]))]
        x = np.arange(500, -1, -10)
        print(y)
        for k in range(len(file_list[num])):
            file_name = os.path.join(ProPath, os.path.join("class" + str(num + 1), file_list[num][k]))
            with open(file_name, 'r') as f:
                for line in f:
                    y[k].append(float(line))
                    print([float(line)])
                y[k].append(float(0.2))
                print(y[k])
                for t in range(51):
                    print(x[t], y[k][t])
        plt.xlabel('Feature Value')
        plt.ylabel('Probability')
        plt.grid(linestyle=":", color="b")
        mark_list = ['X', 'v', 'o', 'x', 'd', '*']
        for k in range(len(file_list[num])):
            plt.plot(x, np.array(y[k]), label="C" + str(num + 1) + "-F" + str(k + 1), marker = mark_list[k], markersize = 3)
        plt.legend()
        #plt.gca().invert_xaxis()
        plt.savefig("results/pictures/UMass/Vgg16/5/class" + str(num + 1) + "test.jpg", dpi = 1800, bbox_inches = 'tight')
        plt.show()
        #plt.savefig('results/pictures/UMass/Vgg16/5/test.jpg')

Draw_picture(ProPath, file_list)
