# Weather Data Analysis

- IN THIS POJECT WE WILL USE FOLLOWING COMMANDS/OPERATIONS TO ANALYZE THE WEATHER'S DATA :-

### Pandas

- Pandas :- Pandas is a library used to work with Data-Set.
- Pandas has Functions for Analyzing,Cleaning,Exploring & Manipulating data.


```python
import pandas as pd
```

### NumPy

- NumPy :- NumPy library is used to perform Mathematical Operation on Arrays.


```python
import numpy as np
```

### Importing the DataSet/DataFrame

- Syntax to Load or import the DataSet(DataFrame)
- d = pd.read_csv(r'csv_FilePath Or Location\csv_fileName')
- d is a variable where we have stored Whole Data Set/frame


```python
d = pd.read_csv(r'A:\MTECH(Data Science)\DataSet\archive\weather.csv')
```

### NOW TO ANALYZE THE WEATHER'S DATA I AM USING FOLLOWING COMMANDS :-

# d

- This command will show whole Data-Set
- print(d) are eqivalent command.


```python
d
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>MinTemp</th>
      <th>MaxTemp</th>
      <th>Rainfall</th>
      <th>Evaporation</th>
      <th>Sunshine</th>
      <th>WindGustDir</th>
      <th>WindGustSpeed</th>
      <th>WindDir9am</th>
      <th>WindDir3pm</th>
      <th>WindSpeed9am</th>
      <th>...</th>
      <th>Humidity3pm</th>
      <th>Pressure9am</th>
      <th>Pressure3pm</th>
      <th>Cloud9am</th>
      <th>Cloud3pm</th>
      <th>Temp9am</th>
      <th>Temp3pm</th>
      <th>RainToday</th>
      <th>RISK_MM</th>
      <th>RainTomorrow</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>8.0</td>
      <td>24.3</td>
      <td>0.0</td>
      <td>3.4</td>
      <td>6.3</td>
      <td>NW</td>
      <td>30.0</td>
      <td>SW</td>
      <td>NW</td>
      <td>6.0</td>
      <td>...</td>
      <td>29</td>
      <td>1019.7</td>
      <td>1015.0</td>
      <td>7</td>
      <td>7</td>
      <td>14.4</td>
      <td>23.6</td>
      <td>No</td>
      <td>3.6</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>1</th>
      <td>14.0</td>
      <td>26.9</td>
      <td>3.6</td>
      <td>4.4</td>
      <td>9.7</td>
      <td>ENE</td>
      <td>39.0</td>
      <td>E</td>
      <td>W</td>
      <td>4.0</td>
      <td>...</td>
      <td>36</td>
      <td>1012.4</td>
      <td>1008.4</td>
      <td>5</td>
      <td>3</td>
      <td>17.5</td>
      <td>25.7</td>
      <td>Yes</td>
      <td>3.6</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>2</th>
      <td>13.7</td>
      <td>23.4</td>
      <td>3.6</td>
      <td>5.8</td>
      <td>3.3</td>
      <td>NW</td>
      <td>85.0</td>
      <td>N</td>
      <td>NNE</td>
      <td>6.0</td>
      <td>...</td>
      <td>69</td>
      <td>1009.5</td>
      <td>1007.2</td>
      <td>8</td>
      <td>7</td>
      <td>15.4</td>
      <td>20.2</td>
      <td>Yes</td>
      <td>39.8</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>3</th>
      <td>13.3</td>
      <td>15.5</td>
      <td>39.8</td>
      <td>7.2</td>
      <td>9.1</td>
      <td>NW</td>
      <td>54.0</td>
      <td>WNW</td>
      <td>W</td>
      <td>30.0</td>
      <td>...</td>
      <td>56</td>
      <td>1005.5</td>
      <td>1007.0</td>
      <td>2</td>
      <td>7</td>
      <td>13.5</td>
      <td>14.1</td>
      <td>Yes</td>
      <td>2.8</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>4</th>
      <td>7.6</td>
      <td>16.1</td>
      <td>2.8</td>
      <td>5.6</td>
      <td>10.6</td>
      <td>SSE</td>
      <td>50.0</td>
      <td>SSE</td>
      <td>ESE</td>
      <td>20.0</td>
      <td>...</td>
      <td>49</td>
      <td>1018.3</td>
      <td>1018.5</td>
      <td>7</td>
      <td>7</td>
      <td>11.1</td>
      <td>15.4</td>
      <td>Yes</td>
      <td>0.0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>361</th>
      <td>9.0</td>
      <td>30.7</td>
      <td>0.0</td>
      <td>7.6</td>
      <td>12.1</td>
      <td>NNW</td>
      <td>76.0</td>
      <td>SSE</td>
      <td>NW</td>
      <td>7.0</td>
      <td>...</td>
      <td>15</td>
      <td>1016.1</td>
      <td>1010.8</td>
      <td>1</td>
      <td>3</td>
      <td>20.4</td>
      <td>30.0</td>
      <td>No</td>
      <td>0.0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>362</th>
      <td>7.1</td>
      <td>28.4</td>
      <td>0.0</td>
      <td>11.6</td>
      <td>12.7</td>
      <td>N</td>
      <td>48.0</td>
      <td>NNW</td>
      <td>NNW</td>
      <td>2.0</td>
      <td>...</td>
      <td>22</td>
      <td>1020.0</td>
      <td>1016.9</td>
      <td>0</td>
      <td>1</td>
      <td>17.2</td>
      <td>28.2</td>
      <td>No</td>
      <td>0.0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>363</th>
      <td>12.5</td>
      <td>19.9</td>
      <td>0.0</td>
      <td>8.4</td>
      <td>5.3</td>
      <td>ESE</td>
      <td>43.0</td>
      <td>ENE</td>
      <td>ENE</td>
      <td>11.0</td>
      <td>...</td>
      <td>47</td>
      <td>1024.0</td>
      <td>1022.8</td>
      <td>3</td>
      <td>2</td>
      <td>14.5</td>
      <td>18.3</td>
      <td>No</td>
      <td>0.0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>364</th>
      <td>12.5</td>
      <td>26.9</td>
      <td>0.0</td>
      <td>5.0</td>
      <td>7.1</td>
      <td>NW</td>
      <td>46.0</td>
      <td>SSW</td>
      <td>WNW</td>
      <td>6.0</td>
      <td>...</td>
      <td>39</td>
      <td>1021.0</td>
      <td>1016.2</td>
      <td>6</td>
      <td>7</td>
      <td>15.8</td>
      <td>25.9</td>
      <td>No</td>
      <td>0.0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>365</th>
      <td>12.3</td>
      <td>30.2</td>
      <td>0.0</td>
      <td>6.0</td>
      <td>12.6</td>
      <td>NW</td>
      <td>78.0</td>
      <td>NW</td>
      <td>WNW</td>
      <td>31.0</td>
      <td>...</td>
      <td>13</td>
      <td>1009.6</td>
      <td>1009.2</td>
      <td>1</td>
      <td>1</td>
      <td>23.8</td>
      <td>28.6</td>
      <td>No</td>
      <td>0.0</td>
      <td>No</td>
    </tr>
  </tbody>
</table>
<p>366 rows × 22 columns</p>
</div>



# d.head()

- This command will show the by default first 5 rows from the loaded DataSet.


```python
d.head()

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>MinTemp</th>
      <th>MaxTemp</th>
      <th>Rainfall</th>
      <th>Evaporation</th>
      <th>Sunshine</th>
      <th>WindGustDir</th>
      <th>WindGustSpeed</th>
      <th>WindDir9am</th>
      <th>WindDir3pm</th>
      <th>WindSpeed9am</th>
      <th>...</th>
      <th>Humidity3pm</th>
      <th>Pressure9am</th>
      <th>Pressure3pm</th>
      <th>Cloud9am</th>
      <th>Cloud3pm</th>
      <th>Temp9am</th>
      <th>Temp3pm</th>
      <th>RainToday</th>
      <th>RISK_MM</th>
      <th>RainTomorrow</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>8.0</td>
      <td>24.3</td>
      <td>0.0</td>
      <td>3.4</td>
      <td>6.3</td>
      <td>NW</td>
      <td>30.0</td>
      <td>SW</td>
      <td>NW</td>
      <td>6.0</td>
      <td>...</td>
      <td>29</td>
      <td>1019.7</td>
      <td>1015.0</td>
      <td>7</td>
      <td>7</td>
      <td>14.4</td>
      <td>23.6</td>
      <td>No</td>
      <td>3.6</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>1</th>
      <td>14.0</td>
      <td>26.9</td>
      <td>3.6</td>
      <td>4.4</td>
      <td>9.7</td>
      <td>ENE</td>
      <td>39.0</td>
      <td>E</td>
      <td>W</td>
      <td>4.0</td>
      <td>...</td>
      <td>36</td>
      <td>1012.4</td>
      <td>1008.4</td>
      <td>5</td>
      <td>3</td>
      <td>17.5</td>
      <td>25.7</td>
      <td>Yes</td>
      <td>3.6</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>2</th>
      <td>13.7</td>
      <td>23.4</td>
      <td>3.6</td>
      <td>5.8</td>
      <td>3.3</td>
      <td>NW</td>
      <td>85.0</td>
      <td>N</td>
      <td>NNE</td>
      <td>6.0</td>
      <td>...</td>
      <td>69</td>
      <td>1009.5</td>
      <td>1007.2</td>
      <td>8</td>
      <td>7</td>
      <td>15.4</td>
      <td>20.2</td>
      <td>Yes</td>
      <td>39.8</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>3</th>
      <td>13.3</td>
      <td>15.5</td>
      <td>39.8</td>
      <td>7.2</td>
      <td>9.1</td>
      <td>NW</td>
      <td>54.0</td>
      <td>WNW</td>
      <td>W</td>
      <td>30.0</td>
      <td>...</td>
      <td>56</td>
      <td>1005.5</td>
      <td>1007.0</td>
      <td>2</td>
      <td>7</td>
      <td>13.5</td>
      <td>14.1</td>
      <td>Yes</td>
      <td>2.8</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>4</th>
      <td>7.6</td>
      <td>16.1</td>
      <td>2.8</td>
      <td>5.6</td>
      <td>10.6</td>
      <td>SSE</td>
      <td>50.0</td>
      <td>SSE</td>
      <td>ESE</td>
      <td>20.0</td>
      <td>...</td>
      <td>49</td>
      <td>1018.3</td>
      <td>1018.5</td>
      <td>7</td>
      <td>7</td>
      <td>11.1</td>
      <td>15.4</td>
      <td>Yes</td>
      <td>0.0</td>
      <td>No</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 22 columns</p>
</div>



# d.tail()

- This command will show the by default last 5 rows from the loaded DataSet.


```python
d.tail()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>MinTemp</th>
      <th>MaxTemp</th>
      <th>Rainfall</th>
      <th>Evaporation</th>
      <th>Sunshine</th>
      <th>WindGustDir</th>
      <th>WindGustSpeed</th>
      <th>WindDir9am</th>
      <th>WindDir3pm</th>
      <th>WindSpeed9am</th>
      <th>...</th>
      <th>Humidity3pm</th>
      <th>Pressure9am</th>
      <th>Pressure3pm</th>
      <th>Cloud9am</th>
      <th>Cloud3pm</th>
      <th>Temp9am</th>
      <th>Temp3pm</th>
      <th>RainToday</th>
      <th>RISK_MM</th>
      <th>RainTomorrow</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>361</th>
      <td>9.0</td>
      <td>30.7</td>
      <td>0.0</td>
      <td>7.6</td>
      <td>12.1</td>
      <td>NNW</td>
      <td>76.0</td>
      <td>SSE</td>
      <td>NW</td>
      <td>7.0</td>
      <td>...</td>
      <td>15</td>
      <td>1016.1</td>
      <td>1010.8</td>
      <td>1</td>
      <td>3</td>
      <td>20.4</td>
      <td>30.0</td>
      <td>No</td>
      <td>0.0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>362</th>
      <td>7.1</td>
      <td>28.4</td>
      <td>0.0</td>
      <td>11.6</td>
      <td>12.7</td>
      <td>N</td>
      <td>48.0</td>
      <td>NNW</td>
      <td>NNW</td>
      <td>2.0</td>
      <td>...</td>
      <td>22</td>
      <td>1020.0</td>
      <td>1016.9</td>
      <td>0</td>
      <td>1</td>
      <td>17.2</td>
      <td>28.2</td>
      <td>No</td>
      <td>0.0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>363</th>
      <td>12.5</td>
      <td>19.9</td>
      <td>0.0</td>
      <td>8.4</td>
      <td>5.3</td>
      <td>ESE</td>
      <td>43.0</td>
      <td>ENE</td>
      <td>ENE</td>
      <td>11.0</td>
      <td>...</td>
      <td>47</td>
      <td>1024.0</td>
      <td>1022.8</td>
      <td>3</td>
      <td>2</td>
      <td>14.5</td>
      <td>18.3</td>
      <td>No</td>
      <td>0.0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>364</th>
      <td>12.5</td>
      <td>26.9</td>
      <td>0.0</td>
      <td>5.0</td>
      <td>7.1</td>
      <td>NW</td>
      <td>46.0</td>
      <td>SSW</td>
      <td>WNW</td>
      <td>6.0</td>
      <td>...</td>
      <td>39</td>
      <td>1021.0</td>
      <td>1016.2</td>
      <td>6</td>
      <td>7</td>
      <td>15.8</td>
      <td>25.9</td>
      <td>No</td>
      <td>0.0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>365</th>
      <td>12.3</td>
      <td>30.2</td>
      <td>0.0</td>
      <td>6.0</td>
      <td>12.6</td>
      <td>NW</td>
      <td>78.0</td>
      <td>NW</td>
      <td>WNW</td>
      <td>31.0</td>
      <td>...</td>
      <td>13</td>
      <td>1009.6</td>
      <td>1009.2</td>
      <td>1</td>
      <td>1</td>
      <td>23.8</td>
      <td>28.6</td>
      <td>No</td>
      <td>0.0</td>
      <td>No</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 22 columns</p>
</div>



# d.head(8)

- This command will show the first N rows from the loaded DataSet.
- d.head(7) = This command will show the first 7 rows from the loaded DataSet.
- d.head(11) = This command will show the first 11 rows from the loaded DataSet.


```python
d.head(8)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>MinTemp</th>
      <th>MaxTemp</th>
      <th>Rainfall</th>
      <th>Evaporation</th>
      <th>Sunshine</th>
      <th>WindGustDir</th>
      <th>WindGustSpeed</th>
      <th>WindDir9am</th>
      <th>WindDir3pm</th>
      <th>WindSpeed9am</th>
      <th>...</th>
      <th>Humidity3pm</th>
      <th>Pressure9am</th>
      <th>Pressure3pm</th>
      <th>Cloud9am</th>
      <th>Cloud3pm</th>
      <th>Temp9am</th>
      <th>Temp3pm</th>
      <th>RainToday</th>
      <th>RISK_MM</th>
      <th>RainTomorrow</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>8.0</td>
      <td>24.3</td>
      <td>0.0</td>
      <td>3.4</td>
      <td>6.3</td>
      <td>NW</td>
      <td>30.0</td>
      <td>SW</td>
      <td>NW</td>
      <td>6.0</td>
      <td>...</td>
      <td>29</td>
      <td>1019.7</td>
      <td>1015.0</td>
      <td>7</td>
      <td>7</td>
      <td>14.4</td>
      <td>23.6</td>
      <td>No</td>
      <td>3.6</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>1</th>
      <td>14.0</td>
      <td>26.9</td>
      <td>3.6</td>
      <td>4.4</td>
      <td>9.7</td>
      <td>ENE</td>
      <td>39.0</td>
      <td>E</td>
      <td>W</td>
      <td>4.0</td>
      <td>...</td>
      <td>36</td>
      <td>1012.4</td>
      <td>1008.4</td>
      <td>5</td>
      <td>3</td>
      <td>17.5</td>
      <td>25.7</td>
      <td>Yes</td>
      <td>3.6</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>2</th>
      <td>13.7</td>
      <td>23.4</td>
      <td>3.6</td>
      <td>5.8</td>
      <td>3.3</td>
      <td>NW</td>
      <td>85.0</td>
      <td>N</td>
      <td>NNE</td>
      <td>6.0</td>
      <td>...</td>
      <td>69</td>
      <td>1009.5</td>
      <td>1007.2</td>
      <td>8</td>
      <td>7</td>
      <td>15.4</td>
      <td>20.2</td>
      <td>Yes</td>
      <td>39.8</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>3</th>
      <td>13.3</td>
      <td>15.5</td>
      <td>39.8</td>
      <td>7.2</td>
      <td>9.1</td>
      <td>NW</td>
      <td>54.0</td>
      <td>WNW</td>
      <td>W</td>
      <td>30.0</td>
      <td>...</td>
      <td>56</td>
      <td>1005.5</td>
      <td>1007.0</td>
      <td>2</td>
      <td>7</td>
      <td>13.5</td>
      <td>14.1</td>
      <td>Yes</td>
      <td>2.8</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>4</th>
      <td>7.6</td>
      <td>16.1</td>
      <td>2.8</td>
      <td>5.6</td>
      <td>10.6</td>
      <td>SSE</td>
      <td>50.0</td>
      <td>SSE</td>
      <td>ESE</td>
      <td>20.0</td>
      <td>...</td>
      <td>49</td>
      <td>1018.3</td>
      <td>1018.5</td>
      <td>7</td>
      <td>7</td>
      <td>11.1</td>
      <td>15.4</td>
      <td>Yes</td>
      <td>0.0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6.2</td>
      <td>16.9</td>
      <td>0.0</td>
      <td>5.8</td>
      <td>8.2</td>
      <td>SE</td>
      <td>44.0</td>
      <td>SE</td>
      <td>E</td>
      <td>20.0</td>
      <td>...</td>
      <td>57</td>
      <td>1023.8</td>
      <td>1021.7</td>
      <td>7</td>
      <td>5</td>
      <td>10.9</td>
      <td>14.8</td>
      <td>No</td>
      <td>0.2</td>
      <td>No</td>
    </tr>
    <tr>
      <th>6</th>
      <td>6.1</td>
      <td>18.2</td>
      <td>0.2</td>
      <td>4.2</td>
      <td>8.4</td>
      <td>SE</td>
      <td>43.0</td>
      <td>SE</td>
      <td>ESE</td>
      <td>19.0</td>
      <td>...</td>
      <td>47</td>
      <td>1024.6</td>
      <td>1022.2</td>
      <td>4</td>
      <td>6</td>
      <td>12.4</td>
      <td>17.3</td>
      <td>No</td>
      <td>0.0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8.3</td>
      <td>17.0</td>
      <td>0.0</td>
      <td>5.6</td>
      <td>4.6</td>
      <td>E</td>
      <td>41.0</td>
      <td>SE</td>
      <td>E</td>
      <td>11.0</td>
      <td>...</td>
      <td>57</td>
      <td>1026.2</td>
      <td>1024.2</td>
      <td>6</td>
      <td>7</td>
      <td>12.1</td>
      <td>15.5</td>
      <td>No</td>
      <td>0.0</td>
      <td>No</td>
    </tr>
  </tbody>
