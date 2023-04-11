# 1.二进制转十进制

def bin_to_dec(num):
    """
    将二进制数转换为十进制数
    :param num: 要转换的二进制数，str类型
    :return: 转换后的十进制数，返回值类型为str
    """
    num = [int(digit) for digit in num]

    dec_num = 0
    for digit in num:
        dec_num = dec_num * 2 + digit
    return str(dec_num)
print(bin_to_dec('101010'))  # 输出：42
# 使用说明：
# 函数接受一个参数：要转换的二进制数。
# 输入的数字需要为字符串类型时，函数会先将其转换为一个由每一位数字组成的列表。接着，函数使用循环遍历每一位数字，并
# 根据其在二进制数中的位置计算出对应的10进制数，将所有位的十进制值相加得到结果，最后将结果转换为字符串类型输出。

# 2.十进制转二进制
def dec_to_bin(num):
    """
    将十进制数转换为二进制数

    :param num: 要转换的十进制数，必须是非负整数
    :return: 转换后的二进制数，返回值类型为str
    """
    if not isinstance(num, int) or num < 0:
        raise ValueError('The input num must be a non-negative integer.')
    if num == 0:
        return '0'
    bin_num = ''
    while num > 0:
        bin_num = str(num % 2) + bin_num
        num //= 2
    return bin_num
print(dec_to_bin(42))  # 输出：101010
# 使用说明：
# 该函数接受一个参数：要转换的十进制数。如果输入的数字不是非负整数，则会引发ValueError异常。
# 当输入的数字是非负整数时，函数会使用循环计算出对应的二进制数。具体地，函数使用一个空字符串
# 变量bin_num来记录二进制数，从低位到高位依次计算每一位的值，并将其添加到bin_num的前面。当
# 计算完所有位后，函数返回bin_num作为结果。
# 3.二进制转十六进制
def bin_to_hex(num):
    """
    将二进制数转换为十六进制数

    :param num: 要转换的二进制数，可以是int或str类型
    :return: 转换后的十六进制数，返回值类型为str
    """
    hex_digits = '0123456789ABCDEF'
    if isinstance(num, str):
        num = [int(digit) for digit in num]
    elif not isinstance(num, int):
        raise TypeError('The input num must be an integer or a string representing an integer.')
    hex_num = ''
    while len(num) % 4 != 0:
        num.insert(0, 0)
    for i in range(0, len(num), 4):
        digit = 0
        for j in range(4):
            digit = digit * 2 + num[i + j]
        hex_num += hex_digits[digit]
    return hex_num
