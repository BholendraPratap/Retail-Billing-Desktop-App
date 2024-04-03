from tkinter import *
from tkinter import messagebox
import random
import os,tempfile,smtplib

billnumber=random.randint(100,1000)
#print(billnumber)
#Functionality part-----------

def clear():
    bathsoapEntry.delete(0,END)
    bathsoapEntry.insert(0,0)
    facecreamEntry.delete(0,END)
    facecreamEntry.insert(0,0)
    facewashEntry.delete(0,END)
    facewashEntry.insert(0,0)
    hairgelEntry.delete(0,END)
    hairgelEntry.insert(0,0)
    hairsprayEntry.delete(0,END)
    hairsprayEntry.insert(0,0)
    daalEntry.delete(0,END)
    daalEntry.insert(0,0)
    teaEntry.delete(0,END)
    teaEntry.insert(0,0)
    sugarEntry.delete(0,END)
    sugarEntry.insert(0,0)
    riceEntry.delete(0,END)
    riceEntry.insert(0,0)
    bodylotionEntry.delete(0,END)
    bodylotionEntry.insert(0,0)
    pepsiEntry.delete(0,END)
    pepsiEntry.insert(0,0)
    wheatEntry.delete(0,END)
    wheatEntry.insert(0,0)
    oilEntry.delete(0,END)
    oilEntry.insert(0,0)
    maazaEntry.delete(0,END)
    maazaEntry.insert(0,0)
    spriteEntry.delete(0,END)
    spriteEntry.insert(0,0)
    dewEntry.delete(0,END)
    dewEntry.insert(0,0)
    cococolaEntry.delete(0,END)
    cococolaEntry.insert(0,0)
    frootiEntry.delete(0,END)
    frootiEntry.insert(0,0)
    
    cosmeticpriceEntry.delete(0,END)
    cosmeticpriceEntry.insert(0,0)
    grocerypriceEntry.delete(0,END)
    grocerypriceEntry.insert(0,0)
    drinkspriceEntry.delete(0,END)
    drinkspriceEntry.insert(0,0)

    drinkstaxEntry.delete(0,END)
    drinkstaxEntry.insert(0,0)
    grocerytaxEntry.delete(0,END)
    grocerytaxEntry.insert(0,0)
    cosmetictaxEntry.delete(0,END)
    cosmetictaxEntry.insert(0,0)

    nameEntry.delete(0,END)
    nameEntry.insert(0,'')
    phoneEntry.delete(0,END)
    phoneEntry.insert(0,'')
    billnumberEntry.delete(0,END)
    billnumberEntry.insert(0,'')

    textarea.delete(0,END)

