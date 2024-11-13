operation_type = input("Operation Type, (+) (-) (/) (x): ");

number1 = input("Number 1: ");
number2 = input("Number 2: ");

def doOperation(n1, n2):
    if (operation_type == "x"):
        
        print(n1, "*", n2, "=", n1 * n2);
        
    elif (operation_type == "+"):
        
        print(n1, "+", n2, "=", n1 + n2);

    elif (operation_type == "-"):
        
        print(n1, "-", n2, "=", n1 - n2);
        
    elif (operation_type == "/"):
        
        print(n1, "/", n2, "=", n1 / n2);
    
    else:
        
        print("Valid operation types are: x for multiplication, + for addition, - for subtraction, and / division");

doOperation(int(number1), int(number2));
