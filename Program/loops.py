# greeting="Good Morning"
#
# if "Good Morning" == greeting:
#     print("Condition is:-", True)
# else:
#     print("Condition is:-", False)
# print("If else condition code is completed")
#
# # For loop
#
# obj = [2, 4, 3, 6, 8, 5, 2]
# print("=======:- 'Run The for loop' -:========")
# for i in range(len(obj)):
#     print(f"Index: {i}, objects: {obj[i]*2}")

# Sum of first Natural numbers 1+2+3+4...

print("====== Sum of first Natural numbers 1+2+3+4... =========")
summation = 0
for j in range(1, 6):
    summation = summation + j
    print('Summation is:-', summation)

print("***************************")
for k in range(1, 10, 2):
    print(k)


print("*************SKIPPING FIRST INDEX**************")
for m in range(10):
    print(m)