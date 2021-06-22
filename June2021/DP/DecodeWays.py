'''
letter from a to b are enocded from 1 to 26, we have to count the number of ways in whih letters can be decoded
'''

from typing import DefaultDict


def decode(s):
    if not s:
        return 0

    n = len(s)
    dp = [0]*(n+1)

    dp[0] = 1
    dp[1] = 0 if s[0]=='0' else 1

    for i in range(2,n+1):
        if 0<int(s[i-1:i])<=9:
            dp[i] += dp[i-1]

        if 10<=int(s[i-2:i])<=26:
            dp[i] += dp[i-2]

    return dp[n]

print(decode('12'))