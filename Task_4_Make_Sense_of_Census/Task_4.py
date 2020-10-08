# Importing header files
import numpy as np
import warnings

path = "./subset_1000.csv"
user_data_dir = "."

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)

#Code starts here
#step 1
census = np.concatenate((data, new_record), axis=0)

#step 2
age = census[:,0]
max_age = max(age)
min_age = min(age)
age_mean = np.mean(age)
age_std = np.std(age)

#step 3
race_0 = census[census[:,2]==0]
race_1 = census[census[:,2]==1]
race_2 = census[census[:,2]==2]
race_3 = census[census[:,2]==3]
race_4 = census[census[:,2]==4]

len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)


minority_race = len_0
if  len_1 < minority_race:
    minority_race = len_1
if len_2 < minority_race:
    minority_race = len_2
if len_3 < minority_race:
    minority_race = len_3
if len_4 < minority_race:
    minority_race = len_4

#step 4
senior_citizens = census[census[:,0] > 60]

working_hours_sum = senior_citizens.sum(axis=0)[6]

senior_citizens_len = len(senior_citizens)

avg_working_hours = working_hours_sum / senior_citizens_len

print(round(avg_working_hours,2))

#step 5
high = census[census[:,1]>10]
low = census[census[:,1]<=10]
avg_pay_high = np.mean(high, axis=0)[7]
avg_pay_high = round(avg_pay_high, 2)
avg_pay_low = round(np.mean(low[:,7]), 2)
