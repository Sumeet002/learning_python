#All about tuples

>>> tup1 = ('chelsea','liverpool','arsenal')
>>> tup1
('chelsea', 'liverpool', 'arsenal')
>>> tup2 = (1,2,3,4,5)
>>> tup2
(1, 2, 3, 4, 5)
>>> tup2 = 1,2,3,4,5
>>> tup2
(1, 2, 3, 4, 5)

tup3 = ('barcelona',1,'real madrid',2 , 'atletico',3)
tup3

>>> tup4 = ()
>>> tup4
()
>>> tup5 = (4,)
>>> tup5
(4,)
>>>


>>> tup3[0]
'barcelona'
>>> tup3[0:3]
('barcelona', 1, 'real madrid')
>>> tup3[3:]
(2, 'atletico', 3)
>>> tup3[-2]
'atletico'
>>> tup3[-2:]
('atletico', 3)
>>> tup3[-4:-1]
('real madrid', 2, 'atletico')

>>> tup1[1] = 43
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment

>>> tup6 = tup1 + tup2
>>> tup6
('chelsea', 'liverpool', 'arsenal', 1, 2, 3, 4, 5)

>>> del tup6[1]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object doesn't support item deletion

del tup6

>>> len(tup2)
5
>>> ('messi')*3
'messimessimessi'

>>> 'mancity' in tup1
False

for x in tup2 :
  print x

>>> tup6 = [2,4,3,5,1]
>>> cmp(tup2,tup6)
1
>>> cmp(tup6,tup2)
-1
>>> cmp(tup2,tup2)
0

>>> max(tup1)
'liverpool'
>>> max(tup2)
5
>>> min(tup3)
1
>>> max(tup3)
'real madrid'
>>> max(tup1)
'liverpool'
>>> min(tup1)
'arsenal'




