unit=float(input("enter a unit:"))
if(unit<=100):
    electricity=unit*5
elif(unit>100 and unit<=200):
    electricity=100*5+((unit-100)*8)
else:
    electicity=(100*5)+(100*8)+((unit-200)*10)
print("the electricity bill:",electricity)
    
    