def send_email():#email button
    def send_gmail():
        try:
            ob=smtplib.SMTP('smtp.gmail.com',587)
            ob.starttls()
            ob.login(senderEntry.get(),passwordEntry.get())
            message=email_textarea.get(1.0,END)
            reciever_address=recieverEntry.get()
            ob.sendmail(senderEntry.get(),reciever_address,message)
            ob.quit()
            messagebox.showinfo('Success',"Bill is successfully sent",parent=root1)
            root1.destroy()
        except:
            messagebox.showerror('Error','Something went wrong, Please try Again',parent=root1)
    if textarea.get(1.0,END)=='\n':
        messagebox.showerror('Error','Bill is empty')
    else:
        root1=Toplevel()
        root1.grab_set()
        root1.title("Send Mail")
        #root1.geometry('700x320')
        root1.config(bg='gray20')
        root1.resizable(0,0)
        
        senderFrame=LabelFrame(root1,text='SENDER',font=('arial',16,'bold'),bd=6,bg='gray20',fg='white')
        senderFrame.grid(row=0,column=0,padx=40,pady=20)

        senderLabel=Label(senderFrame,text="Sender's Email",font=('arial',14,'bold'),bg='gray20',fg='white')
        senderLabel.grid(row=0,column=0,padx=10,pady=8)

        senderEntry=Entry(senderFrame,font=('arial',14,'bold'),bd=2,width=23,relief=RIDGE)
        senderEntry.grid(row=0,column=1,padx=10,pady=8)
        senderEntry.insert(0,"bholendra.22scse2030006@galgotiasuniversity.edu.in")

        passwordLabel=Label(senderFrame,text="password",font=('arial',14,'bold'),bg='gray20',fg='white')
        passwordLabel.grid(row=1,column=0,padx=10,pady=8)
        

        passwordEntry=Entry(senderFrame,font=('arial',14,'bold'),bd=2,width=23,relief=RIDGE,show='*')
        passwordEntry.grid(row=1,column=1,padx=10,pady=8)
        passwordEntry.insert(0,"oezz xrmb xxol ukkd")

        recipientFrame=LabelFrame(root1,text='Recipient',font=('arial',16,'bold'),bd=6,bg='gray20',fg='white')
        recipientFrame.grid(row=1,column=0,padx=40,pady=20)

        recieverLabel=Label(recipientFrame,text="Reciever's email",font=('arial',14,'bold'),bg='gray20',fg='white')
        recieverLabel.grid(row=0,column=0,padx=10,pady=8)

        recieverEntry=Entry(recipientFrame,font=('arial',14,'bold'),bd=2,width=23,relief=RIDGE)
        recieverEntry.grid(row=0,column=1,padx=10,pady=8)

        messageLabel=Label(recipientFrame,text="Message",font=('arial',14,'bold'),bg='gray20',fg='white')
        messageLabel.grid(row=1,column=0,padx=10,pady=8)

        email_textarea=Text(recipientFrame,font=('arial',14,'bold'),bd=2,relief=SUNKEN,width=42,height=11)
        email_textarea.grid(row=2,column=0,columnspan=2)
        email_textarea.delete(1.0,END)
        email_textarea.insert(END,textarea.get(1.0,END).replace('=','').replace('\t\t\t','\t\t'))

        sendButton=Button(root1,text="Send",font=('arial',18,'bold'),width=15,command=send_gmail)
        sendButton.grid(row=2,column=0,pady=20)

        root1.mainloop() 
    
    

def print_bill():  #PRINT BUTTON
    if textarea.get(1.0,END)=='\n':
        messagebox.showerror('Error','No any bill generated till now')
    else:
        file=tempfile.mktemp('.txt')
        open(file,'w').write(textarea.get(1.0,END))
        os.startfile(file,'print')


def search_bill():  #SEARCH BUTTON
    for i in os.listdir('bills/'):
        if i.split('.')[0]==billnumberEntry.get():
            f=open(f'bills/{i}','r')
            textarea.delete(1.0,END)
            for data in f:
                textarea.insert(END,data)
            f.close()
            break
        else:
            messagebox.showerror('Error','Invalid bill number')
        
def total():
    #global variables
    global soapprice,hairgelprice,hairsprayprice,facecreamprice,facewashprice,bodylotionprice,riceprice,daalprice,wheatprice,sugarprice,oilprice,teaprice,frootiprice,spriteprice,pepsiprice,dewprice,cococolaprice,maazaprice,totalbill
    #cosmetics products total
    soapprice=int(bathsoapEntry.get())*20  #unit price
    facecreamprice=int(facecreamEntry.get())*50 
    facewashprice=int(facewashEntry.get())*100 
    hairsprayprice=int(hairsprayEntry.get())*150 
    hairgelprice=int(hairgelEntry.get())*80 
    bodylotionprice=int(bodylotionEntry.get())*200 

    totalcosmeticprice=soapprice+facecreamprice+facewashprice+hairsprayprice+hairgelprice+bodylotionprice
    cosmeticpriceEntry.insert(0,str(totalcosmeticprice)+"Rs")
    cosmetictax=totalcosmeticprice*0.12
    cosmetictaxEntry.delete(0,END)
    cosmetictaxEntry.insert(0,str(cosmetictax)+"Rs")

    #grocery totals
    riceprice=int(riceEntry.get())*30  #unit price
    daalprice=int(daalEntry.get())*120 
    wheatprice=int(wheatEntry.get())*100 
    sugarprice=int(sugarEntry.get())*45 
    teaprice=int(teaEntry.get())*120 
    oilprice=int(oilEntry.get())*200 

    totalgroceryprice=riceprice+daalprice+wheatprice+sugarprice+teaprice+oilprice
    grocerypriceEntry.insert(0,str(totalgroceryprice)+"Rs")
    grocerytax=totalgroceryprice*0.5
    grocerytaxEntry.delete(0,END)
    grocerytaxEntry.insert(0,str(grocerytax)+"Rs")

    #cold drinks totals
    maazaprice=int(maazaEntry.get())*50 #unit price
    pepsiprice=int(pepsiEntry.get())*40
    spriteprice=int(spriteEntry.get())*30
    dewprice=int(dewEntry.get())*45 
    frootiprice=int(frootiEntry.get())*10
    cococolaprice=int(cococolaEntry.get())*100

    totaldrinksprice=maazaprice+pepsiprice+spriteprice+dewprice+frootiprice+cococolaprice
    drinkspriceEntry.insert(0,str(totaldrinksprice)+"Rs")

    drinkstax=totaldrinksprice*0.9
    drinkstaxEntry.delete(0,END)
    drinkstaxEntry.insert(0,str(drinkstax)+"Rs")


    #total bill
    totalbill=totalcosmeticprice+totaldrinksprice+totalgroceryprice+grocerytax+drinkstax+cosmetictax

