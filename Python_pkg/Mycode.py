# # For Debugging use F8 for next
# x=2
# r = x%2
#
# if r == 0:
#     print('Even Number')
# elif r == 1:
#     print('Odd Number')
#
# y = 5
#
# if y == 1:
#     print('One')
# elif y ==2:
#     print('Two')
# elif y==3:
#     print('Three')
# else:
#     print('Wrong input')

# # While Loop to print below output
# # Telusko Rock Rock Rock Rock
# # Telusko Rock Rock Rock Rock
# # Telusko Rock Rock Rock Rock
# # Telusko Rock Rock Rock Rock
# # Telusko Rock Rock Rock Rock
# i = 1
# while i <= 5:
#     print('Telusko', end=' ')
#     j = 5
#     while j > 1:
#         print('Rock', end=' ')
#         j = j -1
#     i = i+1
#     print('')


# For loop
# lst = ['shubham',23,4.6]
# str = 'Shubham'
# for i in str:
#     print(i)
for i in range(20,10,-1):
    if i%5 != 0:
        print(i)
