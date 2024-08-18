class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # initialize ugly number with 1
        ugly_numbers = [1]

        next_mult_of_2 = 2
        next_mult_of_3 = 3
        next_mult_of_5 = 5

        i2 = i3 = i5 = 0
        for _ in range(1, n):
            next_ugly = min(next_mult_of_2, next_mult_of_3, next_mult_of_5)
            ugly_numbers.append(next_ugly)

            if next_ugly == next_mult_of_2:
                i2 += 1
                next_mult_of_2 = ugly_numbers[i2] * 2
            
            if next_ugly == next_mult_of_3:
                i3 += 1
                next_mult_of_3 = ugly_numbers[i3] * 3
            
            if next_ugly == next_mult_of_5:
                i5 += 1
                next_mult_of_5 = ugly_numbers[i5] * 5

        return ugly_numbers[-1]
