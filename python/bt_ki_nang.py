import math
if __name__== '__main__':
    print("1.Nhap hai so a, b: ")
    #Eval tac dung?
    a=eval(input("Nhap a: "))
    b=eval(input("Nhap b: "))
    #Khong dung string + double duoc! -> f,
    print(f"Phan nguyen cua hai so vua nhap la: ", a/b)
    print(f"Phan du cua hai so vua nhap la: ", a % b)
    print("2.Nhap 4 so nguyen a, b, c, d: ")
    a1 = eval(input("Nhap a: "))
    a2 = eval(input("Nhap b: "))
    a3 = eval(input("Nhap c: "))
    a4 = eval(input("Nhap d: "))
    print(f"Trung binh cong cua 4 so vua nhap la: ", (a1 + a2 + a3 + a4) * 1.0 / 4)
    print("3.Nhap gio, phut, giay: ")
    h=eval(input("Nhap gio: "))
    m=eval(input("Nhap phut: "))
    s=eval(input("Nhap giay: "))
    print(f"Tong gio phut giay vua nhap la: ",(h * 3600 + m * 60 * s))
    print("4.Nhap n co 2 chu so: ")
    n=eval(input("Nhap n co 2 chu so: "))
    print(f"Tong gia tri nguyen va du cua so vua nhap la: ", ((n / 10) / (n % 10) + (n / 10) % (n % 10)))
    if n%2==0:
        print(f"5.",n,f" la so chan")
    else:
        print(f"5.",n," la so le")
    if ((n/10)/n%10+(n/10)%(n%10))>10:
        print(f"6.",n,f" co tong nguyen du lon hon 10")
    else:
        print(f"6.",n,f" khong co tong nguyen du lon hon 10")
    if ((n/10)-(n%10))<0:
        print(f"7.",n,f" co hieu 2 chu so nho hon 0")
    else:
        print(f"7.",n,f" co hieu 2 chu so khong nho hon 0")
    if (n/10)==(n%10):
        print(f"8.",n,f" co 2 chu so doi xung")
    else:
        print(f"8.",n,f" co 2 chu so khong doi xung")
    if n/10>n%10:
        print(f"9.Chu so lon nhat cua ",n,f" la: ", n/10)
    else:
        print(f"9.Chu so lon nhat cua ",n,f"la: ", n%10)
    print(f"10.Chu so nghich dao cua n la: ", (n % 10 * 10 + n / 10))
    if n/10>n%10:
        print(f"11.Chu so tang dan cua ",n,f" la: ",n/10,"\t",n%10)
    else:
        print(f"11.Chu so tang dan cua ",n,f" la: ",n%10,"\t",n/10)
    if n/10<n%10:
        print(f"11.Chu so giam dan cua ",n,f" la: ",n/10,"\t",n%10)
    else:
        print(f"11.Chu so giam dan cua ",n,f" la: ",n%10,"\t",n/10)
    print("13.Nhap cac 2 tham so a, b cho pt bac nhat: ")
    a0=eval(input("Nhap a: "))
    b0=eval(input("Nhap b: "))
    if a0 == 0:
        if b0 == 0:
            print(f"Pt " ,a0, "x+" ,b0, f"=0 co vo so nghiem!")
        else:
            print(f"Pt " ,a0, "x+" ,b0, f"=0 vo nghiem!")
    else:
        print(f"Nghiem cua pt " ,a0, "x" ,b0, f"=0 la: ", -b0 / a0)
    print("14.Nhap 3 tham so a, b, c cho pt bac hai sau: ")
    a14 = eval(input("Nhap a: "))
    b14 = eval(input("Nhap b: "))
    c14 = eval(input("Nhap c: "))
    delta = b14 * b14 - 4 * a14 * c14
    if a14 == 0:
        if b14 == 0:
            if c14 == 0:
                print(f"Pt " ,a14, "x^2+" ,b14, "x+" ,c14, "=0 co vo so nghiem!")
            else:
                print(f"Pt " ,a14, "x^2+" ,b14, "x+" ,c14, "=0 vo nghiem!")
        else:
            print(f"Pt " ,a14, "x^2+" ,b14, "x+" ,c14, "=0 co nghiem la: ", -c14 / b14)
    else:
        if delta < 0:
            print(f"Pt " ,a14, "x^2+" ,b14, "x+" ,c14, "=0 vo nghiem!")
        else:
            if delta > 0:
                print(f"Pt " ,a14, "x^2+" ,b14, "x+" ,c14, "=0 co hai nghiem pb: x1=" , (-b14 + math.sqrt(delta) / 2 * a14), " va x2=", (-b14 + math.sqrt(delta) / 2 * a14))
            else:
                print(f"Pt " ,a14, "x^2+" ,b14, "x+" ,c14, "=0 co nghiem kep: ", -b14 / 2 * a14)