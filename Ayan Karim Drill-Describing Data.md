

```python
# Ayan Karim
# Drill: Describing Data

import pandas as pd
import numpy as np
import statistics

# 1.

df = pd.DataFrame()
df['age'] = [14, 12, 11, 10, 8, 6, 8]
print('Mean = ' + str(np.mean(df['age'])))
print('Median = ' + str(np.median(df['age'])))
print('Mode = ' + str(statistics.mode(df['age'])))
print('Variance = ' + str(df['age'].var()))
print('Standard Deviation = ' + str(np.std(df['age'], ddof=1)))
print('Standard Error = ' + str(np.std(df['age'] ,ddof=1) / np.sqrt(len(df['age']))))
```

    Mean = 9.857142857142858
    Median = 10.0
    Mode = 8
    Variance = 7.476190476190475
    Standard Deviation = 2.734262327610589
    Standard Error = 1.0334540197243192



```python
# 2.

# For central tendency, I'd use the mean = 9.86 because it includes all the data points
# and since there are no significant outliers, the mean isn't drastically changed.

# For measure of variance, I would use Standard Error, because it shows that the room 
# for error is very small at +/- 1.03%.
```


```python
# 3.

df['age'] = [14, 12, 11, 10, 8, 7, 8]
print('Mean = ' + str(np.mean(df['age'])))
print('Median = ' + str(np.median(df['age'])))
print('Mode = ' + str(statistics.mode(df['age'])))
print('Variance = ' + str(df['age'].var()))
print('Standard Deviation = ' + str(np.std(df['age'], ddof=1)))
print('Standard Error = ' + str(np.std(df['age'] ,ddof=1) / np.sqrt(len(df['age']))))
```

    Mean = 10.0
    Median = 10.0
    Mode = 8
    Variance = 6.333333333333333
    Standard Deviation = 2.516611478423583
    Standard Error = 0.9511897312113418



```python
# The mean and the measures of variance changed, but the median and mode remained the same.
```


```python
# 4.

from statistics import mode, StatisticsError

df['age'] = [14, 12, 11, 10, 8, 7, 1]
print('Mean = ' + str(np.mean(df['age'])))
print('Median = ' + str(np.median(df['age'])))
try:
    statistics.mode(df['age'])
except StatisticsError:
    print ('No Mode')
print('Variance = ' + str(df['age'].var()))
print('Standard Deviation = ' + str(np.std(df['age'], ddof=1)))
print('Standard Error = ' + str(np.std(df['age'] ,ddof=1) / np.sqrt(len(df['age']))))
```

    Mean = 9.0
    Median = 10.0
    No Mode
    Variance = 18.0
    Standard Deviation = 4.242640687119285
    Standard Error = 1.6035674514745462



```python
# Replacing Cousin Oliver (age 8) with a 1 year old changes my choice measure
# to the median, because the 1 year old is an extreme low data point
# so the mean is sensitive to it.
# I would change using the Standard Error to the Variance because the Variance 
# shows there's lots of variability.
```


```python
# 5.

df = pd.DataFrame()
df['fans'] = [0.20, 0.23, 0.17, 0.05]
np.median(df['fans']) * 100
```




    18.5




```python
# We use the sample median of 18.5% because the sciphi magazine fans are outliers at 5% (0.05).
# This is the best estimate for the population median and for the percentage of American adults
# that are fans of the show at the 50th anniversary.
```
