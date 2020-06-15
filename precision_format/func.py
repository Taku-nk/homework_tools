'''
You can convert the value format with precision like
    0.09999 --> 0.100
    0.123   --> 0.123
    1.234   --> 1.23
    99.99   --> 1.00⨯10²

For example,
consider you have a value = 0.05678.
You want to round the value to
    - '1.23⨯10²' in this format ----> use "to_sig(value, precision=3, index_format=True)"
    - '0.0568'   in this format ----> use "to_sig(value, precision=3, decimal_point=True)"
    - right format automatically ----> use "to_sig(value, precision=3)"
'''


'''make string number from standard to superscript'''
def to_super(number):
    '''input : standard number string
       output: superscript number string'''
    super_num = ''
    if number[1] == '0':
        number = number[:1]+number[2:]
        
    for c in number:
        if c == '0':
            super_num += '⁰'
            
        elif c == '1':
            super_num += '¹'
        elif c == '2':
            super_num += '²'
        elif c == '3':
            super_num += '³'
        elif c == '4':
            super_num += '⁴'
        elif c == '5':
            super_num += '⁵'
        elif c == '6':
            super_num += '⁶'
        elif c == '7':
            super_num += '⁷'
        elif c == '8':
            super_num += '⁸'
        elif c == '9':
            super_num += '⁹'
        elif c == '-':
            super_num += '⁻'
        else:
            pass
    
    return super_num


# returns this kind of things '⨯10²'.
def index10(index_str_number):
    return '⨯10' + to_super(index_str_number)



def to_sig_in(num, precision=3):
    '''returns num string e.g 1.26⨯10⁸
       first_part == 1.25791
       second_part == +08'''
    num_str = '{:e}'.format(num)  # -1.25791e+08
    num_str_list = num_str.split('e') # ['-1.25791', '+08']
    
    first_part = num_str_list[0]
    second_part = num_str_list[1]
    
    first_part = float(first_part)
    first_part = round(first_part, precision-1)
    first_part = str(first_part)
    
    while len(first_part.replace('-', '')) < precision + 1:  # len('1.0') = 3. want it to be 1.00 <--- sig = 3  len=4
        first_part += '0'
        
    second_part = index10(second_part)
    
    
    return first_part + second_part


def count_precision(num_str): # 有効桁数をstring数字から求める。
    '''count the significant digits from string number'''
    rounded_sig = num_str
    rounded_sig = rounded_sig.replace('-', '')
    rounded_sig = rounded_sig.replace('.', '')
    #     print(rounded_sig)
    #     new_rounded_sig = rounded_sig
    while rounded_sig[0] == '0':
        rounded_sig = rounded_sig[1:]

    return len(rounded_sig)   


def is_period(num_str):  # if num_str contains '.', this function returns True
    '''
    find the existance of the period '.'
    example:  0.001, 1.2 42.0 -->True , 100, 56, 193 --> False 
    '''
    for c in num_str:
        if c == '.':
            return True
    else:
        return False



def sig_float(num, precision=3): # 有効数字n桁の小数表示を返す。
    '''
    Round the number with significant format

    sig_float(num, precision=3) if you want 3 significant digits,
    then you will specify 'precision' as 3 for example.
    
    example : returns 0.01299 --> 0.0130
    '''
    rounded = ('{:.' + str(precision) + 'g}').format(num)
    
    
    # 1.230, 102.0 とゼロを最後につける 
    
    
    while count_precision(rounded) < precision:
        if is_period(rounded):
            rounded += '0'
        else:
            rounded += '.0'
    
    
    return rounded


def is_01_to_99(num, precision): 
 # first, if the arguments are  (num=99.99,  precision=3) , 
 # it'll be rounded to 'num = 100' and its format must be '1.00⨯10²'
 # and (num=0.09999, precision=3) must be rounded to 'num=0.100'
    num_str = '{:e}'.format(num)
    num_str = num_str.split('e')
    num_str[0] = str(round(float(num_str[0]), precision-1))
    num_str = '{}e{}'.format(num_str[0], num_str[1])
    num = float(num_str)                                    
    
    rounded = num # will be returned
    
    num *= 100  # 12.3
    num = abs(num)
    count = 0
    while(num > 0):
        count += 1 # 0 -> 1
        num = num//10  # 12.3 -> 1.0
    
    if count == 2:    # 0.123
        return True, rounded  
    elif count == 3:  # 1.234
        return True, rounded  
    elif count == 4:  # 12.34
        return True, rounded  
    else:             # others
        return False, rounded  


def to_sig(num, precision=3, index_format=False, decimal_point=False): 
    '''returns strings of a number with precision and significant format'''
    
    num_type, rounded_num = is_01_to_99(num, precision) # num_type is boolian. if the number is 0.1 to 99.99... then True
    
    # when format style is specified manually
    if index_format == True:
        return to_sig_in(rounded_num, precision)
    if decimal_point == True:
        return sig_float(rounded_num, precision)

    
    # In default, the format style is chosen automatically
    if num_type:
        return sig_float(rounded_num, precision)
    else:
        return to_sig_in(rounded_num, precision)