</table>
<p>8 rows × 22 columns</p>
</div>



# d.shape

- This command will show the Total No. of rows and Total No. of Columns of the loaded DataSet.


```python
d.shape
```




    (366, 22)



# d.index

- This command will show the Range of the loaded DataSet.


```python
d.index
```




    RangeIndex(start=0, stop=366, step=1)



# d.columns

- This command will show the complete Attributes(columns) of the loaded DataSet.


```python
d.columns
```




    Index(['MinTemp', 'MaxTemp', 'Rainfall', 'Evaporation', 'Sunshine',
           'WindGustDir', 'WindGustSpeed', 'WindDir9am', 'WindDir3pm',
           'WindSpeed9am', 'WindSpeed3pm', 'Humidity9am', 'Humidity3pm',
           'Pressure9am', 'Pressure3pm', 'Cloud9am', 'Cloud3pm', 'Temp9am',
           'Temp3pm', 'RainToday', 'RISK_MM', 'RainTomorrow'],
          dtype='object')



# d.dtypes

- This command will show the Data Type of each Column of the loaded DataSet.


```python
d.dtypes
```




    MinTemp          float64
    MaxTemp          float64
    Rainfall         float64
    Evaporation      float64
    Sunshine         float64
    WindGustDir       object
    WindGustSpeed    float64
    WindDir9am        object
    WindDir3pm        object
    WindSpeed9am     float64
    WindSpeed3pm       int64
    Humidity9am        int64
    Humidity3pm        int64
    Pressure9am      float64
    Pressure3pm      float64
    Cloud9am           int64
    Cloud3pm           int64
    Temp9am          float64
    Temp3pm          float64
    RainToday         object
    RISK_MM          float64
    RainTomorrow      object
    dtype: object



# d['Column_Name'].unique()

- This command will show all the unique values of a particular column and it can be apply in only single column.


```python
d['MinTemp'].unique()
```




    array([ 8. , 14. , 13.7, 13.3,  7.6,  6.2,  6.1,  8.3,  8.8,  8.4,  9.1,
            8.5, 10.1, 12.1, 12.4, 13.8, 11.7, 15.6, 15.3, 16.4, 12.8, 12. ,
           15.4, 12.9, 15.1, 13.6, 11.6, 16.6, 14.5, 16.3, 17.2, 16.5, 15. ,
           14.9, 11.8,  9.6,  8.9, 15.5, 10.8,  7.5, 12.6, 14.8, 19.9,  9.2,
           11.3,  9.8, 14.3, 14.4, 15.9, 16.7, 17.5, 14.7, 20.9, 17. , 16. ,
           17.9, 15.2, 10. ,  9.9, 10.3, 12.7, 13.2, 18. , 17.6, 17.1, 18.2,
           16.8, 10.4,  8.6, 11.2, 11.4, 11.5, 13. ,  7.7,  4.4,  7.4,  9.5,
           12.5, 13.9, 12.3, 13.1,  7.1,  4.2,  3.5,  5.3,  7. ,  0.4,  3.2,
            5.9,  8.1,  6.9,  5.6,  7.2,  5.4,  6.3,  7.9,  2.4,  2.5,  5. ,
            3.8,  4.3, -2.1, -1.8,  2.1,  0.5, -0.9, -0.2,  0.1,  1.5,  9.4,
            1.3,  2.2, -0.4,  4.5, -2.7,  0.3,  1.2, -0.3,  4.7,  4.9,  1.4,
           -0.1,  0.6,  4.6, 10.6,  7.8, 10.2,  7.3,  8.7,  1. ,  6.4,  4. ,
            0.9,  0.8, -1.5,  6.6, -1.6, -3.1, -0.6,  3. ,  2.9, -1.3,  1.8,
           -2.6,  2.7, -1.7, -1.1,  2.3, -2.2, -3.5, -1. , -2. , -2.3, -2.8,
           -1.9,  4.8,  3.1, -2.9,  3.7, -3.4, -5.3,  0. , -3.7, -3.3,  4.1,
            5.8,  0.2, -2.5, -0.5,  9. ,  3.9,  0.7,  1.1,  5.1,  6.5,  8.2,
            6.7, 11.9,  3.4,  3.3])



# d.nunique()

- This command will show total no. of in unique values in each column and it can be apply in single column as well as on whole DataFrame.
- d.nunique() Apply in whole DataFrame


```python
d.nunique()
```




    MinTemp          180
    MaxTemp          187
    Rainfall          47
    Evaporation       55
    Sunshine         114
    WindGustDir       16
    WindGustSpeed     35
    WindDir9am        16
    WindDir3pm        16
    WindSpeed9am      22
    WindSpeed3pm      26
    Humidity9am       60
    Humidity3pm       74
    Pressure9am      190
    Pressure3pm      193
    Cloud9am           9
    Cloud3pm           9
    Temp9am          178
    Temp3pm          200
    RainToday          2
    RISK_MM           47
    RainTomorrow       2
    dtype: int64



# d.nunique() Apply in Single DataFrame

- It will show Total No. of Unique values that are present in particular column(Attribute).


```python
d['MinTemp'].nunique()
```




    180



# d.value_counts

- This command will show all the unique values with their count(Times or frequency).
- It can be apply in only single column.


```python
d['MinTemp'].value_counts()
```




    0.5     6
    4.4     6
    15.1    5
    3.2     5
    2.3     5
           ..
    13.9    1
    9.5     1
    7.7     1
    11.4    1
    3.3     1
    Name: MinTemp, Length: 180, dtype: int64




```python
d['RainTomorrow'].value_counts() # Show frequency
```




    No     300
    Yes     66
    Name: RainTomorrow, dtype: int64



# d.info()

- This command will provide us basic information about the DataFrame.


```python
d.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 366 entries, 0 to 365
    Data columns (total 22 columns):
     #   Column         Non-Null Count  Dtype  
    ---  ------         --------------  -----  
     0   MinTemp        366 non-null    float64
     1   MaxTemp        366 non-null    float64
     2   Rainfall       366 non-null    float64
     3   Evaporation    366 non-null    float64
     4   Sunshine       363 non-null    float64
     5   WindGustDir    363 non-null    object 
     6   WindGustSpeed  364 non-null    float64
     7   WindDir9am     335 non-null    object 
     8   WindDir3pm     365 non-null    object 
     9   WindSpeed9am   359 non-null    float64
     10  WindSpeed3pm   366 non-null    int64  
     11  Humidity9am    366 non-null    int64  
     12  Humidity3pm    366 non-null    int64  
     13  Pressure9am    366 non-null    float64
     14  Pressure3pm    366 non-null    float64
     15  Cloud9am       366 non-null    int64  
     16  Cloud3pm       366 non-null    int64  
     17  Temp9am        366 non-null    float64
     18  Temp3pm        366 non-null    float64
     19  RainToday      366 non-null    object 
     20  RISK_MM        366 non-null    float64
     21  RainTomorrow   366 non-null    object 
    dtypes: float64(12), int64(5), object(5)
    memory usage: 63.0+ KB
    

# d.count

- This command will show total no. of Non-NULL values in each column and it can be apply in single column as well as on whole DataFrame.
- Apply in whole DataFrame


```python
d.count()
```




    MinTemp          366
    MaxTemp          366
    Rainfall         366
    Evaporation      366
    Sunshine         363
    WindGustDir      363
    WindGustSpeed    364
    WindDir9am       335
    WindDir3pm       365
    WindSpeed9am     359
    WindSpeed3pm     366
    Humidity9am      366
    Humidity3pm      366
    Pressure9am      366
    Pressure3pm      366
    Cloud9am         366
    Cloud3pm         366
    Temp9am          366
    Temp3pm          366
    RainToday        366
    RISK_MM          366
    RainTomorrow     366
    dtype: int64



# d.notnull().sum()

- This command is used to check all rows amd column are filled or not in our loaded dataframe.


```python
d.notnull().sum()
```




    MinTemp          366
    MaxTemp          366
    Rainfall         366
    Evaporation      366
    Sunshine         363
    WindGustDir      363
    WindGustSpeed    364
    WindDir9am       335
    WindDir3pm       365
    WindSpeed9am     359
    WindSpeed3pm     366
    Humidity9am      366
    Humidity3pm      366
    Pressure9am      366
    Pressure3pm      366
    Cloud9am         366
    Cloud3pm         366
    Temp9am          366
    Temp3pm          366
    RainToday        366
    RISK_MM          366
    RainTomorrow     366
    dtype: int64



# d.isnull().sum()

- This command is used to check NULL values present or not in our dataframe.
- isnull command is used to check for null values.


```python
pd.isnull(d).sum()
```




    MinTemp           0
    MaxTemp           0
    Rainfall          0
    Evaporation       0
    Sunshine          3
    WindGustDir       3
    WindGustSpeed     2
    WindDir9am       31
    WindDir3pm        1
    WindSpeed9am      7
    WindSpeed3pm      0
    Humidity9am       0
    Humidity3pm       0
    Pressure9am       0
    Pressure3pm       0
    Cloud9am          0
    Cloud3pm          0
    Temp9am           0
    Temp3pm           0
    RainToday         0
    RISK_MM           0
    RainTomorrow      0
    dtype: int64



### In this Data_Frame has NULL values so first of all we have to clean it and then we will apply any kind of operations.

- In above cell we have got null values in following columns :-
 Sunshine          3
 WindGustDir       3
 WindGustSpeed     2
 WindDir9am       31
 WindDir3pm        1
 WindSpeed9am      7
- So we have to remove null values by using drop command.


```python
# drop null values
d.dropna(inplace=True)
```

# After removing null values.


```python
pd.isnull(d).sum()
```




    MinTemp          0
    MaxTemp          0
    Rainfall         0
    Evaporation      0
    Sunshine         0
    WindGustDir      0
    WindGustSpeed    0
    WindDir9am       0
    WindDir3pm       0
    WindSpeed9am     0
    WindSpeed3pm     0
    Humidity9am      0
    Humidity3pm      0
    Pressure9am      0
    Pressure3pm      0
    Cloud9am         0
    Cloud3pm         0
    Temp9am          0
    Temp3pm          0
    RainToday        0
    RISK_MM          0
    RainTomorrow     0
    dtype: int64



# Operation - 1

Rename Column


```python
# Syntax
# d.rename('columns={'Old_Name_Of_Column':'New_Name_Of_Column'})
# Rename Temporary
d.rename(columns={'WindGustDir':'WindGustDirection'})
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>MinTemp</th>
      <th>MaxTemp</th>
      <th>Rainfall</th>
      <th>Evaporation</th>
      <th>Sunshine</th>
      <th>WindGustDirection</th>
      <th>WindGustSpeed</th>
      <th>WindDir9am</th>
      <th>WindDir3pm</th>
      <th>WindSpeed9am</th>
      <th>...</th>
      <th>Humidity3pm</th>
      <th>Pressure9am</th>
      <th>Pressure3pm</th>
      <th>Cloud9am</th>
      <th>Cloud3pm</th>
      <th>Temp9am</th>
      <th>Temp3pm</th>
      <th>RainToday</th>
      <th>RISK_MM</th>
      <th>RainTomorrow</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>8.0</td>
      <td>24.3</td>
      <td>0.0</td>
      <td>3.4</td>
      <td>6.3</td>
      <td>NW</td>
      <td>30.0</td>
      <td>SW</td>
      <td>NW</td>
      <td>6.0</td>
      <td>...</td>
      <td>29</td>
      <td>1019.7</td>
      <td>1015.0</td>
      <td>7</td>
      <td>7</td>
      <td>14.4</td>
      <td>23.6</td>
      <td>No</td>
      <td>3.6</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>1</th>
      <td>14.0</td>
      <td>26.9</td>
      <td>3.6</td>
      <td>4.4</td>
      <td>9.7</td>
      <td>ENE</td>
      <td>39.0</td>
      <td>E</td>
      <td>W</td>
      <td>4.0</td>
      <td>...</td>
      <td>36</td>
      <td>1012.4</td>
      <td>1008.4</td>
      <td>5</td>
      <td>3</td>
      <td>17.5</td>
      <td>25.7</td>
      <td>Yes</td>
      <td>3.6</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>2</th>
      <td>13.7</td>
      <td>23.4</td>
      <td>3.6</td>
      <td>5.8</td>
      <td>3.3</td>
      <td>NW</td>
      <td>85.0</td>
      <td>N</td>
      <td>NNE</td>
      <td>6.0</td>
      <td>...</td>
      <td>69</td>
      <td>1009.5</td>
      <td>1007.2</td>
      <td>8</td>
      <td>7</td>
      <td>15.4</td>
      <td>20.2</td>
      <td>Yes</td>
      <td>39.8</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>3</th>
      <td>13.3</td>
      <td>15.5</td>
      <td>39.8</td>
      <td>7.2</td>
      <td>9.1</td>
      <td>NW</td>
      <td>54.0</td>
      <td>WNW</td>
      <td>W</td>
      <td>30.0</td>
      <td>...</td>
      <td>56</td>
      <td>1005.5</td>
      <td>1007.0</td>
      <td>2</td>
      <td>7</td>
      <td>13.5</td>
      <td>14.1</td>
      <td>Yes</td>
      <td>2.8</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>4</th>
      <td>7.6</td>
      <td>16.1</td>
      <td>2.8</td>
      <td>5.6</td>
      <td>10.6</td>
      <td>SSE</td>
      <td>50.0</td>
      <td>SSE</td>
      <td>ESE</td>
      <td>20.0</td>
      <td>...</td>
      <td>49</td>
      <td>1018.3</td>
      <td>1018.5</td>
      <td>7</td>
      <td>7</td>
      <td>11.1</td>
      <td>15.4</td>
      <td>Yes</td>
      <td>0.0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>361</th>
      <td>9.0</td>
      <td>30.7</td>
      <td>0.0</td>
      <td>7.6</td>
      <td>12.1</td>
      <td>NNW</td>
      <td>76.0</td>
      <td>SSE</td>
      <td>NW</td>
      <td>7.0</td>
      <td>...</td>
      <td>15</td>
      <td>1016.1</td>
      <td>1010.8</td>
      <td>1</td>
      <td>3</td>
      <td>20.4</td>
      <td>30.0</td>
      <td>No</td>
      <td>0.0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>362</th>
      <td>7.1</td>
      <td>28.4</td>
      <td>0.0</td>
      <td>11.6</td>
      <td>12.7</td>
      <td>N</td>
      <td>48.0</td>
      <td>NNW</td>
      <td>NNW</td>
      <td>2.0</td>
      <td>...</td>
      <td>22</td>
      <td>1020.0</td>
      <td>1016.9</td>
      <td>0</td>
      <td>1</td>
      <td>17.2</td>
      <td>28.2</td>
      <td>No</td>
      <td>0.0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>363</th>
      <td>12.5</td>
      <td>19.9</td>
      <td>0.0</td>
      <td>8.4</td>
      <td>5.3</td>
      <td>ESE</td>
      <td>43.0</td>
      <td>ENE</td>
      <td>ENE</td>
      <td>11.0</td>
      <td>...</td>
      <td>47</td>
      <td>1024.0</td>
      <td>1022.8</td>
      <td>3</td>
      <td>2</td>
      <td>14.5</td>
      <td>18.3</td>
      <td>No</td>
      <td>0.0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>364</th>
      <td>12.5</td>
      <td>26.9</td>
      <td>0.0</td>
      <td>5.0</td>
      <td>7.1</td>
      <td>NW</td>
      <td>46.0</td>
      <td>SSW</td>
      <td>WNW</td>
      <td>6.0</td>
      <td>...</td>
      <td>39</td>
      <td>1021.0</td>
      <td>1016.2</td>
      <td>6</td>
      <td>7</td>
      <td>15.8</td>
      <td>25.9</td>
      <td>No</td>
      <td>0.0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>365</th>
      <td>12.3</td>
      <td>30.2</td>
      <td>0.0</td>
      <td>6.0</td>
      <td>12.6</td>
      <td>NW</td>
      <td>78.0</td>
      <td>NW</td>
      <td>WNW</td>
      <td>31.0</td>
      <td>...</td>
      <td>13</td>
      <td>1009.6</td>
      <td>1009.2</td>
      <td>1</td>
      <td>1</td>
      <td>23.8</td>
      <td>28.6</td>
      <td>No</td>
      <td>0.0</td>
      <td>No</td>
    </tr>
  </tbody>
</table>
<p>328 rows × 22 columns</p>
</div>




```python
# Above Command Rename Temporary
d.head(2)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>MinTemp</th>
      <th>MaxTemp</th>
      <th>Rainfall</th>
      <th>Evaporation</th>
      <th>Sunshine</th>
      <th>WindGustDir</th>
      <th>WindGustSpeed</th>
      <th>WindDir9am</th>
      <th>WindDir3pm</th>
      <th>WindSpeed9am</th>
      <th>...</th>
      <th>Humidity3pm</th>
      <th>Pressure9am</th>
      <th>Pressure3pm</th>
      <th>Cloud9am</th>
      <th>Cloud3pm</th>
      <th>Temp9am</th>
      <th>Temp3pm</th>
      <th>RainToday</th>
      <th>RISK_MM</th>
      <th>RainTomorrow</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>8.0</td>
      <td>24.3</td>
      <td>0.0</td>
      <td>3.4</td>
      <td>6.3</td>
      <td>NW</td>
      <td>30.0</td>
      <td>SW</td>
      <td>NW</td>
      <td>6.0</td>
      <td>...</td>
      <td>29</td>
      <td>1019.7</td>
      <td>1015.0</td>
      <td>7</td>
      <td>7</td>
      <td>14.4</td>
      <td>23.6</td>
      <td>No</td>
      <td>3.6</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>1</th>
      <td>14.0</td>
      <td>26.9</td>
      <td>3.6</td>
      <td>4.4</td>
      <td>9.7</td>
      <td>ENE</td>
      <td>39.0</td>
      <td>E</td>
      <td>W</td>
      <td>4.0</td>
      <td>...</td>
      <td>36</td>
      <td>1012.4</td>
      <td>1008.4</td>
      <td>5</td>
      <td>3</td>
      <td>17.5</td>
      <td>25.7</td>
      <td>Yes</td>
      <td>3.6</td>
      <td>Yes</td>
    </tr>
  </tbody>
</table>
<p>2 rows × 22 columns</p>
</div>




```python
# To Rename Permanently
# Syntax
# d.rename('columns={Old_Name_Of_Column':'New_Name_Of_Column'},inplace=True)
d.rename(columns={'WindGustDir':'WindGustDirection'},inplace=True) # Rename Permanently
```


```python
# see again it is changed or not?
d.head(2)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>MinTemp</th>
      <th>MaxTemp</th>
      <th>Rainfall</th>
      <th>Evaporation</th>
      <th>Sunshine</th>
      <th>WindGustDirection</th>
      <th>WindGustSpeed</th>
      <th>WindDir9am</th>
      <th>WindDir3pm</th>
      <th>WindSpeed9am</th>
      <th>...</th>
      <th>Humidity3pm</th>
      <th>Pressure9am</th>
      <th>Pressure3pm</th>
      <th>Cloud9am</th>
      <th>Cloud3pm</th>
      <th>Temp9am</th>
      <th>Temp3pm</th>
      <th>RainToday</th>
      <th>RISK_MM</th>
      <th>RainTomorrow</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>8.0</td>
      <td>24.3</td>
      <td>0.0</td>
      <td>3.4</td>
      <td>6.3</td>
      <td>NW</td>
      <td>30.0</td>
      <td>SW</td>
      <td>NW</td>
      <td>6.0</td>
      <td>...</td>
      <td>29</td>
      <td>1019.7</td>
      <td>1015.0</td>
      <td>7</td>
      <td>7</td>
      <td>14.4</td>
      <td>23.6</td>
      <td>No</td>
      <td>3.6</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>1</th>
      <td>14.0</td>
      <td>26.9</td>
      <td>3.6</td>
      <td>4.4</td>
      <td>9.7</td>
      <td>ENE</td>
      <td>39.0</td>
      <td>E</td>
      <td>W</td>
      <td>4.0</td>
      <td>...</td>
      <td>36</td>
      <td>1012.4</td>
      <td>1008.4</td>
      <td>5</td>
      <td>3</td>
      <td>17.5</td>
      <td>25.7</td>
      <td>Yes</td>
      <td>3.6</td>
      <td>Yes</td>
    </tr>
  </tbody>
