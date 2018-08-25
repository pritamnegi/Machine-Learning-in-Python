
** 1. Pandas is a python module that makes data science easy & effective. 


```python
import pandas as pd
```

Different ways of creating Dataframes:

1. Using CSV File.
2. Using Excel File.
3. Using Python Dictionaries
4. Using list of tuples.
5. Using list of dictionaries.


```python
df = pd.read_csv("C:\\Users\\app\\Desktop\\data.csv")
```


```python
print(df)
```

      sample_data  Column1  Column2  Column3  Column4
    0     header1  header2  header3  header4  header5
    1         abc     25.5       87      843     abcd
    2         xyz       30      700      500     xyzw
    3         lmn       60       20      600      cvd
    4         pqr       50      300       10      lop
    5         rst       23     2536       20      poi
    


```python
df1 = pd.read_excel("C:\\Users\\app\\Desktop\\data1.xlsx")
```


```python
print(df1)
```

      header1  header2  header3  header4 header5
    0     abc     25.5       87      843    abcd
    1     xyz     30.0      700      500    xyzw
    2     lmn     60.0       20      600     cvd
    3     pqr     50.0      300       10     lop
    4     rst     23.0     2536       20     poi
    


```python
weather_data = {'Day':['1/1/2018', '1/2/2018', '1/3/2018', '1/4/2018'],
                'Temperature': [32, 35, 28, 24],
                'WindSpeed': [6, 7, 2, 7], 
                'Event': ['Rain', 'Sunny', 'Snow', 'Snow']
               }

df2 = pd.DataFrame(weather_data)
print(df2)
```

            Day  Event  Temperature  WindSpeed
    0  1/1/2018   Rain           32          6
    1  1/2/2018  Sunny           35          7
    2  1/3/2018   Snow           28          2
    3  1/4/2018   Snow           24          7
    


```python
weather_data1 = [['1/1/2018', 32, 6, 'Rain'],
                 ['1/2/2018', 35, 7, 'Sunny'],
                 ['1/3/2018', 28, 2, 'Snow'],
                 ['1/4/2018', 24, 7, 'Snow'],
                ]

df2 = pd.DataFrame(weather_data1, columns = ['Day', 'Temperature', 'WindSpeed', 'Event'])
df2

```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Day</th>
      <th>Temperature</th>
      <th>WindSpeed</th>
      <th>Event</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1/1/2018</td>
      <td>32</td>
      <td>6</td>
      <td>Rain</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1/2/2018</td>
      <td>35</td>
      <td>7</td>
      <td>Sunny</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1/3/2018</td>
      <td>28</td>
      <td>2</td>
      <td>Snow</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1/4/2018</td>
      <td>24</td>
      <td>7</td>
      <td>Snow</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 4th Method

weather_data2 = [ {'Day': '1/1/2018', 'Temperature': 32, 'WindSpeed': 6, 'Event': 'Rain'}, 
                  {'Day': '1/2/2018', 'Temperature': 35, 'WindSpeed': 7, 'Event': 'Sunny'},
                  {'Day': '1/3/2018', 'Temperature': 28, 'WindSpeed': 2, 'Event': 'Snow'},
                  {'Day': '1/4/2018', 'Temperature': 24, 'WindSpeed': 7, 'Event': 'Snow'}
                ]

df3 = pd.DataFrame(weather_data2) 
df3
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Day</th>
      <th>Event</th>
      <th>Temperature</th>
      <th>WindSpeed</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1/1/2018</td>
      <td>Rain</td>
      <td>32</td>
      <td>6</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1/2/2018</td>
      <td>Sunny</td>
      <td>35</td>
      <td>7</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1/3/2018</td>
      <td>Snow</td>
      <td>28</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1/4/2018</td>
      <td>Snow</td>
      <td>24</td>
      <td>7</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.shape
