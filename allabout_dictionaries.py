#All about dictionaries

dict = {'Player': 'Messi' , 'Goals':14 , 'Assists':8}
>>> dict['Player']
'Messi'
>>> dict['Goals']
14

>>> dict['YC']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'YC'

>>> dict['Goals']+=3
>>> dict['Goals']

>>> dict['YC']=2
>>> dict
{'Player': 'Messi', 'YC': 2, 'Assists': 8, 'Goals': 17}
>>> dict['RC']=0
>>> dict
{'Player': 'Messi', 'YC': 2, 'Assists': 8, 'Goals': 17, 'RC': 0}

>>> del dict['RC']
>>> dict
{'Player': 'Messi', 'YC': 2, 'Assists': 8, 'Goals': 17}

>>> dict2 = {'Player':'Messi','Goals':17,'Assists':8,'Player':'RonaldoCR7'}
>>> dict2
{'Player': 'RonaldoCR7', 'Assists': 8, 'Goals': 17}


>>> cmp(dict,dict2)
1

>>> len(dict)
4
>>> str(dict)
"{'Player': 'Messi', 'YC': 2, 'Assists': 8, 'Goals': 17}"

>>> type(dict)
<type 'dict'>
>>> type(dict['Player'])
<type 'str'>
>>> type(dict['Goals'])
<type 'int'>

>>> dict2.clear()
>>> dict2
{}

>>> dict2 = dict.copy()
>>> dict2
{'Player': 'Messi', 'YC': 2, 'Assists': 8, 'Goals': 17}

>>> dict3 = dict.fromkeys(dict)
>>> dict3
{'Player': None, 'YC': None, 'Assists': None, 'Goals': None}

>>> dict.get('Player')
'Messi'
>>> dict.get('Goals')
17

>>> dict.has_key('YC')
True

>>> dict.has_key('RC')
False

>>> dict.items()
[('Player', 'Messi'), ('YC', 2), ('Assists', 8), ('Goals', 17)]

>>> dict.keys()
['Player', 'YC', 'Assists', 'Goals']

>>> dict2 = {'Player':'RonaldoCR7','YC':4,'Assists':3,'Goals':19}
>>> dict.update(dict2)
>>> dict
{'YC': 4, 'Player': 'RonaldoCR7', 'Assists': 3, 'Goals': 19}

>>> dict.values()
[4, 'RonaldoCR7', 3, 19]






