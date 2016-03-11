import unittest

#Find the smallest number which is multiple of all the numbers from 1-n

#Any number to be multiple of all number needs to be a multiple of all prime numbers in that range
def isprime(num):
    if num==0 or num==1:
        return 0
    elif num==2 or num==3:
        return 1
    elif num%2==0:
        return 0
    else:
        for i in range(3,int(num**0.5)+1,2):
            if num%i==0:
                return 0
    return 1
 

def  smallest_multiple(n):
    #to hold list of all prime numbers from 1-n
    prime_list=list()
    # to hold product of all prime numbers in the given range    
    base_product=1

    #finding all prime numbers
    for num in range(1,n+1):
            if isprime(num)==1:
                prime_list.append(num)
    
    #Calculating their product
    for prime_num in prime_list:
        base_product=base_product*prime_num

    #To hold the required result    
    smallest_product=base_product
    while(True):
        undivisible_found=0 
        for i in range(1,n+1):
            #go for the next possible number if this number is NOT divisible by any one in the range
            if (smallest_product%i)!=0:
                undivisible_found=1
                break
        if undivisible_found==0:
            return smallest_product
        else:
            smallest_product=smallest_product+base_product

class Test(unittest.TestCase):

    def test_smallest_multiple(self):
        self.assertEqual(smallest_multiple(10),2520)

    def test_condition_1(self):
        self.assertEqual(smallest_multiple(1),1)

    def test_condition_only_prime(self):
        self.assertEqual(smallest_multiple(3),6)

    def test_condition_only_1_non_prime(self):
        self.assertEqual(smallest_multiple(5),60)


if __name__ == '__main__':
    unittest.main()
