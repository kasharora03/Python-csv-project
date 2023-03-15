#project on furniture sales data
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def menu():
    print("------------------------------------------------------------")
    print("\t\t\t Project Work ")
    print("------------------------------------------------------------")
    print("\t\tAccessing CSV file data using python")
    print("\t\t\tFurniture Sales Data")
    print("Data Analysis")
    print("\t1.Reading Records")
    print("\t\t--1.Display data without index")
    print("\t\t--2.Display records with index")
    print("\t\t--3.Display data from top as per user's choice")
    print("\t\t--4.Display data from bottom as per user's choice")
    print("\t\t--5.Display data from top and bottom as per user's choice ")
    print("\t\t--6.Display data with index specified by user")
    print("\t\t--7.Display data in ascending order of column specified by user")
    print("\t\t--8.Display data in descending order of column specified by user")
    print("\t\t--9.Display the number of Rows and Columns")
    print()
    print("Data Visualization ")
    print("\t2.Analysis of data using different graph")
    print("\t\t--1. Bar Graph ")
    print("\t\t--2.Horizontal Bar Graph ")
    print("\t\t--3.Line Graph ")
    print()
    print("Data Manipulation ")
    print("\t3.Adding Records")
    print()
    print("\t4.Deleting record as per user's choice")
    print("\t\t--1.Deleting records temporarily")
    print()
    print("\t5.Exit Program")

#1
def table():
    record=int(input("Enter choice from Reading Records ="))
    if record==1:
        no_index()
    elif record==2:
        read()
    elif record==3:
        head()
    elif record==4:
        tail()
    elif record==5:
        both()
    elif record==6:
        iloc()
    elif record==7:
        sort()
    elif record==8:
        rsort()
    elif record==9:
        shape()
    else:
        print("Invalid Choice")
        

#1.1 
def no_index():
    print("\tShowing Data Without Index")
    print()
    col=["Order ID","Customer ID","Customer Name","Item Code","Item Name","Price","Quantity","Discount","Grand Total"]
    df1=pd.read_csv("C:\\Users\\simran\\Desktop\\furnitureproject.csv",index_col=0,usecols=col)
    print(df1)
#1.2
def read():
    print("\tShowing Data With Index")
    print()
    col=["Order ID","Customer ID","Customer Name","Item Code","Item Name","Price","Quantity","Discount","Grand Total"]
    df1=pd.read_csv("C:/Users/simran/Desktop/furnitureproject.csv",usecols=col)
    print(df1)



    
#1.3
def head():
    
    col=["Order ID","Customer ID","Customer Name","Item Code","Item Name","Price","Quantity","Discount","Grand Total"]
    df1=pd.read_csv("C:/Users/simran/Desktop/furnitureproject.csv",usecols=col)
    a=int(input("Enter range for rows to be displayed from top="))
    print("\tShowing Data From Top")
    print()
    print(df1.head(a))
   
#1.4
def tail():
    
    col=["Order ID","Customer ID","Customer Name","Item Code","Item Name","Price","Quantity","Discount","Grand Total"]
    df1=pd.read_csv("C:/Users/simran/Desktop/furnitureproject.csv",usecols=col)
    a=int(input("Enter range for rows to be displayed from bottom="))
    print("\tShowing Data From Bottom")
    print()
    print(df1.tail(a))

#1.5
def both():
    
    col=["Order ID","Customer ID","Customer Name","Item Code","Item Name","Price","Quantity","Discount","Grand Total"]
    df1=pd.read_csv("C:/Users/simran/Desktop/furnitureproject.csv",usecols=col)
    a=int(input("Enter range for rows to be displayed from top="))
    b=int(input("Enter range for rows to be displayed from bottom="))
    print("\tShowing Data From Top And Bottom")
    print()
    print(df1.head(a))
    print()
    print(df1.tail(b))
#1.6
def iloc():
    a=int(input("Enter Starting Row Index="))
    b=int(input("Enter Last Row Index="))
    col=["Order ID","Customer ID","Customer Name","Item Code","Item Name","Price","Quantity","Discount","Grand Total"]
    df1=pd.read_csv("C:/Users/simran/Desktop/furnitureproject.csv",usecols=col)
    print(df1.iloc[a:b+1])
    


#1.7
def sort():
    df1=pd.read_csv("C:/Users/simran/Desktop/furnitureproject.csv")
    col=["Order ID","Customer ID","Customer Name","Item Code","Item Name","Price","Quantity","Discount","Grand Total"]
    df1=pd.read_csv("C:/Users/simra/Desktop/furnitureproject.csv",index_col=0,usecols=col)
    print("Sorting columns based on user's choice")
    a=input("Enter Column Name=")
    print(df1.sort_values(by=[a],ascending=True))
