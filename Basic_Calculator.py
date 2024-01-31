def main():
    x = int(input("First number: "))
    y = int(input("Second number: "))
    op = input("Choose operator(+, -, *, /): ")

    if op == '+':
        print("The result is:", x + y)
        
    elif op == '-':
        print("The result is:", x - y)
        
    elif op == '*':
        print("The result is:", x * y)
        
    elif op == '/':
        z = x/y #bölme işleminden sonra z float bir değer oluyo yani ondalıklı olarak görülüyo.
        z2 = int(z) #Burda z'yi int yaptık ve onu yeni bir değere atadık. int olması demek TAM SAYI olması demek aynı zamanda.
        
        if not z / z2 == 1: #Eğer z nin z2 ye bölümü 1'i VERMİYORSA ondalıklı sayıdır.
            print("The result is:", z)
            print("Bu bir ondalıklı sayı.")
            
        else:
            print("The result is:", z2)
            
    else:
        print("ERROR")
        return main()
    
    restart()

def restart():
    r = input("Do you want use again(Y/N)? ")

    if r == "Y":
        return main()
    elif r == "N":
        quit()
    else:
        print("ERROR")
        return restart()

main()