```




    (5, 5)




```python
df.head(4)
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>header1</th>
      <th>header2</th>
      <th>header3</th>
      <th>header4</th>
      <th>header5</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>abc</td>
      <td>25.5</td>
      <td>87</td>
      <td>843</td>
      <td>abcd</td>
    </tr>
    <tr>
      <th>1</th>
      <td>xyz</td>
      <td>30.0</td>
      <td>700</td>
      <td>500</td>
      <td>xyzw</td>
    </tr>
    <tr>
      <th>2</th>
      <td>lmn</td>
      <td>60.0</td>
      <td>20</td>
      <td>600</td>
      <td>cvd</td>
    </tr>
    <tr>
      <th>3</th>
      <td>pqr</td>
      <td>50.0</td>
      <td>300</td>
      <td>10</td>
      <td>lop</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.tail(2)
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>header1</th>
      <th>header2</th>
      <th>header3</th>
      <th>header4</th>
      <th>header5</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>3</th>
      <td>pqr</td>
      <td>50.0</td>
      <td>300</td>
      <td>10</td>
      <td>lop</td>
    </tr>
    <tr>
      <th>4</th>
      <td>rst</td>
      <td>23.0</td>
      <td>2536</td>
      <td>20</td>
      <td>poi</td>
    </tr>
  </tbody>
</table>
</div>




```python
df[1:3]
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>header1</th>
      <th>header2</th>
      <th>header3</th>
      <th>header4</th>
      <th>header5</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>xyz</td>
      <td>30.0</td>
      <td>700</td>
      <td>500</td>
      <td>xyzw</td>
    </tr>
    <tr>
      <th>2</th>
      <td>lmn</td>
      <td>60.0</td>
      <td>20</td>
      <td>600</td>
      <td>cvd</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.columns
```




    Index(['header1', 'header2', 'header3', 'header4', 'header5'], dtype='object')




```python
df3.Day
```




    0    1/1/2018
    1    1/2/2018
    2    1/3/2018
    3    1/4/2018
    Name: Day, dtype: object




```python
type(df3['Day'])
```




    pandas.core.series.Series




```python
df3[['Event', 'Day']]
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Event</th>
      <th>Day</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Rain</td>
      <td>1/1/2018</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Sunny</td>
      <td>1/2/2018</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Snow</td>
      <td>1/3/2018</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Snow</td>
      <td>1/4/2018</td>
    </tr>
  </tbody>
</table>
</div>




```python
df3['Temperature'].max()
```




    35




```python
df3.describe()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Temperature</th>
      <th>WindSpeed</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>4.000000</td>
      <td>4.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>29.750000</td>
      <td>5.500000</td>
    </tr>
    <tr>
      <th>std</th>
      <td>4.787136</td>
      <td>2.380476</td>
    </tr>
    <tr>
      <th>min</th>
      <td>24.000000</td>
      <td>2.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>27.000000</td>
      <td>5.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>30.000000</td>
      <td>6.500000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>32.750000</td>
      <td>7.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>35.000000</td>
      <td>7.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
df3[df3.Temperature>=32]
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Day</th>
      <th>Event</th>
      <th>Temperature</th>
      <th>WindSpeed</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1/1/2018</td>
      <td>Rain</td>
      <td>32</td>
      <td>6</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1/2/2018</td>
      <td>Sunny</td>
      <td>35</td>
      <td>7</td>
    </tr>
  </tbody>
</table>
</div>




```python
df3.index
```




    RangeIndex(start=0, stop=4, step=1)




```python
new_df = df3.set_index(['Temperature'])
new_df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>level_0</th>
      <th>index</th>
      <th>Day</th>
      <th>Event</th>
      <th>WindSpeed</th>
    </tr>
    <tr>
      <th>Temperature</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>32</th>
      <td>0</td>
      <td>0</td>
      <td>1/1/2018</td>
      <td>Rain</td>
      <td>6</td>
    </tr>
    <tr>
      <th>35</th>
      <td>1</td>
      <td>1</td>
      <td>1/2/2018</td>
      <td>Sunny</td>
      <td>7</td>
    </tr>
    <tr>
      <th>28</th>
      <td>2</td>
      <td>2</td>
      <td>1/3/2018</td>
      <td>Snow</td>
      <td>2</td>
    </tr>
    <tr>
      <th>24</th>
      <td>3</td>
      <td>3</td>
      <td>1/4/2018</td>
      <td>Snow</td>
      <td>7</td>
    </tr>
  </tbody>
</table>
</div>




```python
df3.index('Temperature', inplace = True)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-60-b8215d253fae> in <module>()
    ----> 1 df3.index('Temperature', inplace = True)
    

    TypeError: 'RangeIndex' object is not callable



