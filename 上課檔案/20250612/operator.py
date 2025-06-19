'''
#數學
num op num -> num
1 + 1 = 2

%(餘), //(商), **

#邏輯
(1)num op num -> bool
2 > 3 -> False
2 != 2 -> False
>, <, >=, <=, ==, !=
(2)bool op bool -> bool
邏輯閘 logic gates
1.not 反閘
周杰倫:哎呦 不錯喔！
不(not)錯(False) -> True
不(not)行(True) -> False

2.or 或閘
math or english -> 3000
T       F          T
F       T          T
T       T          T
F       F          F

3.and 且閘
奶茶 and 紅茶 -> :)
T        F      F
F        T      F
T        T      T
F        F      F

4.xor (excursive or) 斥或閘
珍奶 xor 烏龍拿鐵 -> :)
T        F         T
F        T         T
T        T         F
F        F         F
'''
a,b = True, True
print(a ^ b)
