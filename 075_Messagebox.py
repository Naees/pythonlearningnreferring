from tkinter import *
from tkinter import messagebox # import messagebox library

def confirm():
    messagebox.showinfo(title="Payment notice", message="Please check before completing payment")
    messagebox.showwarning(title="Payment alert", message="Payment has failed, please try again!!")
    messagebox.showerror(title="Error", message="You seem to have lost connection to the site.. please try again later..")
    
    if messagebox.askokcancel(title="ASK OK status", message="Please confirm pending payment transaction.."):
        print('You have completed the payment..\n Please check your email for the invoice.')
    else:
        print("Payment has failed ending transaction!")
        
        
        
    if messagebox.askretrycancel(title="RETRY status", message="Lets retry the payment entry.."):
        print('There seems to be something wrong when the payment please re-enter the details..')
    else:
        print("Payment has failed ending transaction!")
    
    
    
    if messagebox.askyesno(title="YES NO status", message="Are you a member of Naees Shipping Co."):
        print('Thank you for confirming membership.')
    else:
        print("You are not a member, but you can sign up online to stand a chance and earn rebates/gifts.")
        
    
    
    msgBoxAns = messagebox.askquestion(title="QUESTION status", message="Do you need a carrier/bag?")
    if msgBoxAns == "yes":    
        print('Here have a bag.')
    else:
        print("You will not be charged additional for a carrier.")
        
        
        
    msgBoxAns = messagebox.askyesnocancel(title="YES NO CANCEL status", message="Do you need a GST Tax Rebate on the bill?", icon='info')
    if msgBoxAns == True:    
        print('Please wait for the GST Tax Rebate form to be printed for collection before leaving.')
    elif msgBoxAns == False:
        print("Thank you for shopping with us, please come back again soon.")
    else:
        print("If unsure please approach our customer service staff for more details.")
        
        
        
        
window = Tk()

button = Button(window, command=confirm, text="Complete Payment")
# button = Button(window, command=cancel, text="Cancel")
button.pack()
window.mainloop()