</table>
<p>2 rows × 22 columns</p>
</div>



# Operation - 2

Calculation of Mean


```python
# Syntax
# d.Column_name.mean()
d.MinTemp.mean()
```




    7.7429878048780525




```python
d.MaxTemp.mean()
```




    20.897560975609757




```python
d.mean()
```

    C:\Users\kumar\AppData\Local\Temp\ipykernel_14252\1214089992.py:1: FutureWarning: Dropping of nuisance columns in DataFrame reductions (with 'numeric_only=None') is deprecated; in a future version this will raise TypeError.  Select only valid columns before calling the reduction.
      d.mean()
    




    MinTemp             7.742988
    MaxTemp            20.897561
    Rainfall            1.440854
    Evaporation         4.702439
    Sunshine            8.014939
    WindGustSpeed      40.396341
    WindSpeed9am       10.414634
    WindSpeed3pm       18.185976
    Humidity9am        71.100610
    Humidity3pm        44.003049
    Pressure9am      1019.350000
    Pressure3pm      1016.530793
    Cloud9am            3.905488
    Cloud3pm            4.000000
    Temp9am            12.815549
    Temp3pm            19.556402
    RISK_MM             1.422561
    dtype: float64




```python
d.groupby('MinTemp').mean()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>MaxTemp</th>
      <th>Rainfall</th>
      <th>Evaporation</th>
      <th>Sunshine</th>
      <th>WindGustSpeed</th>
      <th>WindSpeed9am</th>
      <th>WindSpeed3pm</th>
      <th>Humidity9am</th>
      <th>Humidity3pm</th>
      <th>Pressure9am</th>
      <th>Pressure3pm</th>
      <th>Cloud9am</th>
      <th>Cloud3pm</th>
      <th>Temp9am</th>
      <th>Temp3pm</th>
      <th>RISK_MM</th>
    </tr>
    <tr>
      <th>MinTemp</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>-5.3</th>
      <td>13.10</td>
      <td>0.0</td>
      <td>2.2</td>
      <td>7.90</td>
      <td>33.0</td>
      <td>4.0</td>
      <td>20.0</td>
      <td>94.0</td>
      <td>47.0</td>
      <td>1029.60</td>
      <td>1025.60</td>
      <td>6.0</td>
      <td>6.0</td>
      <td>0.10</td>
      <td>12.2</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>-3.7</th>
      <td>14.55</td>
      <td>0.0</td>
      <td>3.0</td>
      <td>10.65</td>
      <td>32.5</td>
      <td>5.5</td>
      <td>16.5</td>
      <td>58.5</td>
      <td>26.5</td>
      <td>1028.40</td>
      <td>1024.45</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>5.35</td>
      <td>13.7</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>-3.5</th>
      <td>9.40</td>
      <td>0.2</td>
      <td>2.0</td>
      <td>6.20</td>
      <td>38.0</td>
      <td>18.0</td>
      <td>17.5</td>
      <td>84.0</td>
      <td>58.0</td>
      <td>1024.15</td>
      <td>1021.85</td>
      <td>4.5</td>
      <td>5.5</td>
      <td>3.45</td>
      <td>7.6</td>
      <td>0.2</td>
    </tr>
    <tr>
      <th>-3.4</th>
      <td>12.50</td>
      <td>0.0</td>
      <td>3.0</td>
      <td>6.80</td>
      <td>48.0</td>
      <td>7.0</td>
      <td>30.0</td>
      <td>89.0</td>
      <td>30.0</td>
      <td>1025.20</td>
      <td>1021.80</td>
      <td>6.0</td>
      <td>7.0</td>
      <td>1.40</td>
      <td>11.2</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>-3.1</th>
      <td>12.00</td>
      <td>0.0</td>
      <td>1.8</td>
      <td>3.90</td>
      <td>35.0</td>
      <td>4.0</td>
      <td>13.0</td>
      <td>80.0</td>
      <td>52.0</td>
      <td>1030.50</td>
      <td>1030.00</td>
      <td>1.0</td>
      <td>6.0</td>
      <td>5.90</td>
      <td>10.2</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>17.9</th>
      <td>33.55</td>
      <td>0.0</td>
      <td>10.4</td>
      <td>10.10</td>
      <td>52.5</td>
      <td>10.5</td>
      <td>15.5</td>
      <td>65.0</td>
      <td>42.0</td>
      <td>1012.95</td>
      <td>1010.35</td>
      <td>3.5</td>
      <td>4.0</td>
      <td>22.15</td>
      <td>27.9</td>
      <td>2.4</td>
    </tr>
    <tr>
      <th>18.0</th>
      <td>34.90</td>
      <td>0.0</td>
      <td>9.2</td>
      <td>9.90</td>
      <td>69.0</td>
      <td>6.0</td>
      <td>13.0</td>
      <td>68.0</td>
      <td>29.0</td>
      <td>1018.00</td>
      <td>1013.70</td>
      <td>1.0</td>
      <td>6.0</td>
      <td>22.20</td>
      <td>33.1</td>
      <td>5.2</td>
    </tr>
    <tr>
      <th>18.2</th>
      <td>22.60</td>
      <td>1.8</td>
      <td>8.0</td>
      <td>0.00</td>
      <td>33.0</td>
      <td>7.0</td>
      <td>13.0</td>
      <td>92.0</td>
      <td>76.0</td>
      <td>1014.40</td>
      <td>1011.50</td>
      <td>8.0</td>
      <td>8.0</td>
      <td>18.50</td>
      <td>22.1</td>
      <td>9.0</td>
    </tr>
    <tr>
      <th>19.9</th>
      <td>22.00</td>
      <td>11.0</td>
      <td>4.4</td>
      <td>5.90</td>
      <td>76.0</td>
      <td>41.0</td>
      <td>30.0</td>
      <td>92.0</td>
      <td>62.0</td>
      <td>996.50</td>
      <td>996.80</td>
      <td>8.0</td>
      <td>3.0</td>
      <td>20.60</td>
      <td>19.6</td>
      <td>17.4</td>
    </tr>
    <tr>
      <th>20.9</th>
      <td>35.70</td>
      <td>0.0</td>
      <td>13.8</td>
      <td>6.90</td>
      <td>50.0</td>
      <td>4.0</td>
      <td>17.0</td>
      <td>61.0</td>
      <td>28.0</td>
      <td>1007.60</td>
      <td>1003.00</td>
      <td>7.0</td>
      <td>2.0</td>
      <td>23.60</td>
      <td>34.0</td>
      <td>2.0</td>
    </tr>
  </tbody>
</table>
<p>170 rows × 16 columns</p>
</div>



# Operation - 3

Calculation of Standard Deviation


```python
# Syntax
# d.Column_name.std()
d.MinTemp.std()
```




    5.945199248454697




```python
d.MaxTemp.std()
```




    6.7073099127283315




```python
d.std()
```

    C:\Users\kumar\AppData\Local\Temp\ipykernel_14252\4080983771.py:1: FutureWarning: Dropping of nuisance columns in DataFrame reductions (with 'numeric_only=None') is deprecated; in a future version this will raise TypeError.  Select only valid columns before calling the reduction.
      d.std()
    




    MinTemp           5.945199
    MaxTemp           6.707310
    Rainfall          4.289427
    Evaporation       2.681183
    Sunshine          3.506646
    WindGustSpeed    13.132176
    WindSpeed9am      7.811544
    WindSpeed3pm      8.926759
    Humidity9am      12.983367
    Humidity3pm      16.605975
    Pressure9am       6.715244
    Pressure3pm       6.469774
    Cloud9am          2.974957
    Cloud3pm          2.652101
    Temp9am           5.542521
    Temp3pm           6.644311
    RISK_MM           4.234023
    dtype: float64



# Operation - 4

Calculation of Variance


```python
# Syntax
# d.Column_name.var()
d.MinTemp.var()
```




    35.3453941038263




```python
d.MaxTemp.var()
```




    44.98800626538374




```python
d.var()
```

    C:\Users\kumar\AppData\Local\Temp\ipykernel_14252\3511739826.py:1: FutureWarning: Dropping of nuisance columns in DataFrame reductions (with 'numeric_only=None') is deprecated; in a future version this will raise TypeError.  Select only valid columns before calling the reduction.
      d.var()
    




    MinTemp           35.345394
    MaxTemp           44.988006
    Rainfall          18.399182
    Evaporation        7.188740
    Sunshine          12.296565
    WindGustSpeed    172.454054
    WindSpeed9am      61.020213
    WindSpeed3pm      79.687020
    Humidity9am      168.567828
    Humidity3pm      275.758400
    Pressure9am       45.094495
    Pressure3pm       41.857979
    Cloud9am           8.850367
    Cloud3pm           7.033639
    Temp9am           30.719543
    Temp3pm           44.146870
    RISK_MM           17.926951
    dtype: float64



# Operation - 5

Calculation of Median


```python
# Syntax
# d.Column_name.median()
d.MinTemp.median()
```




    7.9




```python
d.MaxTemp.median()
```




    20.4




```python
d.median()
```

    C:\Users\kumar\AppData\Local\Temp\ipykernel_14252\3286961719.py:1: FutureWarning: Dropping of nuisance columns in DataFrame reductions (with 'numeric_only=None') is deprecated; in a future version this will raise TypeError.  Select only valid columns before calling the reduction.
      d.median()
    




    MinTemp             7.90
    MaxTemp            20.40
    Rainfall            0.00
    Evaporation         4.40
    Sunshine            8.75
    WindGustSpeed      39.00
    WindSpeed9am        7.00
    WindSpeed3pm       17.00
    Humidity9am        71.00
    Humidity3pm        42.50
    Pressure9am      1019.75
    Pressure3pm      1016.90
    Cloud9am            4.00
    Cloud3pm            4.00
    Temp9am            13.50
    Temp3pm            18.85
    RISK_MM             0.00
    dtype: float64



# Operation - 6

Calculation of Mode


```python
# Syntax
# d.Column_name.mode()
d.MinTemp.mode()
```




    0    4.4
    Name: MinTemp, dtype: float64




```python
d.mode()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>MinTemp</th>
      <th>MaxTemp</th>
      <th>Rainfall</th>
      <th>Evaporation</th>
      <th>Sunshine</th>
      <th>WindGustDirection</th>
      <th>WindGustSpeed</th>
      <th>WindDir9am</th>
      <th>WindDir3pm</th>
      <th>WindSpeed9am</th>
      <th>...</th>
      <th>Humidity3pm</th>
      <th>Pressure9am</th>
      <th>Pressure3pm</th>
      <th>Cloud9am</th>
      <th>Cloud3pm</th>
      <th>Temp9am</th>
      <th>Temp3pm</th>
      <th>RainToday</th>
      <th>RISK_MM</th>
      <th>RainTomorrow</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>4.4</td>
      <td>11.6</td>
      <td>0.0</td>
      <td>2.8</td>
      <td>0.0</td>
      <td>NW</td>
      <td>39.0</td>
      <td>SE</td>
      <td>NW</td>
      <td>6.0</td>
      <td>...</td>
      <td>34.0</td>
      <td>1023.2</td>
      <td>1019.3</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>14.0</td>
      <td>11.1</td>
      <td>No</td>
      <td>0.0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>1</th>
      <td>NaN</td>
      <td>14.7</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>8.4</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>1025.7</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>NaN</td>
      <td>14.8</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>NaN</td>
      <td>18.9</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>4 rows × 22 columns</p>
</div>



# Operation - 7

Calculation of Kurtosis


```python
# Syntax
# d.Column_name.kurt()
# for single attribute
d.MinTemp.kurt()
```




    -1.0678732874693733




```python
# For complete attributers
d.kurt()
```

    C:\Users\kumar\AppData\Local\Temp\ipykernel_14252\1413420561.py:2: FutureWarning: Dropping of nuisance columns in DataFrame reductions (with 'numeric_only=None') is deprecated; in a future version this will raise TypeError.  Select only valid columns before calling the reduction.
      d.kurt()
    




    MinTemp          -1.067873
    MaxTemp          -0.751754
    Rainfall         27.611392
    Evaporation      -0.216054
    Sunshine         -0.266922
    WindGustSpeed     1.594871
    WindSpeed9am      1.535232
    WindSpeed3pm      0.265588
    Humidity9am      -0.145622
    Humidity3pm      -0.118062
    Pressure9am      -0.088998
    Pressure3pm       0.000914
    Cloud9am         -1.719883
    Cloud3pm         -1.621962
    Temp9am          -0.881008
    Temp3pm          -0.670370
    RISK_MM          28.557778
    dtype: float64



# Operation - 8

Calculation of Skewness


```python
# Syntax
# d.Column_name.skew()
d.MinTemp.skew()
```




    -0.07365803681446856




```python
# For complete attributers
d.skew()
```

    C:\Users\kumar\AppData\Local\Temp\ipykernel_14252\3048699516.py:2: FutureWarning: Dropping of nuisance columns in DataFrame reductions (with 'numeric_only=None') is deprecated; in a future version this will raise TypeError.  Select only valid columns before calling the reduction.
      d.skew()
    




    MinTemp         -0.073658
    MaxTemp          0.297350
    Rainfall         4.679845
    Evaporation      0.598352
    Sunshine        -0.737128
    WindGustSpeed    0.891562
    WindSpeed9am     1.430616
    WindSpeed3pm     0.646106
    Humidity9am     -0.091999
    Humidity3pm      0.539732
    Pressure9am     -0.331647
    Pressure3pm     -0.267506
    Cloud9am         0.078980
    Cloud3pm         0.080163
    Temp9am         -0.094301
    Temp3pm          0.263944
    RISK_MM          4.723079
    dtype: float64



# Operation - 9

Calculation of Correlation


