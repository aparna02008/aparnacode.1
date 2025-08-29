import numpy as np

a=np.random.randint(0,100,(7,3))
print("Temperature data week 1:",a)

c=(a.mean(axis=0))
print(c)

print("City A:",c[0])
print("City B:",c[1])
print("City C:",c[2])


d=a.max(axis=1)
print("Maximum temperature of each day:",d)

e=np.argmax(c)
city=["City A","City B","City c"]
print("The city has highest average temperature:",city[e],"with",c[e])# aparnacode2