```python
new_df.reset_index(inplace = True)
new_df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Temperature</th>
      <th>level_0</th>
      <th>index</th>
      <th>Day</th>
      <th>Event</th>
      <th>WindSpeed</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>32</td>
      <td>0</td>
      <td>0</td>
      <td>1/1/2018</td>
      <td>Rain</td>
      <td>6</td>
    </tr>
    <tr>
      <th>1</th>
      <td>35</td>
      <td>1</td>
      <td>1</td>
      <td>1/2/2018</td>
      <td>Sunny</td>
      <td>7</td>
    </tr>
    <tr>
      <th>2</th>
      <td>28</td>
      <td>2</td>
      <td>2</td>
      <td>1/3/2018</td>
      <td>Snow</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>24</td>
      <td>3</td>
      <td>3</td>
      <td>1/4/2018</td>
      <td>Snow</td>
      <td>7</td>
    </tr>
  </tbody>
</table>
</div>




```python
df3.loc['Temperature']
```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    C:\ProgramData\Anaconda3\lib\site-packages\pandas\core\indexing.py in _has_valid_type(self, key, axis)
       1433                 if not ax.contains(key):
    -> 1434                     error()
       1435             except TypeError as e:
    

    C:\ProgramData\Anaconda3\lib\site-packages\pandas\core\indexing.py in error()
       1428                 raise KeyError("the label [%s] is not in the [%s]" %
    -> 1429                                (key, self.obj._get_axis_name(axis)))
       1430 
    

    KeyError: 'the label [Temperature] is not in the [index]'

    
    During handling of the above exception, another exception occurred:
    

    KeyError                                  Traceback (most recent call last)

    <ipython-input-71-536b811ef338> in <module>()
    ----> 1 df3.loc['Temperature']
    

    C:\ProgramData\Anaconda3\lib\site-packages\pandas\core\indexing.py in __getitem__(self, key)
       1326         else:
       1327             key = com._apply_if_callable(key, self.obj)
    -> 1328             return self._getitem_axis(key, axis=0)
       1329 
       1330     def _is_scalar_access(self, key):
    

    C:\ProgramData\Anaconda3\lib\site-packages\pandas\core\indexing.py in _getitem_axis(self, key, axis)
       1549 
       1550         # fall thru to straight lookup
    -> 1551         self._has_valid_type(key, axis)
       1552         return self._get_label(key, axis=axis)
       1553 
    

    C:\ProgramData\Anaconda3\lib\site-packages\pandas\core\indexing.py in _has_valid_type(self, key, axis)
       1440                 raise
       1441             except:
    -> 1442                 error()
       1443 
       1444         return True
    

    C:\ProgramData\Anaconda3\lib\site-packages\pandas\core\indexing.py in error()
       1427                                     "key")
       1428                 raise KeyError("the label [%s] is not in the [%s]" %
    -> 1429                                (key, self.obj._get_axis_name(axis)))
       1430 
       1431             try:
    

    KeyError: 'the label [Temperature] is not in the [index]'



```python
df5 = pd.read_csv("C:\\Users\\app\\Desktop\\data.csv", header = 1)
df5
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>header1</th>
      <th>header2</th>
      <th>header3</th>
      <th>header4</th>
      <th>header5</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>abc</td>
      <td>25.5</td>
      <td>87</td>
      <td>843</td>
      <td>abcd</td>
    </tr>
    <tr>
      <th>1</th>
      <td>xyz</td>
      <td>30.0</td>
      <td>700</td>
      <td>500</td>
      <td>xyzw</td>
    </tr>
    <tr>
      <th>2</th>
      <td>lmn</td>
      <td>60.0</td>
      <td>20</td>
      <td>600</td>
      <td>cvd</td>
    </tr>
    <tr>
      <th>3</th>
      <td>pqr</td>
      <td>50.0</td>
      <td>300</td>
      <td>10</td>
      <td>lop</td>
    </tr>
    <tr>
      <th>4</th>
      <td>rst</td>
      <td>23.0</td>
      <td>2536</td>
      <td>20</td>
      <td>poi</td>
    </tr>
  </tbody>
</table>
</div>




