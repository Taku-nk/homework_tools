## func.to_sig(value, precision, index_format=False, decimal_point=False)
You can convert the value format with precision like
> 0.09999 --> 0.100

> 0.123   --> 0.123

> 1.234   --> 1.23

> 99.99   --> 1.00⨯10²

For example,
consider you have a value = 0.05678.
You want to round the value to
- '5.68⨯10⁻²' in this format ----> use `to_sig(value, precision=3, index_format=True)`
- '0.0568'   in this format ----> use `to_sig(value, precision=3, decimal_point=True)`
- right format automatically ----> use `to_sig(value, precision=3)`