def bill():
    if nameEntry.get()=="" or phoneEntry.get()=="":
        messagebox.showerror("Error","Customer details are required")
    elif cosmeticpriceEntry.get()=="" and grocerypriceEntry.get()=='' and drinkspriceEntry.get()=="":
        messagebox.showerror("Error","No Products Selected")
    elif cosmeticpriceEntry.get()=='0 Rs' and grocerypriceEntry.get()=='0 Rs' and drinkspriceEntry.get()=='0 Rs':
        messagebox.showerror("Error","No products selected")
    else:
        textarea.delete(1.0,END)
        textarea.insert(END,"\t\t*** Welcome Customer ***\n")
        textarea.insert(END,f"Bill No.:{billnumber}")
        textarea.insert(END,f"\nCustomer Name:{nameEntry.get()}")
        textarea.insert(END,f"\nCustomer Phone No. :{phoneEntry.get()}")
        textarea.insert(END,"\n============================================================")
        textarea.insert(END,"Product\t\t\tQuantity\t\t\tPrice")
        textarea.insert(END,"\n============================================================")
        if bathsoapEntry.get()!='0':
            textarea.insert(END,f'\nBath Soap\t\t\t{bathsoapEntry.get()}\t\t\t{soapprice}Rs')
        if hairgelEntry.get()!='0':
            textarea.insert(END,f'\nHair Gel\t\t\t{hairgelEntry.get()}\t\t\t{hairgelprice}Rs')
        if hairsprayEntry.get()!='0':
            textarea.insert(END,f'\nHair Spray\t\t\t{hairsprayEntry.get()}\t\t\t{hairsprayprice}Rs')
        if facecreamEntry.get()!='0':
            textarea.insert(END,f'\nface cream\t\t\t{facecreamEntry.get()}\t\t\t{facecreamprice}Rs')
        if facewashEntry.get()!='0':
            textarea.insert(END,f'\nFace wash\t\t\t{facewashEntry.get()}\t\t\t{facewashprice}Rs')
        if bodylotionEntry.get()!='0':
            textarea.insert(END,f'\nBody Lotion\t\t\t{bodylotionEntry.get()}\t\t\t{bodylotionprice}Rs')
        if riceEntry.get()!='0':
            textarea.insert(END,f'\nRice    \t\t\t{riceEntry.get()}\t\t\t{riceprice}Rs')
        if daalEntry.get()!='0':
            textarea.insert(END,f'\nDaal    \t\t\t{daalEntry.get()}\t\t\t{daalprice}Rs')
        if oilEntry.get()!='0':
            textarea.insert(END,f'\nOil    \t\t\t{oilEntry.get()}\t\t\t{oilprice}Rs')
        if sugarEntry.get()!='0':
            textarea.insert(END,f'\nSugar    \t\t\t{sugarEntry.get()}\t\t\t{sugarprice}Rs')
        if wheatEntry.get()!='0':
            textarea.insert(END,f'\nWheat    \t\t\t{wheatEntry.get()}\t\t\t{wheatprice}Rs')
        if teaEntry.get()!='0':
            textarea.insert(END,f'\nTea    \t\t\t{teaEntry.get()}\t\t\t{teaprice}Rs')
        if maazaEntry.get()!='0':
            textarea.insert(END,f'\nMaaza    \t\t\t{maazaEntry.get()}\t\t\t{maazaprice}Rs')
        if spriteEntry.get()!='0':
            textarea.insert(END,f'\nSprite    \t\t\t{spriteEntry.get()}\t\t\t{spriteprice}Rs')
        if pepsiEntry.get()!='0':
            textarea.insert(END,f'\nPepsi    \t\t\t{pepsiEntry.get()}\t\t\t{pepsiprice}Rs')
        if dewEntry.get()!='0':
            textarea.insert(END,f'\nDew    \t\t\t{dewEntry.get()}\t\t\t{dewprice}Rs')
        if frootiEntry.get()!='0':
            textarea.insert(END,f'\nFrooti    \t\t\t{frootiEntry.get()}\t\t\t{frootiprice}Rs')
        if cococolaEntry.get()!='0':
            textarea.insert(END,f'\nCoca Cola    \t\t\t{cococolaEntry.get()}\t\t\t{cococolaprice}Rs')
        textarea.insert(END,"\n============================================================")
        if cosmetictaxEntry.get!='0.0 Rs':
            textarea.insert(END,f"\nCosmetic Tax \t\t{cosmetictaxEntry.get()}")
        if grocerytaxEntry.get!='0.0 Rs':
            textarea.insert(END,f"\nGrocery Tax \t\t{grocerytaxEntry.get()}")
        if drinkstaxEntry.get!='0.0 Rs':
            textarea.insert(END,f"\nDrinks Tax \t\t{drinkstaxEntry.get()}")
        textarea.insert(END,f"\n\nTotal Bill \t\t\t\t{totalbill}")
        textarea.insert(END,f"\n===========================================================")
        save_bill()

