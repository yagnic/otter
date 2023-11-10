# **Project Setup**

## **Start Project**

<br>

### **1. Download Dataset**
   
To complete this challenge, you will need to start by setting it up:

Go to the link https://www.kaggle.com/datasets/surajjha101/cuisine-rating and click on download option on upper-right corner.

![](/Image/Project_2/kaggle.png)


### **2. Setup workplace**

You can work on this project through any IDE or through kaggle notebook which you can create by clicking on New notebook option on upper-right corner.

For this tutorial, I would be using jupyter notebook

![](/Image/Project_1/jupyter%20notebook_1.png)

Opening new notebook

![](/Image/Project_1/jupyter_new_notebook.png)


### **3. Information on Dataset**
   
  - The data is based on the restaurant ratings given by a customer along with the demographic data of the customers and the food habits of the customers.

### **4. Importing libraries**

For every machine learning / Data Science project, there are certain libraries that are always used so we import them by default.

```python

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

```

### **5. Importing the dataset**

```python
# loading data of players from 2021
data = pd.read_csv("./data/Cuisine_rating.csv")


```
**Note**
- For the data files ending with csv, the read_csv is used for loading the data into dataframe.


### **6. Data Exploration**

- Getting the information of the dataset using the function info()

```python


data.info()


```

output:

![](./Image/Project_2/../../../Image/Project_2/data_info.png)

- From the above output, it can be seen that the dataset contains about 200 entries and 15 columns. The datatypes in the dataset are mostly integers, floats and objects. Memory usage by the dataset from the RAM is about 24 kb.


- Getting the descriptive statistics of from the data for all numerical attributes.


```python



data.describe()


```


output:

![](/Image/Project_2/descriptive.png)



- Getting the descriptive statistics for the object datatype columns or features.



```python



data.describe(include="O")


```


output:

![](/Image/Project_2/descriptive_objects.png)


- Separating the categorical and numerical columns to perform statistical analysis and exploratory data analysis.


separating the categorical columns:

```python


cat = []

for columns in data.columns:
    if data[columns].dtype=="O":
        cat.append(columns)




```

- In the above code cell, we are using the for loop to iterate over all the column names and checking if the column pertaining to the data is in object datatype, if it is object we are appending it to the cat list.


```python

output:


['Location',
 'Gender',
 'Marital Status',
 'Activity',
 'Cuisines',
 'Alcohol ',
 'Smoker',
 'Often A S']
```

 separating the numerical columns:

 **Challenge**

 The challenge is to make a list containing only numerical columns.
```python
 Expected Output:

 ['User ID',
 'Area code',
 'YOB',
 'Budget',
 'Food Rating',
 'Service Rating',
 'Overall Rating']
```

 **Answer**

 - The challenge can be completed using the same code as for categorical columns but with few changes as below.

```python

num = []

for columns in data.columns:
    if data[columns].dtype!="O":
        num.append(columns)



```


**Objectives - Basic**

1. To visualize the top 5 locations based on the number of customers.
2. To visualize the number of males and females in the data.
3. To visualize number of customers based on marital status.
4. To visualize number of customers based on activity.


#### **Objective 1:**

- To complete the objective 1, we need to groupby the data using location and get the size of the data.

```python

data.groupby("Location").size()

```

```python
output:

Location
Cedar Hill, NY         2
Central Park,NY       24
Central Park,ny        8
China Town, NY        22
Market City, MY        2
Market City, NY       20
Riverdale,NY          28
St. George,NY         46
Upper East Side,NY    30
Upper West Side,NY    18
dtype: int64

```


- Then sort the values, so that the locations are ranked based on the number of customers.


```python

data.groupby("Location").size().sort_values(ascending=False)




```

```python
output: 

Location
St. George,NY         46
Upper East Side,NY    30
Riverdale,NY          28
Central Park,NY       24
China Town, NY        22
Market City, NY       20
Upper West Side,NY    18
Central Park,ny        8
Cedar Hill, NY         2
Market City, MY        2
dtype: int64

```

- To visualize, we will use .plot() function on the dataframe and use parameter kind = "bar".


```python

data.groupby("Location").size().sort_values(ascending=False).plot(kind="bar")



```

output:

![](/Image/Project_2/location_plot.png)


#### **Objective 2:**


- To complete the objective 2, we need to groupby the data using gender and get the size of the data.

```python

data.groupby("Gender").size()

```
```python
output:

Gender
Female     82
Male      118
dtype: int64

```

- Then sort the values, so that the gender are ranked based on the number of customers.



```python

data.groupby("Gender").size().sort_values(ascending=False)




```
```python
output: 

Gender
Male      118
Female     82
dtype: int64
```

- To visualize, we will use .plot() function on the dataframe and use parameter kind = "bar".


