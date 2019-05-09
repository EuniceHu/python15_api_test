
#字符串 str
a='hello python15'
# 1:常规用法：字符串的取值和切片
# 1）字符串里面元素：单个字符算一个元素（数字 字母 符号 中文）
# 2）统计字符串的长度：len(a)
print(len(a))
# 3)如何取值：字符串取值是根据索引来的 索引是什么呢？是字符串元素的编号
# 编号是从0开始的  取值方式：变量名[索引]
# 4）切片:用法 变量名[m:n:k] m开始取值的索引位置 n取值结束的位置，取值不包含  k步长
# 取左不取右，取到n-1
print(a[0:13:1])#0 1 2 3 4 5 6 7  8 9 10 11 12
print(a[0:13:3])#0 3 6 9 12
#请把a字符串里面年号为偶数的元素打印出来
print(a[0:13:2])
print(a[::2])
#请把a字符串利用切片实现倒序输出
print(a[::-1])
# 取最后一个元素
print(a[-1])

#字符串的拼接 +
s_1='hello'
s_2='你好'
a=20#转换成字符串 str()强制转化
print(s_1+s_2+str(a))
print(s_1+s_2,a)

# 格式化输出 占坑符 %d %f %s
age=22
height=170.34
hobby='打篮球'
# 格式化输出方法一
print('''---------小cc的个人档案-------------
      年龄是：''',age,'''
      身高是：''',height,'''
      业余爱好是：''',hobby,'''
      ''')
print('''---------小cc的个人档案-------------
      年龄是：%d
      身高是：%0.2f
      业余爱好是：%s
      '''%(age,height,hobby))
# 格式化输出方法二
print('''---------Bay max的个人档案-------------
      年龄是:{0}
      身高是：{2}
      业余爱好是：{0}
      '''.format(age,height,hobby))#0开始编号坑 开始编号元素
# 函数
b='hEllo pPythOn15y'
#切换大小写 upper变成大写 lower变成小写
print(b.upper().lower())
print(b.isupper())
print(b.swapcase())#大小写互换


#replace 替换方法
s=b.replace('l','@',1)
print(s)

#find 查找元素  没有找到就返回-1 只考虑正序  不考虑反序

print(b.find('13y')) #单个字符如果找到了，返回的是遇到的第一个元素的索引的值
#子字符串 长度大于1 如果找到了 就返回子字符串所在第一个元素的位置

print(b.count('o'))
print(b.index('h'))

#布尔值  True False

print(b[1].islower())
print(b[1].isupper())
print('@'.join(b))

print(b.split('l'))#切割  返回的是列表  切片返回的是字符串