```python
# Syntax
# d.corr()
d.corr()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>MinTemp</th>
      <th>MaxTemp</th>
      <th>Rainfall</th>
      <th>Evaporation</th>
      <th>Sunshine</th>
      <th>WindGustSpeed</th>
      <th>WindSpeed9am</th>
      <th>WindSpeed3pm</th>
      <th>Humidity9am</th>
      <th>Humidity3pm</th>
      <th>Pressure9am</th>
      <th>Pressure3pm</th>
      <th>Cloud9am</th>
      <th>Cloud3pm</th>
      <th>Temp9am</th>
      <th>Temp3pm</th>
      <th>RISK_MM</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>MinTemp</th>
      <td>1.000000</td>
      <td>0.745911</td>
      <td>0.197339</td>
      <td>0.634720</td>
      <td>0.007730</td>
      <td>0.190596</td>
      <td>0.058319</td>
      <td>-0.106321</td>
      <td>-0.160781</td>
      <td>-0.013897</td>
      <td>-0.502352</td>
      <td>-0.503255</td>
      <td>0.211640</td>
      <td>0.125914</td>
      <td>0.910805</td>
      <td>0.716051</td>
      <td>0.251519</td>
    </tr>
    <tr>
      <th>MaxTemp</th>
      <td>0.745911</td>
      <td>1.000000</td>
      <td>-0.077263</td>
      <td>0.673162</td>
      <td>0.444863</td>
      <td>0.070911</td>
      <td>-0.296485</td>
      <td>-0.219886</td>
      <td>-0.325106</td>
      <td>-0.520412</td>
      <td>-0.268054</td>
      <td>-0.367040</td>
      <td>-0.187416</td>
      <td>-0.144976</td>
      <td>0.869609</td>
      <td>0.988925</td>
      <td>0.058638</td>
    </tr>
    <tr>
      <th>Rainfall</th>
      <td>0.197339</td>
      <td>-0.077263</td>
      <td>1.000000</td>
      <td>-0.011767</td>
      <td>-0.158062</td>
      <td>0.099442</td>
      <td>0.238705</td>
      <td>0.058151</td>
      <td>0.146321</td>
      <td>0.287244</td>
      <td>-0.348731</td>
      <td>-0.263710</td>
      <td>0.172610</td>
      <td>0.134894</td>
      <td>0.071893</td>
      <td>-0.089740</td>
      <td>0.101909</td>
    </tr>
    <tr>
      <th>Evaporation</th>
      <td>0.634720</td>
      <td>0.673162</td>
      <td>-0.011767</td>
      <td>1.000000</td>
      <td>0.310124</td>
      <td>0.258050</td>
      <td>0.006259</td>
      <td>0.019594</td>
      <td>-0.492218</td>
      <td>-0.374532</td>
      <td>-0.363936</td>
      <td>-0.380702</td>
      <td>-0.114261</td>
      <td>-0.111387</td>
      <td>0.688749</td>
      <td>0.655896</td>
      <td>0.099727</td>
    </tr>
    <tr>
      <th>Sunshine</th>
      <td>0.007730</td>
      <td>0.444863</td>
      <td>-0.158062</td>
      <td>0.310124</td>
      <td>1.000000</td>
      <td>0.084768</td>
      <td>-0.103841</td>
      <td>0.046140</td>
      <td>-0.501596</td>
      <td>-0.760267</td>
      <td>0.025630</td>
      <td>-0.024120</td>
      <td>-0.697603</td>
      <td>-0.657198</td>
      <td>0.199659</td>
      <td>0.463721</td>
      <td>-0.357231</td>
    </tr>
    <tr>
      <th>WindGustSpeed</th>
      <td>0.190596</td>
      <td>0.070911</td>
      <td>0.099442</td>
      <td>0.258050</td>
      <td>0.084768</td>
      <td>1.000000</td>
      <td>0.540717</td>
      <td>0.687071</td>
      <td>-0.338276</td>
      <td>-0.043254</td>
      <td>-0.524737</td>
      <td>-0.510826</td>
      <td>-0.018216</td>
      <td>0.042849</td>
      <td>0.229164</td>
      <td>0.036039</td>
      <td>0.269151</td>
    </tr>
    <tr>
      <th>WindSpeed9am</th>
      <td>0.058319</td>
      <td>-0.296485</td>
      <td>0.238705</td>
      <td>0.006259</td>
      <td>-0.103841</td>
      <td>0.540717</td>
      <td>1.000000</td>
      <td>0.495946</td>
      <td>-0.222337</td>
      <td>0.202122</td>
      <td>-0.344290</td>
      <td>-0.233682</td>
      <td>0.117625</td>
      <td>-0.012990</td>
      <td>-0.017843</td>
      <td>-0.315906</td>
      <td>0.053529</td>
    </tr>
    <tr>
      <th>WindSpeed3pm</th>
      <td>-0.106321</td>
      <td>-0.219886</td>
      <td>0.058151</td>
      <td>0.019594</td>
      <td>0.046140</td>
      <td>0.687071</td>
      <td>0.495946</td>
      <td>1.000000</td>
      <td>-0.260960</td>
      <td>0.015860</td>
      <td>-0.344889</td>
      <td>-0.318008</td>
      <td>-0.033882</td>
      <td>0.011625</td>
      <td>-0.057454</td>
      <td>-0.239119</td>
      <td>0.012931</td>
    </tr>
    <tr>
      <th>Humidity9am</th>
      <td>-0.160781</td>
      <td>-0.325106</td>
      <td>0.146321</td>
      <td>-0.492218</td>
      <td>-0.501596</td>
      <td>-0.338276</td>
      <td>-0.222337</td>
      <td>-0.260960</td>
      <td>1.000000</td>
      <td>0.526695</td>
      <td>0.102250</td>
      <td>0.109549</td>
      <td>0.417496</td>
      <td>0.289618</td>
      <td>-0.395647</td>
      <td>-0.321299</td>
      <td>0.157148</td>
    </tr>
    <tr>
      <th>Humidity3pm</th>
      <td>-0.013897</td>
      <td>-0.520412</td>
      <td>0.287244</td>
      <td>-0.374532</td>
      <td>-0.760267</td>
      <td>-0.043254</td>
      <td>0.202122</td>
      <td>0.015860</td>
      <td>0.526695</td>
      <td>1.000000</td>
      <td>-0.136289</td>
      <td>-0.047607</td>
      <td>0.565174</td>
      <td>0.530715</td>
      <td>-0.230820</td>
      <td>-0.569348</td>
      <td>0.323494</td>
    </tr>
    <tr>
      <th>Pressure9am</th>
      <td>-0.502352</td>
      <td>-0.268054</td>
      <td>-0.348731</td>
      <td>-0.363936</td>
      <td>0.025630</td>
      <td>-0.524737</td>
      <td>-0.344290</td>
      <td>-0.344889</td>
      <td>0.102250</td>
      <td>-0.136289</td>
      <td>1.000000</td>
      <td>0.966744</td>
      <td>-0.168316</td>
      <td>-0.146196</td>
      <td>-0.453669</td>
      <td>-0.229817</td>
      <td>-0.314815</td>
    </tr>
    <tr>
      <th>Pressure3pm</th>
      <td>-0.503255</td>
      <td>-0.367040</td>
      <td>-0.263710</td>
      <td>-0.380702</td>
      <td>-0.024120</td>
      <td>-0.510826</td>
      <td>-0.233682</td>
      <td>-0.318008</td>
      <td>0.109549</td>
      <td>-0.047607</td>
      <td>0.966744</td>
      <td>1.000000</td>
      <td>-0.132247</td>
      <td>-0.146235</td>
      <td>-0.496853</td>
      <td>-0.332099</td>
      <td>-0.336461</td>
    </tr>
    <tr>
      <th>Cloud9am</th>
      <td>0.211640</td>
      <td>-0.187416</td>
      <td>0.172610</td>
      <td>-0.114261</td>
      <td>-0.697603</td>
      <td>-0.018216</td>
      <td>0.117625</td>
      <td>-0.033882</td>
      <td>0.417496</td>
      <td>0.565174</td>
      <td>-0.168316</td>
      <td>-0.132247</td>
      <td>1.000000</td>
      <td>0.528296</td>
      <td>0.010012</td>
      <td>-0.213509</td>
      <td>0.268979</td>
    </tr>
    <tr>
      <th>Cloud3pm</th>
      <td>0.125914</td>
      <td>-0.144976</td>
      <td>0.134894</td>
      <td>-0.111387</td>
      <td>-0.657198</td>
      <td>0.042849</td>
      <td>-0.012990</td>
      <td>0.011625</td>
      <td>0.289618</td>
      <td>0.530715</td>
      <td>-0.146196</td>
      <td>-0.146235</td>
      <td>0.528296</td>
      <td>1.000000</td>
      <td>0.044542</td>
      <td>-0.181667</td>
      <td>0.311882</td>
    </tr>
    <tr>
      <th>Temp9am</th>
      <td>0.910805</td>
      <td>0.869609</td>
      <td>0.071893</td>
      <td>0.688749</td>
      <td>0.199659</td>
      <td>0.229164</td>
      <td>-0.017843</td>
      <td>-0.057454</td>
      <td>-0.395647</td>
      <td>-0.230820</td>
      <td>-0.453669</td>
      <td>-0.496853</td>
      <td>0.010012</td>
      <td>0.044542</td>
      <td>1.000000</td>
      <td>0.843509</td>
      <td>0.201508</td>
    </tr>
    <tr>
      <th>Temp3pm</th>
      <td>0.716051</td>
      <td>0.988925</td>
      <td>-0.089740</td>
      <td>0.655896</td>
      <td>0.463721</td>
      <td>0.036039</td>
      <td>-0.315906</td>
      <td>-0.239119</td>
      <td>-0.321299</td>
      <td>-0.569348</td>
      <td>-0.229817</td>
      <td>-0.332099</td>
      <td>-0.213509</td>
      <td>-0.181667</td>
      <td>0.843509</td>
      <td>1.000000</td>
      <td>0.028888</td>
    </tr>
    <tr>
      <th>RISK_MM</th>
      <td>0.251519</td>
      <td>0.058638</td>
      <td>0.101909</td>
      <td>0.099727</td>
      <td>-0.357231</td>
      <td>0.269151</td>
      <td>0.053529</td>
      <td>0.012931</td>
      <td>0.157148</td>
      <td>0.323494</td>
      <td>-0.314815</td>
      <td>-0.336461</td>
      <td>0.268979</td>
      <td>0.311882</td>
      <td>0.201508</td>
      <td>0.028888</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
</div>



# Operation - 10

FILTER

We are filtring the records where the attribute RainTomorrow has only Yes.


```python
# Syntax
# d[d['Column_name']=='value']

