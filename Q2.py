def replace_repeated_chars(k):
    # 用户输入待操作的字符串
    s = input("请输入一个字符串: ")

    # 使用一个列表来存储字符
    chars = list(s)

    # 遍历列表中的字符
    for i in range(len(chars)):
        # 如果字符在前k个字符中已经出现过就替换为'-'
        if chars[i] in chars[max(0, i - k):i]:
            chars[i] = '-'

    # 重新组合成字符串并返回
    return ''.join(chars)


# 用户输入数字k
k = int(input("请输入一个数字k: "))

# 调用函数并输出结果
print(replace_repeated_chars(k))
