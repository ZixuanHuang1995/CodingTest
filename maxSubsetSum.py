# tsmc hackerank
import math

def maxSubsetSum(arr):
    result = []

    for num in arr:
        factor_sum = 0
        sqrt_n = int(math.isqrt(num))
        
        for i in range(1, sqrt_n + 1):
            if num % i == 0:
                factor_sum += i
                if i != num // i:
                    factor_sum += num // i

        result.append(factor_sum)

    return result

# testing cases
print(maxSubsetSum([12]))  # Output: [28]
print(maxSubsetSum([1, 6, 28]))  # Output: [1, 12, 56]