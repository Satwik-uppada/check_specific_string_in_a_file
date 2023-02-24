# Binary_search function .... it checks where the element is in array
def Binary_search(array,key):
    first=0  # initialize first as 0 for starting index
    last=len(array)-1 # initialize last as len(array)-1 because it takes last index of given array
    while first<=last:  #while loop terminates when the first value is greater than last value.
        mid_value=(first+last)//2  # finding the middle index. "//" for getting absolute value without decimal

        if array[mid_value]==key: # condition used to check if element is found at mid_value of the list
            return print("Found {} at index {}".format(key,mid_value)) # if the key found at mid_value itself it returns it
        elif array[mid_value]<key: # condition checks if key is greater than the mid_value element.
            first=mid_value+1      # initialising the first value with mid_value+1;
        else:                      # condition checks if target is less than the middle element.
            last=mid_value-1       # initialising the last value with mid_value-1;
    return print("{} is not found in this array.".format(key)) # if first index is greater than last then this return below statement

input_values=input("Enter the elements(comma-separated): ") # taking user input separated by commas

# i check the array elements with try and except block
try : # if there is no problem in code return result as per key by executing Binary_search function inside try block
  list=input_values.split(",") # here , i just split the input where "," exists
  array=[]  # i initialize an empty array
  for i in list:  # here ,i call for loop ,i m storing split list into i
       array.append(int(i))
       # storing i in array by append function

  key=int(input("Enter the key element: "))  # taking key value input by user

  Binary_search(array,key)  # calling Binary_search function

except: # if any error in inputs or output this block comes to field to execute
    print("Error")
    print("------------------------------------------------------------------------------------")
    print("*** Help ***")
    print("1.Check the input once,may we it has extra comma or different type of value")
    print("2.Check the key value,May be you gave different data type in it")