#1.8
def rsort():
    df1=pd.read_csv("C:/Users/simran/Desktop/furnitureproject.csv")
    col=["Order ID","Customer ID","Customer Name","Item Code","Item Name","Price","Quantity","Discount","Grand Total"]
    df1=pd.read_csv("C:/Users/simra/Desktop/furnitureproject.csv",index_col=0,usecols=col)
    print("Sorting columns based on user's choice")
    a=input("Enter Column Name=")
    print(df1.sort_values(by=[a],ascending=False))
#1.9
def shape():
    
    df1=pd.read_csv("C:/Users/simran/Desktop/furnitureproject.csv")
    col=["Order ID","Customer ID","Customer Name","Item Code","Item Name","Price","Quantity","Discount","Grand Total"]
    df1=pd.read_csv("C:/Users/simra/Desktop/furnitureproject.csv",usecols=col)
    print("Number of Rows and Columns ")
    print(df1.shape)
    





#2
def graph():
    
    print("1.Bar Graph \n 2.Horizontal Bar Graph \n 3.Line Graph ")
    print()
    ch=int(input("Enter your choice:"))
    if ch==1:
        bar()
    elif ch==2:
        hbar()
    elif ch==3:
        line()
    else:
        print('Invalid Choice')
       
#2.a        
def bar():
    df1=pd.read_csv("C:/Users/simran/Desktop/furnitureproject.csv")#
    print("Columns for X axis \t\t Columns for Y axis")
    print('Order ID\t\t\t Price\n Customer ID\t\t\t Quantity\n Customer Name\t\t\t Discount\n Item Code\t\t\t Grand Total ')
    print()
    a=input('Enter variable for x axis=')
    b=input('Enter variable for y axis=')
    d=df1[a].tolist()
    e=df1[b].tolist()
    plt.bar(d,e,label='Analysis based on conditions',edgecolor='black')
    plt.xlabel(a)
    plt.ylabel(b)
    plt.legend(title='Legend',loc='upper right')
    plt.show()
    
#2.b 
def hbar():
    df1=pd.read_csv("C:/Users/simran/Desktop/furnitureproject.csv")
    print("Columns for X axis \t\t Columns for Y axis")
    print('Order ID\t\t\t Price\n Customer ID\t\t\t Quantity\n Customer Name\t\t\t Discount\n Item Code\t\t\t Grand Total ')
    print()
    a=input('Enter variable for x axis=')
    b=input('Enter variable for y axis=')
    d=df1[a].tolist()
    e=df1[b].tolist()
    plt.barh(d,e,label='Analysis based on conditions',edgecolor='black')
    plt.xlabel(a)
    plt.ylabel(b)
    plt.legend(title='Legend',loc='upper right')
    plt.show()
    
#2.c
def line():
    df1=pd.read_csv("C:/Users/simran/Desktop/furnitureproject.csv")
    print("Columns for X axis \t\t Columns for Y axis")
    print('Order ID\t\t\t Price\n Customer ID\t\t\t Quantity\n Customer Name\t\t\t Discount\n Item Code\t\t\t Grand Total ')
    print()
    a=input('enter variable for x axis=')
    b=input('enter variable for y axis=')
    d=df1[a].tolist()
    e=df1[b].tolist()
    plt.plot(d,e,marker='o',markersize='10',markerfacecolor='red',label='Analysis based on conditions')
    plt.xlabel(a)
    plt.ylabel(b)
    plt.title("Analysis based on conditions")
    plt.legend(title='Legend',loc='upper right')
    plt.show()
    

   




#4  
def addnew():
    a=int(input("Enter Order ID="))
    b=int(input("Enter Customer ID="))
    c=input("Enter Customer Name=")
    d=int(input("Enter Item Code="))
    e=input("Enter Item Name=")
    f=int(input("Enter Price="))
    g=int(input("Enter Quantity="))
    h=int(input("Enter Discount="))
    i=f*g-(f*g*(h/100))
    
    df1=pd.DataFrame(data=[[a,b,c,d,e,f,g,h,i]],columns=["Order ID","Customer ID","Customer Name",
                                                         "Item Code","Item Name","Price","Quantity","Discount","Grand Total"])

    df1.index=range(len(df1.index))
    
    df1.to_csv("C:\\Users\\simran\\Desktop\\furnitureproject.csv",mode='a',header=False)

    
#3.2 temporarily delete 
def tdel():
    col=["Order ID","Customer ID","Customer Name","Item Code","Item Name","Price","Quantity","Discount","Grand Total"]
    df1=pd.read_csv("C:/Users/simran/Desktop/furnitureproject.csv",index_col="Order ID",usecols=col)
    a=int(input("Enter Order ID to delete="))
    df1=df1.drop([a])
    print(df1)


















    
    
