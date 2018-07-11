def main():
 x=int(input(""))
 temp=x
 rev=0
 while(x>0):
    dig=x%10
    rev=rev*10+dig
    x=x//10
 if(temp==rev):
    print("Yes")
 else:
    print("No")

if __name__ == '__main__':
    main()
