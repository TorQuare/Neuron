from matplotlib import pyplot as plt
import os

run_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
bef_ga_values = []
after_ga_values_15 = []
after_ga_values_25 = []
after_ga_values_35 = []
after_ga_values_45 = []
S_length = 15
percent = 8

file = open("Runs.txt", 'r')
for i in file:
    arr = i.split("; ")
    bef_val = arr[0].split()
    aft_val = arr[1].split()
    S_arr_len = arr[2].split()
    percent_arr = arr[3].split()
    val_of_S_arr_len = int(S_arr_len[len(S_arr_len)-1])
    val_to_add = float(aft_val[len(aft_val)-1])*100
    if int(percent_arr[len(percent_arr)-1]) == percent:
        if val_of_S_arr_len == S_length and len(after_ga_values_15) < 10:
            bef_ga_values.append(float(bef_val[len(bef_val)-1])*100)
            after_ga_values_15.append(val_to_add)
        if val_of_S_arr_len == S_length + 10 and len(after_ga_values_25) < 10:
            after_ga_values_25.append(val_to_add)
        if val_of_S_arr_len == S_length + 20 and len(after_ga_values_35) < 10:
            after_ga_values_35.append(val_to_add)
        if val_of_S_arr_len == S_length + 30 and len(after_ga_values_45) < 10:
            after_ga_values_45.append(val_to_add)
        if len(after_ga_values_15) == 10 and len(after_ga_values_25) == 10 \
                and len(after_ga_values_35) == 10 and len(after_ga_values_45) == 10:
            break
file.close()

# plt.plot(run_arr, after_ga_values_15, label="After GA S=15")
# plt.plot(run_arr, after_ga_values_25, label="After GA S=25")
# plt.plot(run_arr, after_ga_values_35, label="After GA S=35")
# plt.plot(run_arr, after_ga_values_45, label="After GA S=45")
# plt.plot(run_arr, bef_ga_values, label="Before GA")
#
# plt.xlabel("Run")
# plt.ylabel("Time")
# plt.legend()
# plt.show()

len_of_s_arr = [15, 25, 35, 45]
avg_of_ga_val = [sum(after_ga_values_15)/len(after_ga_values_15),
                 sum(after_ga_values_25)/len(after_ga_values_25),
                 sum(after_ga_values_35)/len(after_ga_values_35),
                 sum(after_ga_values_45)/len(after_ga_values_45)]

plt.plot(len_of_s_arr, avg_of_ga_val, label="Average")
plt.xlabel("Length of S array")
plt.ylabel("Average time of each GA")
plt.show()
