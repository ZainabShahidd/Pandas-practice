#creating a series from pyton list
import pandas as pd
list = ['zainab','saira','maira']
s = pd.Series(data=list)
print(s)
print(type(s))
#indices with series
import pandas as pd
list = ['zainab','saira','maira']
indices = ['first', 'second', 'third']
s = pd.Series(data=list, index = indices)
print(s)
print(type(s))
#nan values 
import numpy as np
import pandas as pd
list=[1,2,4.5,np.nan, 54]
s=pd.Series(data=list)
print(s)
print(type(s))
#name of a series
import pandas as pd
import numpy as np
list=['zainab','saira','maira']
indices = ['first','second','third']
s = pd.Series(data=list , index= indices, name = 'MySeries')
print(s)
print(type(s))

#create a dictionaries
import pandas as pd
import numpy as np
dic = {
    'name' : "zainab",
    'gender' : 'female',
     'age'   : 20,
     'role'  : "Student"
    }
s= pd.Series(data=dic)
print(s)

#series from scalar value
import numpy as np
import pandas as pd
s=pd.Series(data = 25)
print(s)

#empty series
import numpy as np
import pandas as pd
s= pd.Series(dtype='float64')
print(s)

#Attributes of pandas series
import pandas as pd
import numpy as np
dict = {0:'Zainab', 1: 'ushna', 2:'maham', 3: np.nan, 4:'ruqia', 5:'farwa'}
s = pd.Series(data=dict , name='myseries')
print(s)

#changing index of a series object
import numpy as np
import pandas as pd
list = ['zainab','ushna','maham','farwa','ruqia']
s = pd.Series(data = list )
print(s)

arr = np.random.randint(low= 100, high= 200 , size=5)
s.index = arr
print(s)
print(s.index)

#first use of index(identification)
#identification using integers 
import numpy as np
import pandas as pd
list = ['zainab','saira','maira']
indices = [5,2,3]
s = pd.Series(data=list, index=indices)
print(s)
print(s[5])
print(s.loc[2])

#fancy indexing
import numpy as np
import pandas as pd
list = ['zainab','ushna','maham','farwa']
indices=[5,34,22,89]
s=pd.Series(data=list , index=indices)
print(s)
print(s[[34,5]])
print(s.loc[[5,22]])

#negative indexing
import numpy as np
import pandas as pd
list= ['zainab','maham','ushna','farwa','ruqia']
indices=[23,78,45,21,12]
s=pd.Series(data=list, index=indices)
print(s)
print(s.iloc[-5])

#Second use of index(selection)
#selection/filtering/subsetting
import numpy as np
import pandas as pd
list= ['zainab','saira','maira','ushna','farwa']
indices= [82,6,7,34,23]
s=pd.Series(data=list , index=indices)
print(s)
print(s[1:5])
print(s.loc[6:7])

#third use of indexing(alignment)
#adding two series object
import pandas as pd
import numpy as np
list1=[1,2,3,4,5];
list2=[3,4,5,6,6];
s1 = pd.Series(data=list1);
s2= pd.Series(data=list2);
print(s1)
print(s1.index)

#adding
import pandas as pd
import numpy as np
list1=[1,3,5,7,8];
list2=[2,3,4,5,7];
s1 = pd.Series(data=list1);
s2= pd.Series(data=list2);
s3=s1+s2
print(s3)
print(s3.index)