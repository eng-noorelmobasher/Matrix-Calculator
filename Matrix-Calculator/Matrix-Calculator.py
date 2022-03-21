while True:
 print("\n This Matrix Calculator Has Been Made By Nooreldeen ElMobashar \n")
 print("Some Hints For Using Calculator\n")
 print("To Get The Transpose Of The Matrix Type 'T' \n" )
 print("To Do Mathmatical Operations On Matrices Type 'M' \n")
 print("To Get The Inverse Of The Matrix Type 'I' \n")
 print("To Use Cramer's Rule Type 'C' \n")
 operation = input("Choose The Operation You Want: ")
 if operation == "M" :
    first_matrix = input("Choose The Kind of The First Matrix you want - (3*3 , 2*3 , 1*3 , 3*2 , 3*1 , 2*2 , 1*2 , 2*1 ): ")
    if first_matrix == "3*3" :
        a11 = int(input("\nEnter a11 : "))
        a12 = int(input("Enter a12 : "))
        a13 = int(input("Enter a13 : "))
        a21 = int(input("Enter a21 : "))
        a22 = int(input("Enter a22 : "))
        a23 = int(input("Enter a23 : "))
        a31 = int(input("Enter a31 : "))
        a32 = int(input("Enter a32 : "))
        a33 = int(input("Enter a33 : "))
        print("\nYour First Matrix is:  "  "[",a11,a12,a13,"]")
        print("                      " , "[",a21,a22,a23,"]")
        print("                      " , "[",a31,a32,a33,"]" , "\n")
        second_matrix = input("Choose The Kind of The Second Matrix you want - (3*3 , 2*3 , 1*3 , 3*2 , 3*1 , 2*2 , 1*2 , 2*1 ): ")
        if second_matrix == "3*3" :
         b11 = int(input("\nEnter b11 : "))
         b12 = int(input("Enter b12 : "))
         b13 = int(input("Enter b13 : "))
         b21 = int(input("Enter b21 : "))
         b22 = int(input("Enter b22 : "))
         b23 = int(input("Enter b23 : "))
         b31 = int(input("Enter b31 : "))
         b32 = int(input("Enter b32 : "))
         b33 = int(input("Enter b33 : "))
         print("\nYour Second Matrix is:" , "[",b11,b12,b13,"]")
         print("                      " , "[",b21,b22,b23,"]")
         print("                      " , "[",b31,b32,b33,"]" , "\n") 
         opt = input("Choose The Operation You Want: ( * , +  , - ) : ")  
         if opt == "*" :
            print("\nYour Result is: " ,"[",(a11*b11) + (a12*b21) + (a13*b31) , (a11*b12) + (a12*b22) + (a13*b32) , (a11*b13) + (a12*b23) + (a13*b33),"]")    
            print("                " ,"[",(a21*b11) + (a22*b21) + (a23*b31) , (a21*b12) + (a22*b22) + (a23*b32) , (a21*b13) + (a22*b23) + (a23*b33),"]")
            print("                " ,"[",(a31*b11) + (a32*b21) + (a33*b31) , (a31*b12) + (a32*b22) + (a33*b32) , (a31*b13) + (a32*b23) + (a33*b33),"]")
         elif opt == "+":
            print("\nYour Result is: " , "[" , (a11+b11) , (a12+b12) , (a13+b13) , "]")   
            print("                  " , "[" , (a21+b21) , (a22+b22) , (a23+b23) , "]") 
            print("                  " , "[" , (a31+b31) , (a32+b32) , (a33+b33) , "]")  
         elif opt == "-":
            print("\nYour Result is: " , "[" , (a11-b11) , (a12-b12) , (a13-b13) , "]")   
            print("                  " , "[" , (a21-b21) , (a22-b22) , (a23-b23) , "]") 
            print("                  " , "[" , (a31-b31) , (a32-b32) , (a33-b33) , "]")   
         else:
                print("wrong input")  
        elif second_matrix == "2*3" :
            b11 = int(input("\nEnter b11 : "))
            b12 = int(input("Enter b12 : "))
            b13 = int(input("Enter b13 : "))
            b21 = int(input("Enter b21 : "))
            b22 = int(input("Enter b22 : "))
            b23 = int(input("Enter b23 : "))
            print("\nYour Second Matrix is:" , "[",b11,b12,b13,"]")
            print("                      " , "[",b21,b22,b23,"]" , "\n")
            opt = input("Choose The Operation You Want: ( * , +  , - ) : ")  
            if opt == "*":
                print("Impossible to multiplicate 3*3 with 3*2") 
            elif opt == "+":
                print("Impossible to Add 3*3 to 3*2") 
            elif opt == "-":
                print("Impossible to Subtract 3*3 from 3*2") 
            else:
                print("wrong input")        
        elif second_matrix == "1*3" :
            b11 = int(input("\nEnter b11 : "))
            b12 = int(input("Enter b12 : "))
            b13 = int(input("Enter b13 : "))
            print("\nYour Second Matrix is:" , "[",b11,b12,b13,"]" , "\n")      
            opt = input("Choose The Operation You Want: ( * , +  , - ) : ")  
            if opt == "*":
                print("Impossible to multiplicate 3*3 with 3*1") 
            elif opt == "+":
                print("Impossible to Add 3*3 to 3*1") 
            elif opt == "-":
                print("Impossible to Subtract 3*3 from 3*1") 
            else:
                print("wrong input")           
        elif second_matrix == "2*2" :
            b11 = int(input("\nEnter b11 : "))
            b12 = int(input("Enter b12 : "))
            b21 = int(input("Enter b21 : "))
            b22 = int(input("Enter b22 : "))
            print("\nYour Second Matrix is:" , "[",b11,b12,"]")
            print("                      " , "[",b21,b22,"]" , "\n")
            opt = input("Choose The Operation You Want: ( * , +  , - ) : ")  
            if opt == "*":
                print("Impossible to multiplicate 3*3 with 2*2") 
            elif opt == "+":
                print("Impossible to Add 3*3 to 2*2") 
            elif opt == "-":
                print("Impossible to Subtract 3*3 from 2*2") 
            else:
                print("wrong input") 
        elif second_matrix == "2*1" :
            b11 = int(input("\nEnter b11 : "))
            b21 = int(input("Enter b21 : " , "\n"))
            print("\nYour Second Matrix is:" , "[",b11,"]")
            print("                      " , "[",b21,"]" , "\n")  
            opt = input("Choose The Operation You Want: ( * , +  , - ) : ")  
            if opt == "*":
                print("Impossible to multiplicate 3*3 with 2*1") 
            elif opt == "+":
                print("Impossible to Add 3*3 to 2*1") 
            elif opt == "-":
                print("Impossible to Subtract 3*3 from 2*1") 
            else:
                print("wrong input")  
        elif second_matrix == "1*2" :
            b11 = int(input("\nEnter b11 : "))
            print("\nYour Second Matrix is:" , "[",b11,b12,"]" , "\n")     
            opt = input("Choose The Operation You Want: ( * , +  , - ) : ")  
            if opt == "*":
                print("Impossible to multiplicate 3*3 with 2*2") 
            elif opt == "+":
                print("Impossible to Add 3*3 to 2*2") 
            elif opt == "-":
                print("Impossible to Subtract 3*3 from 2*2") 
            else:
                print("wrong input")  
        elif second_matrix == "3*2" :
            b11 = int(input("\nEnter b11 : "))
            b12 = int(input("Enter b12 : "))
            b21 = int(input("Enter b21 : "))
            b22 = int(input("Enter b22 : "))
            b31 = int(input("Enter b31 : "))
            b32 = int(input("Enter b32 : "))
            print("\nYour Second Matrix is:" , "[",b11,b12,"]")
            print("                      " , "[",b21,b22,"]")
            print("                      " , "[",b31,b32,"]" , "\n") 
            opt = input("Choose The Operation You Want: ( * , +  , - ) : ")  
            if opt == "*":
             print("\nYour Result is: " ,"[",(a11*b11) + (a12*b21) + (a13*b31) , (a11*b12) + (a12*b22) + (a13*b32) ,"]")    
             print("                " ,"[",(a21*b11) + (a22*b21) + (a23*b31) , (a21*b12) + (a22*b22) + (a23*b32) ,"]")
             print("                " ,"[",(a31*b11) + (a32*b21) + (a33*b31) , (a31*b12) + (a32*b22) + (a33*b32) ,"]")
            elif opt == "+":
                print("Impossible to Add 3*3 to 3*2") 
            elif opt == "-":
                print("Impossible to Subtract 3*3 from 3*2") 
            else:
                print("wrong input")  
        elif second_matrix == "3*1" :
            b11 = int(input("\nEnter b11 : "))
            b21 = int(input("Enter b21 : "))
            b31 = int(input("Enter b31 : "))
            print("\nYour Second Matrix is:" , "[",b11,"]")
            print("                      " , "[",b21,"]")
            print("                      " , "[",b31,"]" , "\n") 
            opt = input("Choose The Operation You Want: ( * , +  , - ) : ")  
            if opt == "*":
             print("\nYour Result is: " ,"[",(a11*b11) + (a12*b21) + (a13*b31) ,"]")    
             print("                " ,"[",(a21*b11) + (a22*b21) + (a23*b31) ,"]")
             print("                " ,"[",(a31*b11) + (a32*b21) + (a33*b31) ,"]")
            elif opt == "+":
                print("Impossible to Add 3*3 to 3*1") 
            elif opt == "-":
                print("Impossible to Subtract 3*3 from 3*1") 
            else:
                print("wrong input")   
    elif first_matrix == "3*2" :
        a11 = int(input("\nEnter a11 : "))
        a12 = int(input("Enter a12 : "))
        a21 = int(input("Enter a21 : "))
        a22 = int(input("Enter a22 : "))
        a31 = int(input("Enter a31 : "))
        a32 = int(input("Enter a32 : "))
        print("\nYour First Matrix is:  "  "[",a11,a12,"]")
        print("                      " , "[",a21,a22,"]")
        print("                      " , "[",a31,a32,"]" , "\n")
        second_matrix = input("Choose The Kind of The Second Matrix you want - (3*3 , 2*3 , 1*3 , 3*2 , 3*1 , 2*2 , 1*2 , 2*1 ): ")
        if second_matrix == "2*3" :
         b11 = int(input("\nEnter b11 : "))
         b12 = int(input("Enter b12 : "))
         b13 = int(input("Enter b13 : "))
         b21 = int(input("Enter b21 : "))
         b22 = int(input("Enter b22 : "))
         b23 = int(input("Enter b23 : "))
         print("\nYour Second Matrix is:" , "[",b11,b12,b13,"]")
         print("                      " , "[",b21,b22,b23,"]" , "\n")
         opt = input("Choose The Operation You Want: ( * , +  , - ) : ")  
         if opt == "*" :
            print("\nYour Result is: " ,"[",(a11*b11) + (a12*b21) , (a11*b12) + (a12*b22) , (a11*b13) + (a12*b23) ,"]")    
            print("                " ,"[",(a21*b11) + (a22*b21) , (a21*b12) + (a22*b22) , (a21*b13) + (a22*b23) ,"]")
            print("                " ,"[",(a31*b11) + (a32*b21) , (a31*b12) + (a32*b22) , (a31*b13) + (a32*b23) ,"]")
         elif opt == "+":
                print("Impossible to Add 3*2 to 2*3") 
         elif opt == "-":
                print("Impossible to Subtract 3*2 from 2*3")   
         else:
                print("wrong input")  
        elif second_matrix == "3*3" :
            b11 = int(input("\nEnter b11 : "))
            b12 = int(input("Enter b12 : "))
            b13 = int(input("Enter b13 : "))
            b21 = int(input("Enter b21 : "))
            b22 = int(input("Enter b22 : "))
            b23 = int(input("Enter b23 : "))
            b31 = int(input("Enter b31 : "))
            b32 = int(input("Enter b32 : "))
            b33 = int(input("Enter b33 : "))
            print("\nYour Second Matrix is:" , "[",b11,b12,b13,"]")
            print("                      " , "[",b21,b22,b23,"]")
            print("                      " , "[",b31,b32,b33,"]" , "\n") 
            opt = input("Choose The Operation You Want: ( * , +  , - ) : ")  
            if opt == "*":
                print("Impossible to multiplicate 3*2 with 3*3") 
            elif opt == "+":
                print("Impossible to Add 3*2 to 3*3") 
            elif opt == "-":
                print("Impossible to Subtract 3*2 from 3*3") 
            else:
                print("wrong input")        
        elif second_matrix == "1*3" :
            b11 = int(input("\nEnter b11 : "))
            b12 = int(input("Enter b12 : "))
            b13 = int(input("Enter b13 : "))
            print("\nYour Second Matrix is:" , "[",b11,b12,b13,"]" , "\n")    
            opt = input("Choose The Operation You Want: ( * , +  , - ) : ")  
            if opt == "*":
                print("Impossible to multiplicate 3*3 with 3*1") 
            elif opt == "+":
                print("Impossible to Add 3*3 to 3*1") 
            elif opt == "-":
                print("Impossible to Subtract 3*3 from 3*1") 
            else:
                print("wrong input")           
        elif second_matrix == "2*2" :
            b11 = int(input("\nEnter b11 : "))
            b12 = int(input("Enter b12 : "))
            b21 = int(input("Enter b21 : "))
            b22 = int(input("Enter b22 : "))
            print("\nYour Second Matrix is:" , "[",b11,b12,"]")
            print("                      " , "[",b21,b22,"]" , "\n")
            opt = input("Choose The Operation You Want: ( * , +  , - ) : ")  
            if opt == "*":
             print("\nYour Result is: " ,"[",(a11*b11) + (a12*b21) , (a11*b12) + (a12*b22) ,"]")    
             print("                " ,"[",(a21*b11) + (a22*b21) , (a21*b12) + (a22*b22) ,"]")
             print("                " ,"[",(a31*b11) + (a32*b21) , (a31*b12) + (a32*b22) ,"]")
            elif opt == "+":
                print("Impossible to Add 3*2 to 2*2") 
            elif opt == "-":
                print("Impossible to Subtract 3*2 from 2*2") 
            else:
                print("wrong input") 
        elif second_matrix == "2*1" :
            b11 = int(input("\nEnter b11 : "))
            b21 = int(input("Enter b21 : "))
            print("\nYour Second Matrix is:" , "[",b11,"]")
            print("                      " , "[",b21,"]" , "\n")
            opt = input("Choose The Operation You Want: ( * , +  , - ) : ")  
            if opt == "*":
             print("\nYour Result is: " ,"[",(a11*b11) + (a12*b21) ,"]")    
             print("                " ,"[",(a21*b11) + (a22*b21) ,"]")
             print("                " ,"[",(a31*b11) + (a32*b21) ,"]")
            elif opt == "+":
                print("Impossible to Add 3*2 to 2*1") 
            elif opt == "-":
                print("Impossible to Subtract 3*2 from 2*1") 
            else:
                print("wrong input")  
        elif second_matrix == "1*2" :
            b11 = int(input("\nEnter b11 : "))
            b12 = int(input("Enter b12 : "))
            print("\nYour Second Matrix is:" , "[",b11,b12,"]" , "\n")
            opt = input("Choose The Operation You Want: ( * , +  , - ) : ")  
            if opt == "*":
                print("Impossible to multiplicate 3*2 with 1*2") 
            elif opt == "+":
                print("Impossible to Add 3*2 to 1*2") 
            elif opt == "-":
                print("Impossible to Subtract 3*2 from 1*2") 
            else:
                print("wrong input")  
        elif second_matrix == "3*2" :
            b11 = int(input("\nEnter b11 : "))
            b12 = int(input("Enter b12 : "))
            b21 = int(input("Enter b21 : "))
            b22 = int(input("Enter b22 : "))
            b31 = int(input("Enter b31 : "))
            b32 = int(input("Enter b32 : "))
            print("\nYour Second Matrix is:" , "[",b11,b12,"]")
            print("                      " , "[",b21,b22,"]")
            print("                      " , "[",b31,b32,"]" , "\n") 
            opt = input("Choose The Operation You Want: ( * , +  , - ) : ")  
            if opt == "*":
             print("Impossible to multiplicate 3*2 with 3*2") 
            elif opt == "+":
             print("\nYour Result is: " , "[" , (a11+b11) , (a12+b12) ,"]")   
             print("                  " , "[" , (a21+b21) , (a22+b22) ,"]") 
             print("                  " , "[" , (a31+b31) , (a32+b32) ,"]")  
            elif opt == "-":
             print("\nYour Result is: " , "[" , (a11-b11) , (a12-b12) ,"]")   
             print("                  " , "[" , (a21-b21) , (a22-b22) ,"]") 
             print("                  " , "[" , (a31-b31) , (a32-b32) ,"]")   
            else:
                print("wrong input")  
        elif second_matrix == "3*1" :
            b11 = int(input("\nEnter b11 : "))
            b21 = int(input("Enter b21 : "))
            b31 = int(input("Enter b31 : "))
            print("\nYour Second Matrix is:" , "[",b11,"]")
            print("                      " , "[",b21,"]")
            print("                      " , "[",b31,"]" , "\n") 
            opt = input("Choose The Operation You Want: ( * , +  , - ) : ")  
            if opt == "*":
                print("Impossible to multiplicate 3*2 with 3*1") 
            elif opt == "+":
                print("Impossible to Add 3*2 to 3*1") 
            elif opt == "-":
                print("Impossible to Subtract 3*2 from 3*1") 
            else:
                print("wrong input")    
    elif first_matrix == "2*3" :
        a11 = int(input("\nEnter a11 : "))
        a12 = int(input("Enter a12 : "))
        a13 = int(input("Enter a13 : "))
        a21 = int(input("Enter a21 : "))
        a22 = int(input("Enter a22 : "))
        a23 = int(input("Enter a23 : "))
        print("\nYour First Matrix is:  "  "[",a11,a12,a13,"]")
        print("                      " , "[",a21,a22,a23,"]" , "\n")
        second_matrix = input("Choose The Kind of The Second Matrix you want - (3*3 , 2*3 , 1*3 , 3*2 , 3*1 , 2*2 , 1*2 , 2*1 ): ")
        if second_matrix == "3*3" :
            b11 = int(input("\nEnter b11 : "))
            b12 = int(input("Enter b12 : "))
            b13 = int(input("Enter b13 : "))
            b21 = int(input("Enter b21 : "))
            b22 = int(input("Enter b22 : "))
            b23 = int(input("Enter b23 : "))
            b31 = int(input("Enter b31 : "))
            b32 = int(input("Enter b32 : "))
            b33 = int(input("Enter b33 : "))
            print("\nYour Second Matrix is:" , "[",b11,b12,b13,"]")
            print("                      " , "[",b21,b22,b23,"]")
            print("                      " , "[",b31,b32,b33,"]" , "\n") 
            opt = input("Choose The Operation You Want: ( * , +  , - ) : ")  
            if opt == "*":
             print("\nYour Result is: " ,"[",(a11*b11) + (a12*b21) + (a13*b31) , (a11*b12) + (a12*b22) + (a13*b32) , (a11*b13) + (a12*b23) + (a13*b33),"]")    
             print("                " ,"[",(a21*b11) + (a22*b21) + (a23*b31) , (a21*b12) + (a22*b22) + (a23*b32) , (a21*b13) + (a22*b23) + (a23*b33),"]")
            elif opt == "+":
                print("Impossible to Add 2*3 to 3*3") 
            elif opt == "-":
                print("Impossible to Subtract 2*3 from 3*3") 
            else:
                print("wrong input") 
        elif second_matrix == "2*3" :
            b11 = int(input("\nEnter b11 : "))
            b12 = int(input("Enter b12 : "))
            b13 = int(input("Enter b13 : "))
            b21 = int(input("Enter b21 : "))
            b22 = int(input("Enter b22 : "))
            b23 = int(input("Enter b23 : "))
            print("\nYour Second Matrix is:" , "[",b11,b12,b13,"]")
            print("                      " , "[",b21,b22,b23,"]" , "\n")
            opt = input("Choose The Operation You Want: ( * , +  , - ) : ")  
            if opt == "*":
                print("Impossible to multiplicate 2*3 with 2*3") 
            elif opt == "+":
             print("\nYour Result is: " , "[" , (a11+b11) , (a12+b12) , (a13+b13) , "]")   
             print("                  " , "[" , (a21+b21) , (a22+b22) , (a23+b23) , "]") 
            elif opt == "-":
             print("\nYour Result is: " , "[" , (a11-b11) , (a12-b12) , (a13-b13) , "]")   
             print("                  " , "[" , (a21-b21) , (a22-b22) , (a23-b23) , "]") 
            else:
                print("wrong input") 
        elif second_matrix == "1*3" :
            b11 = int(input("\nEnter b11 : "))
            b12 = int(input("Enter b12 : "))
            b13 = int(input("Enter b13 : "))
            print("\nYour Second Matrix is:" , "[",b11,b12,b13,"]" , "\n")    
            opt = input("Choose The Operation You Want: ( * , +  , - ) : ")  
            if opt == "*":
                print("Impossible to multiplicate 2*3 with 1*3") 
            elif opt == "+":
                print("Impossible to Add 2*3 to 1*3") 
            elif opt == "-":
                print("Impossible to Subtract 2*3 from 1*3") 
            else:
                print("wrong input") 
        elif second_matrix == "3*2" :
            b11 = int(input("\nEnter b11 : "))
            b12 = int(input("Enter b12 : "))
            b21 = int(input("Enter b21 : "))
            b22 = int(input("Enter b22 : "))
            b31 = int(input("Enter b31 : "))
            b32 = int(input("Enter b32 : "))
            print("\nYour Second Matrix is:" , "[",b11,b12,"]")
            print("                      " , "[",b21,b22,"]")
            print("                      " , "[",b31,b32,"]" , "\n") 
            opt = input("Choose The Operation You Want: ( * , +  , - ) : ")  
            if opt == "*":
             print("\nYour Result is: " ,"[",(a11*b11) + (a12*b21) + (a13*b31) , (a11*b12) + (a12*b22) + (a13*b32) ,"]")    
             print("                " ,"[",(a21*b11) + (a22*b21) + (a23*b31) , (a21*b12) + (a22*b22) + (a23*b32) ,"]" , "\n") 
            elif opt == "+":
             print("Impossible to Add 2*3 to 3*2")
            elif opt == "-":
             print("Impossible to Subtract 2*3 from 3*2") 
            else: 
                print("wrong input")    
        elif second_matrix == "3*1" :
            b11 = int(input("\nEnter b11 : "))
            b21 = int(input("Enter b21 : "))
            b31 = int(input("Enter b31 : "))
            print("\nYour Second Matrix is:" , "[",b11,b12,"]")
            print("                      " , "[",b21,b22,"]")
            print("                      " , "[",b31,b32,"]" , "\n") 
            opt = input("Choose The Operation You Want: ( * , +  , - ) : ")  
            if opt == "*":
             print("\nYour Result is: " ,"[",(a11*b11) + (a12*b21) + (a13*b31) ,"]")    
             print("                " ,"[",(a21*b11) + (a22*b21) + (a23*b31) ,"]" , "\n") 
            elif opt == "+":
             print("Impossible to Add 2*3 to 3*1")
            elif opt == "-":
             print("Impossible to Subtract 2*3 from 3*1") 
            else: 
                print("wrong input")  
        elif second_matrix == "2*2" :
            b11 = int(input("\nEnter b11 : "))
            b12 = int(input("Enter b12 : "))
            b21 = int(input("Enter b21 : "))
            b22 = int(input("Enter b22 : "))
            print("\nYour Second Matrix is:" , "[",b11,b12,"]" , "\n")   
            print("                        " , "[",b21,b22,"]" , "\n")  
            opt = input("Choose The Operation You Want: ( * , +  , - ) : ")  
            if opt == "*":
                print("Impossible to multiplicate 2*3 with 2*2") 
            elif opt == "+":
                print("Impossible to Add 2*3 to 2*2") 
            elif opt == "-":
                print("Impossible to Subtract 2*3 from 2*2") 
            else:
                print("wrong input") 
        elif second_matrix == "1*2" :
            b11 = int(input("\nEnter b11 : "))
            b12 = int(input("Enter b12 : "))
            print("\nYour Second Matrix is:" , "[",b11,b12,"]" , "\n")   
            opt = input("Choose The Operation You Want: ( * , +  , - ) : ")  
            if opt == "*":
                print("Impossible to multiplicate 2*3 with 1*2") 
            elif opt == "+":
                print("Impossible to Add 2*3 to 1*2") 
            elif opt == "-":
                print("Impossible to Subtract 2*3 from 1*2") 
            else:
                print("wrong input") 
        elif second_matrix == "2*1" :
            b11 = int(input("\nEnter b11 : "))
            b21 = int(input("Enter b21 : "))
            print("\nYour Second Matrix is:" , "[",b11,"]" , "\n")   
            print("                        " , "[",b21,"]" , "\n")  
            opt = input("Choose The Operation You Want: ( * , +  , - ) : ")  
            if opt == "*":
                print("Impossible to multiplicate 2*3 with 1*3") 
            elif opt == "+":
                print("Impossible to Add 2*3 to 1*3") 
            elif opt == "-":
                print("Impossible to Subtract 2*3 from 1*3") 
            else:
                print("wrong input") 
        else:
            print("Wrong input")
    elif first_matrix == "1*3" :
        a11 = int(input("\nEnter a11 : "))
        a12 = int(input("Enter a12 : "))
        a13 = int(input("Enter a13 : "))
        print("\nYour First Matrix is:  "  "[",a11,a12,a13,"]" , "\n")
        second_matrix = input("Choose The Kind of The Second Matrix you want - (3*3 , 2*3 , 1*3 , 3*2 , 3*1 , 2*2 , 1*2 , 2*1) : ")
        if second_matrix == "3*3" :
            b11 = int(input("\nEnter b11 : "))
            b12 = int(input("Enter b12 : "))
            b13 = int(input("Enter b13 : "))
            b21 = int(input("Enter b21 : "))
            b22 = int(input("Enter b22 : "))
            b23 = int(input("Enter b23 : "))
            b31 = int(input("Enter b31 : "))
            b32 = int(input("Enter b32 : "))
            b33 = int(input("Enter b33 : "))
            print("\nYour Second Matrix is:" , "[",b11,b12,b13,"]")
            print("                      " , "[",b21,b22,b23,"]")
            print("                      " , "[",b31,b32,b33,"]" , "\n") 
            opt = input("Choose The Operation You Want: ( * , +  , - ) : ")  
            if opt == "*":
             print("\nYour Result is: " ,"[",(a11*b11) + (a12*b21) + (a13*b31) , (a11*b12) + (a12*b22) + (a13*b32) , (a11*b13) + (a12*b23) + (a13*b33),"]" , "\n")    
            elif opt == "+":
                print("Impossible to Add 1*3 to 3*3") 
            elif opt == "-":
                print("Impossible to Subtract 1*3 from 3*3") 
            else:
                print("wrong input")   
        elif second_matrix == "2*3" :
            b11 = int(input("\nEnter b11 : "))
            b12 = int(input("Enter b12 : "))
            b13 = int(input("Enter b13 : "))
            b21 = int(input("Enter b21 : "))
            b22 = int(input("Enter b22 : "))
            b23 = int(input("Enter b23 : "))
            print("\nYour Second Matrix is:" , "[",b11,b12,b13,"]")
            print("                      " , "[",b21,b22,b23,"]" , "\n")
            opt = input("Choose The Operation You Want: ( * , +  , - ) : ")  
            if opt == "*":
                print("Impossible to multiplicate 1*3 with 2*3") 
            elif opt == "+":
                print("Impossible to Add 1*3 to 2*3")
            elif opt == "-":
                print("Impossible to Subtract 1*3 from 2*3") 
            else:
                print("wrong input") 
        elif second_matrix == "1*3" :
            b11 = int(input("\nEnter b11 : "))
            b12 = int(input("Enter b12 : "))
            b13 = int(input("Enter b13 : "))
            print("\nYour Second Matrix is:" , "[",b11,b12,b13,"]")
            opt = input("Choose The Operation You Want: ( * , +  , - ) : ")  
            if opt == "*":
                print("Impossible to multiplicate 1*3 with 2*3") 
            elif opt == "+":
             print("\nYour Result is: " , "[" , (a11+b11) , (a12+b12) , (a13+b13) , "]")   
            elif opt == "-":
             print("\nYour Result is: " , "[" , (a11-b11) , (a12-b12) , (a13-b13) , "]")   
            else:
                print("wrong input") 
        elif second_matrix == "3*2" :
            b11 = int(input("\nEnter b11 : "))
            b12 = int(input("Enter b12 : "))
            b21 = int(input("Enter b21 : "))
            b22 = int(input("Enter b22 : "))
            b31 = int(input("Enter b31 : "))
            b32 = int(input("Enter b32 : "))
            print("\nYour Second Matrix is:" , "[",b11,b12,"]")
            print("                      " , "[",b21,b22,"]")
            print("                      " , "[",b31,b32,"]" , "\n") 
            opt = input("Choose The Operation You Want: ( * , +  , - ) : ")  
            if opt == "*":
             print("\nYour Result is: " ,"[",(a11*b11) + (a12*b21) + (a13*b31) , (a11*b12) + (a12*b22) + (a13*b32) ,"]" , "\n")     
            elif opt == "+":
             print("Impossible to Add 1*3 to 3*2")
            elif opt == "-":
             print("Impossible to Subtract 1*3 from 3*2") 
            else: 
                print("wrong input")       
        elif second_matrix == "3*1" :
            b11 = int(input("\nEnter b11 : "))
            b21 = int(input("Enter b21 : "))
            b31 = int(input("Enter b31 : "))
            print("\nYour Second Matrix is:" , "[",b11,b12,"]")
            print("                      " , "[",b21,b22,"]")
            print("                      " , "[",b31,b32,"]" , "\n") 
            opt = input("Choose The Operation You Want: ( * , +  , - ) : ")  
            if opt == "*":
             print("\nYour Result is: " ,"[",(a11*b11) + (a12*b21) + (a13*b31) ,"]" , "\n")     
            elif opt == "+":
             print("Impossible to Add 1*3 to 3*1")
            elif opt == "-":
             print("Impossible to Subtract 1*3 from 3*1") 
            else: 
                print("wrong input")   
        elif second_matrix == "2*2" :
            b11 = int(input("\nEnter b11 : "))
            b12 = int(input("Enter b12 : "))
            b21 = int(input("Enter b21 : "))
            b22 = int(input("Enter b22 : "))
            print("\nYour Second Matrix is:" , "[",b11,b12,"]" , "\n")   
            print("                        " , "[",b21,b22,"]" , "\n")  
            opt = input("Choose The Operation You Want: ( * , +  , - ) : ")  
            if opt == "*":
                print("Impossible to multiplicate 1*3 with 2*2") 
            elif opt == "+":
                print("Impossible to Add 1*3 to 2*2") 
            elif opt == "-":
                print("Impossible to Subtract 1*3 from 2*2") 
            else:
                print("wrong input") 
        elif second_matrix == "1*2" :
            b11 = int(input("\nEnter b11 : "))
            b12 = int(input("Enter b12 : "))
            print("\nYour Second Matrix is:" , "[",b11,b12,"]" , "\n")   
            opt = input("Choose The Operation You Want: ( * , +  , - ) : ")  
            if opt == "*":
                print("Impossible to multiplicate 1*3 with 1*2") 
            elif opt == "+":
                print("Impossible to Add 1*3 to 1*2") 
            elif opt == "-":
                print("Impossible to Subtract 1*3 from 1*2") 
            else:
                print("wrong input") 
        elif second_matrix == "2*1" :
            b11 = int(input("\nEnter b11 : "))
            b21 = int(input("Enter b21 : "))
            print("\nYour Second Matrix is:" , "[",b11,"]" , "\n")   
            print("                        " , "[",b21,"]" , "\n")  
            opt = input("Choose The Operation You Want: ( * , +  , - ) : ")  
            if opt == "*":
                print("Impossible to multiplicate 1*3 with 1*3") 
            elif opt == "+":
                print("Impossible to Add 1*3 to 1*3") 
            elif opt == "-":
                print("Impossible to Subtract 1*3 from 1*3") 
            else:
                print("wrong input") 
        else:
            print("Wrong input")                              
    elif first_matrix == "3*1" :
        a11 = int(input("\nEnter a11 : "))
        a21 = int(input("Enter a21 : "))
        a31 = int(input("Enter a31 : "))
        print("\nYour First Matrix is:  "  "[",a11,"]")
        print("                      " , "[",a21,"]")
        print("                      " , "[",a31,"]" , "\n")
        second_matrix = input("Choose The Kind of The Second Matrix you want - (3*3 , 2*3 , 1*3 , 3*2 , 3*1 , 2*2 , 1*2 , 2*1) : ")  
        if second_matrix == "3*3" :
            b11 = int(input("\nEnter b11 : "))
            b12 = int(input("Enter b12 : "))
            b13 = int(input("Enter b13 : "))
            b21 = int(input("Enter b21 : "))
            b22 = int(input("Enter b22 : "))
            b23 = int(input("Enter b23 : "))
            b31 = int(input("Enter b31 : "))
            b32 = int(input("Enter b32 : "))
            b33 = int(input("Enter b33 : "))
            print("\nYour Second Matrix is:" , "[",b11,b12,b13,"]")
            print("                      " , "[",b21,b22,b23,"]")
            print("                      " , "[",b31,b32,b33,"]" , "\n") 
            opt = input("Choose The Operation You Want: ( * , +  , - ) : ")
            if opt == "*":
                print("Impossible to multiplicate 3*1 with 3*3") 
            elif opt == "+":
                print("Impossible to Add 3*1 to 3*3")
            elif opt == "-":
                print("Impossible to Subtract 3*1 from 3*3") 
            else:
                print("wrong input") 
        elif second_matrix == "2*3" :
            b11 = int(input("\nEnter b11 : "))
            b12 = int(input("Enter b12 : "))
            b13 = int(input("Enter b13 : "))
            b21 = int(input("Enter b21 : "))
            b22 = int(input("Enter b22 : "))
            b23 = int(input("Enter b23 : "))
            print("\nYour Second Matrix is:" , "[",b11,b12,b13,"]")
            print("                      " , "[",b21,b22,b23,"]" , "\n")
            opt = input("Choose The Operation You Want: ( * , +  , - ) : ")
            if opt == "*":
                print("Impossible to multiplicate 3*1 with 2*3") 
            elif opt == "+":
                print("Impossible to Add 3*1 to 2*3")
            elif opt == "-":
                print("Impossible to Subtract 3*1 from 2*3") 
            else:
                print("wrong input") 
        if second_matrix == "1*3" :
            b11 = int(input("\nEnter b11 : "))
            b12 = int(input("Enter b12 : "))
            b13 = int(input("Enter b13 : "))
            print("\nYour Second Matrix is:" , "[",b11,b12,b13,"]" , "\n")
            opt = input("Choose The Operation You Want: ( * , +  , - ) : ")  
            if opt == "*":
             print("\nYour Result is: " ,"[",(a11*b11) , (a11*b12)  , (a11*b13) ,"]")    
             print("                " ,"[",(a21*b11) , (a21*b12) , (a21*b13) ,"]")
             print("                " ,"[",(a31*b11) , (a31*b12) , (a31*b13) ,"]")
            elif opt == "+":
                print("Impossible to Add 3*1 to 1*3") 
            elif opt == "-":
                print("Impossible to Subtract 3*1 from 1*3") 
            else:
                print("wrong input") 
        elif second_matrix == "3*2" :
            b11 = int(input("\nEnter b11 : "))
            b12 = int(input("Enter b12 : "))
            b21 = int(input("Enter b21 : "))
            b22 = int(input("Enter b22 : "))
            b31 = int(input("Enter b31 : "))
            b32 = int(input("Enter b32 : "))        
            print("\nYour Second Matrix is:" , "[",b11,b12,"]")
            print("                      " , "[",b21,b22,"]")
            print("                      " , "[",b31,b32,"]" , "\n")        
            opt = input("Choose The Operation You Want: ( * , +  , - ) : ")
            if opt == "*":
                print("Impossible to multiplicate 3*1 with 3*2") 
            elif opt == "+":
                print("Impossible to Add 3*1 to 3*2")
            elif opt == "-":
                print("Impossible to Subtract 3*1 from 3*2") 
            else:
                print("wrong input")  
        elif second_matrix == "3*1" :
            b11 = int(input("\nEnter b11 : "))
            b21 = int(input("Enter b21 : "))
            b31 = int(input("Enter b31 : "))
            print("\nYour Second Matrix is:" , "[",b11,"]")
            print("                        " , "[",b21,"]")
            print("                        " , "[",b31,"]")
            opt = input("Choose The Operation You Want: ( * , +  , - ) : ")  
            if opt == "*":
                print("Impossible to multiplicate 3*1 with 3*1") 
            elif opt == "+":
             print("\nYour Result is: " , "[" , (a11+b11) , "]") 
             print("                  " , "[" , (a21+b21) , "]")
             print("                  " , "[" , (a31+b31) , "]")  
            elif opt == "-":
             print("\nYour Result is: " , "[" , (a11-b11) , "]") 
             print("                  " , "[" , (a21-b21) , "]")
             print("                  " , "[" , (a31-b31) , "]")  
            else:
                print("wrong input") 
        elif second_matrix == "2*2" :
            b11 = int(input("\nEnter b11 : "))
            b12 = int(input("Enter b12 : "))
            b21 = int(input("Enter b21 : "))
            b22 = int(input("Enter b22 : "))
            print("\nYour Second Matrix is:" , "[",b11,b12,"]" , "\n")   
            print("                        " , "[",b21,b22,"]" , "\n")  
            opt = input("Choose The Operation You Want: ( * , +  , - ) : ")  
            if opt == "*":
                print("Impossible to multiplicate 3*1 with 2*2") 
            elif opt == "+":
                print("Impossible to Add 3*1 to 2*2") 
            elif opt == "-":
                print("Impossible to Subtract 3*1 from 2*2") 
            else:
                print("wrong input") 
        elif second_matrix == "1*2" :
            b11 = int(input("\nEnter b11 : "))
            b12 = int(input("Enter b12 : "))
            print("\nYour Second Matrix is:" , "[",b11,b12,"]" , "\n")   
            opt = input("Choose The Operation You Want: ( * , +  , - ) : ")  
            if opt == "*":
             print("\nYour Result is: " ,"[",(a11*b11) , (a11*b12) ,"]")    
             print("                " ,"[",(a21*b11) , (a21*b12) ,"]")
             print("                " ,"[",(a31*b11) , (a31*b12) ,"]") 
            elif opt == "+":
                print("Impossible to Add 3*1 to 1*2") 
            elif opt == "-":
                print("Impossible to Subtract 3*1 from 1*2") 
            else:
                print("wrong input") 
        elif second_matrix == "2*1" :
            b11 = int(input("\nEnter b11 : "))
            b21 = int(input("Enter b21 : "))
            print("\nYour Second Matrix is:" , "[",b11,"]" , "\n")   
            print("                        " , "[",b21,"]" , "\n")  
            opt = input("Choose The Operation You Want: ( * , +  , - ) : ")  
            if opt == "*":
                print("Impossible to multiplicate 3*1 with 2*1") 
            elif opt == "+":
                print("Impossible to Add 3*1 to 2*1") 
            elif opt == "-":
                print("Impossible to Subtract 3*1 from 2*1") 
            else:
                print("wrong input") 
        else:
            print("Wrong input")  
    elif first_matrix == "2*2" :
        a11 = int(input("\nEnter a11 : "))
        a12 = int(input("Enter a12 : "))    
        a21 = int(input("Enter a21 : "))
        a22 = int(input("Enter a22 : "))
        print("\nYour First Matrix is:  "  "[",a11,a12,"]")
        print("                      " , "[",a21,a22,"]" , "\n")
        second_matrix = input("Choose The Kind of The Second Matrix you want - (3*3 , 2*3 , 1*3 , 3*2 , 3*1 , 2*2 , 1*2 , 2*1) : ") 
        if second_matrix == "3*3" :
            b11 = int(input("\nEnter b11 : "))
            b12 = int(input("Enter b12 : "))
            b13 = int(input("Enter b13 : "))
            b21 = int(input("Enter b21 : "))
            b22 = int(input("Enter b22 : "))
            b23 = int(input("Enter b23 : "))
            b31 = int(input("Enter b31 : "))
            b32 = int(input("Enter b32 : "))
            b33 = int(input("Enter b33 : "))
            print("\nYour Second Matrix is:" , "[",b11,b12,b13,"]")
            print("                      " , "[",b21,b22,b23,"]")
            print("                      " , "[",b31,b32,b33,"]" , "\n") 
            opt = input("Choose The Operation You Want: ( * , +  , - ) : ")
            if opt == "*":
                print("Impossible to multiplicate 2*2 with 3*3") 
            elif opt == "+":
                print("Impossible to Add 2*2 to 3*3")
            elif opt == "-":
                print("Impossible to Subtract 2*2 from 3*3") 
            else:
                print("wrong input")
        elif second_matrix == "2*3" :
            b11 = int(input("\nEnter b11 : "))
            b12 = int(input("Enter b12 : "))
            b13 = int(input("Enter b13 : "))
            b21 = int(input("Enter b21 : "))
            b22 = int(input("Enter b22 : "))
            b23 = int(input("Enter b23 : "))
            print("\nYour Second Matrix is:" , "[",b11,b12,b13,"]")
            print("                      " , "[",b21,b22,b23,"]" , "\n")
            opt = input("Choose The Operation You Want: ( * , +  , - ) : ")
            if opt == "*":
             print("\nYour Result is: " ,"[",(a11*b11) + (a12*b21) , (a11*b12) + (a12*b22) , (a11*b13) + (a12*b23) ,"]")    
             print("                " ,"[",(a21*b11) + (a22*b21) , (a21*b12) + (a22*b22) , (a21*b13) + (a22*b23) ,"]")
            elif opt == "+":
                print("Impossible to Add 2*2 to 2*3")
            elif opt == "-":
                print("Impossible to Subtract 2*2 from 2*3") 
            else:
                print("wrong input") 
        elif second_matrix == "1*3" :
            b11 = int(input("\nEnter b11 : "))
            b12 = int(input("Enter b12 : "))
            b13 = int(input("Enter b13 : "))
            print("\nYour Second Matrix is:" , "[",b11,b12,b13,"]" , "\n")
            opt = input("Choose The Operation You Want: ( * , +  , - ) : ")
            if opt == "*":
                print("Impossible to multiplicate 2*2 with 1*3") 
            elif opt == "+":
                print("Impossible to Add 2*2 to 1*3")
            elif opt == "-":
                print("Impossible to Subtract 2*2 from 1*3") 
            else:
                print("wrong input")
        elif second_matrix == "3*2" :
            b11 = int(input("\nEnter b11 : "))
            b12 = int(input("Enter b12 : "))
            b21 = int(input("Enter b21 : "))
            b22 = int(input("Enter b22 : "))
            b31 = int(input("Enter b31 : "))
            b32 = int(input("Enter b32 : "))
            print("\nYour Second Matrix is:" , "[",b11,b12,"]")
            print("                      " , "[",b21,b22,"]")
            print("                      " , "[",b31,b32,"]" , "\n") 
            opt = input("Choose The Operation You Want: ( * , +  , - ) : ")
            if opt == "*":
                print("Impossible to multiplicate 2*2 with 3*2") 
            elif opt == "+":
                print("Impossible to Add 2*2 to 3*2")
            elif opt == "-":
                print("Impossible to Subtract 2*2 from 3*2") 
            else:
                print("wrong input")    
        elif second_matrix == "3*1" :
            b11 = int(input("\nEnter b11 : "))
            b21 = int(input("Enter b21 : "))
            b31 = int(input("Enter b31 : "))
            print("\nYour Second Matrix is:" , "[",b11,"]")
            print("                      " , "[",b21,"]")
            print("                      " , "[",b31,"]" , "\n") 
            opt = input("Choose The Operation You Want: ( * , +  , - ) : ")
            if opt == "*":
                print("Impossible to multiplicate 2*2 with 1*3") 
            elif opt == "+":
                print("Impossible to Add 2*2 to 1*3")
            elif opt == "-":
                print("Impossible to Subtract 2*2 from 1*3") 
            else:
                print("wrong input")
        elif second_matrix == "2*2" :
            b11 = int(input("\nEnter b11 : "))
            b12 = int(input("Enter b12 : "))
            b21 = int(input("Enter b21 : "))
            b22 = int(input("Enter b22 : "))
            print("\nYour Second Matrix is:" , "[",b11,b12,"]" , "\n")   
            print("                        " , "[",b21,b22,"]" , "\n")  
            opt = input("Choose The Operation You Want: ( * , +  , - ) : ")  
            if opt == "*":
             print("\nYour Result is: " ,"[",(a11*b11) + (a12*b21) , (a11*b12) + (a12*b22) ,"]")    
             print("                " ,"[",(a21*b11) + (a22*b21) , (a21*b12) + (a22*b22) ,"]")
            elif opt == "+":
             print("\nYour Result is: " ,"[",(a11+b11) , (a12+b12) ,"]")    
             print("                " ,"[",(a21+b21) , (a22+b22),"]")
            elif opt == "-":
             print("\nYour Result is: " ,"[",(a11-b11) , (a12-b12) ,"]")    
             print("                " ,"[",(a21-b21) , (a22-b22),"]") 
            else:
                print("wrong input")
        elif second_matrix == "1*2" :
            b11 = int(input("\nEnter b11 : "))
            b12 = int(input("Enter b12 : "))
            print("\nYour Second Matrix is:" , "[",b11,b12,"]" , "\n")    
            opt = input("Choose The Operation You Want: ( * , +  , - ) : ")  
            if opt == "*":
                print("Impossible to multiplicate 2*2 with 1*2") 
            elif opt == "+":
                print("Impossible to Add 2*2 to 1*2") 
            elif opt == "-":
                print("Impossible to Subtract 2*2 from 1*2") 
            else:
                print("wrong input") 
        elif second_matrix == "2*1" :
            b11 = int(input("\nEnter b11 : "))
            b21 = int(input("Enter b21 : "))
            print("\nYour Second Matrix is:" , "[",b11,"]" , "\n")   
            print("                        " , "[",b21,"]" , "\n")  
            opt = input("Choose The Operation You Want: ( * , +  , - ) : ")  
            if opt == "*":
             print("\nYour Result is: " ,"[",(a11*b11) + (a12*b21) ,"]")    
             print("                " ,"[",(a21*b11) + (a22*b21) ,"]")
            elif opt == "+":
                print("Impossible to Add 2*2 to 2*1") 
            elif opt == "-":
                print("Impossible to Subtract 2*2 from 2*1") 
            else:
                print("wrong input") 
    elif first_matrix == "1*2" :
        a11 = int(input("\nEnter a11 : "))
        a12 = int(input("Enter a12 : "))    
        print("\nYour First Matrix is:  "  "[",a11,a12,"]")
        second_matrix = input("Choose The Kind of The Second Matrix you want - (3*3 , 2*3 , 1*3 , 3*2 , 3*1 , 2*2 , 1*2 , 2*1) : ") 
        if second_matrix == "3*3" :
            b11 = int(input("\nEnter b11 : "))
            b12 = int(input("Enter b12 : "))
            b13 = int(input("Enter b13 : "))
            b21 = int(input("Enter b21 : "))
            b22 = int(input("Enter b22 : "))
            b23 = int(input("Enter b23 : "))
            b31 = int(input("Enter b31 : "))
            b32 = int(input("Enter b32 : "))
            b33 = int(input("Enter b33 : "))
            print("\nYour Second Matrix is:" , "[",b11,b12,b13,"]")
            print("                      " , "[",b21,b22,b23,"]")
            print("                      " , "[",b31,b32,b33,"]" , "\n") 
            opt = input("Choose The Operation You Want: ( * , +  , - ) : ")
            if opt == "*":
                print("Impossible to multiplicate 1*2 with 3*3") 
            elif opt == "+":
                print("Impossible to Add 1*2 to 3*3")
            elif opt == "-":
                print("Impossible to Subtract 1*2 from 3*3") 
            else:
                print("wrong input") 
        elif second_matrix == "2*3" :
            b11 = int(input("\nEnter b11 : "))
            b12 = int(input("Enter b12 : "))
            b13 = int(input("Enter b13 : "))
            b21 = int(input("Enter b21 : "))
            b22 = int(input("Enter b22 : "))
            b23 = int(input("Enter b23 : "))
            print("\nYour Second Matrix is:" , "[",b11,b12,b13,"]")
            print("                      " , "[",b21,b22,b23,"]" , "\n")
            opt = input("Choose The Operation You Want: ( * , +  , - ) : ")
            if opt == "*":
             print("\nYour Result is: " ,"[",(a11*b11) + (a12*b21) , (a11*b12) + (a12*b22) , (a11*b13) + (a12*b23) ,"]")
            elif opt == "+":
                print("Impossible to Add 1*2 to 2*3")
            elif opt == "-":
                print("Impossible to Subtract 1*2 from 2*3") 
            else:
                print("wrong input") 
        elif second_matrix == "1*3" :
            b11 = int(input("\nEnter b11 : "))
            b12 = int(input("Enter b12 : "))
            b13 = int(input("Enter b13 : "))
            print("\nYour Second Matrix is:" , "[",b11,b12,b13,"]" , "\n")
            opt = input("Choose The Operation You Want: ( * , +  , - ) : ")
            if opt == "*":
                print("Impossible to multiplicate 1*2 with 1*3") 
            elif opt == "+":
                print("Impossible to Add 1*2 to 1*3")
            elif opt == "-":
                print("Impossible to Subtract 1*2 from 1*3") 
            else:
                print("wrong input")
        elif second_matrix == "3*2" :
            b11 = int(input("\nEnter b11 : "))
            b12 = int(input("Enter b12 : "))
            b21 = int(input("Enter b21 : "))
            b22 = int(input("Enter b22 : "))
            b31 = int(input("Enter b31 : "))
            b32 = int(input("Enter b32 : "))
            print("\nYour Second Matrix is:" , "[",b11,b12,"]")
            print("                      " , "[",b21,b22,"]")
            print("                      " , "[",b31,b32,"]" , "\n") 
            opt = input("Choose The Operation You Want: ( * , +  , - ) : ")
            if opt == "*":
                print("Impossible to multiplicate 1*2 with 3*2") 
            elif opt == "+":
                print("Impossible to Add 1*2 to 3*2")
            elif opt == "-":
                print("Impossible to Subtract 1*2 from 3*2") 
            else:
                print("wrong input") 
        elif second_matrix == "3*1" :
            b11 = int(input("\nEnter b11 : "))
            b21 = int(input("Enter b21 : "))
            b31 = int(input("Enter b31 : "))
            print("\nYour Second Matrix is:" , "[",b11,"]")
            print("                      " , "[",b21,"]")
            print("                      " , "[",b31,"]" , "\n") 
            opt = input("Choose The Operation You Want: ( * , +  , - ) : ")
            if opt == "*":
                print("Impossible to multiplicate 1*2 with 3*1") 
            elif opt == "+":
                print("Impossible to Add 1*2 to 3*1")
            elif opt == "-":
                print("Impossible to Subtract 1*2 from 3*1") 
            else:
                print("wrong input") 
        elif second_matrix == "2*2" :
            b11 = int(input("\nEnter b11 : "))
            b12 = int(input("Enter b12 : "))
            b21 = int(input("Enter b21 : "))
            b22 = int(input("Enter b22 : "))
            print("\nYour Second Matrix is:" , "[",b11,b12,"]")
            print("                      " , "[",b21,b22,"]")
            opt = input("Choose The Operation You Want: ( * , +  , - ) : ")
            if opt == "*":
             print("\nYour Result is: " ,"[",(a11*b11) + (a12*b21) , (a11*b12) + (a12*b22) ,"]")    
            elif opt == "+":
                print("Impossible to Add 1*2 to 2*2")
            elif opt == "-":
                print("Impossible to Subtract 1*2 from 2*2") 
            else:
                print("wrong input") 
        elif second_matrix == "1*2" :
            b11 = int(input("\nEnter b11 : "))
            b12 = int(input("Enter b12 : "))
            print("\nYour Second Matrix is:" , "[",b11,b12,"]" , "\n")
            opt = input("Choose The Operation You Want: ( * , +  , - ) : ")
            if opt == "*":
                print("Impossible to multiplicate 1*2 with 1*2") 
            elif opt == "+":
             print("\nYour Result is: " ,"[",(a11+b11) , (a12+b12) ,"]")
            elif opt == "-":
             print("\nYour Result is: " ,"[",(a11-b11) , (a12-b12) ,"]")
            else:
                print("wrong input")
        elif second_matrix == "2*1" :
            b11 = int(input("\nEnter b11 : "))
            b21 = int(input("Enter b21 : "))
            print("\nYour Second Matrix is:" , "[",b11,"]")
            print("                      " , "[",b21,"]")
            opt = input("Choose The Operation You Want: ( * , +  , - ) : ")
            if opt == "*":
             print("\nYour Result is: " ,"[",(a11*b11) + (a12*b21) ,"]")    
            elif opt == "+":
                print("Impossible to Add 1*2 to 2*1")
            elif opt == "-":
                print("Impossible to Subtract 1*2 from 2*1") 
            else:
                print("wrong input") 
    elif first_matrix == "2*1" :
        a11 = int(input("\nEnter a11 : "))
        a21 = int(input("Enter a21 : "))    
        print("\nYour First Matrix is:  "  "[",a11,"]")
        print("                         "  "[",a21,"]")
        second_matrix = input("Choose The Kind of The Second Matrix you want - (3*3 , 2*3 , 1*3 , 3*2 , 3*1 , 2*2 , 1*2 , 2*1) : ") 
        if second_matrix == "3*3" :
            b11 = int(input("\nEnter b11 : "))
            b12 = int(input("Enter b12 : "))
            b13 = int(input("Enter b13 : "))
            b21 = int(input("Enter b21 : "))
            b22 = int(input("Enter b22 : "))
            b23 = int(input("Enter b23 : "))
            b31 = int(input("Enter b31 : "))
            b32 = int(input("Enter b32 : "))
            b33 = int(input("Enter b33 : "))
            print("\nYour Second Matrix is:" , "[",b11,b12,b13,"]")
            print("                      " , "[",b21,b22,b23,"]")
            print("                      " , "[",b31,b32,b33,"]" , "\n") 
            opt = input("Choose The Operation You Want: ( * , +  , - ) : ")
            if opt == "*":
                print("Impossible to multiplicate 2*1 with 3*3") 
            elif opt == "+":
                print("Impossible to Add 2*1 to 3*3")
            elif opt == "-":
                print("Impossible to Subtract 2*1 from 3*3") 
            else:
                print("wrong input") 
        elif second_matrix == "2*3" :
            b11 = int(input("\nEnter b11 : "))
            b12 = int(input("Enter b12 : "))
            b13 = int(input("Enter b13 : "))
            b21 = int(input("Enter b21 : "))
            b22 = int(input("Enter b22 : "))
            b23 = int(input("Enter b23 : "))
            print("\nYour Second Matrix is:" , "[",b11,b12,b13,"]")
            print("                      " , "[",b21,b22,b23,"]" , "\n")
            opt = input("Choose The Operation You Want: ( * , +  , - ) : ")
            if opt == "*":
                print("Impossible to multiplicate 2*1 with 2*3")
            elif opt == "+":
                print("Impossible to Add 2*1 to 2*3")
            elif opt == "-":
                print("Impossible to Subtract 2*1 from 2*3") 
            else:
                print("wrong input")
        elif second_matrix == "1*3" :
            b11 = int(input("\nEnter b11 : "))
            b12 = int(input("Enter b12 : "))
            b13 = int(input("Enter b13 : "))
            print("\nYour Second Matrix is:" , "[",b11,b12,b13,"]" , "\n")
            opt = input("Choose The Operation You Want: ( * , +  , - ) : ")
            if opt == "*":
             print("\nYour Result is: " ,"[",(a11*b11) , (a11*b12) , (a11*b13) ,"]")
             print("                  " ,"[",(a21*b11) , (a21*b12) , (a21*b13) ,"]")
            elif opt == "+":
                print("Impossible to Add 2*1 to 2*3")
            elif opt == "-":
                print("Impossible to Subtract 2*1 from 2*3") 
            else:
                print("wrong input")  
        elif second_matrix == "3*2" :
            b11 = int(input("\nEnter b11 : "))
            b12 = int(input("Enter b12 : "))
            b21 = int(input("Enter b21 : "))
            b22 = int(input("Enter b22 : "))
            b31 = int(input("Enter b31 : "))
            b32 = int(input("Enter b32 : " , "\n"))
            print("\nYour Second Matrix is:" , "[",b11,b12,"]")
            print("                      " , "[",b21,b22,"]")
            print("                      " , "[",b31,b32,"]" , "\n")
            opt = input("Choose The Operation You Want: ( * , +  , - ) : ")
            if opt == "*":
                print("Impossible to multiplicate 2*1 with 3*2")
            elif opt == "+":
                print("Impossible to Add 2*1 to 3*2")
            elif opt == "-":
                print("Impossible to Subtract 2*1 from 3*2") 
            else:
                print("wrong input")
        elif second_matrix == "3*1" :
            b11 = int(input("\nEnter b11 : "))
            b21 = int(input("Enter b21 : "))
            b31 = int(input("Enter b31 : "))
            print("\nYour Second Matrix is:" , "[",b11,"]")
            print("                      " , "[",b21,"]")
            print("                      " , "[",b31,"]" , "\n")
            opt = input("Choose The Operation You Want: ( * , +  , - ) : ")
            if opt == "*":
                print("Impossible to multiplicate 2*1 with 3*1")
            elif opt == "+":
                print("Impossible to Add 2*1 to 3*1")
            elif opt == "-":
                print("Impossible to Subtract 2*1 from 3*1") 
            else:
                print("wrong input")
        elif second_matrix == "2*2" :
            b11 = int(input("\nEnter b11 : "))
            b12 = int(input("Enter b12 : "))
            b21 = int(input("Enter b21 : "))
            b22 = int(input("Enter b22 : "))
            print("\nYour Second Matrix is:" , "[",b11,b12,"]")
            print("                      " , "[",b21,b22,"]" , "\n")
            opt = input("Choose The Operation You Want: ( * , +  , - ) : ")
            if opt == "*":
                print("Impossible to multiplicate 2*1 with 2*2")
            elif opt == "+":
                print("Impossible to Add 2*1 to 2*2")
            elif opt == "-":
                print("Impossible to Subtract 2*1 from 2*2") 
            else:
                print("wrong input")
        elif second_matrix == "1*2" :
            b11 = int(input("\nEnter b11 : "))
            b12 = int(input("Enter b12 : "))
            print("\nYour Second Matrix is:" , "[",b11,b12,"]" , "\n")
            opt = input("Choose The Operation You Want: ( * , +  , - ) : ")
            if opt == "*":
             print("\nYour Result is: " ,"[",(a11*b11) , (a11*b12) ,"]")
             print("                  " ,"[",(a21*b11) , (a21*b12) ,"]")
            elif opt == "+":
                print("Impossible to Add 2*1 to 1*2")
            elif opt == "-":
                print("Impossible to Subtract 2*1 from 1*2") 
            else:
                print("wrong input") 
        elif second_matrix == "2*1" :
            b11 = int(input("\nEnter b11 : "))
            b21 = int(input("Enter b21 : "))
            print("\nYour Second Matrix is:" , "[",b11,"]" )
            print("                        " , "[",b21,"]" , "\n")
            opt = input("Choose The Operation You Want: ( * , +  , - ) : ")
            if opt == "*":
                print("Impossible to multiplicate 2*1 with 2*1")
            elif opt == "+":
             print("\nYour Result is: " ,"[",(a11+b11) ,"]")
             print("                  " ,"[",(a21+b21) ,"]")
            elif opt == "-":
             print("\nYour Result is: " ,"[",(a11-b11) ,"]")
             print("                  " ,"[",(a21-b21) ,"]")
            else:
                print("wrong input") 
    else:
     print("wrong input")
 elif operation == "T"  :
     transpose_matrix = input("Type The Kind Of Matrix You Want to Get Its Transpose ('3*3 , 2*3 , 1*3 , 3*2 , 3*1 , 2*2 , 1*2 , 2*1 '): \n")
     if transpose_matrix == "3*3":
        a11 = int(input("\nEnter a11 : "))
        a12 = int(input("Enter a12 : "))
        a13 = int(input("Enter a13 : "))
        a21 = int(input("Enter a21 : "))
        a22 = int(input("Enter a22 : "))
        a23 = int(input("Enter a23 : "))
        a31 = int(input("Enter a31 : "))
        a32 = int(input("Enter a32 : "))
        a33 = int(input("Enter a33 : "))
        print("\nYour Matrix is:       " , "[",a11,a12,a13,"]")
        print("                      " , "[",a21,a22,a23,"]")
        print("                      " , "[",a31,a32,a33,"]" , "\n") 
        print("\nYour Matrix Transpose is:     " , "[",a11,a21,a31,"]")
        print("                              " , "[",a12,a22,a32,"]")
        print("                              " , "[",a13,a23,a33,"]" , "\n")   
     elif transpose_matrix == "2*3" :
        a11 = int(input("\nEnter a11 : "))
        a12 = int(input("Enter a12 : "))
        a13 = int(input("Enter a13 : "))
        a21 = int(input("Enter a21 : "))
        a22 = int(input("Enter a22 : "))
        a23 = int(input("Enter a23 : "))
        print("\nYour Matrix is:       " , "[",a11,a12,a13,"]")
        print("                      " , "[",a21,a22,a23,"]" , "\n")
        print("\nYour Matrix Transpose is:     " , "[",a11,a21,"]")
        print("                              " , "[",a12,a22,"]")
        print("                              " , "[",a13,a23,"]" , "\n")
     elif transpose_matrix == "1*3" :
        a11 = int(input("\nEnter a11 : "))
        a12 = int(input("Enter a12 : "))
        a13 = int(input("Enter a13 : "))
        print("\nYour Matrix is:  " , "[",a11,a12,a13,"]" , "\n") 
        print("\nYour Matrix Transpose is:     " , "[",a11,"]")
        print("                              " , "[",a12,"]")
        print("                              " , "[",a13,"]" , "\n") 
     elif transpose_matrix == "3*2" :
        a11 = int(input("\nEnter a11 : "))
        a12 = int(input("Enter a12 : "))
        a21 = int(input("Enter a21 : "))
        a22 = int(input("Enter a22 : "))
        a31 = int(input("Enter a31 : "))
        a32 = int(input("Enter a32 : "))
        print("\nYour Matrix is:       " , "[",a11,a12,"]")
        print("                      " , "[",a21,a22,"]")
        print("                      " , "[",a31,a32,"]" , "\n") 
        print("\nYour Matrix Transpose is:     " , "[",a11,a21,a31,"]")
        print("                              " , "[",a12,a22,a32,"]" , "\n")
     elif transpose_matrix == "3*1" :
        a11 = int(input("\nEnter a11 : "))
        a21 = int(input("Enter a21 : "))
        a31 = int(input("Enter a31 : "))
        print("\nYour Matrix is:       " , "[",a11,"]")
        print("                      " , "[",a21,"]")
        print("                      " , "[",a31,"]" , "\n") 
        print("\nYour Matrix Transpose is:  " , "[",a11,a21,a31,"]" , "\n")    
     elif transpose_matrix == "2*2" :
        a11 = int(input("\nEnter a11 : "))
        a12 = int(input("Enter a12 : "))
        a21 = int(input("Enter a21 : "))
        a22 = int(input("Enter a22 : "))
        print("\nYour Matrix is:       " , "[",a11,a12,"]")
        print("                      " , "[",a21,a22,"]" , "\n")
        print("\nYour Matrix Transpose is:     " , "[",a11,a21,"]")
        print("                              " , "[",a12,a22,"]" , "\n") 
     elif transpose_matrix == "1*2" :
        a11 = int(input("\nEnter a11 : "))
        a12 = int(input("Enter a12 : "))
        print("\nYour Matrix is:  " , "[",a11,a12,"]" , "\n")
        print("\nYour Matrix Transpose is:     " , "[",a11,"]")
        print("                              " , "[",a12,"]" , "\n")  
     elif transpose_matrix == "2*1" :
        a11 = int(input("\nEnter a11 : "))
        a21 = int(input("Enter a21 : "))
        print("\nYour Matrix is:       " , "[",a11,"]")
        print("                      " , "[",a21,"]" , "\n")
        print("\nYour Matrix Transpose is:  " , "[",a11,a21,"]" , "\n")            
     else:
         print("Wrong Input")
 elif operation == "I" :
     inverse_matrix = input("Choose The Matrix You Want To Inverse ('3*3 , 2*2'): ")
     if inverse_matrix == "2*2" :
        a11 = int(input("\nEnter a11: "))
        a12 = int(input("Enter a12: "))
        a21 = int(input("Enter a21: "))
        a22 = int(input("Enter a22: "))
        print("\nYour Matrix is:       " , "[",a11,a12,"]")
        print("                      " , "[",a21,a22,"]" , "\n")
        print("\nThe inverse Of The Matrix is:     " ,"1    " , "[",a22,-a21,"]")
        print("                                " , "______ " , "[",-a12,a11,"]" , "\n") 
        print("                                 " , (a11*a22) - (a12*a21) , "\n")

     elif inverse_matrix == "3*3" :
        a11 = int(input("\nEnter a11 : "))
        a12 = int(input("Enter a12 : "))
        a13 = int(input("Enter a13 : "))
        a21 = int(input("Enter a21 : "))
        a22 = int(input("Enter a22 : "))
        a23 = int(input("Enter a23 : "))
        a31 = int(input("Enter a31 : "))
        a32 = int(input("Enter a32 : "))
        a33 = int(input("Enter a33 : "))
        print("\nYour Matrix is:       " , "[",a11,a12,a13,"]")
        print("                      " , "[",a21,a22,a23,"]")
        print("                      " , "[",a31,a32,a33,"]" , "\n") 
        print("Firstly We Find The Transpose Of The Matrix. \n")
        print("\nYour Matrix Transpose is:     " , "[",a11,a21,a31,"]")
        print("                              " , "[",a12,a22,a32,"]")
        print("                              " , "[",a13,a23,a33,"]" , "\n") 
        print("Secondly We Find adj(A) Which is replacing each element in 'A Transpose' by its Cofactor \n")
        print(" adj(A) = " , "[" , (a22*a33)-(a32*a23) , (a12*a33)-(a32*a13) , (a12*a23)-(a22*a13) ,"]" )
        print("          " , "[" , (a23*a31)-(a21*a33) , (a11*a33)-(a31*a13) , (a21*a13)-(a23*a11) ,"]" )
        print("          " , "[" , (a32*a21)-(a22*a31) , (a11*a32)-(a31*a12) , (a11*a22)-(a21*a12) ,"]" , "\n" )
        print("Then We Find |A|. \n")
        dA = (a11)*((a22*a33)-(a32*a23)) - (a12)*((a21*a33)-(a23*a31)) + (a13)*((a21*a32)-(a22*a31))
        print("|A| =" , dA ,"\n")
        print("\nThe inverse Of The Matrix is:     " ,"1    " , "[" , (a22*a33)-(a32*a23) , (a12*a33)-(a32*a13) , (a12*a23)-(a22*a13) ,"]")
        print("                                " , "______ " , "[" , (a23*a31)-(a21*a33) , (a11*a33)-(a31*a13) , (a21*a13)-(a23*a11) ,"]" , "\n") 
        print("                                  " ,  dA  ,"  ","[" , (a32*a21)-(a22*a31) , (a11*a32)-(a31*a12) , (a11*a22)-(a21*a12) ,"]" "\n")

     else:
        print("Wrong Input") 
 elif operation == "C" :
     print("\nFirst Equation: ")
     a11 = int(input("Enter The X Factor: "))
     a12 = int(input("Enter The Y Factor: "))
     a13 = int(input("Enter The Z Factor: "))
     b1 = int(input("Enter The Equation Result: "))
     print("\nSeconed Equation: ")
     a21 = int(input("Enter The X Factor: "))
     a22 = int(input("Enter The Y Factor: "))
     a23 = int(input("Enter The Z Factor: "))
     b2 = int(input("Enter The Equation Result: "))
     print("\nThird Equation: ")
     a31 = int(input("Enter The X Factor: "))
     a32 = int(input("Enter The Y Factor: "))
     a33 = int(input("Enter The Z Factor: "))
     b3 = int(input("Enter The Equation Result: "))
     print("\n   " , "|", b1,a12,a13,"|")
     print("   " , "|", b2,a22,a23,"|")
     print("   " , "|", b3,a32,a33,"|")
     print("X =" , "_____________")
     print("\n   " , "|", a11,a12,a13,"|")
     print("   " , "|", a21,a22,a23,"|")
     print("   " , "|", a31,a32,a33,"|" , "\n")
     print("   " , "|", a11,b1,a13,"|")
     print("   " , "|", a21,b2,a23,"|")
     print("   " , "|", a31,b3,a33,"|")
     print("Y =" , "_____________")
     print("\n   " , "|", a11,a12,a13,"|")
     print("   " , "|", a21,a22,a23,"|")
     print("   " , "|", a31,a32,a33,"|" , "\n")
     print("   " , "|", a11,a12,b1,"|")
     print("   " , "|", a21,a22,b2,"|")
     print("   " , "|", a31,a32,b3,"|")
     print("Z =" , "_____________")
     print("\n   " , "|", a11,a12,a13,"|")
     print("   " , "|", a21,a22,a23,"|")
     print("   " , "|", a31,a32,a33,"|" , "\n")
     dA = (a11)*((a22*a33)-(a32*a23)) - (a12)*((a21*a33)-(a23*a31)) + (a13)*((a21*a32)-(a22*a31))
     x = (b1)*((a22*a33)-(a32*a23)) - (a12)*((b2*a33)-(a23*b3)) + (a13)*((b2*a32)-(a22*b3))
     y = (a11)*((b2*a33)-(b3*a23)) - (b1)*((a21*a33)-(a23*a31)) + (a13)*((a21*b3)-(b2*a31))
     z = (a11)*((a22*b3)-(a32*b2)) - (a12)*((a21*b3)-(b2*a31)) + (b1)*((a21*a32)-(a22*a31))
     X = x/dA
     Y = y/dA
     Z = z/dA
     print("\nX = " , X , "\n")
     print("\nY = " , Y , "\n")
     print("\nZ = " , Z , "\n")
 else:
      print("Wrong Input")  
 while True:
        answer = str(input('Run again? (y/n):'))
        if answer in ('y','n') :
         break
        print("invalid input.")
 if answer == 'y' :
        continue
 else:
      print('Goodbye')
      break