def save_bill():
    global billnumber
    result=messagebox.askyesno('Confirm','Do you want to save the bill?')
    if result:
        bill_content=textarea.get(1.0,END)
        file=open(f'bills/{billnumber}.txt','w')
        file.write(bill_content)
        file.close()
        messagebox.showinfo("Success",f"{billnumber} is saved successfully")
        billnumber=random.randint(100,1000)


#GUI part
#STRUCTURE OF BASIC WINDOW AND TITLE
root=Tk()
root.title("Retail Billing System")
root.geometry("1270x685")
root.iconbitmap('bill.ico')
headingLabel=Label(root,text="Retail Billing System",font=('times new roman',25,'bold'),bg='gray20',fg='gold',bd=12,relief=GROOVE)
headingLabel.pack(fill=X)

#structure for customer details
customer_details_frame=LabelFrame(root,text='Customer Details',font=('times new roman',12,'bold'),bg='gray20',fg='gold',bd=8,relief=GROOVE)
customer_details_frame.pack(fill=X)

nameLabel=Label(customer_details_frame,text="Name",font=('times new roman',12,'bold'),bg='gray20',fg='white',bd=8)
nameLabel.grid(row=0,column=0,padx=20)

nameEntry=Entry(customer_details_frame,font=('arial',12),bd=7,width=20)
nameEntry.grid(row=0,column=1,padx=8)

phoneLabel=Label(customer_details_frame,text="Phone Number",font=('times new roman',12,'bold'),bg='gray20',fg='white',bd=8)
phoneLabel.grid(row=0,column=2,padx=20,pady=2)

phoneEntry=Entry(customer_details_frame,font=('arial',12),bd=7,width=20)
phoneEntry.grid(row=0,column=3,padx=8)

billnumberLabel=Label(customer_details_frame,text="Bill Number",font=('times new roman',12,'bold'),bg='gray20',fg='white',bd=8)
billnumberLabel.grid(row=0,column=4,padx=20,pady=2)

billnumberEntry=Entry(customer_details_frame,font=('arial',12),bd=7,width=20)
billnumberEntry.grid(row=0,column=5,padx=8)

searchButton=Button(customer_details_frame,text='SEARCH',font=('arial',12,'bold'),bd=7,command=search_bill)
searchButton.grid(row=0,column=6,padx=20)

#structure for products frame
productsFrame=Frame(root)
productsFrame.pack()

cosmeticsFrame=LabelFrame(productsFrame,text='Cosmetics',font=('times new roman',12,'bold'),bg='gray20',fg='gold',bd=8)
cosmeticsFrame.grid(row=0,column=0)

bathsoapLabel=Label(cosmeticsFrame,text="Bath Soap",font=('times new roman',12,'bold'),bg='gray20',fg='white',bd=8)
bathsoapLabel.grid(row=0,column=0,padx=10,pady=6,sticky='w')

