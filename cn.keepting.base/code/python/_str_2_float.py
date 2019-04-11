#思路：比如123.999   根据"."分割成"123"和"999"，转成数字后再123+999/10^3=123+0.999=123.999
from functools import reduce
def _str_2_float(s):
    return  reduce(lambda x,y: x+y/(10**len(str(y))),map(int,s.split(".")))
print(_str_2_float("123.999")+0.001)

#输出
# 124.0