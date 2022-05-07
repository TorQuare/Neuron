from matplotlib import pyplot as plt
import os

run_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
bef_ga_values = []
after_ga_values = []
S_length = 15
percent = 8

file = open("Runs.txt", 'r')
for i in file:
    arr = i.split("; ")
    S_arr_len = arr[2].split()
    percent_arr = arr[3].split()
    bef_val = arr[0].split()
    aft_val = arr[1].split()
    if int(S_arr_len[len(S_arr_len)-1]) == S_length and int(percent_arr[len(percent_arr)-1]) == percent:
        bef_ga_values.append(float(bef_val[len(bef_val)-1])*100)
        after_ga_values.append(float(aft_val[len(bef_val)-1])*100)
        if len(after_ga_values) == 10:
            break
file.close()

print(after_ga_values)

plt.plot(run_arr, after_ga_values, label="After GA")
plt.plot(run_arr, bef_ga_values, label="Before GA")

plt.xlabel("Run")
plt.ylabel("Time")
plt.legend()
plt.show()
