"""
ChineseYuan convert Zimbabwean.py
该代码用于实现人民币与津巴布韦币的转换
"""
CCY = input("Please input CCY with sum:")  # 输入带有缩写字母的货币量
if CCY[-3:] in ['CNY', 'cny']:  # 检测输入的货币类型
    ZWL = 2195.4865 * eval(CCY[0:-3])  # 如果是人民币，转化为津巴布韦币
    print("The converted Zimbabwean currency is {:.2f}ZWL".format(ZWL))  # 输出转化值和货币类型
elif CCY[-3:] in ['ZWL', 'zwl']:  # 检测输入的货币类型
    CNY = eval(CCY[0:-3]) / 2195.4865  # 如果是津巴布韦币，转化为人民币
    print("The converted Chinese Yuan is {:.2f}CNY".format(CNY))  # 输出转化值和货币类型
else:  # 检测输入的货币类型
    print("Error!!!")  # 如果不是这两种货币，报错
