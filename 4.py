x = input("Enter any character: ");
if x == '0':
    exit();
else:
    if((x>='a' and x<='z') or (x>='A' and x<='Z')):
    	print(x, "is an alphabet.");
    else:
    	print(x, "is not an alphabet.");