d[d['RainTomorrow']=='Yes']
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>MinTemp</th>
      <th>MaxTemp</th>
      <th>Rainfall</th>
      <th>Evaporation</th>
      <th>Sunshine</th>
      <th>WindGustDirection</th>
      <th>WindGustSpeed</th>
      <th>WindDir9am</th>
      <th>WindDir3pm</th>
      <th>WindSpeed9am</th>
      <th>...</th>
      <th>Humidity3pm</th>
      <th>Pressure9am</th>
      <th>Pressure3pm</th>
      <th>Cloud9am</th>
      <th>Cloud3pm</th>
      <th>Temp9am</th>
      <th>Temp3pm</th>
      <th>RainToday</th>
      <th>RISK_MM</th>
      <th>RainTomorrow</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>8.0</td>
      <td>24.3</td>
      <td>0.0</td>
      <td>3.4</td>
      <td>6.3</td>
      <td>NW</td>
      <td>30.0</td>
      <td>SW</td>
      <td>NW</td>
      <td>6.0</td>
      <td>...</td>
      <td>29</td>
      <td>1019.7</td>
      <td>1015.0</td>
      <td>7</td>
      <td>7</td>
      <td>14.4</td>
      <td>23.6</td>
      <td>No</td>
      <td>3.6</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>1</th>
      <td>14.0</td>
      <td>26.9</td>
      <td>3.6</td>
      <td>4.4</td>
      <td>9.7</td>
      <td>ENE</td>
      <td>39.0</td>
      <td>E</td>
      <td>W</td>
      <td>4.0</td>
      <td>...</td>
      <td>36</td>
      <td>1012.4</td>
      <td>1008.4</td>
      <td>5</td>
      <td>3</td>
      <td>17.5</td>
      <td>25.7</td>
      <td>Yes</td>
      <td>3.6</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>2</th>
      <td>13.7</td>
      <td>23.4</td>
      <td>3.6</td>
      <td>5.8</td>
      <td>3.3</td>
      <td>NW</td>
      <td>85.0</td>
      <td>N</td>
      <td>NNE</td>
      <td>6.0</td>
      <td>...</td>
      <td>69</td>
      <td>1009.5</td>
      <td>1007.2</td>
      <td>8</td>
      <td>7</td>
      <td>15.4</td>
      <td>20.2</td>
      <td>Yes</td>
      <td>39.8</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>3</th>
      <td>13.3</td>
      <td>15.5</td>
      <td>39.8</td>
      <td>7.2</td>
      <td>9.1</td>
      <td>NW</td>
      <td>54.0</td>
      <td>WNW</td>
      <td>W</td>
      <td>30.0</td>
      <td>...</td>
      <td>56</td>
      <td>1005.5</td>
      <td>1007.0</td>
      <td>2</td>
      <td>7</td>
      <td>13.5</td>
      <td>14.1</td>
      <td>Yes</td>
      <td>2.8</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>8</th>
      <td>8.8</td>
      <td>19.5</td>
      <td>0.0</td>
      <td>4.0</td>
      <td>4.1</td>
      <td>S</td>
      <td>48.0</td>
      <td>E</td>
      <td>ENE</td>
      <td>19.0</td>
      <td>...</td>
      <td>48</td>
      <td>1026.1</td>
      <td>1022.7</td>
      <td>7</td>
      <td>7</td>
      <td>14.1</td>
      <td>18.9</td>
      <td>No</td>
      <td>16.2</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>16</th>
      <td>13.8</td>
      <td>31.2</td>
      <td>0.0</td>
      <td>7.2</td>
      <td>8.4</td>
      <td>ESE</td>
      <td>44.0</td>
      <td>WSW</td>
      <td>W</td>
      <td>6.0</td>
      <td>...</td>
      <td>23</td>
      <td>1014.4</td>
      <td>1009.8</td>
      <td>7</td>
      <td>6</td>
      <td>20.2</td>
      <td>29.8</td>
      <td>No</td>
      <td>1.2</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>21</th>
      <td>16.4</td>
      <td>19.4</td>
      <td>0.4</td>
      <td>9.2</td>
      <td>0.0</td>
      <td>E</td>
      <td>26.0</td>
      <td>ENE</td>
      <td>E</td>
      <td>6.0</td>
      <td>...</td>
      <td>72</td>
      <td>1010.7</td>
      <td>1008.9</td>
      <td>8</td>
      <td>8</td>
      <td>16.5</td>
      <td>18.3</td>
      <td>No</td>
      <td>25.8</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>29</th>
      <td>13.6</td>
      <td>24.1</td>
      <td>0.4</td>
      <td>2.6</td>
      <td>0.5</td>
      <td>NNW</td>
      <td>30.0</td>
      <td>SSW</td>
      <td>S</td>
      <td>6.0</td>
      <td>...</td>
      <td>49</td>
      <td>1017.2</td>
      <td>1013.3</td>
      <td>8</td>
      <td>7</td>
      <td>17.3</td>
      <td>23.2</td>
      <td>No</td>
      <td>22.6</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>30</th>
      <td>15.1</td>
      <td>20.4</td>
      <td>22.6</td>
      <td>2.4</td>
      <td>0.2</td>
      <td>SSE</td>
      <td>41.0</td>
      <td>E</td>
      <td>S</td>
      <td>6.0</td>
      <td>...</td>
      <td>90</td>
      <td>1015.0</td>
      <td>1014.1</td>
      <td>8</td>
      <td>8</td>
      <td>17.0</td>
      <td>16.3</td>
      <td>Yes</td>
      <td>4.2</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>32</th>
      <td>16.6</td>
      <td>24.2</td>
      <td>0.2</td>
      <td>6.6</td>
      <td>4.7</td>
      <td>NW</td>
      <td>50.0</td>
      <td>WNW</td>
      <td>NW</td>
      <td>13.0</td>
      <td>...</td>
      <td>60</td>
      <td>1007.9</td>
      <td>1004.6</td>
      <td>7</td>
      <td>7</td>
      <td>20.5</td>
      <td>19.9</td>
      <td>No</td>
      <td>6.6</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>36</th>
      <td>17.2</td>
      <td>25.8</td>
      <td>0.0</td>
      <td>4.2</td>
      <td>8.8</td>
      <td>SW</td>
      <td>41.0</td>
      <td>NW</td>
      <td>N</td>
      <td>6.0</td>
      <td>...</td>
      <td>74</td>
      <td>1014.5</td>
      <td>1011.5</td>
      <td>6</td>
      <td>7</td>
      <td>21.5</td>
      <td>22.6</td>
      <td>No</td>
      <td>4.0</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>44</th>
      <td>10.1</td>
      <td>29.9</td>
      <td>0.0</td>
      <td>6.8</td>
      <td>8.8</td>
      <td>E</td>
      <td>41.0</td>
      <td>SE</td>
      <td>WNW</td>
      <td>2.0</td>
      <td>...</td>
      <td>36</td>
      <td>1012.6</td>
      <td>1010.2</td>
      <td>1</td>
      <td>8</td>
      <td>17.4</td>
      <td>29.1</td>
      <td>No</td>
      <td>5.4</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>45</th>
      <td>15.5</td>
      <td>21.1</td>
      <td>5.4</td>
      <td>6.4</td>
      <td>0.9</td>
      <td>S</td>
      <td>31.0</td>
      <td>SSE</td>
      <td>NE</td>
      <td>6.0</td>
      <td>...</td>
      <td>86</td>
      <td>1010.1</td>
      <td>1008.6</td>
      <td>8</td>
      <td>8</td>
      <td>16.6</td>
      <td>20.0</td>
      <td>Yes</td>
      <td>1.4</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>48</th>
      <td>12.8</td>
      <td>21.0</td>
      <td>0.0</td>
      <td>6.4</td>
      <td>0.8</td>
      <td>NE</td>
      <td>22.0</td>
      <td>NE</td>
      <td>ENE</td>
      <td>7.0</td>
      <td>...</td>
      <td>54</td>
      <td>1018.0</td>
      <td>1015.6</td>
      <td>8</td>
      <td>8</td>
      <td>16.1</td>
      <td>20.0</td>
      <td>No</td>
      <td>3.4</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>49</th>
      <td>12.6</td>
      <td>23.1</td>
      <td>3.4</td>
      <td>1.6</td>
      <td>2.3</td>
      <td>NNW</td>
      <td>30.0</td>
      <td>N</td>
      <td>NW</td>
      <td>4.0</td>
      <td>...</td>
      <td>74</td>
      <td>1015.8</td>
      <td>1014.1</td>
      <td>8</td>
      <td>7</td>
      <td>15.3</td>
      <td>20.4</td>
      <td>Yes</td>
      <td>6.4</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>50</th>
      <td>14.8</td>
      <td>29.5</td>
      <td>6.4</td>
      <td>1.8</td>
      <td>8.1</td>
      <td>N</td>
      <td>41.0</td>
      <td>NW</td>
      <td>NW</td>
      <td>6.0</td>
      <td>...</td>
      <td>48</td>
      <td>1012.9</td>
      <td>1008.3</td>
      <td>2</td>
      <td>7</td>
      <td>21.0</td>
      <td>28.2</td>
      <td>Yes</td>
      <td>11.0</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>51</th>
      <td>19.9</td>
      <td>22.0</td>
      <td>11.0</td>
      <td>4.4</td>
      <td>5.9</td>
      <td>NNW</td>
      <td>76.0</td>
      <td>N</td>
      <td>WNW</td>
      <td>41.0</td>
      <td>...</td>
      <td>62</td>
      <td>996.5</td>
      <td>996.8</td>
      <td>8</td>
      <td>3</td>
      <td>20.6</td>
      <td>19.6</td>
      <td>Yes</td>
      <td>17.4</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>53</th>
      <td>12.4</td>
      <td>24.4</td>
      <td>0.0</td>
      <td>6.2</td>
      <td>12.1</td>
      <td>NW</td>
      <td>44.0</td>
      <td>NNW</td>
      <td>WNW</td>
      <td>7.0</td>
      <td>...</td>
      <td>43</td>
      <td>1012.8</td>
      <td>1009.7</td>
      <td>6</td>
      <td>4</td>
      <td>15.0</td>
      <td>22.5</td>
      <td>No</td>
      <td>3.4</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>56</th>
      <td>14.3</td>
      <td>26.7</td>
      <td>0.0</td>
      <td>7.2</td>
      <td>7.1</td>
      <td>NNW</td>
      <td>65.0</td>
      <td>N</td>
      <td>NNW</td>
      <td>7.0</td>
      <td>...</td>
      <td>64</td>
      <td>1017.3</td>
      <td>1014.3</td>
      <td>7</td>
      <td>7</td>
      <td>19.8</td>
      <td>19.0</td>
      <td>No</td>
      <td>14.4</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>72</th>
      <td>20.9</td>
      <td>35.7</td>
      <td>0.0</td>
      <td>13.8</td>
      <td>6.9</td>
      <td>SW</td>
      <td>50.0</td>
      <td>E</td>
      <td>WNW</td>
      <td>4.0</td>
      <td>...</td>
      <td>28</td>
      <td>1007.6</td>
      <td>1003.0</td>
      <td>7</td>
      <td>2</td>
      <td>23.6</td>
      <td>34.0</td>
      <td>No</td>
      <td>2.0</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>76</th>
      <td>17.9</td>
      <td>33.2</td>
      <td>0.0</td>
      <td>10.4</td>
      <td>8.4</td>
      <td>N</td>
      <td>59.0</td>
      <td>N</td>
      <td>NNE</td>
      <td>15.0</td>
      <td>...</td>
      <td>62</td>
      <td>1008.5</td>
      <td>1006.1</td>
      <td>6</td>
      <td>7</td>
      <td>24.5</td>
      <td>23.5</td>
      <td>No</td>
      <td>4.8</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>78</th>
      <td>15.1</td>
      <td>20.4</td>
      <td>0.0</td>
      <td>9.6</td>
      <td>0.1</td>
      <td>ESE</td>
      <td>39.0</td>
      <td>ESE</td>
      <td>ESE</td>
      <td>17.0</td>
      <td>...</td>
      <td>55</td>
      <td>1017.5</td>
      <td>1015.8</td>
      <td>8</td>
      <td>8</td>
      <td>17.8</td>
      <td>19.4</td>
      <td>No</td>
      <td>18.8</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>79</th>
      <td>15.3</td>
      <td>19.6</td>
      <td>18.8</td>
      <td>5.0</td>
      <td>0.0</td>
      <td>NE</td>
      <td>33.0</td>
      <td>SSE</td>
      <td>NNE</td>
      <td>9.0</td>
      <td>...</td>
      <td>88</td>
      <td>1008.7</td>
      <td>1006.0</td>
      <td>8</td>
      <td>8</td>
      <td>18.0</td>
      <td>18.6</td>
      <td>Yes</td>
      <td>12.2</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>90</th>
      <td>18.0</td>
      <td>34.9</td>
      <td>0.0</td>
      <td>9.2</td>
      <td>9.9</td>
      <td>NW</td>
      <td>69.0</td>
      <td>N</td>
      <td>W</td>
      <td>6.0</td>
      <td>...</td>
      <td>29</td>
      <td>1018.0</td>
      <td>1013.7</td>
      <td>1</td>
      <td>6</td>
      <td>22.2</td>
      <td>33.1</td>
      <td>No</td>
      <td>5.2</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>91</th>
      <td>17.6</td>
      <td>27.8</td>
      <td>5.2</td>
      <td>10.2</td>
      <td>3.6</td>
      <td>ESE</td>
      <td>39.0</td>
      <td>N</td>
      <td>NNW</td>
      <td>13.0</td>
      <td>...</td>
      <td>49</td>
      <td>1014.6</td>
      <td>1012.8</td>
      <td>7</td>
      <td>8</td>
      <td>21.4</td>
      <td>26.3</td>
      <td>Yes</td>
      <td>2.2</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>94</th>
      <td>17.1</td>
      <td>29.6</td>
      <td>0.0</td>
      <td>5.8</td>
      <td>9.2</td>
      <td>E</td>
      <td>48.0</td>
      <td>SE</td>
      <td>ESE</td>
      <td>9.0</td>
      <td>...</td>
      <td>38</td>
      <td>1016.7</td>
      <td>1012.8</td>
      <td>6</td>
      <td>7</td>
      <td>21.7</td>
      <td>29.1</td>
      <td>No</td>
      <td>1.8</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>95</th>
      <td>18.2</td>
      <td>22.6</td>
      <td>1.8</td>
      <td>8.0</td>
      <td>0.0</td>
      <td>ENE</td>
      <td>33.0</td>
      <td>SSE</td>
      <td>ENE</td>
      <td>7.0</td>
      <td>...</td>
      <td>76</td>
      <td>1014.4</td>
      <td>1011.5</td>
      <td>8</td>
      <td>8</td>
      <td>18.5</td>
      <td>22.1</td>
      <td>Yes</td>
      <td>9.0</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>98</th>
      <td>14.5</td>
      <td>24.2</td>
      <td>0.0</td>
      <td>6.8</td>
      <td>5.9</td>
      <td>SSW</td>
      <td>61.0</td>
      <td>N</td>
      <td>NNW</td>
      <td>11.0</td>
      <td>...</td>
      <td>76</td>
      <td>999.4</td>
      <td>998.9</td>
      <td>7</td>
      <td>7</td>
      <td>17.9</td>
      <td>20.3</td>
      <td>No</td>
      <td>16.2</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>102</th>
      <td>8.9</td>
      <td>26.0</td>
      <td>0.0</td>
      <td>5.0</td>
      <td>10.7</td>
      <td>NE</td>
      <td>31.0</td>
      <td>SE</td>
      <td>NE</td>
      <td>7.0</td>
      <td>...</td>
      <td>34</td>
      <td>1016.1</td>
      <td>1011.7</td>
      <td>1</td>
      <td>5</td>
      <td>14.6</td>
      <td>24.2</td>
      <td>No</td>
      <td>4.4</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>103</th>
      <td>14.5</td>
      <td>24.2</td>
      <td>4.4</td>
      <td>6.6</td>
      <td>5.9</td>
      <td>W</td>
      <td>48.0</td>
      <td>NNW</td>
      <td>WNW</td>
      <td>9.0</td>
      <td>...</td>
      <td>60</td>
      <td>1010.8</td>
      <td>1006.8</td>
      <td>8</td>
      <td>5</td>
      <td>15.8</td>
      <td>22.6</td>
      <td>Yes</td>
      <td>11.0</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>111</th>
      <td>12.0</td>
      <td>28.9</td>
      <td>0.0</td>
      <td>7.2</td>
      <td>8.2</td>
      <td>ESE</td>
      <td>39.0</td>
      <td>SSE</td>
      <td>WNW</td>
      <td>2.0</td>
      <td>...</td>
      <td>31</td>
      <td>1012.2</td>
      <td>1009.1</td>
      <td>2</td>
      <td>7</td>
      <td>17.4</td>
      <td>28.6</td>
      <td>No</td>
      <td>1.8</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>112</th>
      <td>16.3</td>
      <td>24.8</td>
      <td>1.8</td>
      <td>7.8</td>
      <td>3.8</td>
      <td>S</td>
      <td>50.0</td>
      <td>NNW</td>
      <td>N</td>
      <td>4.0</td>
      <td>...</td>
      <td>56</td>
      <td>1011.8</td>
      <td>1008.4</td>
      <td>7</td>
      <td>7</td>
      <td>17.5</td>
      <td>24.0</td>
      <td>Yes</td>
      <td>6.6</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>119</th>
      <td>14.8</td>
      <td>17.3</td>
      <td>0.0</td>
      <td>7.6</td>
      <td>0.8</td>
      <td>SSE</td>
      <td>48.0</td>
      <td>S</td>
      <td>SE</td>
      <td>13.0</td>
      <td>...</td>
      <td>78</td>
      <td>1010.0</td>
      <td>1009.9</td>
      <td>7</td>
      <td>7</td>
      <td>15.7</td>
      <td>15.3</td>
      <td>No</td>
      <td>10.4</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>144</th>
      <td>15.5</td>
      <td>22.4</td>
      <td>0.6</td>
      <td>4.8</td>
      <td>1.9</td>
      <td>NW</td>
      <td>28.0</td>
      <td>SSE</td>
      <td>WNW</td>
      <td>6.0</td>
      <td>...</td>
      <td>68</td>
      <td>1018.7</td>
      <td>1015.4</td>
      <td>8</td>
      <td>7</td>
      <td>17.1</td>
      <td>21.1</td>
      <td>No</td>
      <td>6.4</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>145</th>
      <td>13.1</td>
      <td>17.4</td>
      <td>6.4</td>
      <td>2.8</td>
      <td>0.0</td>
      <td>NNW</td>
      <td>43.0</td>
      <td>N</td>
      <td>N</td>
      <td>11.0</td>
      <td>...</td>
      <td>93</td>
      <td>1010.2</td>
      <td>1006.5</td>
      <td>8</td>
      <td>8</td>
      <td>16.4</td>
      <td>16.6</td>
      <td>Yes</td>
      <td>19.8</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>153</th>
      <td>5.3</td>
      <td>23.3</td>
      <td>0.0</td>
      <td>3.6</td>
      <td>5.6</td>
      <td>NNW</td>
      <td>83.0</td>
      <td>SSW</td>
      <td>NW</td>
      <td>2.0</td>
      <td>...</td>
      <td>26</td>
      <td>1018.0</td>
      <td>1010.5</td>
      <td>1</td>
      <td>8</td>
      <td>9.5</td>
      <td>22.5</td>
      <td>No</td>
      <td>2.6</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>163</th>
      <td>6.1</td>
      <td>24.1</td>
      <td>0.0</td>
      <td>4.6</td>
      <td>6.1</td>
      <td>WNW</td>
      <td>35.0</td>
      <td>SSW</td>
      <td>WNW</td>
      <td>6.0</td>
      <td>...</td>
      <td>32</td>
      <td>1019.2</td>
      <td>1015.8</td>
      <td>7</td>
      <td>3</td>
      <td>11.5</td>
      <td>23.7</td>
      <td>No</td>
      <td>2.0</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>164</th>
      <td>7.1</td>
      <td>19.8</td>
      <td>2.0</td>
      <td>3.2</td>
      <td>7.7</td>
      <td>W</td>
      <td>39.0</td>
      <td>SSE</td>
      <td>NW</td>
      <td>13.0</td>
      <td>...</td>
      <td>56</td>
      <td>1018.4</td>
      <td>1013.8</td>
      <td>5</td>
      <td>2</td>
      <td>10.7</td>
      <td>19.1</td>
      <td>Yes</td>
      <td>5.2</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>178</th>
      <td>7.9</td>
      <td>18.7</td>
      <td>0.0</td>
      <td>5.8</td>
      <td>5.8</td>
      <td>NW</td>
      <td>59.0</td>
      <td>NNW</td>
      <td>NW</td>
      <td>26.0</td>
      <td>...</td>
      <td>51</td>
      <td>1003.2</td>
      <td>997.7</td>
      <td>6</td>
      <td>6</td>
      <td>14.4</td>
      <td>16.6</td>
      <td>No</td>
      <td>7.2</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>196</th>
      <td>-0.4</td>
      <td>17.9</td>
      <td>0.0</td>
      <td>2.4</td>
      <td>8.7</td>
      <td>NW</td>
      <td>33.0</td>
      <td>NNE</td>
      <td>NW</td>
      <td>2.0</td>
      <td>...</td>
      <td>40</td>
      <td>1023.5</td>
      <td>1018.7</td>
      <td>1</td>
      <td>2</td>
      <td>6.8</td>
      <td>17.7</td>
      <td>No</td>
      <td>1.8</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>206</th>
      <td>-0.3</td>
      <td>17.5</td>
      <td>0.0</td>
      <td>1.6</td>
      <td>8.4</td>
      <td>W</td>
      <td>39.0</td>
      <td>SE</td>
      <td>NNW</td>
      <td>6.0</td>
      <td>...</td>
      <td>48</td>
      <td>1025.5</td>
      <td>1021.8</td>
      <td>1</td>
      <td>5</td>
      <td>6.2</td>
      <td>17.2</td>
      <td>No</td>
      <td>3.8</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>207</th>
      <td>4.7</td>
      <td>18.5</td>
      <td>3.8</td>
      <td>2.0</td>
      <td>5.1</td>
      <td>ESE</td>
      <td>22.0</td>
      <td>NNW</td>
      <td>W</td>
      <td>6.0</td>
      <td>...</td>
      <td>50</td>
      <td>1026.6</td>
      <td>1023.1</td>
      <td>7</td>
      <td>4</td>
      <td>7.0</td>
      <td>17.9</td>
      <td>Yes</td>
      <td>5.2</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>215</th>
      <td>9.8</td>
      <td>14.4</td>
      <td>0.8</td>
      <td>0.6</td>
      <td>0.0</td>
      <td>ESE</td>
      <td>20.0</td>
      <td>S</td>
      <td>ESE</td>
      <td>9.0</td>
      <td>...</td>
      <td>86</td>
      <td>1028.5</td>
      <td>1027.2</td>
      <td>8</td>
      <td>8</td>
      <td>12.1</td>
      <td>13.6</td>
      <td>No</td>
      <td>3.8</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>231</th>
      <td>4.0</td>
      <td>15.9</td>
      <td>0.0</td>
      <td>0.6</td>
      <td>2.0</td>
      <td>NNW</td>
      <td>17.0</td>
      <td>SE</td>
      <td>SSE</td>
      <td>6.0</td>
      <td>...</td>
      <td>63</td>
      <td>1022.5</td>
      <td>1019.7</td>
      <td>8</td>
      <td>7</td>
      <td>8.4</td>
      <td>14.8</td>
      <td>No</td>
      <td>4.8</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>242</th>
      <td>0.5</td>
      <td>15.4</td>
      <td>0.0</td>
      <td>2.4</td>
      <td>6.4</td>
      <td>W</td>
      <td>70.0</td>
      <td>NW</td>
      <td>NNW</td>
      <td>22.0</td>
      <td>...</td>
      <td>68</td>
      <td>1017.2</td>
      <td>1010.2</td>
      <td>1</td>
      <td>7</td>
      <td>9.7</td>
      <td>12.9</td>
      <td>No</td>
      <td>2.0</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>252</th>
      <td>1.8</td>
      <td>8.7</td>
      <td>0.0</td>
      <td>1.8</td>
      <td>1.2</td>
      <td>NW</td>
      <td>65.0</td>
      <td>NW</td>
      <td>NW</td>
      <td>31.0</td>
      <td>...</td>
      <td>85</td>
      <td>1014.6</td>
      <td>1010.5</td>
      <td>7</td>
      <td>7</td>
      <td>6.0</td>
      <td>6.9</td>
      <td>No</td>
      <td>1.6</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>260</th>
      <td>1.3</td>
      <td>10.6</td>
      <td>0.0</td>
      <td>0.8</td>
      <td>5.6</td>
      <td>NW</td>
      <td>46.0</td>
      <td>NNW</td>
      <td>WNW</td>
      <td>24.0</td>
      <td>...</td>
      <td>73</td>
      <td>1010.8</td>
      <td>1009.4</td>
      <td>3</td>
      <td>5</td>
      <td>7.7</td>
      <td>8.2</td>
      <td>No</td>
      <td>1.2</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>269</th>
      <td>-2.3</td>
      <td>9.7</td>
      <td>0.0</td>
      <td>1.4</td>
      <td>1.9</td>
      <td>SSE</td>
      <td>28.0</td>
      <td>SSE</td>
      <td>WSW</td>
      <td>6.0</td>
      <td>...</td>
      <td>66</td>
      <td>1013.8</td>
      <td>1010.0</td>
      <td>7</td>
      <td>7</td>
      <td>1.0</td>
      <td>7.8</td>
      <td>No</td>
      <td>1.4</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>274</th>
      <td>3.0</td>
      <td>9.7</td>
      <td>1.0</td>
      <td>2.6</td>
      <td>0.7</td>
      <td>W</td>
      <td>65.0</td>
      <td>NW</td>
      <td>NW</td>
      <td>19.0</td>
      <td>...</td>
      <td>82</td>
      <td>1005.1</td>
      <td>1001.3</td>
      <td>8</td>
      <td>7</td>
      <td>9.6</td>
      <td>8.6</td>
      <td>No</td>
      <td>6.6</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>280</th>
      <td>-0.6</td>
      <td>11.1</td>
      <td>0.0</td>
      <td>3.0</td>
      <td>5.0</td>
      <td>NNW</td>
      <td>41.0</td>
      <td>SE</td>
      <td>N</td>
      <td>7.0</td>
      <td>...</td>
      <td>78</td>
      <td>1018.4</td>
      <td>1015.9</td>
      <td>7</td>
      <td>7</td>
      <td>3.8</td>
      <td>5.7</td>
      <td>No</td>
      <td>1.2</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>303</th>
      <td>0.5</td>
      <td>16.3</td>
      <td>0.0</td>
      <td>1.8</td>
      <td>4.1</td>
      <td>NNW</td>
      <td>39.0</td>
      <td>SSW</td>
      <td>WSW</td>
      <td>4.0</td>
      <td>...</td>
      <td>45</td>
      <td>1023.7</td>
      <td>1017.5</td>
      <td>7</td>
      <td>8</td>
      <td>6.2</td>
      <td>15.4</td>
      <td>No</td>
      <td>4.0</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>304</th>
      <td>6.1</td>
      <td>17.2</td>
      <td>4.0</td>
      <td>2.2</td>
      <td>2.4</td>
      <td>NW</td>
      <td>59.0</td>
      <td>NW</td>
      <td>WNW</td>
      <td>24.0</td>
      <td>...</td>
      <td>85</td>
      <td>1011.2</td>
      <td>1010.4</td>
      <td>7</td>
      <td>7</td>
      <td>13.5</td>
      <td>12.6</td>
      <td>Yes</td>
      <td>7.4</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>317</th>
      <td>9.0</td>
      <td>25.5</td>
      <td>0.0</td>
      <td>5.6</td>
      <td>10.2</td>
      <td>NW</td>
      <td>50.0</td>
      <td>N</td>
      <td>NW</td>
      <td>20.0</td>
      <td>...</td>
      <td>31</td>
      <td>1015.3</td>
      <td>1011.4</td>
      <td>3</td>
      <td>1</td>
      <td>17.5</td>
      <td>25.1</td>
      <td>No</td>
      <td>9.8</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>318</th>
      <td>13.1</td>
      <td>19.4</td>
      <td>9.8</td>
      <td>8.8</td>
      <td>6.0</td>
      <td>NNW</td>
      <td>67.0</td>
      <td>N</td>
      <td>NW</td>
      <td>39.0</td>
      <td>...</td>
      <td>43</td>
      <td>1007.3</td>
      <td>1006.0</td>
      <td>7</td>
      <td>1</td>
      <td>16.7</td>
      <td>18.2</td>
      <td>Yes</td>
      <td>1.6</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>319</th>
      <td>8.7</td>
      <td>19.7</td>
      <td>1.6</td>
      <td>5.2</td>
      <td>8.0</td>
      <td>NW</td>
      <td>98.0</td>
      <td>NW</td>
      <td>NNW</td>
      <td>31.0</td>
      <td>...</td>
      <td>33</td>
      <td>1009.1</td>
      <td>1001.5</td>
      <td>3</td>
      <td>6</td>
      <td>15.6</td>
      <td>18.5</td>
      <td>Yes</td>
      <td>3.4</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>326</th>
      <td>3.2</td>
      <td>21.9</td>
      <td>0.0</td>
      <td>6.8</td>
      <td>5.2</td>
      <td>NW</td>
      <td>80.0</td>
      <td>SSE</td>
      <td>NW</td>
      <td>2.0</td>
      <td>...</td>
      <td>50</td>
      <td>1012.1</td>
      <td>1006.5</td>
      <td>1</td>
      <td>8</td>
      <td>15.9</td>
      <td>21.0</td>
      <td>No</td>
      <td>17.4</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>337</th>
      <td>16.8</td>
      <td>28.9</td>
      <td>0.0</td>
      <td>10.0</td>
      <td>10.8</td>
      <td>NNW</td>
      <td>70.0</td>
      <td>NW</td>
      <td>NW</td>
      <td>31.0</td>
      <td>...</td>
      <td>22</td>
      <td>1016.3</td>
      <td>1011.8</td>
      <td>1</td>
      <td>1</td>
      <td>22.5</td>
      <td>28.4</td>
      <td>No</td>
      <td>7.6</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>338</th>
      <td>14.4</td>
      <td>20.7</td>
      <td>7.6</td>
      <td>9.4</td>
      <td>4.9</td>
      <td>NNW</td>
      <td>33.0</td>
      <td>NNW</td>
      <td>NNW</td>
      <td>20.0</td>
      <td>...</td>
      <td>65</td>
      <td>1015.5</td>
      <td>1013.2</td>
      <td>8</td>
      <td>4</td>
      <td>14.5</td>
      <td>19.3</td>
      <td>Yes</td>
      <td>3.0</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>340</th>
      <td>11.2</td>
      <td>18.0</td>
      <td>0.0</td>
      <td>4.8</td>
      <td>8.4</td>
      <td>W</td>
      <td>65.0</td>
      <td>N</td>
      <td>W</td>
      <td>24.0</td>
      <td>...</td>
      <td>40</td>
      <td>1009.5</td>
      <td>1005.3</td>
      <td>5</td>
      <td>4</td>
      <td>12.8</td>
      <td>16.2</td>
      <td>No</td>
      <td>8.2</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>347</th>
      <td>6.7</td>
      <td>26.1</td>
      <td>0.0</td>
      <td>6.2</td>
      <td>7.5</td>
      <td>SSW</td>
      <td>70.0</td>
      <td>NE</td>
      <td>NNW</td>
      <td>6.0</td>
      <td>...</td>
      <td>47</td>
      <td>1020.9</td>
      <td>1016.0</td>
      <td>4</td>
      <td>7</td>
      <td>16.3</td>
      <td>23.2</td>
      <td>No</td>
      <td>13.2</td>
      <td>Yes</td>
    </tr>
  </tbody>