bathsoapEntry=Entry(cosmeticsFrame,font=('times new roman',12,'bold'),width=12,bd=5)
bathsoapEntry.grid(row=0,column=1,padx=10,pady=6)
bathsoapEntry.insert(0,0)

facecreamLabel=Label(cosmeticsFrame,text="Face Cream",font=('times new roman',12,'bold'),bg='gray20',fg='white',bd=8)
facecreamLabel.grid(row=1,column=0,padx=10,pady=6,sticky='w')

facecreamEntry=Entry(cosmeticsFrame,font=('times new roman',12,'bold'),width=12,bd=5)
facecreamEntry.grid(row=1,column=1,padx=10,pady=6)
facecreamEntry.insert(0,0)

facewashLabel=Label(cosmeticsFrame,text="Face Wash",font=('times new roman',12,'bold'),bg='gray20',fg='white',bd=8)
facewashLabel.grid(row=2,column=0,padx=10,pady=6,sticky='w')

facewashEntry=Entry(cosmeticsFrame,font=('times new roman',12,'bold'),width=12,bd=5)
facewashEntry.grid(row=2,column=1,padx=10,pady=6)
facewashEntry.insert(0,0)

hairsprayLabel=Label(cosmeticsFrame,text="Hair Spray",font=('times new roman',12,'bold'),bg='gray20',fg='white',bd=8)
hairsprayLabel.grid(row=3,column=0,padx=10,pady=6,sticky='w')

hairsprayEntry=Entry(cosmeticsFrame,font=('times new roman',12,'bold'),width=12,bd=5)
hairsprayEntry.grid(row=3,column=1,padx=10,pady=6)
hairsprayEntry.insert(0,0)

hairgelLabel=Label(cosmeticsFrame,text="Hair Gel",font=('times new roman',12,'bold'),bg='gray20',fg='white',bd=8)
hairgelLabel.grid(row=4,column=0,padx=10,pady=9,sticky='w')

hairgelEntry=Entry(cosmeticsFrame,font=('times new roman',12,'bold'),width=12,bd=5)
hairgelEntry.grid(row=4,column=1,padx=10,pady=6)
hairgelEntry.insert(0,0)

bodylotionLabel=Label(cosmeticsFrame,text="Body Lotion",font=('times new roman',12,'bold'),bg='gray20',fg='white',bd=8)
bodylotionLabel.grid(row=5,column=0,padx=10,pady=6,sticky='w')

bodylotionEntry=Entry(cosmeticsFrame,font=('times new roman',12,'bold'),width=12,bd=5)
bodylotionEntry.grid(row=5,column=1,padx=10,pady=6)
bodylotionEntry.insert(0,0)

groceryFrame=LabelFrame(productsFrame,text='Grocery',font=('times new roman',12,'bold'),bg='gray20',fg='gold',bd=8)
groceryFrame.grid(row=0,column=1)

riceLabel=Label(groceryFrame,text="Rice",font=('times new roman',12,'bold'),bg='gray20',fg='white',bd=8)
riceLabel.grid(row=0,column=0,padx=10,pady=6,sticky='w')

riceEntry=Entry(groceryFrame,font=('times new roman',12,'bold'),width=12,bd=5)
riceEntry.grid(row=0,column=1,padx=10,pady=6)
riceEntry.insert(0,0)

oilLabel=Label(groceryFrame,text="Oil",font=('times new roman',12,'bold'),bg='gray20',fg='white',bd=8)
oilLabel.grid(row=1,column=0,padx=10,pady=6,sticky='w')

oilEntry=Entry(groceryFrame,font=('times new roman',12,'bold'),width=12,bd=5)
oilEntry.grid(row=1,column=1,padx=10,pady=6)
oilEntry.insert(0,0)

daalLabel=Label(groceryFrame,text="Daal",font=('times new roman',12,'bold'),bg='gray20',fg='white',bd=8)
daalLabel.grid(row=2,column=0,padx=10,pady=6,sticky='w')

daalEntry=Entry(groceryFrame,font=('times new roman',12,'bold'),width=12,bd=5)
daalEntry.grid(row=2,column=1,padx=10,pady=9)
daalEntry.insert(0,0)

wheatLabel=Label(groceryFrame,text="Wheat",font=('times new roman',12,'bold'),bg='gray20',fg='white',bd=8)
wheatLabel.grid(row=3,column=0,padx=10,pady=6,sticky='w')