```python
df6 = pd.read_csv("C:\\Users\\app\\Desktop\\data.csv", header = None)
df6
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>sample_data</td>
      <td>Column1</td>
      <td>Column2</td>
      <td>Column3</td>
      <td>Column4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>header1</td>
      <td>header2</td>
      <td>header3</td>
      <td>header4</td>
      <td>header5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>abc</td>
      <td>25.5</td>
      <td>87</td>
      <td>843</td>
      <td>abcd</td>
    </tr>
    <tr>
      <th>3</th>
      <td>xyz</td>
      <td>30</td>
      <td>700</td>
      <td>500</td>
      <td>xyzw</td>
    </tr>
    <tr>
      <th>4</th>
      <td>lmn</td>
      <td>60</td>
      <td>20</td>
      <td>600</td>
      <td>cvd</td>
    </tr>
    <tr>
      <th>5</th>
      <td>pqr</td>
      <td>50</td>
      <td>300</td>
      <td>10</td>
      <td>lop</td>
    </tr>
    <tr>
      <th>6</th>
      <td>rst</td>
      <td>23</td>
      <td>2536</td>
      <td>20</td>
      <td>poi</td>
    </tr>
  </tbody>
</table>
</div>




```python
df7 = pd.read_csv("C:\\Users\\app\\Desktop\\data.csv", header = None, names = ["header1", "hedaer2", "header3", "header4"])
df7
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>header1</th>
      <th>hedaer2</th>
      <th>header3</th>
      <th>header4</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>sample_data</th>
      <td>Column1</td>
      <td>Column2</td>
      <td>Column3</td>
      <td>Column4</td>
    </tr>
    <tr>
      <th>header1</th>
      <td>header2</td>
      <td>header3</td>
      <td>header4</td>
      <td>header5</td>
    </tr>
    <tr>
      <th>abc</th>
      <td>25.5</td>
      <td>87</td>
      <td>843</td>
      <td>abcd</td>
    </tr>
    <tr>
      <th>xyz</th>
      <td>30</td>
      <td>700</td>
      <td>500</td>
      <td>xyzw</td>
    </tr>
    <tr>
      <th>lmn</th>
      <td>60</td>
      <td>20</td>
      <td>600</td>
      <td>cvd</td>
    </tr>
    <tr>
      <th>pqr</th>
      <td>50</td>
      <td>300</td>
      <td>10</td>
      <td>lop</td>
    </tr>
    <tr>
      <th>rst</th>
      <td>23</td>
      <td>2536</td>
      <td>20</td>
      <td>poi</td>
    </tr>
  </tbody>
</table>
</div>




```python
df8 = pd.read_csv("C:\\Users\\app\\Desktop\\data.csv", nrows = 2)
df8

```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>sample_data</th>
      <th>Column1</th>
      <th>Column2</th>
      <th>Column3</th>
      <th>Column4</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>header1</td>
      <td>header2</td>
      <td>header3</td>
      <td>header4</td>
      <td>header5</td>
    </tr>
    <tr>
      <th>1</th>
      <td>abc</td>
      <td>25.5</td>
      <td>87</td>
      <td>843</td>
      <td>abcd</td>
    </tr>
  </tbody>
</table>
</div>




```python
df9 = pd.read_csv("C:\\Users\\app\\Desktop\\data.csv", na_values = ["not available", "NaN"])
df9
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>sample_data</th>
      <th>Column1</th>
      <th>Column2</th>
      <th>Column3</th>
      <th>Column4</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>header1</td>
      <td>header2</td>
      <td>header3</td>
      <td>header4</td>
      <td>header5</td>
    </tr>
    <tr>
      <th>1</th>
      <td>abc</td>
      <td>25.5</td>
      <td>87</td>
      <td>843</td>
      <td>abcd</td>
    </tr>
    <tr>
      <th>2</th>
      <td>xyz</td>
      <td>-30</td>
      <td>700</td>
      <td>500</td>
      <td>xyzw</td>
    </tr>
    <tr>
      <th>3</th>
      <td>lmn</td>
      <td>60</td>
      <td>20</td>
      <td>600</td>
      <td>cvd</td>
    </tr>
    <tr>
      <th>4</th>
      <td>pqr</td>
      <td>50</td>
      <td>300</td>
      <td>10</td>
      <td>lop</td>
    </tr>
    <tr>
      <th>5</th>
      <td>rst</td>
      <td>23</td>
      <td>2536</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
df10 = pd.read_csv("C:\\Users\\app\\Desktop\\data.csv", na_values = ["Not Available", -1])
df10
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>sample_data</th>
      <th>Column1</th>
      <th>Column2</th>
      <th>Column3</th>
      <th>Column4</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>header1</td>
      <td>header2</td>
      <td>header3</td>
      <td>header4</td>
      <td>header5</td>
    </tr>
    <tr>
      <th>1</th>
      <td>abc</td>
      <td>25.5</td>
      <td>87</td>
      <td>843</td>
      <td>abcd</td>
    </tr>
    <tr>
      <th>2</th>
      <td>xyz</td>
      <td>NaN</td>
      <td>700</td>
      <td>500</td>
      <td>xyzw</td>
    </tr>
    <tr>
      <th>3</th>
      <td>lmn</td>
      <td>60</td>
      <td>20</td>
      <td>600</td>
      <td>cvd</td>
    </tr>
    <tr>
      <th>4</th>
      <td>pqr</td>
      <td>50</td>
      <td>300</td>
      <td>10</td>
      <td>lop</td>
    </tr>
    <tr>
      <th>5</th>
      <td>rst</td>
      <td>23</td>
      <td>2536</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
df10.to_csv("new_data.csv")
```


