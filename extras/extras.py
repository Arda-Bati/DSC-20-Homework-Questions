"""
DSC 20 HW 07
NAME:
PID:
"""

def xor_strings(bin_num1, bin_num2):
    """
    Does XOR opearation on two single digit binary numbers
    >>> xor_strings('0', '0')
    '0'
    >>> xor_strings('0', '1')
    '1'
    >>> xor_strings('1', '0')
    '1'
    >>> xor_strings('1', '1')
    '0'

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    """
    assert isinstance(bin_num1, str)
    assert isinstance(bin_num2, str)
    assert len(bin_num1) == len(bin_num2) == 1
    return '0' if(bin_num1 == bin_num2) else '1';

## Question 1 ##

def char_encode(chars_str):
    """
    Returns gray encoding version of the chars_str.
    Parameters: (str) chars_str, composed only of letters from the english
    alphabet (should be validated)
    Returns: (str) chars_str in gray encoding.
    Restrictions: You should do input validation.
    >>> char_encode('MaRinA')
    '01010\\n00000\\n11001\\n01100\\n01011\\n00000'
    >>> char_encode('EniGma')
    '00110\\n01011\\n01100\\n00101\\n01010\\n00000'
    >>> arda_str = char_encode('Arda')
    >>> print(arda_str)
    00000
    11001
    00010
    00000

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    """

    def convert_bin_gray(binary_enc):
        """
        Converts binary encoded number into gray encoding
        """
        gray_enc = '';
        gray_enc += binary_enc[0];
        for i in range(1, len(binary_enc)):
            gray_enc += xor_strings(binary_enc[i - 1], binary_enc[i])
        return gray_enc;

    assert isinstance(chars_str, str)
    alphabet_start = 'a'
    alphabet_end   = 'z'
    l_bound, u_bound = ord(alphabet_start), ord(alphabet_end)
    chars_str = chars_str.lower()
    assert all(l_bound <= ord(char) <= u_bound  for char in chars_str)

    pad_len = 5
    encoding = ''
    for char in chars_str:
        binary_enc = '{0:05b}'.format(ord(char) - l_bound)
        gray_enc   = convert_bin_gray(binary_enc)
        encoding   += gray_enc + '\n'
    return encoding[:-1]

## Question X.1 ##

def split_num(num, limit):
    """
    Implements the split_num function described in QX.1 of HW06.
    Restrictions:
    You should use recursion. You should do input validation.
    Parameters:
    num   (int): The number to be split.
    limit (float): Division should stop if each element is smaller than
    this number
    Returns:
    (tuple) The number num, split in tuple form.
    >>> split_num(5, limit = 5)
    5
    >>> split_num(5, limit = 2.5)
    (2.5, 2.5)
    >>> split_num(5, limit = 1.25)
    ((1.25, 1.25), (1.25, 1.25))
    >>> split_num(5, limit = 1)
    (((0.625, 0.625), (0.625, 0.625)), ((0.625, 0.625), (0.625, 0.625)))

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    """
    assert isinstance(limit, (int, float))
    assert num > 0
    assert limit > 0
    round_factor = 3
    s_size = 2

    if num <= limit:
        return round(num, round_factor)
    else:
        return (split_num(num / s_size, limit), split_num(num / s_size, limit))

## Question X.2 ##
def split_with_levels(num, levels):
    """
    Implements the split_with_levels function described in QX.2 of HW06.
    Restrictions:
    You should use recursion. You should do input validation.
    Parameters:
    num    (int): The number to be split.
    levels (int): The splits should be done for "levels" times
    Returns:
    (tuple) The number num, split in tuple form.
    split_with_levels(4, 1)
    (2.0, 2.0)
    split_with_levels(3, 2)
    ((0.75, 0.75), (0.75, 0.75))
    split_with_levels(5, 3)
    (((0.625, 0.625), (0.625, 0.625)), ((0.625, 0.625), (0.625, 0.625)))

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    """
    assert isinstance(levels, int)
    assert num > 0
    assert levels >= 0
    round_factor = 3
    s_size = 2
    def split_num(num):
        if num <= limit:
            return round(num, round_factor)
        else:
            return (split_num(num / s_size), split_num(num / s_size))

    limit = num / (s_size ** (levels))
    return split_num(num)

## Question X.3 ##
def split_division_n(num, levels, s_size):
    """
    Implements the split_num function described in QX.3 of HW06.
    Restrictions:
    You should use recursion. You should do input validation.
    Parameters:
    num    (int): The number to be split.
    levels (int): The splits should be done for "levels" times.
    s_size (int): Split size for the splits at each level
    Returns:
    (tuple) The number num, split in tuple form.
    >>> split_division_n(5, levels = 1, s_size = 4)
    (1.25, 1.25, 1.25, 1.25)
    >>> split_division_n(5, levels = 2, s_size = 3)
    ((0.556, 0.556, 0.556), (0.556, 0.556, 0.556), (0.556, 0.556, 0.556))
    >>> split_division_n(5, levels = 3, s_size = 2)
    (((0.625, 0.625), (0.625, 0.625)), ((0.625, 0.625), (0.625, 0.625)))
    >>> split_division_n(4, levels = 2, s_size = 3)
    ((0.444, 0.444, 0.444), (0.444, 0.444, 0.444), (0.444, 0.444, 0.444))

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    """
    assert isinstance(levels, int)
    assert isinstance(s_size, int)
    assert num > 0
    assert levels >= 0
    assert s_size >= 2
    round_factor = 3
    def split_num_V2(num):
        if num <= limit:
            return round(num, round_factor)
        else:
            return tuple(split_num_V2(num / s_size) for i in range(s_size))

    limit = num / (s_size ** (levels))
    return split_num_V2(num)
