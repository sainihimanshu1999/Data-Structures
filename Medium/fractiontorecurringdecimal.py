'''Fraction to recurring decimal'''


def recurringdecimal(numerator,denominator):
    quo,rem = divmod(abs(numerator),abs(denominator))
    sign = '-' if numerator*denominator < 0 else ''
    result = [sign+str(quo),'.']
    remainders = {}


    while rem>0 and rem not in remainders:
        remainders[rem] = len(result)
        quo,rem = divmod(abs(rem*10),abs(denominator))
        result.append(str(quo))


    if rem in remainders:
        index = remainders[rem]
        result.indert(index,'(')
        result.append(')')

    return ''.join(result).rstrip('.')