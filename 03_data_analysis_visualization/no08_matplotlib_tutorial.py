#Matplotlib - useful for making plots
import matplotlib.pyplot as plt
#import numpy to get data for plots
import numpy as np

x = np.linspace(0,10,100)
y = np.sin(x)
z = np.cos(x)
print("Array:\n",x)
print("Sine of array:\n",y)
print("Cosine of array:\n",z)

plt.plot(x,y)#plotting values
plt.show()#general - line plot
plt.plot(x,z)
plt.xlabel('Angle')#name for X-Axis
plt.ylabel('Cosine Value')#name for Y-Axis
plt.title('Cosine Waveform')#name for the Plot
plt.show()#plot display

#PLotting multiple graphs in a single plot
a = np.linspace(-10,10,20)
b = a**2#parabola
c = a*2
d = a/2
plt.plot(a,b,'r+')#plots in plus and red color
plt.plot(a,c,'g.')#plots in dots and green color
plt.plot(a,d,'b*')#b for blue
plt.show()
#other signs are x,- is for line plot, '=' is not allowed

#Bar plots
fig = plt.figure()
ax = fig.add_axes([0.1,0.1,0.8,0.8]) #0.1,0.1 origin, 0.8,0.8 are height and width
languages = ['English','Spanish','French','Latin','Bengali']
people = [100,50,30,65,95]
ax.bar(languages,people)
plt.xlabel('LANGUAGES')
plt.ylabel('NUMBER OF PEOPLE')
plt.show()

#Pie Chart
ax.pie(people ,labels = languages, autopct = '%1.1f%%' )
plt.show()

#Scatter Plot
x1 = np.linspace(0,10,30)
y1 = np.sin(x1)
z1 = np.cos(x1)
fig1 = plt.figure()
ax = fig1.add_axes([0.1,0.1,0.8,0.8])
ax.scatter(x1,y1,color='g')
ax.scatter(x1,z1,color='b')
plt.show()

#3D Scatter Plot
fig2 = plt.figure()
ax = plt.axes(projection = '3d')
z = 20 * np.random.random(1000)
x = np.sin(z)
y = np.cos(z)
ax.scatter(x,y,z, c=z, cmap= 'Blues')
plt.show()