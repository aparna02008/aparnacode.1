import numpy as np
a=np.random.randint(0,100,30)
b=a.reshape(30,1)
print(b)
print("Average Temperature:",b.mean())
print("Maximum Temperature:",b.max())
print("Minimum Temperature:",b.min())
days_above_temp=np.sum(b>b.mean())
days_below_temp=np.sum(b<b.mean())
print("Days above mean temperature:",days_above_temp)
print("Days below mean temperature:",days_below_temp)
hot_thershold=75
cold_thershold=25
hot_days=np.sum(b>=hot_thershold)
cold_days=np.sum(b<=cold_thershold)
print("Hot days",hot_days)
print("Cold days",cold_days)