wheatEntry=Entry(groceryFrame,font=('times new roman',12,'bold'),width=12,bd=5)
wheatEntry.grid(row=3,column=1,padx=10,pady=6)
wheatEntry.insert(0,0)

sugarLabel=Label(groceryFrame,text="Sugar",font=('times new roman',12,'bold'),bg='gray20',fg='white',bd=8)
sugarLabel.grid(row=4,column=0,padx=10,pady=6,sticky='w')

sugarEntry=Entry(groceryFrame,font=('times new roman',12,'bold'),width=12,bd=5)
sugarEntry.grid(row=4,column=1,padx=10,pady=6)
sugarEntry.insert(0,0)

teaLabel=Label(groceryFrame,text="Tea",font=('times new roman',12,'bold'),bg='gray20',fg='white',bd=8)
teaLabel.grid(row=5,column=0,padx=10,pady=6,sticky='w')

teaEntry=Entry(groceryFrame,font=('times new roman',12,'bold'),width=12,bd=5)
teaEntry.grid(row=5,column=1,padx=10,pady=6)
teaEntry.insert(0,0)

drinksFrame=LabelFrame(productsFrame,text='Cold drinks',font=('times new roman',12,'bold'),bg='gray20',fg='gold',bd=8)
drinksFrame.grid(row=0,column=2)

maazaLabel=Label(drinksFrame,text="Maaza",font=('times new roman',12,'bold'),bg='gray20',fg='white',bd=8)
maazaLabel.grid(row=0,column=0,padx=10,pady=6,sticky='w')

maazaEntry=Entry(drinksFrame,font=('times new roman',12,'bold'),width=12,bd=5)
maazaEntry.grid(row=0,column=1,padx=10,pady=6)
maazaEntry.insert(0,0)

pepsiLabel=Label(drinksFrame,text="Pepsi",font=('times new roman',12,'bold'),bg='gray20',fg='white',bd=8)
pepsiLabel.grid(row=1,column=0,padx=10,pady=6,sticky='w')

pepsiEntry=Entry(drinksFrame,font=('times new roman',12,'bold'),width=12,bd=5)
pepsiEntry.grid(row=1,column=1,padx=10,pady=6)
pepsiEntry.insert(0,0)

spriteLabel=Label(drinksFrame,text="Sprite",font=('times new roman',12,'bold'),bg='gray20',fg='white',bd=8)
spriteLabel.grid(row=2,column=0,padx=10,pady=6,sticky='w')

spriteEntry=Entry(drinksFrame,font=('times new roman',12,'bold'),width=12,bd=5)
spriteEntry.grid(row=2,column=1,padx=10,pady=6)
spriteEntry.insert(0,0)

dewLabel=Label(drinksFrame,text="Dew",font=('times new roman',12,'bold'),bg='gray20',fg='white',bd=8)
dewLabel.grid(row=3,column=0,padx=10,pady=6,sticky='w')

dewEntry=Entry(drinksFrame,font=('times new roman',12,'bold'),width=12,bd=5)
dewEntry.grid(row=3,column=1,padx=10,pady=6)
dewEntry.insert(0,0)

frootiLabel=Label(drinksFrame,text="Frooti",font=('times new roman',12,'bold'),bg='gray20',fg='white',bd=8)
frootiLabel.grid(row=4,column=0,padx=10,pady=6,sticky='w')

frootiEntry=Entry(drinksFrame,font=('times new roman',12,'bold'),width=12,bd=5)
frootiEntry.grid(row=4,column=1,padx=10,pady=6)
frootiEntry.insert(0,0)

cococolaLabel=Label(drinksFrame,text="Coco Cola",font=('times new roman',12,'bold'),bg='gray20',fg='white',bd=8)
cococolaLabel.grid(row=5,column=0,padx=10,pady=6,sticky='w')

cococolaEntry=Entry(drinksFrame,font=('times new roman',12,'bold'),width=12,bd=5)
cococolaEntry.grid(row=5,column=1,padx=10,pady=6)
cococolaEntry.insert(0,0)

billframe=Frame(productsFrame,bd=8,relief=GROOVE)
billframe.grid(row=0,column=3,padx=10)