</table>
<p>60 rows × 22 columns</p>
</div>



# Operation - 11

FILTER

We are filtring the records where the attribute RainTomorrow has only No.


```python
d[d['RainTomorrow']=='No']
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>MinTemp</th>
      <th>MaxTemp</th>
      <th>Rainfall</th>
      <th>Evaporation</th>
      <th>Sunshine</th>
      <th>WindGustDirection</th>
      <th>WindGustSpeed</th>
      <th>WindDir9am</th>
      <th>WindDir3pm</th>
      <th>WindSpeed9am</th>
      <th>...</th>
      <th>Humidity3pm</th>
      <th>Pressure9am</th>
      <th>Pressure3pm</th>
      <th>Cloud9am</th>
      <th>Cloud3pm</th>
      <th>Temp9am</th>
      <th>Temp3pm</th>
      <th>RainToday</th>
      <th>RISK_MM</th>
      <th>RainTomorrow</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>4</th>
      <td>7.6</td>
      <td>16.1</td>
      <td>2.8</td>
      <td>5.6</td>
      <td>10.6</td>
      <td>SSE</td>
      <td>50.0</td>
      <td>SSE</td>
      <td>ESE</td>
      <td>20.0</td>
      <td>...</td>
      <td>49</td>
      <td>1018.3</td>
      <td>1018.5</td>
      <td>7</td>
      <td>7</td>
      <td>11.1</td>
      <td>15.4</td>
      <td>Yes</td>
      <td>0.0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6.2</td>
      <td>16.9</td>
      <td>0.0</td>
      <td>5.8</td>
      <td>8.2</td>
      <td>SE</td>
      <td>44.0</td>
      <td>SE</td>
      <td>E</td>
      <td>20.0</td>
      <td>...</td>
      <td>57</td>
      <td>1023.8</td>
      <td>1021.7</td>
      <td>7</td>
      <td>5</td>
      <td>10.9</td>
      <td>14.8</td>
      <td>No</td>
      <td>0.2</td>
      <td>No</td>
    </tr>
    <tr>
      <th>6</th>
      <td>6.1</td>
      <td>18.2</td>
      <td>0.2</td>
      <td>4.2</td>
      <td>8.4</td>
      <td>SE</td>
      <td>43.0</td>
      <td>SE</td>
      <td>ESE</td>
      <td>19.0</td>
      <td>...</td>
      <td>47</td>
      <td>1024.6</td>
      <td>1022.2</td>
      <td>4</td>
      <td>6</td>
      <td>12.4</td>
      <td>17.3</td>
      <td>No</td>
      <td>0.0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8.3</td>
      <td>17.0</td>
      <td>0.0</td>
      <td>5.6</td>
      <td>4.6</td>
      <td>E</td>
      <td>41.0</td>
      <td>SE</td>
      <td>E</td>
      <td>11.0</td>
      <td>...</td>
      <td>57</td>
      <td>1026.2</td>
      <td>1024.2</td>
      <td>6</td>
      <td>7</td>
      <td>12.1</td>
      <td>15.5</td>
      <td>No</td>
      <td>0.0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>9</th>
      <td>8.4</td>
      <td>22.8</td>
      <td>16.2</td>
      <td>5.4</td>
      <td>7.7</td>
      <td>E</td>
      <td>31.0</td>
      <td>S</td>
      <td>ESE</td>
      <td>7.0</td>
      <td>...</td>
      <td>32</td>
      <td>1024.1</td>
      <td>1020.7</td>
      <td>7</td>
      <td>1</td>
      <td>13.3</td>
      <td>21.7</td>
      <td>Yes</td>
      <td>0.0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>361</th>
      <td>9.0</td>
      <td>30.7</td>
      <td>0.0</td>
      <td>7.6</td>
      <td>12.1</td>
      <td>NNW</td>
      <td>76.0</td>
      <td>SSE</td>
      <td>NW</td>
      <td>7.0</td>
      <td>...</td>
      <td>15</td>
      <td>1016.1</td>
      <td>1010.8</td>
      <td>1</td>
      <td>3</td>
      <td>20.4</td>
      <td>30.0</td>
      <td>No</td>
      <td>0.0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>362</th>
      <td>7.1</td>
      <td>28.4</td>
      <td>0.0</td>
      <td>11.6</td>
      <td>12.7</td>
      <td>N</td>
      <td>48.0</td>
      <td>NNW</td>
      <td>NNW</td>
      <td>2.0</td>
      <td>...</td>
      <td>22</td>
      <td>1020.0</td>
      <td>1016.9</td>
      <td>0</td>
      <td>1</td>
      <td>17.2</td>
      <td>28.2</td>
      <td>No</td>
      <td>0.0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>363</th>
      <td>12.5</td>
      <td>19.9</td>
      <td>0.0</td>
      <td>8.4</td>
      <td>5.3</td>
      <td>ESE</td>
      <td>43.0</td>
      <td>ENE</td>
      <td>ENE</td>
      <td>11.0</td>
      <td>...</td>
      <td>47</td>
      <td>1024.0</td>
      <td>1022.8</td>
      <td>3</td>
      <td>2</td>
      <td>14.5</td>
      <td>18.3</td>
      <td>No</td>
      <td>0.0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>364</th>
      <td>12.5</td>
      <td>26.9</td>
      <td>0.0</td>
      <td>5.0</td>
      <td>7.1</td>
      <td>NW</td>
      <td>46.0</td>
      <td>SSW</td>
      <td>WNW</td>
      <td>6.0</td>
      <td>...</td>
      <td>39</td>
      <td>1021.0</td>
      <td>1016.2</td>
      <td>6</td>
      <td>7</td>
      <td>15.8</td>
      <td>25.9</td>
      <td>No</td>
      <td>0.0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>365</th>
      <td>12.3</td>
      <td>30.2</td>
      <td>0.0</td>
      <td>6.0</td>
      <td>12.6</td>
      <td>NW</td>
      <td>78.0</td>
      <td>NW</td>
      <td>WNW</td>
      <td>31.0</td>
      <td>...</td>
      <td>13</td>
      <td>1009.6</td>
      <td>1009.2</td>
      <td>1</td>
      <td>1</td>
      <td>23.8</td>
      <td>28.6</td>
      <td>No</td>
      <td>0.0</td>
      <td>No</td>
    </tr>
  </tbody>
</table>
<p>268 rows × 22 columns</p>
</div>



# Operation - 12

Calculation of Minimum Value


```python
# This command will give us minimum value from each column.
d.min()
```




    MinTemp               -5.3
    MaxTemp                7.6
    Rainfall               0.0
    Evaporation            0.2
    Sunshine               0.0
    WindGustDirection        E
    WindGustSpeed         13.0
    WindDir9am               E
    WindDir3pm               E
    WindSpeed9am           2.0
    WindSpeed3pm             4
    Humidity9am             36
    Humidity3pm             13
    Pressure9am          996.5
    Pressure3pm          996.8
    Cloud9am                 0
    Cloud3pm                 0
    Temp9am                0.1
    Temp3pm                5.1
    RainToday               No
    RISK_MM                0.0
    RainTomorrow            No
    dtype: object




```python
# For Particular column
d['RISK_MM'].min()
```




    0.0




```python
d.groupby('MinTemp').min()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>MaxTemp</th>
      <th>Rainfall</th>
      <th>Evaporation</th>
      <th>Sunshine</th>
      <th>WindGustDirection</th>
      <th>WindGustSpeed</th>
      <th>WindDir9am</th>
      <th>WindDir3pm</th>
      <th>WindSpeed9am</th>
      <th>WindSpeed3pm</th>
      <th>...</th>
      <th>Humidity3pm</th>
      <th>Pressure9am</th>
      <th>Pressure3pm</th>
      <th>Cloud9am</th>
      <th>Cloud3pm</th>
      <th>Temp9am</th>
      <th>Temp3pm</th>
      <th>RainToday</th>
      <th>RISK_MM</th>
      <th>RainTomorrow</th>
    </tr>
    <tr>
      <th>MinTemp</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>-5.3</th>
      <td>13.1</td>
      <td>0.0</td>
      <td>2.2</td>
      <td>7.9</td>
      <td>NW</td>
      <td>33.0</td>
      <td>N</td>
      <td>NNW</td>
      <td>4.0</td>
      <td>20</td>
      <td>...</td>
      <td>47</td>
      <td>1029.6</td>
      <td>1025.6</td>
      <td>6</td>
      <td>6</td>
      <td>0.1</td>
      <td>12.2</td>
      <td>No</td>
      <td>0.0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>-3.7</th>
      <td>14.4</td>
      <td>0.0</td>
      <td>2.6</td>
      <td>10.4</td>
      <td>NNW</td>
      <td>22.0</td>
      <td>N</td>
      <td>N</td>
      <td>2.0</td>
      <td>11</td>
      <td>...</td>
      <td>25</td>
      <td>1025.8</td>
      <td>1020.9</td>
      <td>0</td>
      <td>0</td>
      <td>5.2</td>
      <td>13.4</td>
      <td>No</td>
      <td>0.0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>-3.5</th>
      <td>7.6</td>
      <td>0.0</td>
      <td>1.6</td>
      <td>4.7</td>
      <td>ESE</td>
      <td>26.0</td>
      <td>N</td>
      <td>ESE</td>
      <td>6.0</td>
      <td>11</td>
      <td>...</td>
      <td>48</td>
      <td>1014.8</td>
      <td>1012.6</td>
      <td>1</td>
      <td>5</td>
      <td>3.3</td>
      <td>5.1</td>
      <td>No</td>
      <td>0.0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>-3.4</th>
      <td>12.5</td>
      <td>0.0</td>
      <td>3.0</td>
      <td>6.8</td>
      <td>SSE</td>
      <td>48.0</td>
      <td>NNW</td>
      <td>WNW</td>
      <td>7.0</td>
      <td>30</td>
      <td>...</td>
      <td>30</td>
      <td>1025.2</td>
      <td>1021.8</td>
      <td>6</td>
      <td>7</td>
      <td>1.4</td>
      <td>11.2</td>
      <td>No</td>
      <td>0.0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>-3.1</th>
      <td>12.0</td>
      <td>0.0</td>
      <td>1.8</td>
      <td>3.9</td>
      <td>ESE</td>
      <td>35.0</td>
      <td>SSW</td>
      <td>NE</td>
      <td>4.0</td>
      <td>13</td>
      <td>...</td>
      <td>52</td>
      <td>1030.5</td>
      <td>1030.0</td>
      <td>1</td>
      <td>6</td>
      <td>5.9</td>
      <td>10.2</td>
      <td>No</td>
      <td>0.0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>17.9</th>
      <td>33.2</td>
      <td>0.0</td>
      <td>10.4</td>
      <td>8.4</td>
      <td>ENE</td>
      <td>46.0</td>
      <td>N</td>
      <td>NNE</td>
      <td>6.0</td>
      <td>11</td>
      <td>...</td>
      <td>22</td>
      <td>1008.5</td>
      <td>1006.1</td>
      <td>1</td>
      <td>1</td>
      <td>19.8</td>
      <td>23.5</td>
      <td>No</td>
      <td>0.0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>18.0</th>
      <td>34.9</td>
      <td>0.0</td>
      <td>9.2</td>
      <td>9.9</td>
      <td>NW</td>
      <td>69.0</td>
      <td>N</td>
      <td>W</td>
      <td>6.0</td>
      <td>13</td>
      <td>...</td>
      <td>29</td>
      <td>1018.0</td>
      <td>1013.7</td>
      <td>1</td>
      <td>6</td>
      <td>22.2</td>
      <td>33.1</td>
      <td>No</td>
      <td>5.2</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>18.2</th>
      <td>22.6</td>
      <td>1.8</td>
      <td>8.0</td>
      <td>0.0</td>
      <td>ENE</td>
      <td>33.0</td>
      <td>SSE</td>
      <td>ENE</td>
      <td>7.0</td>
      <td>13</td>
      <td>...</td>
      <td>76</td>
      <td>1014.4</td>
      <td>1011.5</td>
      <td>8</td>
      <td>8</td>
      <td>18.5</td>
      <td>22.1</td>
      <td>Yes</td>
      <td>9.0</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>19.9</th>
      <td>22.0</td>
      <td>11.0</td>
      <td>4.4</td>
      <td>5.9</td>
      <td>NNW</td>
      <td>76.0</td>
      <td>N</td>
      <td>WNW</td>
      <td>41.0</td>
      <td>30</td>
      <td>...</td>
      <td>62</td>
      <td>996.5</td>
      <td>996.8</td>
      <td>8</td>
      <td>3</td>
      <td>20.6</td>
      <td>19.6</td>
      <td>Yes</td>
      <td>17.4</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>20.9</th>
      <td>35.7</td>
      <td>0.0</td>
      <td>13.8</td>
      <td>6.9</td>
      <td>SW</td>
      <td>50.0</td>
      <td>E</td>
      <td>WNW</td>
      <td>4.0</td>
      <td>17</td>
      <td>...</td>
      <td>28</td>
      <td>1007.6</td>
      <td>1003.0</td>
      <td>7</td>
      <td>2</td>
      <td>23.6</td>
      <td>34.0</td>
      <td>No</td>
      <td>2.0</td>
      <td>Yes</td>
    </tr>
  </tbody>
</table>
<p>170 rows × 21 columns</p>
</div>



# d.sum()


```python
d.sum()
```




    MinTemp                                                         2539.7
    MaxTemp                                                         6854.4
    Rainfall                                                         472.6
    Evaporation                                                     1542.4
    Sunshine                                                        2628.9
    WindGustDirection    NWENENWNWSSESESEESENEWNWNWNWEESESENEWNWEESENNE...
    WindGustSpeed                                                  13250.0
    WindDir9am           SWENWNWSSESESESEESSEESWNWSSEWSWSWNNENNWNENESWS...
    WindDir3pm           NWWNNEWESEEESEEENEESENWNWNWWWWSWWNEWNNWNWESENE...
    WindSpeed9am                                                    3416.0
    WindSpeed3pm                                                      5965
    Humidity9am                                                      23321
    Humidity3pm                                                      14433
    Pressure9am                                                   334346.8
    Pressure3pm                                                   333422.1
    Cloud9am                                                          1281
    Cloud3pm                                                          1312
    Temp9am                                                         4203.5
    Temp3pm                                                         6414.5
    RainToday            NoYesYesYesYesNoNoNoNoYesNoNoNoNoNoNoNoYesNoNo...
    RISK_MM                                                          466.6
    RainTomorrow         YesYesYesYesNoNoNoNoYesNoNoNoNoNoNoNoYesNoNoNo...
    dtype: object



# d.describe()

- This command will show us count, mean, std, min, max of whole dataframe.