```python
# copying only specific columns

df10.to_csv("new_data1.csv", columns = ['sample_data', 'Column1'])
```


```python
df10.to_csv("new_data2.csv", header = False)
```


```python
df1
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>header1</th>
      <th>header2</th>
      <th>header3</th>
      <th>header4</th>
      <th>header5</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>abc</td>
      <td>25.5</td>
      <td>87</td>
      <td>843</td>
      <td>abcd</td>
    </tr>
    <tr>
      <th>1</th>
      <td>xyz</td>
      <td>30.0</td>
      <td>700</td>
      <td>500</td>
      <td>xyzw</td>
    </tr>
    <tr>
      <th>2</th>
      <td>lmn</td>
      <td>60.0</td>
      <td>20</td>
      <td>600</td>
      <td>cvd</td>
    </tr>
    <tr>
      <th>3</th>
      <td>pqr</td>
      <td>50.0</td>
      <td>300</td>
      <td>10</td>
      <td>lop</td>
    </tr>
    <tr>
      <th>4</th>
      <td>rst</td>
      <td>23.0</td>
      <td>2536</td>
      <td>20</td>
      <td>poi</td>
    </tr>
  </tbody>
</table>
</div>




```python
def convert_value(cell):
    if cell == "n.a.":
        return 'XYZ'
    return cell
```


```python
df1 = pd.read_excel("C:\\Users\\app\\Desktop\\data1.xlsx", converters = convert_value(Column4))
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-106-b242ee5d14b5> in <module>()
    ----> 1 df1 = pd.read_excel("C:\\Users\\app\\Desktop\\data1.xlsx", converters = convert_value(df1.Column4))
    

    <ipython-input-98-ee1d900cb82b> in convert_value(cell)
          1 def convert_value(cell):
    ----> 2     if cell == "n.a.":
          3         return 'XYZ'
          4     return cell
    

    C:\ProgramData\Anaconda3\lib\site-packages\pandas\core\generic.py in __nonzero__(self)
        953         raise ValueError("The truth value of a {0} is ambiguous. "
        954                          "Use a.empty, a.bool(), a.item(), a.any() or a.all()."
    --> 955                          .format(self.__class__.__name__))
        956 
        957     __bool__ = __nonzero__
    

    ValueError: The truth value of a Series is ambiguous. Use a.empty, a.bool(), a.item(), a.any() or a.all().



