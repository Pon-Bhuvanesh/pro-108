from calendar import c
import random
from re import X
import plotly.express as px
count=[]
Phone_result=[]
for i in range(0,100):
    Apple=random.randint(5,5)
    Samsung=random.randint(5,5)
    Nokia=random.randint(5,5)
    Motorola=random.randint(5,5)
    Phone_result.append(Apple+Samsung+Nokia+Motorola)
    count.append(i)

print(count,Phone_result)

fig=px.bar(x=Phone_result,y=count)
fig.show()