#program to compute discount
total_amount=float(input("enter the amount purchased:"))
if total_amount>1000:
                   discount=0.05*total_amount
                   payable_amount=total_amount-discount
                   print("the discount is",discount,"the price after discount is",payable_amount)
else:
                       print("no discount")
                         
