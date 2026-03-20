class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend==-2147483648 and divisor==-1:
            return 2147483647

        sign=(dividend>0)==(divisor>0)
        dividend,divisor=abs(dividend),abs(divisor)

        res=0

        while dividend>=divisor:
            temp_divisor=divisor
            multiple=1

            while dividend>=(temp_divisor<<1):
                temp_divisor<<=1
                multiple<<=1

            dividend-=temp_divisor
            res+=multiple


        return res if sign else -res 