```python
d.describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>MinTemp</th>
      <th>MaxTemp</th>
      <th>Rainfall</th>
      <th>Evaporation</th>
      <th>Sunshine</th>
      <th>WindGustSpeed</th>
      <th>WindSpeed9am</th>
      <th>WindSpeed3pm</th>
      <th>Humidity9am</th>
      <th>Humidity3pm</th>
      <th>Pressure9am</th>
      <th>Pressure3pm</th>
      <th>Cloud9am</th>
      <th>Cloud3pm</th>
      <th>Temp9am</th>
      <th>Temp3pm</th>
      <th>RISK_MM</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>328.000000</td>
      <td>328.000000</td>
      <td>328.000000</td>
      <td>328.000000</td>
      <td>328.000000</td>
      <td>328.000000</td>
      <td>328.000000</td>
      <td>328.000000</td>
      <td>328.000000</td>
      <td>328.000000</td>
      <td>328.000000</td>
      <td>328.000000</td>
      <td>328.000000</td>
      <td>328.000000</td>
      <td>328.000000</td>
      <td>328.000000</td>
      <td>328.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>7.742988</td>
      <td>20.897561</td>
      <td>1.440854</td>
      <td>4.702439</td>
      <td>8.014939</td>
      <td>40.396341</td>
      <td>10.414634</td>
      <td>18.185976</td>
      <td>71.100610</td>
      <td>44.003049</td>
      <td>1019.350000</td>
      <td>1016.530793</td>
      <td>3.905488</td>
      <td>4.000000</td>
      <td>12.815549</td>
      <td>19.556402</td>
      <td>1.422561</td>
    </tr>
    <tr>
      <th>std</th>
      <td>5.945199</td>
      <td>6.707310</td>
      <td>4.289427</td>
      <td>2.681183</td>
      <td>3.506646</td>
      <td>13.132176</td>
      <td>7.811544</td>
      <td>8.926759</td>
      <td>12.983367</td>
      <td>16.605975</td>
      <td>6.715244</td>
      <td>6.469774</td>
      <td>2.974957</td>
      <td>2.652101</td>
      <td>5.542521</td>
      <td>6.644311</td>
      <td>4.234023</td>
    </tr>
    <tr>
      <th>min</th>
      <td>-5.300000</td>
      <td>7.600000</td>
      <td>0.000000</td>
      <td>0.200000</td>
      <td>0.000000</td>
      <td>13.000000</td>
      <td>2.000000</td>
      <td>4.000000</td>
      <td>36.000000</td>
      <td>13.000000</td>
      <td>996.500000</td>
      <td>996.800000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.100000</td>
      <td>5.100000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>2.850000</td>
      <td>15.500000</td>
      <td>0.000000</td>
      <td>2.550000</td>
      <td>6.000000</td>
      <td>31.000000</td>
      <td>6.000000</td>
      <td>11.000000</td>
      <td>63.000000</td>
      <td>32.000000</td>
      <td>1014.800000</td>
      <td>1012.400000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>8.175000</td>
      <td>14.500000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>7.900000</td>
      <td>20.400000</td>
      <td>0.000000</td>
      <td>4.400000</td>
      <td>8.750000</td>
      <td>39.000000</td>
      <td>7.000000</td>
      <td>17.000000</td>
      <td>71.000000</td>
      <td>42.500000</td>
      <td>1019.750000</td>
      <td>1016.900000</td>
      <td>4.000000</td>
      <td>4.000000</td>
      <td>13.500000</td>
      <td>18.850000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>12.800000</td>
      <td>25.800000</td>
      <td>0.200000</td>
      <td>6.600000</td>
      <td>10.700000</td>
      <td>46.000000</td>
      <td>13.000000</td>
      <td>24.000000</td>
      <td>80.000000</td>
      <td>54.000000</td>
      <td>1024.300000</td>
      <td>1021.125000</td>
      <td>7.000000</td>
      <td>7.000000</td>
      <td>17.200000</td>
      <td>24.225000</td>
      <td>0.200000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>20.900000</td>
      <td>35.800000</td>
      <td>39.800000</td>
      <td>13.800000</td>
      <td>13.600000</td>
      <td>98.000000</td>
      <td>41.000000</td>
      <td>52.000000</td>
      <td>99.000000</td>
      <td>93.000000</td>
      <td>1035.700000</td>
      <td>1033.200000</td>
      <td>8.000000</td>
      <td>8.000000</td>
      <td>24.700000</td>
      <td>34.500000</td>
      <td>39.800000</td>
    </tr>
  </tbody>
</table>
</div>



# Operation - 13

Calculation of Maximum Value


```python
# This command will give us maximum value from each column.
d.max()
```




    MinTemp                20.9
    MaxTemp                35.8
    Rainfall               39.8
    Evaporation            13.8
    Sunshine               13.6
    WindGustDirection       WSW
    WindGustSpeed          98.0
    WindDir9am              WSW
    WindDir3pm              WSW
    WindSpeed9am           41.0
    WindSpeed3pm             52
    Humidity9am              99
    Humidity3pm              93
    Pressure9am          1035.7
    Pressure3pm          1033.2
    Cloud9am                  8
    Cloud3pm                  8
    Temp9am                24.7
    Temp3pm                34.5
    RainToday               Yes
    RISK_MM                39.8
    RainTomorrow            Yes
    dtype: object




```python
# For Particular column
d['RISK_MM'].max()
```




    39.8




```python
d.groupby('MinTemp').max()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>MaxTemp</th>
      <th>Rainfall</th>
      <th>Evaporation</th>
      <th>Sunshine</th>
      <th>WindGustDirection</th>
      <th>WindGustSpeed</th>
      <th>WindDir9am</th>
      <th>WindDir3pm</th>
      <th>WindSpeed9am</th>
      <th>WindSpeed3pm</th>
      <th>...</th>
      <th>Humidity3pm</th>
      <th>Pressure9am</th>
      <th>Pressure3pm</th>
      <th>Cloud9am</th>
      <th>Cloud3pm</th>
      <th>Temp9am</th>
      <th>Temp3pm</th>
      <th>RainToday</th>
      <th>RISK_MM</th>
      <th>RainTomorrow</th>
    </tr>
    <tr>
      <th>MinTemp</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>-5.3</th>
      <td>13.1</td>
      <td>0.0</td>
      <td>2.2</td>
      <td>7.9</td>
      <td>NW</td>
      <td>33.0</td>
      <td>N</td>
      <td>NNW</td>
      <td>4.0</td>
      <td>20</td>
      <td>...</td>
      <td>47</td>
      <td>1029.6</td>
      <td>1025.6</td>
      <td>6</td>
      <td>6</td>
      <td>0.1</td>
      <td>12.2</td>
      <td>No</td>
      <td>0.0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>-3.7</th>
      <td>14.7</td>
      <td>0.0</td>
      <td>3.4</td>
      <td>10.9</td>
      <td>SSE</td>
      <td>43.0</td>
      <td>SE</td>
      <td>NNW</td>
      <td>9.0</td>
      <td>22</td>
      <td>...</td>
      <td>28</td>
      <td>1031.0</td>
      <td>1028.0</td>
      <td>0</td>
      <td>0</td>
      <td>5.5</td>
      <td>14.0</td>
      <td>No</td>
      <td>0.0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>-3.5</th>
      <td>11.2</td>
      <td>0.4</td>
      <td>2.4</td>
      <td>7.7</td>
      <td>NW</td>
      <td>50.0</td>
      <td>NW</td>
      <td>NW</td>
      <td>30.0</td>
      <td>24</td>
      <td>...</td>
      <td>68</td>
      <td>1033.5</td>
      <td>1031.1</td>
      <td>8</td>
      <td>6</td>
      <td>3.6</td>
      <td>10.1</td>
      <td>No</td>
      <td>0.4</td>
      <td>No</td>
    </tr>
    <tr>
      <th>-3.4</th>
      <td>12.5</td>
      <td>0.0</td>
      <td>3.0</td>
      <td>6.8</td>
      <td>SSE</td>
      <td>48.0</td>
      <td>NNW</td>
      <td>WNW</td>
      <td>7.0</td>
      <td>30</td>
      <td>...</td>
      <td>30</td>
      <td>1025.2</td>
      <td>1021.8</td>
      <td>6</td>
      <td>7</td>
      <td>1.4</td>
      <td>11.2</td>
      <td>No</td>
      <td>0.0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>-3.1</th>
      <td>12.0</td>
      <td>0.0</td>
      <td>1.8</td>
      <td>3.9</td>
      <td>ESE</td>
      <td>35.0</td>
      <td>SSW</td>
      <td>NE</td>
      <td>4.0</td>
      <td>13</td>
      <td>...</td>
      <td>52</td>
      <td>1030.5</td>
      <td>1030.0</td>
      <td>1</td>
      <td>6</td>
      <td>5.9</td>
      <td>10.2</td>
      <td>No</td>
      <td>0.0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>17.9</th>
      <td>33.9</td>
      <td>0.0</td>
      <td>10.4</td>
      <td>11.8</td>
      <td>N</td>
      <td>59.0</td>
      <td>S</td>
      <td>W</td>
      <td>15.0</td>
      <td>20</td>
      <td>...</td>
      <td>62</td>
      <td>1017.4</td>
      <td>1014.6</td>
      <td>6</td>
      <td>7</td>
      <td>24.5</td>
      <td>32.3</td>
      <td>No</td>
      <td>4.8</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>18.0</th>
      <td>34.9</td>
      <td>0.0</td>
      <td>9.2</td>
      <td>9.9</td>
      <td>NW</td>
      <td>69.0</td>
      <td>N</td>
      <td>W</td>
      <td>6.0</td>
      <td>13</td>
      <td>...</td>
      <td>29</td>
      <td>1018.0</td>
      <td>1013.7</td>
      <td>1</td>
      <td>6</td>
      <td>22.2</td>
      <td>33.1</td>
      <td>No</td>
      <td>5.2</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>18.2</th>
      <td>22.6</td>
      <td>1.8</td>
      <td>8.0</td>
      <td>0.0</td>
      <td>ENE</td>
      <td>33.0</td>
      <td>SSE</td>
      <td>ENE</td>
      <td>7.0</td>
      <td>13</td>
      <td>...</td>
      <td>76</td>
      <td>1014.4</td>
      <td>1011.5</td>
      <td>8</td>
      <td>8</td>
      <td>18.5</td>
      <td>22.1</td>
      <td>Yes</td>
      <td>9.0</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>19.9</th>
      <td>22.0</td>
      <td>11.0</td>
      <td>4.4</td>
      <td>5.9</td>
      <td>NNW</td>
      <td>76.0</td>
      <td>N</td>
      <td>WNW</td>
      <td>41.0</td>
      <td>30</td>
      <td>...</td>
      <td>62</td>
      <td>996.5</td>
      <td>996.8</td>
      <td>8</td>
      <td>3</td>
      <td>20.6</td>
      <td>19.6</td>
      <td>Yes</td>
      <td>17.4</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>20.9</th>
      <td>35.7</td>
      <td>0.0</td>
      <td>13.8</td>
      <td>6.9</td>
      <td>SW</td>
      <td>50.0</td>
      <td>E</td>
      <td>WNW</td>
      <td>4.0</td>
      <td>17</td>
      <td>...</td>
      <td>28</td>
      <td>1007.6</td>
      <td>1003.0</td>
      <td>7</td>
      <td>2</td>
      <td>23.6</td>
      <td>34.0</td>
      <td>No</td>
      <td>2.0</td>
      <td>Yes</td>
    </tr>
  </tbody>
</table>
<p>170 rows × 21 columns</p>
</div>



# Operation - 14

str.contains

# Retrieved data only if RainToday is Yes


```python
d[(d['RainToday'].str.contains('Yes'))]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>MinTemp</th>
      <th>MaxTemp</th>
      <th>Rainfall</th>
      <th>Evaporation</th>
      <th>Sunshine</th>
      <th>WindGustDirection</th>
      <th>WindGustSpeed</th>
      <th>WindDir9am</th>
      <th>WindDir3pm</th>
      <th>WindSpeed9am</th>
      <th>...</th>
      <th>Humidity3pm</th>
      <th>Pressure9am</th>
      <th>Pressure3pm</th>
      <th>Cloud9am</th>
      <th>Cloud3pm</th>
      <th>Temp9am</th>
      <th>Temp3pm</th>
      <th>RainToday</th>
      <th>RISK_MM</th>
      <th>RainTomorrow</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>14.0</td>
      <td>26.9</td>
      <td>3.6</td>
      <td>4.4</td>
      <td>9.7</td>
      <td>ENE</td>
      <td>39.0</td>
      <td>E</td>
      <td>W</td>
      <td>4.0</td>
      <td>...</td>
      <td>36</td>
      <td>1012.4</td>
      <td>1008.4</td>
      <td>5</td>
      <td>3</td>
      <td>17.5</td>
      <td>25.7</td>
      <td>Yes</td>
      <td>3.6</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>2</th>
      <td>13.7</td>
      <td>23.4</td>
      <td>3.6</td>
      <td>5.8</td>
      <td>3.3</td>
      <td>NW</td>
      <td>85.0</td>
      <td>N</td>
      <td>NNE</td>
      <td>6.0</td>
      <td>...</td>
      <td>69</td>
      <td>1009.5</td>
      <td>1007.2</td>
      <td>8</td>
      <td>7</td>
      <td>15.4</td>
      <td>20.2</td>
      <td>Yes</td>
      <td>39.8</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>3</th>
      <td>13.3</td>
      <td>15.5</td>
      <td>39.8</td>
      <td>7.2</td>
      <td>9.1</td>
      <td>NW</td>
      <td>54.0</td>
      <td>WNW</td>
      <td>W</td>
      <td>30.0</td>
      <td>...</td>
      <td>56</td>
      <td>1005.5</td>
      <td>1007.0</td>
      <td>2</td>
      <td>7</td>
      <td>13.5</td>
      <td>14.1</td>
      <td>Yes</td>
      <td>2.8</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>4</th>
      <td>7.6</td>
      <td>16.1</td>
      <td>2.8</td>
      <td>5.6</td>
      <td>10.6</td>
      <td>SSE</td>
      <td>50.0</td>
      <td>SSE</td>
      <td>ESE</td>
      <td>20.0</td>
      <td>...</td>
      <td>49</td>
      <td>1018.3</td>
      <td>1018.5</td>
      <td>7</td>
      <td>7</td>
      <td>11.1</td>
      <td>15.4</td>
      <td>Yes</td>
      <td>0.0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>9</th>
      <td>8.4</td>
      <td>22.8</td>
      <td>16.2</td>
      <td>5.4</td>
      <td>7.7</td>
      <td>E</td>
      <td>31.0</td>
      <td>S</td>
      <td>ESE</td>
      <td>7.0</td>
      <td>...</td>
      <td>32</td>
      <td>1024.1</td>
      <td>1020.7</td>
      <td>7</td>
      <td>1</td>
      <td>13.3</td>
      <td>21.7</td>
      <td>Yes</td>
      <td>0.0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>320</th>
      <td>3.9</td>
      <td>13.2</td>
      <td>3.4</td>
      <td>6.6</td>
      <td>11.0</td>
      <td>WNW</td>
      <td>65.0</td>
      <td>WNW</td>
      <td>WNW</td>
      <td>26.0</td>
      <td>...</td>
      <td>33</td>
      <td>1017.0</td>
      <td>1017.6</td>
      <td>3</td>
      <td>1</td>
      <td>7.1</td>
      <td>12.2</td>
      <td>Yes</td>
      <td>0.0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>327</th>
      <td>7.8</td>
      <td>16.2</td>
      <td>17.4</td>
      <td>6.4</td>
      <td>7.9</td>
      <td>NW</td>
      <td>50.0</td>
      <td>NW</td>
      <td>N</td>
      <td>15.0</td>
      <td>...</td>
      <td>44</td>
      <td>1016.7</td>
      <td>1017.8</td>
      <td>7</td>
      <td>1</td>
      <td>8.0</td>
      <td>14.3</td>
      <td>Yes</td>
      <td>0.0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>338</th>
      <td>14.4</td>
      <td>20.7</td>
      <td>7.6</td>
      <td>9.4</td>
      <td>4.9</td>
      <td>NNW</td>
      <td>33.0</td>
      <td>NNW</td>
      <td>NNW</td>
      <td>20.0</td>
      <td>...</td>
      <td>65</td>
      <td>1015.5</td>
      <td>1013.2</td>
      <td>8</td>
      <td>4</td>
      <td>14.5</td>
      <td>19.3</td>
      <td>Yes</td>
      <td>3.0</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>339</th>
      <td>10.3</td>
      <td>21.3</td>
      <td>3.0</td>
      <td>4.2</td>
      <td>6.7</td>
      <td>NNW</td>
      <td>43.0</td>
      <td>ENE</td>
      <td>N</td>
      <td>7.0</td>
      <td>...</td>
      <td>46</td>
      <td>1018.1</td>
      <td>1013.6</td>
      <td>8</td>
      <td>1</td>
      <td>11.7</td>
      <td>19.8</td>
      <td>Yes</td>
      <td>0.0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>341</th>
      <td>0.3</td>
      <td>16.0</td>
      <td>8.2</td>
      <td>5.4</td>
      <td>11.8</td>
      <td>NW</td>
      <td>57.0</td>
      <td>NNW</td>
      <td>N</td>
      <td>11.0</td>
      <td>...</td>
      <td>45</td>
      <td>1016.8</td>
      <td>1013.3</td>
      <td>1</td>
      <td>1</td>
      <td>6.9</td>
      <td>14.6</td>
      <td>Yes</td>
      <td>0.0</td>
      <td>No</td>
    </tr>
  </tbody>
</table>
<p>61 rows × 22 columns</p>
</div>




```python
d[d['RainToday']=='Yes']
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>MinTemp</th>
      <th>MaxTemp</th>
      <th>Rainfall</th>
      <th>Evaporation</th>
      <th>Sunshine</th>
      <th>WindGustDirection</th>
      <th>WindGustSpeed</th>
      <th>WindDir9am</th>
      <th>WindDir3pm</th>
      <th>WindSpeed9am</th>
      <th>...</th>
      <th>Humidity3pm</th>
      <th>Pressure9am</th>
      <th>Pressure3pm</th>
      <th>Cloud9am</th>
      <th>Cloud3pm</th>
      <th>Temp9am</th>
      <th>Temp3pm</th>
      <th>RainToday</th>
      <th>RISK_MM</th>
      <th>RainTomorrow</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>14.0</td>
      <td>26.9</td>
      <td>3.6</td>
      <td>4.4</td>
      <td>9.7</td>
      <td>ENE</td>
      <td>39.0</td>
      <td>E</td>
      <td>W</td>
      <td>4.0</td>
      <td>...</td>
      <td>36</td>
      <td>1012.4</td>
      <td>1008.4</td>
      <td>5</td>
      <td>3</td>
      <td>17.5</td>
      <td>25.7</td>
      <td>Yes</td>
      <td>3.6</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>2</th>
      <td>13.7</td>
      <td>23.4</td>
      <td>3.6</td>
      <td>5.8</td>
      <td>3.3</td>
      <td>NW</td>
      <td>85.0</td>
      <td>N</td>
      <td>NNE</td>
      <td>6.0</td>
      <td>...</td>
      <td>69</td>
      <td>1009.5</td>
      <td>1007.2</td>
      <td>8</td>
      <td>7</td>
      <td>15.4</td>
      <td>20.2</td>
      <td>Yes</td>
      <td>39.8</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>3</th>
      <td>13.3</td>
      <td>15.5</td>
      <td>39.8</td>
      <td>7.2</td>
      <td>9.1</td>
      <td>NW</td>
      <td>54.0</td>
      <td>WNW</td>
      <td>W</td>
      <td>30.0</td>
      <td>...</td>
      <td>56</td>
      <td>1005.5</td>
      <td>1007.0</td>
      <td>2</td>
      <td>7</td>
      <td>13.5</td>
      <td>14.1</td>
      <td>Yes</td>
      <td>2.8</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>4</th>
      <td>7.6</td>
      <td>16.1</td>
      <td>2.8</td>
      <td>5.6</td>
      <td>10.6</td>
      <td>SSE</td>
      <td>50.0</td>
      <td>SSE</td>
      <td>ESE</td>
      <td>20.0</td>
      <td>...</td>
      <td>49</td>
      <td>1018.3</td>
      <td>1018.5</td>
      <td>7</td>
      <td>7</td>
      <td>11.1</td>
      <td>15.4</td>
      <td>Yes</td>
      <td>0.0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>9</th>
      <td>8.4</td>
      <td>22.8</td>
      <td>16.2</td>
      <td>5.4</td>
      <td>7.7</td>
      <td>E</td>
      <td>31.0</td>
      <td>S</td>
      <td>ESE</td>
      <td>7.0</td>
      <td>...</td>
      <td>32</td>
      <td>1024.1</td>
      <td>1020.7</td>
      <td>7</td>
      <td>1</td>
      <td>13.3</td>
      <td>21.7</td>
      <td>Yes</td>
      <td>0.0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>320</th>
      <td>3.9</td>
      <td>13.2</td>
      <td>3.4</td>
      <td>6.6</td>
      <td>11.0</td>
      <td>WNW</td>
      <td>65.0</td>
      <td>WNW</td>
      <td>WNW</td>
      <td>26.0</td>
      <td>...</td>
      <td>33</td>
      <td>1017.0</td>
      <td>1017.6</td>
      <td>3</td>
      <td>1</td>
      <td>7.1</td>
      <td>12.2</td>
      <td>Yes</td>
      <td>0.0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>327</th>
      <td>7.8</td>
      <td>16.2</td>
      <td>17.4</td>
      <td>6.4</td>
      <td>7.9</td>
      <td>NW</td>
      <td>50.0</td>
      <td>NW</td>
      <td>N</td>
      <td>15.0</td>
      <td>...</td>
      <td>44</td>
      <td>1016.7</td>
      <td>1017.8</td>
      <td>7</td>
      <td>1</td>
      <td>8.0</td>
      <td>14.3</td>
      <td>Yes</td>
      <td>0.0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>338</th>
      <td>14.4</td>
      <td>20.7</td>
      <td>7.6</td>
      <td>9.4</td>
      <td>4.9</td>
      <td>NNW</td>
      <td>33.0</td>
      <td>NNW</td>
      <td>NNW</td>
      <td>20.0</td>
      <td>...</td>
      <td>65</td>
      <td>1015.5</td>
      <td>1013.2</td>
      <td>8</td>
      <td>4</td>
      <td>14.5</td>
      <td>19.3</td>
      <td>Yes</td>
      <td>3.0</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>339</th>
      <td>10.3</td>
      <td>21.3</td>
      <td>3.0</td>
      <td>4.2</td>
      <td>6.7</td>
      <td>NNW</td>
      <td>43.0</td>
      <td>ENE</td>
      <td>N</td>
      <td>7.0</td>
      <td>...</td>
      <td>46</td>
      <td>1018.1</td>
      <td>1013.6</td>
      <td>8</td>
      <td>1</td>
      <td>11.7</td>
      <td>19.8</td>
      <td>Yes</td>
      <td>0.0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>341</th>
      <td>0.3</td>
      <td>16.0</td>
      <td>8.2</td>
      <td>5.4</td>
      <td>11.8</td>
      <td>NW</td>
      <td>57.0</td>
      <td>NNW</td>
      <td>N</td>
      <td>11.0</td>
      <td>...</td>
      <td>45</td>
      <td>1016.8</td>
      <td>1013.3</td>
      <td>1</td>
      <td>1</td>
      <td>6.9</td>
      <td>14.6</td>
      <td>Yes</td>
      <td>0.0</td>
      <td>No</td>
    </tr>
  </tbody>
