
>>> str1 = "That’s classified. If I tell you I’ll have to kill you"
>>> str1
'That\xe2\x80\x99s classified. If I tell you I\xe2\x80\x99ll have to kill you'

>>> print str1
That’s classified. If I tell you I’ll have to kill you

>>> print str1[0:5]
That

>>> print str1[21:]
If I tell you I’ll have to kill you

>>> str2 = "You know nothing"
>>> str2
'You know nothing'

>>> str2+" John Snow!"
'You know nothing John Snow!'

str2 = str2+" John Snow!"

>>> str2[:17] + "Stanis"
'You know nothing Stanis'

>>> str3 = "Say what again "
>>> str3*2
'Say what again Say what again '

>>> 'say' in str3
False
>>> 'Say' in str3
True

>>> print "I keep saying that the sexy job in the next %d years will be %s. And I’m not kidding" % (5,'statisticians')
I keep saying that the sexy job in the next 5 years will be statisticians. And I’m not kidding





