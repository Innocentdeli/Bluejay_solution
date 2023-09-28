#!/usr/bin/env python
# coding: utf-8

# In[90]:


import pandas as pd
from datetime import datetime, timedelta


# In[91]:


data = pd.read_excel('./Assignment_Timecard.xlsx')


# In[92]:


data.head(50)


# In[93]:


data.info()


# In[ ]:





# In[94]:


def qualified_employees(data):
    consecutive_days_worked = 0
    current_employee = None
    previous_end_time = None
    employees_7_days_worked = []
    employees_10_hours_shift = []
    employees_14_hours_shift = []

    for index, row in data.iterrows():
        if current_employee != row['Employee Name']:
            consecutive_days_worked = 1
            current_employee = row['Employee Name']
            previous_end_time = None
        else:
            consecutive_days_worked += 1
            # Check for consecutive_days_worked (7 days)
            if consecutive_days_worked == 7:
                employees_7_days_worked.append((row['Employee Name'], row['Position ID']))
        
        # Check for less than 10 hours but greater than 1 hour between shifts
        if previous_end_time:
            time_between_shifts = row['Time'] - previous_end_time
            if timedelta(hours=1) < time_between_shifts < timedelta(hours=10):
                employees_10_hours_shift.append((row['Employee Name'], row['Position ID']))

        # Check for more than 14 hours in a single shift
        shift_duration = row['Time Out'] - row['Time']
        if shift_duration > timedelta(hours=14):
            employees_14_hours_shift.append((row['Employee Name'], row['Position ID']))

        previous_end_time = row['Time Out']

    return employees_7_days_worked, employees_10_hours_shift, employees_14_hours_shift

employees_with_conditions = qualified_employees(data)

x,y,z = employees_with_conditions 
#where x represent employees_7_days_worked
#y represents  employees_10_hours_shift
#and z represents employees_14_hours_shift


# In[95]:


len(x)


# In[96]:


len(y)


# In[97]:


len(z)


# In[98]:


print(x)


# In[99]:


print(y)


# In[100]:


print(z)


# In[104]:





# In[ ]:




