from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import filedialog
import pymysql


def action():
        def wd():
                winsignup.destroy()

        def toggle2():
                    if t_btn['text']=='=':
            
                       t_btn.config(text='x',cursor="hand2")
                    else :
            
                        t_btn.config(text='=',cursor="hand2")
                        t_btn.config(text='x',cursor="hand2")
                        t_btn.config(text='=',cursor="hand2")
                    
          
                    margin=Label(winsignup,bg='skyblue',width='20',height='25')
                    margin.place(x=0,y=75)
                    
                    btn=Button(winsignup,text='CUSTOMER ADD',fg='blue',bg='light green',cursor="hand2",font='verdana 10 bold',command=action1)
                    btn.place(x=4,y=90)

                    btn=Button(winsignup,text='PRODUCT ADD',fg='blue',bg='light green',font='verdana 10 bold',command=action3)
                    btn.place(x=4,y=150)

                    btn=Button(winsignup,text='SALES BILLING',fg='blue',bg='light green',font='verdana 10 bold',command=action2)
                    btn.place(x=4,y=210)


                    btn=Button(winsignup,text='REPORT',fg='blue',bg='light green',font='verdana 10 bold',command=action4)
                    btn.place(x=4,y=270)
                    
                    btn=Button(winsignup,text='SIGN OUT',fg='blue',bg='light green',font='verdana 10 bold',command=wd)
                    btn.place(x=4,y=390)
                    
        winsignup = Tk()
        label_text=StringVar()
        label1_text=StringVar()
        winsignup.title("DataBase Connection")
        winsignup.maxsize(width=800 ,  height=500)
        winsignup.minsize(width=800 ,  height=500)
        winsignup['bg']='white'
        scroll=Scrollbar(winsignup, orient=VERTICAL)

        margin=Label(winsignup,bg='skyblue',width='200',height='3')
        margin.place(x=0,y=3)
        
        margin=Label(winsignup,text="<-click",fg="red",bg='skyblue',font='Verdana 12 bold')
        margin.place(x=80,y=20)
        

        t_btn=Button(winsignup,text='=',fg='blue',font='verdana 25 bold',bd=0,activebackground='blue',cursor="hand2",activeforeground='white',command=toggle2)
        t_btn.place(x=10,y=10)

        hm= Label(winsignup, text= "GST BILLING",bg='skyblue' ,fg='blue',font='verdana 25 bold')
        hm.place(x=200,y=14)

        yscrollbar=Scrollbar(winsignup,orient=VERTICAL)
        xscrollbar=Scrollbar(winsignup,orient=HORIZONTAL)

        yscrollbar.pack(side=RIGHT,fill=Y)
        xscrollbar.pack(side=BOTTOM,fill=X)

        txtbox=Text(winsignup,height=500,width=80,yscrollcommand=yscrollbar.set,xscrollcommand=xscrollbar.set,wrap="none")
        yscrollbar.config(command=txtbox.yview)
        xscrollbar.config(command=txtbox.xview)

        txtbox.pack(pady=50)
    
        txtbox.insert(END,'''\n\n\n CUSTOMER ADD: Definition
    Customer add is a great tool to use in order to store valuable information about your customers. Alongside other pertinent data points, customer notes will also be displayed in each conversation to ensure this information is easily accessible to you.
    Customer notes are internal-facing only, so you don't need to worry about customers seeing what information is stored under their name.

    To add a customer note, simply open a customer conversation or contact profile and click on “Add Note” in the Customer Notes section.

    Added notes can be edited, and all notes added will be sorted in chronological order with the newest note on topr when contacting Google Ads customer support and also to link your account with other Google products like Google Analytics or Business Profile,

    PRODUCT ADD:
    Product add are a richer form of presentation for snippets in search results than just text. They are used for products and product reviews, and can include additional information such as ratings, review information, price, and availability.
    Merchant listing experiences rely on more specific data about a product, such as its price and availability. Only pages from which a shopper can purchase a product are eligible for merchant listing experiences, not pages with links to other sites that sell the product.
    Google may attempt to verify merchant listing product data before showing the information in search results.

    Result enhancements
    If you provide additional product information beyond the required properties, your content may receive additional visual enhancements, helping your content to stand out in search results. See Structured data type definitions for all required and recommended product information.

    Search result enhancements are shown at the discretion of each experience, and may change over time. For this reason, it is recommended to provide as much rich product information as available, without concern for the exact experiences that will use it. Here are some examples of how merchant listing experiences may be enhanced:

    Ratings: Enhance the appearance of your search result by providing customer reviews and ratings.
    Pros and Cons: Identify pros and cons in your product review description so they can be highlighted in search results.
    \nShipping: Share shipping costs, especially free shipping, so shoppers understand the total cost.
    Availability: Provide availability data to help customers know when you currently have a product in stock.
    Price drop: Price drops are computed by Google by observing price changes for the product over time. Price drops are not guaranteed to be shown.

    SALES BILLING:
    Billing Document means an electronic and/or hardcopy document such a proforma invoice, sales invoice, purchase receipt, or other document issued by Provider, which indicates the items, quantities, and prices for the items to be provided to Subscriber
    the duration of the Subscription Term. The term “Billing Period” means the minimum time interval within the Subscription Term, as specified on the Billing Document, for which the Subscription Fee is prepaid on a recurring basis for the duration of the Subscription Term.
    The term “Data” means the characters and symbols contained in the Library in digital form.
    The Data serve to display and reproduce the Information. The term “Information” means any documented information resource intended to be accessible to a broad range of consumers. The term “Library” means a periodic publication consisting of a set of Data, which may be published in a variety of editions, each of which is distinctively identified by a title and other designating attributes such as a product number or locator code.
    The Library serves solely as the technical means of transferring Information from Provider to Subscriber.
    As used in this Agreement and any Supplementary Agreements, the term “Library” refers to any specific edition of the Library for which Subscriber has acquired the Library End-User License. This Agreement covers any and all such Libraries. The term “Library End-User License Agreement” (or “Library End-User License”)
    means a license agreement that permits Subscriber to designate Authorized Users, up to the maximum number indicated on the Billing Document,
    who are granted permission to use the Library under the terms and conditions stipulated in the corresponding license agreement.
    The term “License” means the documented permission granted by the Licensor to Licensee (whether free of charge or in exchange for a License Fee, as determined by the Licensor) to install and use the specific item listed on the Billing Document. The provisions of a License are documented in a license agreement, such as the Library End-User License Agreement and User Software licenses.
    The terms “Licensor” and “Licensee” shall have the meaning as defined in the appropriate.

    IVOICE:
     A Invoice at Topbrandsforyou.com. Find Make A Invoice. Now with us! Awesome Info. Find it Here. Search Now. Updated Info. Relevant Results. Get Latest Info. Attractive Results. Latest Today. Fast Response. More Info.
     Services: Answers, Information, Social, Related Searches.

    REPORT:
    The 2022 report of the Lancet Countdown is published as the world confronts profound and concurrent systemic shocks. Countries and health systems continue to contend with the health, social,
    economic impacts of the COVID-19 pandemic, while Russia's invasion of Ukraine and a persistent fossil fuel overdependence has pushed the world into global energy and cost-of-living crises.
    As these crises unfold, climate change escalates unabated.
    Its worsening impacts are increasingly affecting the foundations of human health and wellbeing, exacerbating the vulnerability of the world's populations to concurrent health threats.
    During 2021 and 2022, extreme weather events caused devastation across every continent, adding further pressure to health services already grappling with the impacts of the COVID-19 pandemic.''')







def action1():

    def submit():
            if  uid.get()=="" or csname.get()=="" or dob.get()=="" or exp.get()=="" or md.get()==""  :
                          messagebox.showerror("Error" , "All Fields Are Required" , parent = winsignup)
            else:
                    con = pymysql.connect(host="localhost",user="root",password="",database="gst")
                    cur = con.cursor()
                    cur.execute("insert into billing values(%s,%s,%s,%s,%s)",

                                (
                                    uid.get(),
                                    csname.get(),
                                    dob.get(),
                                    exp.get(),
                                    md.get()
                                    ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success" , " Successfull SAved" , parent = winsignup)
    


        


    winsignup = Tk()
    label_text=StringVar()
    label1_text=StringVar()
    winsignup.title("DataBase Connection")
    winsignup.maxsize(width=800 ,  height=500)
    winsignup.minsize(width=800 ,  height=500)
    winsignup['bg']='pink'
    scroll=Scrollbar(winsignup, orient=VERTICAL)

    heading = Label(winsignup , text = "GST BILLING:CUSTOMER ADD" , font = 'Verdana 20 bold')
    heading.place(x=100 , y=20)

    margin=Label(winsignup,bg='white',width='2000',height='3')
    margin.place(x=0,y=70)

    btn = Button(winsignup, text = "CUSTOMER ADD",bg="yellow",font='Verdana 7 bold')
    btn.place(x=60, y=80)
    btn = Button(winsignup, text = "PRODUCT ADD",bg="yellow",font='Verdana 7 bold',command=action3)
    btn.place(x=160, y=80)
    btn = Button(winsignup, text = "SALES BILLING",bg="yellow",font='Verdana 7 bold',command=action2)
    btn.place(x=260, y=80)
    btn = Button(winsignup, text = "REPORT",bg="yellow",font='Verdana 7 bold',command=action4)
    btn.place(x=460, y=80)

	 
    uid= Label(winsignup, text= "upolad CUST id :" ,bg="green",fg="white", font='Verdana 10 bold')
    uid.place(x=170,y=130)

    prname = Label(winsignup, text= "CUSTOMERNAME :" ,bg="green",fg="white", font='Verdana 10 bold')
    prname.place(x=170,y=160)

    dob= Label(winsignup, text= "D O B:" , bg="green",fg="white",font='Verdana 10 bold')
    dob.place(x=170,y=190)

    exp= Label(winsignup, text= "EXPERIENCE:" , bg="green",fg="white",font='Verdana 10 bold')
    exp.place(x=170,y=220)

    md= Label(winsignup, text= "MORE DETAILS:" , bg="green",fg="white",font='Verdana 10 bold')
    md.place(x=170,y=255)


    uid= Entry(winsignup,text="",textvariable =uid)
    uid.place(x=420,y=130)
            
    csname= Entry(winsignup, text= "",textvariable =prname)
    csname.place(x=420,y=160)
            
    dob= Entry(winsignup,text="",textvariable =dob)
    dob.place(x=420,y=190)
            
    exp=Entry(winsignup,textvariable =exp)
    exp.place(x=420,y=220)
            
    md= Entry(winsignup,textvariable =md,font='20')
    md.place(x=420, y=255)

    btn_signup = Button(winsignup, text = "SUMBIT",bg='yellow' ,font='Verdana 10 bold',command=submit)
    btn_signup.place(x=320,y=300)


def action2():

    def sign():
            if  ino.get()=="" or ci.get()=="" or name.get()=="" or date.get()=="" or address.get()=="" or ph.get()=="" or pid.get()=="" or na.get()=="" or qty.get()=="" or tot.get()=="" or gst.get()=="" or dis.get()=="" or net.get()=="" :
                          messagebox.showerror("Error" , "All Fields Are Required" , parent = winsignup)
            else:
                    con = pymysql.connect(host="localhost",user="root",password="",database="gst")
                    cur = con.cursor()
                    cur.execute("insert into sales values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",

                                (
                                    ino.get(),
                                    ci.get(),
                                    name.get(),
                                    date.get(),
                                    address.get(),
                                    ph.get(),
                                    pid.get(),
                                    na.get(),
                                    qty.get(),
                                    tot.get(),
                                    gst.get(),
                                    dis.get(),
                                    net.get()                                
                                    ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success" , " Successfull SAved" , parent = winsignup)
    



        


    winsignup = Tk()
    label_text=StringVar()
    label1_text=StringVar()
    winsignup.title("DataBase Connection")
    winsignup.maxsize(width=800 ,  height=700)
    winsignup.minsize(width=800 ,  height=700)
    winsignup['bg']='skyblue'
    scroll=Scrollbar(winsignup, orient=VERTICAL)

    heading = Label(winsignup , text = "GST BILIING:SALES BILLING" ,foreground="Blue", font = 'Verdana 20 bold')
    heading.place(x=150 , y=20)

    margin=Label(winsignup,bg='white',width='2000')
    margin.place(x=0,y=80)

    btn = Button(winsignup, text = "CUSTOMER ADD" ,bg="yellow",font='Verdana 7 bold',command=action1)
    btn.place(x=60, y=80)
    btn = Button(winsignup, text = "PRODUCT ADD" ,bg="yellow",font='Verdana 7 bold',command=action3)
    btn.place(x=160, y=80)
    btn = Button(winsignup, text = "SALES BILLING" ,bg="yellow",font='Verdana 7 bold')
    btn.place(x=260, y=80)
    btn = Button(winsignup, text = "REPORT" ,bg="yellow",font='Verdana 7 bold',command=action4)
    btn.place(x=460, y=80)



    
 
    ino= Label(winsignup, text= "INVOICE NUMBER:" ,bg="green",fg="white", font='Verdana 10 bold')
    ino.place(x=50,y=130)

    ci = Label(winsignup, text= "CUSTOMER ID :" ,bg="green",fg="white", font='Verdana 10 bold')
    ci.place(x=50,y=160)

    name= Label(winsignup, text= "NAME:" , bg="green",fg="white",font='Verdana 10 bold')
    name.place(x=50,y=190)

    date= Label(winsignup, text= "DATE:" , bg="green",fg="white",font='Verdana 10 bold')
    date.place(x=370,y=130)

    address= Label(winsignup, text= "ADDRESS:" , bg="green",fg="white",font='Verdana 10 bold')
    address.place(x=370,y=160)

    ph= Label(winsignup, text= "PHONE:" , bg="green",fg="white",font='Verdana 10 bold')
    ph.place(x=370,y=190)

    pid = Label(winsignup, text= "PRODUCT ID:" ,bg="green",fg="white", font='Verdana 10 bold')
    pid.place(x=170,y=320)

    na= Label(winsignup, text="NAME:" ,bg="green",fg="white", font='Verdana 10 bold')
    na.place(x=170,y=350)
    
    qty = Label(winsignup, text= "QULAITY:" , bg="green",fg="white",font='Verdana 10 bold')
    qty.place(x=170,y=380)

    tot=Label(winsignup,text="TOTAL:",bg="green",fg="white",font='Verdana 10 bold')
    tot.place(x=170,y=410)

    gst=Label(winsignup,text="GST:",bg="green",fg="white",font='Verdana 10 bold')
    gst.place(x=170,y=440)

    dis=Label(winsignup,text="DISCOUNT:",bg="green",fg="white",font='Verdana 10 bold')
    dis.place(x=170,y=470)

    net=Label(winsignup,text="NET:",bg="green",fg="white",font='Verdana 10 bold')
    net.place(x=170,y=500)

  
    ino= Entry(winsignup,text="",textvariable =ino)	
    ino.place(x=200,y=130)
            
    ci= Entry(winsignup, text= "",textvariable =ci)
    ci.place(x=200,y=160)
            
    name= Entry(winsignup,text="",textvariable =name)
    name.place(x=200,y=190)
            
    date=Entry(winsignup,textvariable =date)
    date.place(x=520,y=130)
            
    address= Entry(winsignup,textvariable =address)
    address.place(x=520, y=160)
            
    ph= Entry(winsignup,textvariable =ph)
    ph.place(x=520,y=190)
            
    pid= Entry(winsignup,textvariable =pid)
    pid.place(x=420 , y=320)
            
    na= Entry(winsignup,textvariable =na)
    na.place(x=420 , y=350)
            
    qty=Entry(winsignup,textvariable =qty)
    qty.place(x=420 , y=380)
            
    tot= Entry(winsignup,textvariable =tot)
    tot.place(x=420 , y=410)
            
    gst= Entry(winsignup,textvariable =gst)
    gst.place(x=420 , y=440)
            
    dis= Entry(winsignup,textvariable =dis)
    dis.place(x=420 , y=470)

    net= Entry(winsignup,textvariable =net)
    net.place(x=420 , y=500)
    
    btn_signup = Button(winsignup, text = "SUMBIT",bg='yellow' ,font='Verdana 10 bold',command=sign)
    btn_signup.place(x=380,y=570)


def action3():

    def submit1():
            if  uid.get()=="" or prname.get()=="" or pr.get()=="" or qty.get()=="" or md.get()==""  :
                          messagebox.showerror("Error" , "All Fields Are Required" , parent = winsignup)
            else:
                    con = pymysql.connect(host="localhost",user="root",password="",database="gst")
                    cur = con.cursor()
                    cur.execute("insert into billing values(%s,%s,%s,%s,%s)",

                                (
                                    uid.get(),
                                    prname.get(),
                                    pr.get(),
                                    qty.get(),
                                    md.get()
                                    ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success" , " Successfull SAved" , parent = winsignup)
    


        


    winsignup = Tk()
    label_text=StringVar()
    label1_text=StringVar()
    winsignup.title("DataBase Connection")
    winsignup.maxsize(width=800 ,  height=500)
    winsignup.minsize(width=800 ,  height=500)
    winsignup['bg']='orange'
    scroll=Scrollbar(winsignup, orient=VERTICAL)

    heading = Label(winsignup , text = "GST BILLING:PRODUCT ADD" , font = 'Verdana 20 bold')
    heading.place(x=100 , y=20)

    margin=Label(winsignup,bg='white',width='2000',height='3')
    margin.place(x=0,y=70)

    btn = Button(winsignup, text = "CUSTOMER ADD",bg="yellow",font='Verdana 7 bold',command=action1)
    btn.place(x=60, y=80)
    btn = Button(winsignup, text = "PRODUCT ADD",bg="yellow",font='Verdana 7 bold')
    btn.place(x=160, y=80)
    btn = Button(winsignup, text = "SALES BILLING",bg="yellow",font='Verdana 7 bold',command=action2)
    btn.place(x=260, y=80)
    btn = Button(winsignup, text = "REPORT",bg="yellow",font='Verdana 7 bold',command=action4)
    btn.place(x=460, y=80)

	 
    uid= Label(winsignup, text= "PRODUCT id :" ,bg="green",fg="white", font='Verdana 10 bold')
    uid.place(x=170,y=130)

    prname = Label(winsignup, text= "PRODUCTNAME :" ,bg="green",fg="white", font='Verdana 10 bold')
    prname.place(x=170,y=160)

    pr= Label(winsignup, text= "PRICE:" , bg="green",fg="white",font='Verdana 10 bold')
    pr.place(x=170,y=190)

    qty= Label(winsignup, text= "QUANTITY:" , bg="green",fg="white",font='Verdana 10 bold')
    qty.place(x=170,y=220)

    md= Label(winsignup, text= "MORE DETAILS:" , bg="green",fg="white",font='Verdana 10 bold')
    md.place(x=170,y=255)


    uid= Entry(winsignup,text="",textvariable =uid)
    uid.place(x=420,y=130)
            
    prname= Entry(winsignup, text= "",textvariable =prname)
    prname.place(x=420,y=160)
            
    pr= Entry(winsignup,text="",textvariable =pr)
    pr.place(x=420,y=190)
            
    qty=Entry(winsignup,textvariable =qty)
    qty.place(x=420,y=220)
            
    md= Entry(winsignup,textvariable =md,font='20')
    md.place(x=420, y=255)

    btn_signup = Button(winsignup, text = "SUMBIT",bg='yellow' ,font='Verdana 10 bold',command=submit1)
    btn_signup.place(x=320,y=300)



def action4():

    def submit2():
            if  uid.get()=="" or prname.get()=="" or rd.get()==""  :
                          messagebox.showerror("Error" , "All Fields Are Required" , parent = winsignup)
            else:
                    con = pymysql.connect(host="localhost",user="root",password="",database="gst")
                    cur = con.cursor()
                    cur.execute("insert into billing values(%s,%s,%s)",

                                (
                                    uid.get(),
                                    prname.get(),
                                    rd.get()
                                    ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success" , " Successfull SAved" , parent = winsignup)
    


        


    winsignup = Tk()
    label_text=StringVar()
    label1_text=StringVar()
    winsignup.title("DataBase Connection")
    winsignup.maxsize(width=800 ,  height=500)
    winsignup.minsize(width=800 ,  height=500)
    winsignup['bg']='red'
    scroll=Scrollbar(winsignup, orient=VERTICAL)

    heading = Label(winsignup , text = "GST BILLING:REPORT" , font = 'Verdana 20 bold')
    heading.place(x=100 , y=20)

    margin=Label(winsignup,bg='white',width='2000',height='3')
    margin.place(x=0,y=70)

    btn = Button(winsignup, text = "CUSTOMER ADD",bg="yellow",font='Verdana 7 bold',command=action1)
    btn.place(x=60, y=80)
    btn = Button(winsignup, text = "PRODUCT ADD",bg="yellow",font='Verdana 7 bold',command=action3)
    btn.place(x=160, y=80)
    btn = Button(winsignup, text = "SALES BILLING",bg="yellow",font='Verdana 7 bold',command=action2)
    btn.place(x=260, y=80)
    
    btn = Button(winsignup, text = "REPORT",bg="yellow",font='Verdana 7 bold')
    btn.place(x=460, y=80)

	 
    uid= Label(winsignup, text= "PRODUCT id :" ,bg="green",fg="white", font='Verdana 10 bold')
    uid.place(x=170,y=130)

    prname = Label(winsignup, text= "PRODUCTNAME :" ,bg="green",fg="white", font='Verdana 10 bold')
    prname.place(x=170,y=160)


    rd= Label(winsignup, text= "REPORT DETAILS:" , bg="green",fg="white",font='Verdana 10 bold')
    rd.place(x=170,y=255)


    uid= Entry(winsignup,text="",textvariable =uid)
    uid.place(x=420,y=130)
            
    prname= Entry(winsignup, text= "",textvariable =prname)
    prname.place(x=420,y=160)
            
            
    rd= Entry(winsignup,textvariable =rd,font='20')
    rd.place(x=420, y=255)

    btn_signup = Button(winsignup, text = "SUMBIT",bg='yellow' ,font='Verdana 10 bold',command=submit2)
    btn_signup.place(x=320,y=300)





winsignup = Tk()
label_text=StringVar()
label1_text=StringVar()
winsignup.title("DataBase Connection")
winsignup.maxsize(width=800 ,  height=500)
winsignup.minsize(width=800 ,  height=500)
winsignup['bg']='white'
scroll=Scrollbar(winsignup, orient=VERTICAL)


             
		 
login = Label(winsignup, text= "ADMIN LOGIN " ,fg="blue", font='Verdana 20 bold')
login.place(x=270,y=110)

usname= Label(winsignup, text= "USER NAME :" ,bg="green",fg="white",font='Verdana 10 bold')
usname.place(x=170,y=200)


password= Label(winsignup, text= "PASSWORD:" , bg="green",fg="white",font='Verdana 10 bold')
password.place(x=170,y=250)




usname= Entry(winsignup,text="")
usname.place(x=420,y=200)


password= Entry(winsignup,show='*', width=20)
password.place(x=420 , y=250)

def show_hide():
    if c['text']=='show':
        password.config(show='')
        c.config(text='hide')
    else:
        password.config(show='*')
        c.config(text='show')

    
c=Button(winsignup,text="show",command=show_hide,bg='red',fg='white')
c.place(x=580,y=250)


btn_signup = Button(winsignup, text = "Next Page" ,bg="yellow",font='Verdana 15 bold',command=action)
btn_signup.place(x=500, y=300)

def lg():
        if  usname.get()=="" or password.get()==""  :
                          messagebox.showerror("Error" , "All Fields Are Required" , parent = winsignup)
        else:
                    con = pymysql.connect(host="localhost",user="root",password="",database="gst")
                    cur = con.cursor()
                    cur.execute("insert into billing values(%s,%s,%s,%s,%s)",

                                (
                                    usname.get(),
                                    password.get()
                                    ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success" , " Successfull SAved" , parent = winsignup)


btn_signup = Button(winsignup, text = "Submit" ,bg="yellow",font='Verdana 15 bold',command=lg)
btn_signup.place(x=300, y=300)  
    


        


    
		
