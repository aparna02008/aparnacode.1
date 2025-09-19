import numpy as np
months=int(input("Enter the months"))
income=[]
expenses=[]
category=3
for i in range(months):
    print(f"Month {i+1}")
    m_income=int(input("Enter this month income"))
    income.append(m_income)
    for j in range(category): 
          m_expenses=int(input("Enter the monthly expenses"))
          expenses.append(m_expenses)
income=np.array(income)
expenses=np.array((expenses))
expenses=expenses.reshape(months,category)
i_total=income.sum()
e_total=expenses.sum()
print("Total Income",i_total)
print("Total Expenses",e_total)
percentage=(expenses/e_total)*100
print(percentage)
labels=np.where(percentage>50,"High",
        np.where(percentage>20,"Medium","Low"))
print(labels)

