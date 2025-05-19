class AdvancedMath:
    def power(self,base,exponent):
        return base**exponent
    def factorial(self,n):
        if n==0 or n==1:
            return 1
        else:
            return n*self.factorial(n-1)