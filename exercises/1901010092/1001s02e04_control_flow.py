for a in range(1,10):    #a属于1-9之间的变量数
    for b in range(1,a+1):     #b属于 a就是上面那个变量数再+1的数，就是a如果是2 那b就是3
        print(f"{a}*{b}={a*b}",end='\t') #print是输出 显示的意思，后面的f是格式化，{}是字典 索引的意思 end就是最后 \t就是回车键，到这里就需要回车换下一行了。
    print("")   #根据上面的编码 来显示结果
pass
y = 1                 # y 赋值为1
while y <= 10:        # y小于10的情况下 循环
    if y % 2 != 0:    # 如果Y除以2 结果不等于0，说明这是奇数
        s = 1         # S 赋值为1
        while s < y + 1:   #循环使用，当 S 小于 Y+1的时候
            print( y, "*", s, '=', y*s, sep='', end='\t' )  #输入  先是符号定位，后面的 y*s,为什么不用引号呢？没搞懂的地方，
                                                            #后面 一定是为了中间有空格分隔用的SEP  一个是END 为了当前行结束后自动回车下一行的
            s += 1      #这一步 S 要以加1的数量递增计算
        print()        #输出 显示整体结果
    y += 1             #这里的Y 跟上面的语句是相配套的，只有加上这个才可以 Y以1的数量递增计算