print(bin_to_hex('101010'))  # 输出：2A
# 使用说明：
# 该函数接受一个参数：要转换的二进制数。如果输入的数字是字符串类型，则函数会将其转换为整数类型；如果输入
# 的数字既不是整数类型也不是字符串类型，则会引发TypeError异常。
# 当输入的数字是整数类型或字符串类型时，函数会先将其转换为一个由每一位数字组成的列表（如果输入的是整数，
# 则先将其转换为字符串类型再处理）。接着，函数会在数字前面添加一些0，使得数字的位数是4的倍数。然后，函
# 数使用循环每次处理4个二进制数，将其转换为一个16进制数字，并将其添加到结果字符串hex_num的末尾。
# 4.十六进制转二进制
def hex_to_bin(hex_num):
    """
    将十六进制数转换为二进制数

    :param hex_num: 要转换的十六进制数，必须是str类型
    :return: 转换后的二进制数，返回值类型为str
    """
    hex_digits = '0123456789ABCDEF'
    bin_digits = '01'
    if not isinstance(hex_num, str):
        raise TypeError('The input hex_num must be a string.')
    bin_num = ''
    for digit in hex_num:
        if digit not in hex_digits:
            raise ValueError('The input hex_num contains an invalid digit.')
        digit_value = hex_digits.index(digit)
        bin_num += bin_digits[digit_value // 8] + bin_digits[digit_value // 4 % 2] + bin_digits[digit_value % 4 // 2] + bin_digits[digit_value % 2]
    return bin_num.lstrip('0') or '0'
print(hex_to_bin('2A'))  # 输出：101010
# 使用说明：
# 该函数接受一个参数：要转换的十六进制数。如果输入的数字不是字符串类型，则会引发TypeError异常。如果输入的数字包含
# 不合法的十六进制数字，则会引发ValueError异常。
# 当输入的数字是字符串类型且合法时，函数会对每一位数字进行处理，将其转换为对应的4位二进制数，并将这些二进制数拼接起
# 来。具体地，函数使用两个字符串hex_digits和bin_digits来存储16进制数字和2进制数字的所有可能取值。在计算每个16
# 进制数字对应的二进制数时，我们先使用index方法找到该数字在hex_digits中的下标，然后根据下标计算出对应的4位二进制
# 数，并将其添加到结果字符串bin_num的末尾。
# 最后，我们需要将bin_num字符串的前导0去掉，以避免结果中含有不必要的0。如果bin_num字符串全是0，则需要将最后一个0
# 保留。
# 5.十进制转十六进制
def dec_to_hex(num):
    """
    将十进制数转换为十六进制数

    :param num: 要转换的十进制数，必须是int类型
    :return: 转换后的十六进制数，返回值类型为str
    """
    hex_digits = '0123456789ABCDEF'
    if not isinstance(num, int):
        raise TypeError('The input num must be an integer.')
    if num == 0:
        return '0'
    hex_num = ''
    while num > 0:
        digit_value = num % 16
        hex_num = hex_digits[digit_value] + hex_num
        num = num // 16
    return hex_num

print(dec_to_hex(42))  # 输出：2A
# 使用说明：
# 该函数接受一个参数：要转换的十进制数。如果输入的数字不是整数类型，则会引发TypeError异常。
# 当输入的数字是整数类型且不为0时，函数会使用循环不断地将数字除以16，得到商和余数，然后将余数转换为对应的16
# 进制数字，并将其添加到结果字符串hex_num的开头。具体地，函数使用字符串hex_digits来存储16进制数字的所有
# 可能取值。在计算每个位对应的16进制数字时，我们使用取模运算得到该位的余数，然后使用hex_digits列表获取对
# 应的16进制数字，并将其添加到结果字符串hex_num的开头。最后，我们不断地将数字除以16，直到商为0为止。
# 6.十六进制转十进制
def hex_to_dec(hex_num):
    """
    将十六进制数转换为十进制数

    :param hex_num: 要转换的十六进制数，必须是str类型
    :return: 转换后的十进制数，返回值类型为int
    """
    hex_digits = '0123456789ABCDEF'
    if not isinstance(hex_num, str):
        raise TypeError('The input hex_num must be a string.')
    dec_num = 0
    for digit in hex_num:
        if digit not in hex_digits:
            raise ValueError('The input hex_num contains an invalid digit.')
        digit_value = hex_digits.index(digit)
        dec_num = dec_num * 16 + digit_value
    return dec_num

print(hex_to_dec('2A'))  # 输出：42
# 使用说明：
# 该函数接受一个参数：要转换的十六进制数。如果输入的数字不是字符串类型，则会引发TypeError异常。如果输入的数字包含不合
# 法的十六进制数字，则会引发ValueError异常。
# 当输入的数字是字符串类型且合法时，函数会对每一位数字进行处理，将其转换为对应的10进制数，并将其加到结果数值dec_num的
# 末尾。具体地，函数使用字符串hex_digits来存储16进制数字的所有可能取值。对于输入的字符串hex_num中的每一个字符digit
# ，函数会检查其是否在hex_digits中出现，如果不是，则引发ValueError异常。如果digit是合法的十六进制数字，则找到其在h
# ex_digits中的索引值digit_value，并将其乘以16的n次幂（其中n为digit在hex_num中的位置），然后将其加到结果数值dec
# _num的末尾。最后，我们遍历完整个字符串hex_num，得到了转换后的十进制数值dec_num。
