#NUMPY - maths numerical python
import numpy as np#shortens the abbreviation

from time import process_time #proves numpy is faster
#time taken by list
python_list = [ i for i in range(10000000)]
start_time1 = process_time(); print("Start time:",start_time1)
python_list = [i+5 for i in python_list]
end_time1 = process_time(); print("End time:",end_time1)
print("Time taken by list",end_time1 - start_time1)
#time taken by numpy array
np_array = np.array([i for i in range(10000000)])
start_time2 = process_time();print("Start time:",start_time2)
np_array += 5
end_time2 = process_time(); print("End time:",end_time2)
print("Time taken by array",end_time2 - start_time2)#numpy>fast>>list

np_arr = np.array([1,2,3,4,5])
print(np_arr,type(np_arr),"size:",np_arr.shape)
np_mat = np.array([(1,2,3,4,5),(5,4,3,2,1)],dtype = float)
print(np_mat,type(np_mat),"size:",np_mat.shape) 
#Initial placeholders
x = np.zeros((3,5))#zeros
print(x)
y = np.ones((4,7),dtype = int)#ones
print(y)
z = np.full((2,6),8.23)#any other number
print(z)
a = np.eye(4)#identity matrix
print(a)
b = np.random.random((4,5))#random values between 0 and 1
print(b)
c = np.random.randint(30,70,(3,6))#random values between 30 and 70
print(c)
d = np.linspace(10,30,6,dtype = int)#evenly spaced 6 values, 30 included
print(d)
e = np.arange(10,30,5.5)#difference between the evenly spaced numbers, ie, step
print(e)
#list into array
list2 = [10,20,30,40,50,60]
nparr = np.asarray(list2)
print(nparr, type(nparr))
#Analysing a numpy array
r = np.random.randint(10,90,(4,7))
print("array:")
print(r)
print("shape:",r.shape)
print("dimensions:",r.ndim)
print("no of elements:",r.size)
print("data type:",r.dtype)

#Mathematical Operations
lst1 = [9,8,7,6,5]
lst2 = [1,2,3,4,5]
print(lst1 + lst2) #2 lists are joined

n_arr1 = np.random.randint(11,20,(3,3))
print("ARRAY 1:\n",n_arr1)
n_arr2 = np.random.randint(1,10,(3,3))
print("ARRAY 2:\n",n_arr2)
print("SUM:\n",np.add(n_arr1,n_arr2)) #print(n_arr1 + n_arr2)
print("DiIFFERENCE:\n",np.subtract(n_arr1,n_arr2)) #print(n_arr1 - n_arr2)
print("PRODUCT:\n",np.multiply(n_arr1,n_arr2)) #print(n_arr1 * n_arr2)
print("QUOTIENT:\n",np.divide(n_arr1,n_arr2)) #print(n_arr1 / n_arr2)
print("REMAINDER:\n",np.remainder(n_arr1,n_arr2)) #print(n_arr1 % n_arr2)

#Array Manipulation
#transposing
arr1 = np.random.randint(11,20,(2,3))
print("Array:\n",arr1, arr1.shape)
trans =arr1.T #np.transpose(arr1) 
print("Transpose:\n",trans, trans.shape)
#reshaping
arr1 = arr1.reshape(3,2)
print("Array Reshaped:\n",arr1,arr1.shape)