</table>
<p>61 rows × 22 columns</p>
</div>



# Operation - 15


```python
d[d['RainToday']=='No']
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>MinTemp</th>
      <th>MaxTemp</th>
      <th>Rainfall</th>
      <th>Evaporation</th>
      <th>Sunshine</th>
      <th>WindGustDirection</th>
      <th>WindGustSpeed</th>
      <th>WindDir9am</th>
      <th>WindDir3pm</th>
      <th>WindSpeed9am</th>
      <th>...</th>
      <th>Humidity3pm</th>
      <th>Pressure9am</th>
      <th>Pressure3pm</th>
      <th>Cloud9am</th>
      <th>Cloud3pm</th>
      <th>Temp9am</th>
      <th>Temp3pm</th>
      <th>RainToday</th>
      <th>RISK_MM</th>
      <th>RainTomorrow</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>8.0</td>
      <td>24.3</td>
      <td>0.0</td>
      <td>3.4</td>
      <td>6.3</td>
      <td>NW</td>
      <td>30.0</td>
      <td>SW</td>
      <td>NW</td>
      <td>6.0</td>
      <td>...</td>
      <td>29</td>
      <td>1019.7</td>
      <td>1015.0</td>
      <td>7</td>
      <td>7</td>
      <td>14.4</td>
      <td>23.6</td>
      <td>No</td>
      <td>3.6</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6.2</td>
      <td>16.9</td>
      <td>0.0</td>
      <td>5.8</td>
      <td>8.2</td>
      <td>SE</td>
      <td>44.0</td>
      <td>SE</td>
      <td>E</td>
      <td>20.0</td>
      <td>...</td>
      <td>57</td>
      <td>1023.8</td>
      <td>1021.7</td>
      <td>7</td>
      <td>5</td>
      <td>10.9</td>
      <td>14.8</td>
      <td>No</td>
      <td>0.2</td>
      <td>No</td>
    </tr>
    <tr>
      <th>6</th>
      <td>6.1</td>
      <td>18.2</td>
      <td>0.2</td>
      <td>4.2</td>
      <td>8.4</td>
      <td>SE</td>
      <td>43.0</td>
      <td>SE</td>
      <td>ESE</td>
      <td>19.0</td>
      <td>...</td>
      <td>47</td>
      <td>1024.6</td>
      <td>1022.2</td>
      <td>4</td>
      <td>6</td>
      <td>12.4</td>
      <td>17.3</td>
      <td>No</td>
      <td>0.0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8.3</td>
      <td>17.0</td>
      <td>0.0</td>
      <td>5.6</td>
      <td>4.6</td>
      <td>E</td>
      <td>41.0</td>
      <td>SE</td>
      <td>E</td>
      <td>11.0</td>
      <td>...</td>
      <td>57</td>
      <td>1026.2</td>
      <td>1024.2</td>
      <td>6</td>
      <td>7</td>
      <td>12.1</td>
      <td>15.5</td>
      <td>No</td>
      <td>0.0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>8</th>
      <td>8.8</td>
      <td>19.5</td>
      <td>0.0</td>
      <td>4.0</td>
      <td>4.1</td>
      <td>S</td>
      <td>48.0</td>
      <td>E</td>
      <td>ENE</td>
      <td>19.0</td>
      <td>...</td>
      <td>48</td>
      <td>1026.1</td>
      <td>1022.7</td>
      <td>7</td>
      <td>7</td>
      <td>14.1</td>
      <td>18.9</td>
      <td>No</td>
      <td>16.2</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>361</th>
      <td>9.0</td>
      <td>30.7</td>
      <td>0.0</td>
      <td>7.6</td>
      <td>12.1</td>
      <td>NNW</td>
      <td>76.0</td>
      <td>SSE</td>
      <td>NW</td>
      <td>7.0</td>
      <td>...</td>
      <td>15</td>
      <td>1016.1</td>
      <td>1010.8</td>
      <td>1</td>
      <td>3</td>
      <td>20.4</td>
      <td>30.0</td>
      <td>No</td>
      <td>0.0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>362</th>
      <td>7.1</td>
      <td>28.4</td>
      <td>0.0</td>
      <td>11.6</td>
      <td>12.7</td>
      <td>N</td>
      <td>48.0</td>
      <td>NNW</td>
      <td>NNW</td>
      <td>2.0</td>
      <td>...</td>
      <td>22</td>
      <td>1020.0</td>
      <td>1016.9</td>
      <td>0</td>
      <td>1</td>
      <td>17.2</td>
      <td>28.2</td>
      <td>No</td>
      <td>0.0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>363</th>
      <td>12.5</td>
      <td>19.9</td>
      <td>0.0</td>
      <td>8.4</td>
      <td>5.3</td>
      <td>ESE</td>
      <td>43.0</td>
      <td>ENE</td>
      <td>ENE</td>
      <td>11.0</td>
      <td>...</td>
      <td>47</td>
      <td>1024.0</td>
      <td>1022.8</td>
      <td>3</td>
      <td>2</td>
      <td>14.5</td>
      <td>18.3</td>
      <td>No</td>
      <td>0.0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>364</th>
      <td>12.5</td>
      <td>26.9</td>
      <td>0.0</td>
      <td>5.0</td>
      <td>7.1</td>
      <td>NW</td>
      <td>46.0</td>
      <td>SSW</td>
      <td>WNW</td>
      <td>6.0</td>
      <td>...</td>
      <td>39</td>
      <td>1021.0</td>
      <td>1016.2</td>
      <td>6</td>
      <td>7</td>
      <td>15.8</td>
      <td>25.9</td>
      <td>No</td>
      <td>0.0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>365</th>
      <td>12.3</td>
      <td>30.2</td>
      <td>0.0</td>
      <td>6.0</td>
      <td>12.6</td>
      <td>NW</td>
      <td>78.0</td>
      <td>NW</td>
      <td>WNW</td>
      <td>31.0</td>
      <td>...</td>
      <td>13</td>
      <td>1009.6</td>
      <td>1009.2</td>
      <td>1</td>
      <td>1</td>
      <td>23.8</td>
      <td>28.6</td>
      <td>No</td>
      <td>0.0</td>
      <td>No</td>
    </tr>
  </tbody>
</table>
<p>267 rows × 22 columns</p>
</div>



# If 'RainToday =='No' AND 'Rainfall'==0.0 AND 'RISK_MM'==0.0 Then It May be No Rain Tomorrow


```python
d[(d['RainToday']=='No')&(d['Rainfall']==0.0)&(d['RISK_MM']==0.0)]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>MinTemp</th>
      <th>MaxTemp</th>
      <th>Rainfall</th>
      <th>Evaporation</th>
      <th>Sunshine</th>
      <th>WindGustDirection</th>
      <th>WindGustSpeed</th>
      <th>WindDir9am</th>
      <th>WindDir3pm</th>
      <th>WindSpeed9am</th>
      <th>...</th>
      <th>Humidity3pm</th>
      <th>Pressure9am</th>
      <th>Pressure3pm</th>
      <th>Cloud9am</th>
      <th>Cloud3pm</th>
      <th>Temp9am</th>
      <th>Temp3pm</th>
      <th>RainToday</th>
      <th>RISK_MM</th>
      <th>RainTomorrow</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>7</th>
      <td>8.3</td>
      <td>17.0</td>
      <td>0.0</td>
      <td>5.6</td>
      <td>4.6</td>
      <td>E</td>
      <td>41.0</td>
      <td>SE</td>
      <td>E</td>
      <td>11.0</td>
      <td>...</td>
      <td>57</td>
      <td>1026.2</td>
      <td>1024.2</td>
      <td>6</td>
      <td>7</td>
      <td>12.1</td>
      <td>15.5</td>
      <td>No</td>
      <td>0.0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>12</th>
      <td>10.1</td>
      <td>27.9</td>
      <td>0.0</td>
      <td>7.2</td>
      <td>13.0</td>
      <td>WNW</td>
      <td>30.0</td>
      <td>S</td>
      <td>NW</td>
      <td>6.0</td>
      <td>...</td>
      <td>29</td>
      <td>1022.0</td>
      <td>1017.1</td>
      <td>0</td>
      <td>1</td>
      <td>17.0</td>
      <td>27.1</td>
      <td>No</td>
      <td>0.0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>13</th>
      <td>12.1</td>
      <td>30.9</td>
      <td>0.0</td>
      <td>6.2</td>
      <td>12.4</td>
      <td>NW</td>
      <td>44.0</td>
      <td>WNW</td>
      <td>W</td>
      <td>7.0</td>
      <td>...</td>
      <td>20</td>
      <td>1017.3</td>
      <td>1013.1</td>
      <td>1</td>
      <td>4</td>
      <td>19.7</td>
      <td>30.7</td>
      <td>No</td>
      <td>0.0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>14</th>
      <td>10.1</td>
      <td>31.2</td>
      <td>0.0</td>
      <td>8.8</td>
      <td>13.1</td>
      <td>NW</td>
      <td>41.0</td>
      <td>S</td>
      <td>W</td>
      <td>6.0</td>
      <td>...</td>
      <td>16</td>
      <td>1018.2</td>
      <td>1013.7</td>
      <td>0</td>
      <td>1</td>
      <td>18.7</td>
      <td>30.4</td>
      <td>No</td>
      <td>0.0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>15</th>
      <td>12.4</td>
      <td>32.1</td>
      <td>0.0</td>
      <td>8.4</td>
      <td>11.1</td>
      <td>E</td>
      <td>46.0</td>
      <td>SE</td>
      <td>WSW</td>
      <td>7.0</td>
      <td>...</td>
      <td>22</td>
      <td>1017.9</td>
      <td>1012.8</td>
      <td>0</td>
      <td>3</td>
      <td>19.1</td>
      <td>30.7</td>
      <td>No</td>
      <td>0.0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>361</th>
      <td>9.0</td>
      <td>30.7</td>
      <td>0.0</td>
      <td>7.6</td>
      <td>12.1</td>
      <td>NNW</td>
      <td>76.0</td>
      <td>SSE</td>
      <td>NW</td>
      <td>7.0</td>
      <td>...</td>
      <td>15</td>
      <td>1016.1</td>
      <td>1010.8</td>
      <td>1</td>
      <td>3</td>
      <td>20.4</td>
      <td>30.0</td>
      <td>No</td>
      <td>0.0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>362</th>
      <td>7.1</td>
      <td>28.4</td>
      <td>0.0</td>
      <td>11.6</td>
      <td>12.7</td>
      <td>N</td>
      <td>48.0</td>
      <td>NNW</td>
      <td>NNW</td>
      <td>2.0</td>
      <td>...</td>
      <td>22</td>
      <td>1020.0</td>
      <td>1016.9</td>
      <td>0</td>
      <td>1</td>
      <td>17.2</td>
      <td>28.2</td>
      <td>No</td>
      <td>0.0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>363</th>
      <td>12.5</td>
      <td>19.9</td>
      <td>0.0</td>
      <td>8.4</td>
      <td>5.3</td>
      <td>ESE</td>
      <td>43.0</td>
      <td>ENE</td>
      <td>ENE</td>
      <td>11.0</td>
      <td>...</td>
      <td>47</td>
      <td>1024.0</td>
      <td>1022.8</td>
      <td>3</td>
      <td>2</td>
      <td>14.5</td>
      <td>18.3</td>
      <td>No</td>
      <td>0.0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>364</th>
      <td>12.5</td>
      <td>26.9</td>
      <td>0.0</td>
      <td>5.0</td>
      <td>7.1</td>
      <td>NW</td>
      <td>46.0</td>
      <td>SSW</td>
      <td>WNW</td>
      <td>6.0</td>
      <td>...</td>
      <td>39</td>
      <td>1021.0</td>
      <td>1016.2</td>
      <td>6</td>
      <td>7</td>
      <td>15.8</td>
      <td>25.9</td>
      <td>No</td>
      <td>0.0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>365</th>
      <td>12.3</td>
      <td>30.2</td>
      <td>0.0</td>
      <td>6.0</td>
      <td>12.6</td>
      <td>NW</td>
      <td>78.0</td>
      <td>NW</td>
      <td>WNW</td>
      <td>31.0</td>
      <td>...</td>
      <td>13</td>
      <td>1009.6</td>
      <td>1009.2</td>
      <td>1</td>
      <td>1</td>
      <td>23.8</td>
      <td>28.6</td>
      <td>No</td>
      <td>0.0</td>
      <td>No</td>
    </tr>
  </tbody>
</table>
<p>184 rows × 22 columns</p>
</div>




```python
d[(d['RainToday']=='Yes')&(d['Rainfall']!=0.0)]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>MinTemp</th>
      <th>MaxTemp</th>
      <th>Rainfall</th>
      <th>Evaporation</th>
      <th>Sunshine</th>
      <th>WindGustDirection</th>
      <th>WindGustSpeed</th>
      <th>WindDir9am</th>
      <th>WindDir3pm</th>
      <th>WindSpeed9am</th>
      <th>...</th>
      <th>Humidity3pm</th>
      <th>Pressure9am</th>
      <th>Pressure3pm</th>
      <th>Cloud9am</th>
      <th>Cloud3pm</th>
      <th>Temp9am</th>
      <th>Temp3pm</th>
      <th>RainToday</th>
      <th>RISK_MM</th>
      <th>RainTomorrow</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>14.0</td>
      <td>26.9</td>
      <td>3.6</td>
      <td>4.4</td>
      <td>9.7</td>
      <td>ENE</td>
      <td>39.0</td>
      <td>E</td>
      <td>W</td>
      <td>4.0</td>
      <td>...</td>
      <td>36</td>
      <td>1012.4</td>
      <td>1008.4</td>
      <td>5</td>
      <td>3</td>
      <td>17.5</td>
      <td>25.7</td>
      <td>Yes</td>
      <td>3.6</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>2</th>
      <td>13.7</td>
      <td>23.4</td>
      <td>3.6</td>
      <td>5.8</td>
      <td>3.3</td>
      <td>NW</td>
      <td>85.0</td>
      <td>N</td>
      <td>NNE</td>
      <td>6.0</td>
      <td>...</td>
      <td>69</td>
      <td>1009.5</td>
      <td>1007.2</td>
      <td>8</td>
      <td>7</td>
      <td>15.4</td>
      <td>20.2</td>
      <td>Yes</td>
      <td>39.8</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>3</th>
      <td>13.3</td>
      <td>15.5</td>
      <td>39.8</td>
      <td>7.2</td>
      <td>9.1</td>
      <td>NW</td>
      <td>54.0</td>
      <td>WNW</td>
      <td>W</td>
      <td>30.0</td>
      <td>...</td>
      <td>56</td>
      <td>1005.5</td>
      <td>1007.0</td>
      <td>2</td>
      <td>7</td>
      <td>13.5</td>
      <td>14.1</td>
      <td>Yes</td>
      <td>2.8</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>4</th>
      <td>7.6</td>
      <td>16.1</td>
      <td>2.8</td>
      <td>5.6</td>
      <td>10.6</td>
      <td>SSE</td>
      <td>50.0</td>
      <td>SSE</td>
      <td>ESE</td>
      <td>20.0</td>
      <td>...</td>
      <td>49</td>
      <td>1018.3</td>
      <td>1018.5</td>
      <td>7</td>
      <td>7</td>
      <td>11.1</td>
      <td>15.4</td>
      <td>Yes</td>
      <td>0.0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>9</th>
      <td>8.4</td>
      <td>22.8</td>
      <td>16.2</td>
      <td>5.4</td>
      <td>7.7</td>
      <td>E</td>
      <td>31.0</td>
      <td>S</td>
      <td>ESE</td>
      <td>7.0</td>
      <td>...</td>
      <td>32</td>
      <td>1024.1</td>
      <td>1020.7</td>
      <td>7</td>
      <td>1</td>
      <td>13.3</td>
      <td>21.7</td>
      <td>Yes</td>
      <td>0.0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>320</th>
      <td>3.9</td>
      <td>13.2</td>
      <td>3.4</td>
      <td>6.6</td>
      <td>11.0</td>
      <td>WNW</td>
      <td>65.0</td>
      <td>WNW</td>
      <td>WNW</td>
      <td>26.0</td>
      <td>...</td>
      <td>33</td>
      <td>1017.0</td>
      <td>1017.6</td>
      <td>3</td>
      <td>1</td>
      <td>7.1</td>
      <td>12.2</td>
      <td>Yes</td>
      <td>0.0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>327</th>
      <td>7.8</td>
      <td>16.2</td>
      <td>17.4</td>
      <td>6.4</td>
      <td>7.9</td>
      <td>NW</td>
      <td>50.0</td>
      <td>NW</td>
      <td>N</td>
      <td>15.0</td>
      <td>...</td>
      <td>44</td>
      <td>1016.7</td>
      <td>1017.8</td>
      <td>7</td>
      <td>1</td>
      <td>8.0</td>
      <td>14.3</td>
      <td>Yes</td>
      <td>0.0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>338</th>
      <td>14.4</td>
      <td>20.7</td>
      <td>7.6</td>
      <td>9.4</td>
      <td>4.9</td>
      <td>NNW</td>
      <td>33.0</td>
      <td>NNW</td>
      <td>NNW</td>
      <td>20.0</td>
      <td>...</td>
      <td>65</td>
      <td>1015.5</td>
      <td>1013.2</td>
      <td>8</td>
      <td>4</td>
      <td>14.5</td>
      <td>19.3</td>
      <td>Yes</td>
      <td>3.0</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>339</th>
      <td>10.3</td>
      <td>21.3</td>
      <td>3.0</td>
      <td>4.2</td>
      <td>6.7</td>
      <td>NNW</td>
      <td>43.0</td>
      <td>ENE</td>
      <td>N</td>
      <td>7.0</td>
      <td>...</td>
      <td>46</td>
      <td>1018.1</td>
      <td>1013.6</td>
      <td>8</td>
      <td>1</td>
      <td>11.7</td>
      <td>19.8</td>
      <td>Yes</td>
      <td>0.0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>341</th>
      <td>0.3</td>
      <td>16.0</td>
      <td>8.2</td>
      <td>5.4</td>
      <td>11.8</td>
      <td>NW</td>
      <td>57.0</td>
      <td>NNW</td>
      <td>N</td>
      <td>11.0</td>
      <td>...</td>
      <td>45</td>
      <td>1016.8</td>
      <td>1013.3</td>
      <td>1</td>
      <td>1</td>
      <td>6.9</td>
      <td>14.6</td>
      <td>Yes</td>
      <td>0.0</td>
      <td>No</td>
    </tr>
  </tbody>
</table>
<p>61 rows × 22 columns</p>
</div>



### In this Weather Data Analysis we apply Following Algoriths for Weather prediction :-
 - Decision Tree
 - NBC
 - SVM
 - ARIMA


### I have completed this projet with the help of online resourses and plateform.

- Name - Aatish Kumar Baitha
- M.Tech(Data Science 2nd Year Student)

### My Linkedin Profile -
- www.linkedin.com/in/aatish-kumar-baitha-ba9523191

### My Blog -
- https://computersciencedatascience.blogspot.com/

### Thank you!