```python

data.groupby("Gender").size().sort_values(ascending=False).plot(kind="bar")



```

output:

![](/Image/Project_2/gender_plot.png)



#### **Objective 3:**


- To complete the objective 2, we need to groupby the data using Marital Status and get the size of the data.

```python

data.groupby("Marital Status").size()

```
```python
output:

Marital Status
Divorced     14
Married      86
Single      100
dtype: int64
```


- Then sort the values, so that the Marital Status are ranked based on the number of customers.


```python

data.groupby("Marital Status").size().sort_values(ascending=False)




```
```python
output: 

Marital Status
Single      100
Married      86
Divorced     14
dtype: int64
```

- To visualize, we will use .plot() function on the dataframe and use parameter kind = "bar".


```python

data.groupby("Marital Status").size().sort_values(ascending=False).plot(kind="bar")



```

output:

![](/Image/Project_2/marital_plot.png)




#### **Objective 4:**

The objective 4 should be done by the reader, it will be similar to previous objectives.



**Objectives - Intermediate**

1. To get the average budget for the whole data.
2. To get the average budget spent by male and female in the data.
3. To get the average budget based on marital status
4. To get the average budget based on activity


#### **Objective 1:**

- To complete the objective 1, we need to get the mean of the data for the feature budget.

```python

data.budget.mean()

```

```python
output:

3.815
```


#### **Objective 2:**


- To complete the objective 2, we need to groupby the data using gender and aggregate based on mean of the budget.

```python

data.groupby("Gender").agg({"Budget":"mean"})

```


output:


![](./Image/Project_2/../../../Image/Project_2/groupby_gender.png)



#### **Objective 3:**


- To complete the objective 3, we need to groupby the data using Marital Status and aggregate budget using mean.

```python

data.groupby("Marital Status").agg({"Budget":"mean"})

```


output:

![](./Image/Project_2/../../../Image/Project_2/groupby_marital.png)






#### **Objective 4:**



- To complete the objective 2, we need to groupby the data using activity and aggregate budget using mean.

```python

data.groupby("Activity").agg({"Budget":"mean"})

```

output:

![](./Image/Project_2/../../../Image/Project_2/groupby_activity.png)




**Challenge**

The above objectives should be performed by the reader for Food Rating, Service Rating and Overall Rating.






**Objectives - Advanced**

1. To check based on the data, if the customers who had alcohol gave more overall rating or the ones who didn't had alcohol.
2. To check the customer with huge difference in food rating and service rating.
3. To check based on the data, if the customers who smoke gave more overall rating or the ones who didn't smoke.
4. To check which cuisine has got the highest rating.


#### **Objective-1:**


- To complete the objective-1, we need to groupby on the alcohol and aggregate on the overall rating using mean.


```python

data.groupby("Alcohol ").agg({"Overall Rating":"mean"})



```


output:


![](./Image/Project_2/../../../Image/Project_2/groupby_alcohol.png)





#### **Objective-2:**

- To complete objective-2, we need to get the difference between food rating and service rating. Then we need to sort the data based on the difference in descending order.


```python

data["rating_difference"] = abs(data["Food Rating"] - data["Service Rating"])
data.sort_values(by="rating_difference",ascending=False)

```




output:

![](/Image/Project_2/difference.png)



#### **Objective-3:**

This objective is similar to the objective-1. This can be successfully completed using the below code.


```python

data.groupby("Smoker").agg({"Overall Rating":"mean"})



```


output:


![](/Image/Project_2/groupy_smoker.png)



#### **Objective-4:**


To complete this objective, we need to groupby based on cuisine and aggregate the cuisine base on the overall rating using the mean.


```python

data.groupby("Cuisines").agg({"Overall Rating":"mean"}).sort_values(by="Cuisines",ascending=False)



```


output:

![](/Image/Project_2/cuisine_rating.png)



**Bonus Objectives**

1. Finding the cuisine with lowest and highest budgets.


- To complete this objective, first we need to groupby using the cuisine and aggregate based on mean.
  
```python

data.groupby("Cuisines").agg({"Budget":"mean"}).sort_values(by="Budget",ascending=False)


```

output:

![](/Image/Project_2/cuisines_budget.png)



- Then get the head of the data and convert it into array using values to get the array. Then access the zero index to get the cuisine.


```python


data.groupby("Cuisines").agg({"Budget":"mean"}).sort_values(by="Budget",ascending=False).head(1).index.values[0]



```
```python
output:


'Japanese'

```
- Then get the tail of the data and convert it into array using values to get the array. Then access the zero index to get the cuisine.



```python


    data.groupby("Cuisines").agg({"Budget":"mean"}).sort_values(by="Budget",ascending=False).tail(1).index.values[0]


```
```python
output:


'Indian'

```

