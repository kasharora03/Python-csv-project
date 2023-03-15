import furniture
import pandas as pd
import numpy as np
furniture.menu()

choice='YES'
while choice=='YES':

    ch=int(input('Enter Choice from main menu[1,2,3,4,5,6]='))
    if ch==1:
        print("\t\tReading Records")
        print(" Choose from menu under Reading Records[1,2,3,4,5,6,7,8,9,10,11]")
        furniture.table()
    elif ch==2:
        print("Enter coice from menu under Data Vizualization[1,2,3]")
        furniture.graph()
                
    elif ch==3:
        print("Enter records column wise")
        furniture.addnew()
        print("Records Added Successfully")

    elif ch==4:

        furniture.tdel()
    elif ch==5:
        print(" Program Exited")
        print('Thank You for using the program')
        print('\t Made By:')
        print('\t KASHISH ARORA \n')
        break
               
    else:
        print("Invalid Choice")
    choice=input("Do you want to continue the program \n Press YES/NO=" )
    if choice=='YES':
        print()
    else:
        print('Thank You for using the program')
        print('\t Made By:')
        print('\t KASHISH ARORA \n ')
    
           
        