billareaLabel=Label(billframe,text='Bill Area',font=('times new roman',12,'bold'),bd=7,relief=GROOVE)
billareaLabel.pack(fill=X)

scrollbar=Scrollbar(billframe,orient=VERTICAL)
scrollbar.pack(side=RIGHT,fill=Y)
textarea=Text(billframe,height=16,width=60,yscrollcommand=scrollbar.set)
textarea.pack()
scrollbar.config(command=textarea.yview)


#structure for bill menu
billmenuFrame=LabelFrame(root,text='Bill Menu',font=('times new roman',12,'bold'),bg='gray20',fg='gold',bd=8)
billmenuFrame.pack()

cosmeticpriceLabel=Label(billmenuFrame,text="Cosmetic Price",font=('times new roman',12,'bold'),bg='gray20',fg='white',bd=8)
cosmeticpriceLabel.grid(row=0,column=0,padx=10,pady=6,sticky='w')

cosmeticpriceEntry=Entry(billmenuFrame,font=('times new roman',12,'bold'),width=10,bd=5)
cosmeticpriceEntry.grid(row=0,column=1,padx=10,pady=6)

grocerypriceLabel=Label(billmenuFrame,text="Grocery Price",font=('times new roman',12,'bold'),bg='gray20',fg='white',bd=8)
grocerypriceLabel.grid(row=1,column=0,padx=10,pady=6,sticky='w')

grocerypriceEntry=Entry(billmenuFrame,font=('times new roman',12,'bold'),width=10,bd=5)
grocerypriceEntry.grid(row=1,column=1,padx=10,pady=6)

drinkspriceLabel=Label(billmenuFrame,text="Cold Drink Price",font=('times new roman',12,'bold'),bg='gray20',fg='white',bd=8)
drinkspriceLabel.grid(row=2,column=0,padx=10,pady=6,sticky='w')

drinkspriceEntry=Entry(billmenuFrame,font=('times new roman',12,'bold'),width=10,bd=5)
drinkspriceEntry.grid(row=2,column=1,padx=10,pady=6)

###############

cosmetictaxLabel=Label(billmenuFrame,text="Cosmetic Tax",font=('times new roman',12,'bold'),bg='gray20',fg='white',bd=8)
cosmetictaxLabel.grid(row=0,column=2,padx=10,pady=6,sticky='w')

cosmetictaxEntry=Entry(billmenuFrame,font=('times new roman',12,'bold'),width=10,bd=5)
cosmetictaxEntry.grid(row=0,column=3,padx=10,pady=6)

grocerytaxLabel=Label(billmenuFrame,text="Grocery Tax",font=('times new roman',12,'bold'),bg='gray20',fg='white',bd=8)
grocerytaxLabel.grid(row=1,column=2,padx=10,pady=6,sticky='w')

grocerytaxEntry=Entry(billmenuFrame,font=('times new roman',12,'bold'),width=10,bd=5)
grocerytaxEntry.grid(row=1,column=3,padx=10,pady=6)

drinkstaxLabel=Label(billmenuFrame,text="Cold Drink Tax",font=('times new roman',12,'bold'),bg='gray20',fg='white',bd=8)
drinkstaxLabel.grid(row=2,column=2,padx=10,pady=6,sticky='w')

drinkstaxEntry=Entry(billmenuFrame,font=('times new roman',12,'bold'),width=10,bd=5)
drinkstaxEntry.grid(row=2,column=3,padx=10,pady=6)

##########Buttons############

buttonFrame=Frame(billmenuFrame,bd=8,relief=GROOVE)
buttonFrame.grid(row=0,column=4,rowspan=3)

totalButton=Button(buttonFrame,text='Total',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8,pady=10,command=total)
totalButton.grid(row=0,column=0,pady=20,padx=5)

billButton=Button(buttonFrame,text='Bill',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8,pady=10,command=bill)
billButton.grid(row=0,column=1,pady=20,padx=5)

emailButton=Button(buttonFrame,text='Email',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8,pady=10,command=send_email)
emailButton.grid(row=0,column=2,pady=20,padx=5)

printButton=Button(buttonFrame,text='Print',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8,pady=10,command=print_bill)
printButton.grid(row=0,column=3,pady=20,padx=5)

clearButton=Button(buttonFrame,text='Clear',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8,pady=10,command=clear)
clearButton.grid(row=0,column=4,pady=20,padx=5)



root.mainloop()