```python
df1
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>sample_data</th>
      <th>Column1</th>
      <th>Column2</th>
      <th>Column3</th>
      <th>Column4</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>header1</td>
      <td>header2</td>
      <td>header3</td>
      <td>header4</td>
      <td>header5</td>
    </tr>
    <tr>
      <th>1</th>
      <td>abc</td>
      <td>25.5</td>
      <td>87</td>
      <td>843</td>
      <td>abcd</td>
    </tr>
    <tr>
      <th>2</th>
      <td>xyz</td>
      <td>30</td>
      <td>700</td>
      <td>500</td>
      <td>xyzw</td>
    </tr>
    <tr>
      <th>3</th>
      <td>lmn</td>
      <td>60</td>
      <td>20</td>
      <td>600</td>
      <td>cvd</td>
    </tr>
    <tr>
      <th>4</th>
      <td>pqr</td>
      <td>50</td>
      <td>300</td>
      <td>10</td>
      <td>lop</td>
    </tr>
    <tr>
      <th>5</th>
      <td>rst</td>
      <td>23</td>
      <td>2536</td>
      <td>n.a.</td>
      <td>n.a.</td>
    </tr>
  </tbody>
</table>
</div>




```python
df1.to_excel("new_file.xlsx", sheet_name = "Data", startrow = 1, startcol = 2)
```


```python
df11 = pd.read_excel("C:\\Users\\app\\Desktop\\data2.xlsx")
df11
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>sample_data</th>
      <th>Column1</th>
      <th>Column2</th>
      <th>Column3</th>
      <th>Column4</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>header1</td>
      <td>header2</td>
      <td>header3</td>
      <td>header4</td>
      <td>header5</td>
    </tr>
    <tr>
      <th>1</th>
      <td>abc</td>
      <td>25.5</td>
      <td>87</td>
      <td>843</td>
      <td>abcd</td>
    </tr>
    <tr>
      <th>2</th>
      <td>xyz</td>
      <td>30</td>
      <td>700</td>
      <td>500</td>
      <td>xyzw</td>
    </tr>
    <tr>
      <th>3</th>
      <td>lmn</td>
      <td>60</td>
      <td>20</td>
      <td>600</td>
      <td>cvd</td>
    </tr>
    <tr>
      <th>4</th>
      <td>pqr</td>
      <td>50</td>
      <td>300</td>
      <td>10</td>
      <td>lop</td>
    </tr>
    <tr>
      <th>5</th>
      <td>rst</td>
      <td>23</td>
      <td>2536</td>
      <td>30</td>
      <td>lom</td>
    </tr>
  </tbody>
</table>
</div>




```python
df3
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>level_0</th>
      <th>index</th>
      <th>Day</th>
      <th>Event</th>
      <th>Temperature</th>
      <th>WindSpeed</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>0</td>
      <td>1/1/2018</td>
      <td>Rain</td>
      <td>32</td>
      <td>6</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>1</td>
      <td>1/2/2018</td>
      <td>Sunny</td>
      <td>35</td>
      <td>7</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>2</td>
      <td>1/3/2018</td>
      <td>Snow</td>
      <td>28</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>3</td>
      <td>1/4/2018</td>
      <td>Snow</td>
      <td>24</td>
      <td>7</td>
    </tr>
  </tbody>
</table>
</div>




```python
with pd.ExcelWriter('combined_data2.xlsx') as writer:
    df1.to_excel(writer, sheet_name = "headers_data")
    df3.to_excel(writer, sheet_name = "Weather")
```

** Handle Missing Data

1. fillna
2. dropna
3. interpolate
4. replace


```python
new_df1 = df1.fillna(0)
new_df1
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>sample_data</th>
      <th>Column1</th>
      <th>Column2</th>
      <th>Column3</th>
      <th>Column4</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>header1</td>
      <td>header2</td>
      <td>header3</td>
      <td>header4</td>
      <td>header5</td>
    </tr>
    <tr>
      <th>1</th>
      <td>abc</td>
      <td>25.5</td>
      <td>87</td>
      <td>843</td>
      <td>abcd</td>
    </tr>
    <tr>
      <th>2</th>
      <td>xyz</td>
      <td>30</td>
      <td>700</td>
      <td>500</td>
      <td>xyzw</td>
    </tr>
    <tr>
      <th>3</th>
      <td>lmn</td>
      <td>60</td>
      <td>20</td>
      <td>600</td>
      <td>cvd</td>
    </tr>
    <tr>
      <th>4</th>
      <td>pqr</td>
      <td>50</td>
      <td>300</td>
      <td>10</td>
      <td>lop</td>
    </tr>
    <tr>
      <th>5</th>
      <td>rst</td>
      <td>23</td>
      <td>2536</td>
      <td>n.a.</td>
      <td>n.a.</td>
    </tr>
  </tbody>
</table>
</div>




```python
new_df = df.fillna({
    'Temperature': 0,
    'WindSpeed': 0,
    'Event': 'No Event'
})
```


```python
new_df = df.fillna(method = "ffill")
new_df = df.fillna(method = "bfill")


new_df = df.fillna(method = "bfill", axis = 'columns')
new_df = df.fillna(method = "bfill", limit = 2)



```


```python
new_df = df.interpolate()

new_df = df.interpolate(method = 'time')

```


```python
new_df = df.dropna()
new_df = df.dropna(how = "all")

new_df = df.dropna(thresh = 1)
```


```python
new_df = df.replace(-999999, np.NaN)
new_df = df.replace([-999999, 10555], np.NaN)
```
