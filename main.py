# def is_prime(num):
#     if num > 1:
#         for i in range(2, num):
#             if num % i == 0:
#                 return False
#         return True
#     else:
#         return False
#
# def get_first_n_primes(n):
#     primes = []
#     i = 2
#     while len(primes) < n:
#         if is_prime(i):
#             primes.append(i)
#         i += 1
#     return primes

# def mean(numbers):
#     return sum(numbers) / len(numbers)
#
# first_10_primes = get_first_n_primes(10)
# mean_of_first_10_primes = mean(first_10_primes)
#
# print("The mean of the first 10 prime numbers is:", mean_of_first_10_primes)


str="satwik uppada"
print(str.center(40,"*"))
str2="*************satwik uppada**************"
print(len(str2))