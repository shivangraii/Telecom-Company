    #                       IMPORTED MODULES



import random
import pickle
import time
import datetime



#                      DEFINED FUNCTIONS



#1 Function to get a NEW SIM    
def new_sim():
    
    print('\nHi User\n')
    
    sim_type=int(input('Want a Prepaid Sim Enter 1.\nFor a Postpaid Sim Enter 2 : '))
    
    
    
    #PREPAID PROGRAM for NEW SIM
    if sim_type==1:
    
        pre_cust={}
    
        
        cust_id = random.randint(100,999)
        pre_cust['User ID']=cust_id
        
        cust_name=input('\nEnter Name: ')
        pre_cust['Name']=cust_name
        
        cust_number = random.randint(6000000000, 7999999999)
        pre_cust['Phone Number']=cust_number
        
        pre_cust['Number Type']='PRE-PAID'
    
        
        cust_plan=[]
        print('\n\nChoose a plan ')
        print('\nPlans are as Follows:')
        time.sleep(3)
        print('\n 1. BRONZE\n1 GB DATA\Per Day\nUNLIMITED Voice & SMS\nSTD only\nValidity:30 Days\nRs.179')
        time.sleep(2)
        print('\n 2. SILVER\n2 GB DATA\Per Day\nUNLIMITED Voice & SMS\nSTD only\nValidity:30 Days\nRs.249')
        time.sleep(2)
        print('\n 3. GOLD\n5 GB DATA\Per Day\nUNLIMITED Voice & SMS\nSTD only\nValidity:30 Days\nRs.349')
        time.sleep(2)
        print('\n 4. GOLD+\n6 GB DATA\Per Day\nUNLIMITED Voice & SMS\nSTD & ISD\nValidity:30 Days\nRs.579')
        time.sleep(2)
        print('\n 5. PLATINUM\n10 GB DATA\Per Day\nUNLIMITED Voice & SMS\nSTD & ISD\nValidity:30 Days\nRs.949')
        time.sleep(2)
        
        while 1:
            plan_type=int(input('Enter Preferred Choice:'))
            if plan_type==1:
                cust_plan='BRONZE'
                break
            elif plan_type==2:
                cust_plan='SILVER'
                break
            elif plan_type==3:
                cust_plan='GOLD'
                break
            elif plan_type==4:
                cust_plan='GOLD+'
                break
            elif plan_type==5:
                cust_plan='PLATINUM'
                break
            else:
                print('Invalid Entry')
        pre_cust['Plan Type']=cust_plan
        
        print('Enter Date of Birth')
        while 1:
            y=int(input('\nEnter Year: '))
            if y>1950 and y<2019:
                year=y
                break
            else:
                print("\nRE-ENTER\nYou dont look that OLD !")
        
        while 1:
            m=int(input('Enter Month: '))
            if m>=1 and m<=12:
                month=m
                break
            else:
                print('\nEnter Valid month !')
        
        while 1:
            if m==(1,3,5,7,8,10,12):
                d=int(input('Enter the Date: '))
                if d>=1 and d<=31:
                    date=d
                    break
                else:
                    print('\nEnter date According to month')
            elif m==2:
                if y%4==0:
                    d=int(input('Enter the Date: '))
                    if d>=1 and d<=29:
                        date=d
                        break
                    else:
                        print('\nEnter date According to month')
                else:
                    d=int(input('Enter the Date: '))
                    if d>=1 and d<=28:
                        date=d
                        break
                    else:
                        print('\nEnter date According to month')
            else:
                d=int(input('Enter the Date: '))
                if d>=1 and d<=30:
                    date=d
                    break
                else:
                    print('\nEnter date According to month')
        cust_dob=[date,month,year]
        pre_cust['D.O.B.']=cust_dob
        
        while 1:
            cust_aadha=int(input('Enter Aadhar ID: '))
            cust_aadhar=str(cust_aadha)
            if len(cust_aadhar)==12:
                pre_cust['Aadhar ID']=cust_aadhar
                break
            else:
                print('\nRe-Enter\n12 DIGIT NUMBER ONLY !')
        
        cust_address=input('Enter Address: ')
        pre_cust['Address']=cust_address
        
        cust_mail=input('Enter E-mail ID: ')
        pre_cust['Mail ID']=cust_mail
        
        CurrentDate=datetime.datetime.now()
        pre_cust['Account Created on']=CurrentDate
    
        
        print("\nGathering Information...\nGenerating New Number")
        print("Please wait for 5 seconds")
        time.sleep(5)
        print("\nYour Customer ID is: ")
        print(cust_id)
        print("\nYour New Phone Number is: ")
        print(cust_number)
        time.sleep(5)
        
        
        cust_acc_file=open('customer.dat','ab')
        pickle.dump(pre_cust,cust_acc_file)
        cust_acc_file.close()
        
        
        print('\nYour NEW PHONE NUMBER will be activated within 4 Hours')
        print('\n\nRedirecting to Main Menu...')
        time.sleep(5)
        
        
        
    #POSTPAID PROGRAM for NEW SIM
    elif sim_type==2:
        
        post_cust={}
    
        
        cust_id = random.randint(1000,9999)
        post_cust['User ID']=cust_id
        
        cust_name=input('\nEnter Name: ')
        post_cust['Name']=cust_name
        
        cust_number = random.randint(8000000000, 9999999999)
        post_cust['Phone Number']=cust_number
        
        post_cust['Number Type']='POST-PAID'
        
        
        cust_plan=[]
        print('\n\n To get a new Phone Number, You have to choose a plan which matches your needs')
        print('\nPlans are as Follows:')
        time.sleep(3)
        print('\n 1. BRONZE\n75 GB DATA\nUNLIMITED Voice & SMS\nSTD only\nValidity:30 Days\n200 GB Roll-Over DATA\nRs.299')
        time.sleep(2)
        print('\n 2. SILVER\n100 GB DATA\nUNLIMITED Voice & SMS\nSTD only\nValidity:30 Days\n200 GB Roll-Over DATA\nRs.399')
        time.sleep(2)
        print('\n 3. GOLD\n150 GB DATA\nUNLIMITED Voice & SMS\nSTD only\nValidity:30 Days\n200 GB Roll-Over DATA\nRs.599')
        time.sleep(2)
        print('\n 4. GOLD+\n200 GB DATA\nUNLIMITED Voice & SMS\nSTD & ISD\nValidity:30 Days\n400 GB Roll-Over DATA\nRs.799')
        time.sleep(2)
        print('\n 5. PLATINUM\n300 GB DATA\nUNLIMITED Voice & SMS\nSTD & ISD\nValidity:30 Days\n500 GB Roll-Over DATA\nRs.999')
        time.sleep(2)
 
        
        while 1:
            plan_type=int(input('Enter Preferred Choice:'))
            if plan_type==1:
                cust_plan='BRONZE'
                break
            elif plan_type==2:
                cust_plan='SILVER'
                break
            elif plan_type==3:
                cust_plan='GOLD'
                break
            elif plan_type==4:
                cust_plan='GOLD+'
                break
            elif plan_type==5:
                cust_plan='PLATINUM'
                break
            else:
                print('Invalid Entry')
        post_cust['Plan Type']=cust_plan
        
        print('Enter Date of Birth')
        while 1:
            y=int(input('\nEnter Year: '))
            if y<2019 and y>1950:
                year=y
                break
            else:
                print("\nRE-ENTER\nYou dont look that OLD !")
        
        while 1:
            m=int(input('Enter Month: '))
            if m<=12 and m>=1:
                month=m
                break
            else:
                print('\nEnter Valid month !')
        
        while 1:
            if m in (1,3,5,7,8,10,12):
                d=int(input('Enter the Date: '))
                if d>=1 and d<=31:
                    date=d
                    break
            elif m==2:
                if y%4==0:
                    d=int(input('Enter the Date: '))
                    if d>=1 and d<=29:
                        date=d
                        break
                    else:
                        print('\nRe-Enter date according to month')
                else:
                    d=int(input('Enter the Date: '))
                    if d>=1 and d<=28:
                        date=d
                        break
                    else:
                        print('\nRe-Enter date according to month')
            elif m in (4,6,9,11): 
                d=int(input('Enter the Date: '))
                if d>=1 and d<=30:
                    date=d
                    break
            else:
                print('\nRe-Enter date according to month')
        cust_dob=[date,month,year]
        post_cust['D.O.B.']=cust_dob
        
        while 1:
            cust_aadha=int(input('Enter Aadhar ID: '))
            cust_aadhar=str(cust_aadha)
            if len(cust_aadhar)==12:
                post_cust['Aadhar ID']=cust_aadhar
                break
            else:
                print('\nRe-Enter\n12 DIGIT NUMBER ONLY !')
        
        cust_address=input('Enter Address: ')
        post_cust['Address']=cust_address
        
        cust_mail=input('Enter E-mail ID: ')
        post_cust['Mail ID']=cust_mail
        
        CurrentDate=datetime.datetime.now()
        post_cust['Account Created on']=CurrentDate
        
    
        print("\nGathering Information...\nGenerating New Number")
        print("Please wait for 5 seconds")
        time.sleep(5)
        print("\nYour Customer ID is: ")
        print(cust_id)
        print("\nYour New Phone Number is: ")
        print(cust_number)
        time.sleep(5)
        
        
        cust_acc_file=open('customer.dat','ab')
        pickle.dump(post_cust,cust_acc_file)
        cust_acc_file.close()
        
        
        print('\nYour NEW PHONE NUMBER will be activated within 4 Hours')
        print('\n\nRedirecting to Main Menu...')
        time.sleep(5)
        
    else:
        print("\nInvalid Entry...\n")
        print('\n\nRedirecting to Main Menu...')
        time.sleep(2)
        
        
        
        
#2 Function to CHECK BALANCE and ACCOUNT DETAILS
def chk_det():
    
    file=open('customer.dat','rb')
    cust_id = int(input("ENTER USER ID : "))
    
    try:
        while True:
            data=pickle.load(file)
            if data['User ID']==cust_id :
                print('Your Details are as Follows: ')
                for i in data:
                    print(i,':',data[i])
                time.sleep(10)
                print('\n\nRedirecting to Main Menu')
                time.sleep(5)
            
            
            if cust_id==18:
                print(data)
    
            
    except EOFError:
        print('\n\nRedirecting to Main Menu')
        time.sleep(5)
    
    
    
#3 Function to Discover Various Prepaid and Postpaid Programs
def disc_plan():
    
    
    type=int(input('\nWhich Type of Plan you want to Discover ?\nFor Prepaid Press 1 and 2 for Postpaid:'))
    
    if type==1:
        print('\nPRE-PAID PLANS ARE AS FOLLOWS:')
        print('\n 1. BRONZE\n1 GB DATA\Per Day\nUNLIMITED Voice & SMS\nSTD only\nValidity:30 Days\nRs.179')
        time.sleep(2)
        print('\n 2. SILVER\n2 GB DATA\Per Day\nUNLIMITED Voice & SMS\nSTD only\nValidity:30 Days\nRs.249')
        time.sleep(2)
        print('\n 3. GOLD\n5 GB DATA\Per Day\nUNLIMITED Voice & SMS\nSTD only\nValidity:30 Days\nRs.349')
        time.sleep(2)
        print('\n 4. GOLD+\n6 GB DATA\Per Day\nUNLIMITED Voice & SMS\nSTD & ISD\nValidity:30 Days\nRs.579')
        time.sleep(2)
        print('\n 5. PLATINUM\n10 GB DATA\Per Day\nUNLIMITED Voice & SMS\nSTD & ISD\nValidity:30 Days\nRs.949')
        time.sleep(4)
        print('\n\nRedirecting to Main Menu')
        time.sleep(5)
    
    
    elif type==2:
        print('\nPOST-PAID PLANS ARE AS FOLLOWS:')
        print('\n 1. BRONZE\n75 GB DATA\nUNLIMITED Voice & SMS\nSTD only\nValidity:30 Days\n200 GB Roll-Over DATA\nRs.299')
        time.sleep(2)
        print('\n 2. SILVER\n100 GB DATA\nUNLIMITED Voice & SMS\nSTD only\nValidity:30 Days\n200 GB Roll-Over DATA\nRs.399')
        time.sleep(2)
        print('\n 3. GOLD\n150 GB DATA\nUNLIMITED Voice & SMS\nSTD only\nValidity:30 Days\n200 GB Roll-Over DATA\nRs.599')
        time.sleep(2)
        print('\n 4. GOLD+\n200 GB DATA\nUNLIMITED Voice & SMS\nSTD & ISD\nValidity:30 Days\n400 GB Roll-Over DATA\nRs.799')
        time.sleep(2)
        print('\n 5. PLATINUM\n300 GB DATA\nUNLIMITED Voice & SMS\nSTD & ISD\nValidity:30 Days\n500 GB Roll-Over DATA\nRs.999')
        time.sleep(4)
        print('\n\nRedirecting to Main Menu')
        time.sleep(5)
    
    
    else:
        print('\nInvalid Input')
        print('\nRedirecting to Main Menu')
        time.sleep(5)
        
        
    
#4 Function to Recharge/Pay
def rec_pay():
    
    
    file1=open('customer.dat','rb')
    file2=open('temp.dat','wb')
    cust_id = int(input("ENTER USER ID :"))
    
    
    try:
        while True:
            data=pickle.load(file1)
            
            if data['User ID']==cust_id :
                
                type=int(input('\n1 for Prepaid and 2 for Postpaid\n'))
                
                if type==1:
                    print('\nPre-Paid Plans are as Follows:')
                    time.sleep(3)
                    print('\n 1. BRONZE\n1 GB DATA\Per Day\nUNLIMITED Voice & SMS\nSTD only\nValidity:30 Days\nRs.179')
                    time.sleep(2)
                    print('\n 2. SILVER\n2 GB DATA\Per Day\nUNLIMITED Voice & SMS\nSTD only\nValidity:30 Days\nRs.249')
                    time.sleep(2)
                    print('\n 3. GOLD\n5 GB DATA\Per Day\nUNLIMITED Voice & SMS\nSTD only\nValidity:30 Days\nRs.349')
                    time.sleep(2)
                    print('\n 4. GOLD+\n6 GB DATA\Per Day\nUNLIMITED Voice & SMS\nSTD & ISD\nValidity:30 Days\nRs.579')
                    time.sleep(2)
                    print('\n 5. PLATINUM\n10 GB DATA\Per Day\nUNLIMITED Voice & SMS\nSTD & ISD\nValidity:30 Days\nRs.949')
                    time.sleep(2)
                    
                    while 1:
                        
                        plan_type=int(input('Enter Preferred Choice:'))
                        
                        if plan_type==1:
                            data.update({'Plan Type':'BRONZE'})
                            pickle.dump(data,file2)
                            print('Recharged')
                            time.sleep(4)
                            break
                        elif plan_type==2:
                            data.update({'Plan Type':'SILVER'})
                            pickle.dump(data,file2)
                            print('Recharged')
                            time.sleep(4)
                            break
                        elif plan_type==3:
                            data.update({'Plan Type':'GOLD'})
                            pickle.dump(data,file2)
                            print('Recharged')
                            time.sleep(4)
                            break
                        elif plan_type==4:
                            data.update({'Plan Type':'GOLD+'})
                            pickle.dump(data,file2)
                            print('Recharged')
                            time.sleep(4)
                            break
                        elif plan_type==5:
                            data.update({'Plan Type':'PLATINUM'})
                            pickle.dump(data,file2)
                            print('Recharged')
                            time.sleep(4)
                            break
                        else:
                            print('Invalid Entry')
                    
                    
                elif type==2:
                    print('\nPost-Paid Plans are as Follows:')
                    time.sleep(3)
                    print('\n 1. BRONZE\n75 GB DATA\nUNLIMITED Voice & SMS\nSTD only\nValidity:30 Days\n200 GB Roll-Over DATA\nRs.299')
                    time.sleep(2)
                    print('\n 2. SILVER\n100 GB DATA\nUNLIMITED Voice & SMS\nSTD only\nValidity:30 Days\n200 GB Roll-Over DATA\nRs.399')
                    time.sleep(2)
                    print('\n 3. GOLD\n150 GB DATA\nUNLIMITED Voice & SMS\nSTD only\nValidity:30 Days\n200 GB Roll-Over DATA\nRs.599')
                    time.sleep(2)
                    print('\n 4. GOLD+\n200 GB DATA\nUNLIMITED Voice & SMS\nSTD & ISD\nValidity:30 Days\n400 GB Roll-Over DATA\nRs.799')
                    time.sleep(2)
                    print('\n 5. PLATINUM\n300 GB DATA\nUNLIMITED Voice & SMS\nSTD & ISD\nValidity:30 Days\n500 GB Roll-Over DATA\nRs.999')
                    time.sleep(2)
                    
                    while 1:
                        
                        plan_type=int(input('Enter Preferred Choice:'))
                        
                        if plan_type==1:
                            data.update({'Plan Type':'BRONZE'})
                            pickle.dump(data,file2)
                            print('Recharged')
                            time.sleep(4)
                            break
                        elif plan_type==2:
                            data.update({'Plan Type':'SILVER'})
                            pickle.dump(data,file2)
                            print('Recharged')
                            time.sleep(4)
                            break
                        elif plan_type==3:
                            data.update({'Plan Type':'GOLD'})
                            pickle.dump(data,file2)
                            print('Recharged')
                            time.sleep(4)
                            break
                        elif plan_type==4:
                            data.update({'Plan Type':'GOLD+'})
                            pickle.dump(data,file2)
                            print('Recharged')
                            time.sleep(4)
                            break
                        elif plan_type==5:
                            data.update({'Plan Type':'PLATINUM'})
                            pickle.dump(data,file2)
                            print('Recharged')
                            time.sleep(4)
                            break
                        else:
                            print('Invalid Entry')
                            
                        break
            
            else:
                pickle.dump(data,file2)
    
    except EOFError:
        pass
    
    file1.close()
    file2.close()
    
    
    file1=open('customer.dat','wb')
    file2=open('temp.dat','rb')
    
    try:
        while True:
            record=pickle.load(file2)
            pickle.dump(record,file1)
    except EOFError:
        pass
        



#5 Function to Change Various Details
def change_det():
    
    file1=open('customer.dat','rb')
    file2=open('temp.dat','wb')
    
    cust_id = int(input("ENTER USER ID :"))
    
    try:
        while True:
            data=pickle.load(file1)
            
            if data['User ID']==cust_id :
                print('\n1. Change Name')
                print('2. Change D.O.B.')
                print('3. Change Number Type')
                print('4. Update Email Address')
                print('5. Update Aadhar Number')
                print('6. Update Address')
                print('7. Exit')
                
                while 1:
                    menu=int(input('Enter Preferred Choice:'))
                    
                    if menu==1:
                        name=input('Enter Correct Name: ')
                        data.update({'Name':name})
                        pickle.dump(data,file2)
                        print('Updated')
                        time.sleep(4)
                        break
                    elif menu==2:
                        print('Enter Date of Birth')
                        while 1:
                            y=int(input('\nEnter Year: '))
                            if y<2019 and y>1950:
                                year=y
                                break
                            else:
                                print("\nRE-ENTER\nYou dont look that OLD !")
                        
                        while 1:
                            m=int(input('Enter Month: '))
                            if m<=12 and m>=1:
                                month=m
                                break
                            else:
                                print('\nEnter Valid month !')
                        
                        while 1:
                            if m==(1,3,5,7,8,10,12):
                                d=int(input('Enter the Date: '))
                                if d>=1 and d<=31:
                                    date=d
                                    break
                                else:
                                    print('\nEnter date According to month')
                            elif m==2:
                                if y%4==0:
                                    d=int(input('Enter the Date: '))
                                    if d>=1 and d<=29:
                                        date=d
                                        break
                                    else:
                                        print('\nEnter date According to month')
                                else:
                                    d=int(input('Enter the Date: '))
                                    if d>=1 and d<=28:
                                        date=d
                                        break
                                    else:
                                        print('\nEnter date According to month')
                            else:
                                d=int(input('Enter the Date: '))
                                if d>=1 and d<=30:
                                    date=d
                                    break
                                else:
                                    print('\nEnter date According to month')
                        cust_dob=[date,month,year]
                        data.update({'D.O.B.':cust_dob})
                        pickle.dump(data,file2)
                        print('Updated')
                        time.sleep(4)
                        break
                    elif menu==3:
                        print('\nTo Change From PRE-PAID to POST-PAID press 1')
                        print('For POST-PAID to PRE-PAID press 2')
                        
                        type=int(input('Enter :'))
                        
                        if type==1:
                            data.update({'Number Type':'POST-PAID'})
                            pickle.dump(data,file2)
                            print('Updated')
                        elif type==2:
                            data.update({'Number Type':'PRE-PAID'})
                            pickle.dump(data,file2)
                            print('Updated')
                        else:
                            print('Invalid Input')
                        time.sleep(4)
                        break
                    elif menu==4:
                        mail=input('Enter Email ID: ')
                        data.update({'Mail ID':mail})
                        pickle.dump(data,file2)
                        print('Updated')
                        time.sleep(4)
                        break
                    elif menu==5:
                        while 1:
                            cust_aadha=int(input('Enter Aadhar ID: '))
                            cust_aadhar=str(cust_aadha)
                            if len(cust_aadhar)==12:
                                cust_aadhar_new=cust_aadhar
                                break
                            else:
                                print('\nRe-Enter\n12 DIGIT NUMBER ONLY !')
                        data.update({'Aadhar ID':cust_aadhar_new})
                        pickle.dump(data,file2)
                        print('Updated')
                        time.sleep(4)
                        break
                    elif menu==6:
                        Address=input('Enter Address: ')
                        data.update({'Address':Address})
                        pickle.dump(data,file2)
                        print('Updated')
                        time.sleep(4)
                        break
                    elif menu==7:
                        pickle.dump(data,file2)
                        break
                    else:
                        print('Invalid Entry')
                        break 
            
            else:
                pickle.dump(data,file2)
    
    except EOFError:
        pass
    
    file1.close()
    file2.close()
    
    
    file1=open('customer.dat','wb')
    file2=open('temp.dat','rb')
    
    
    try:
        while True:
            record=pickle.load(file2)
            pickle.dump(record,file1)
    except EOFError:
        pass
    
    
    

#6 Function for Frequently asked Questions
def faq():
    
    while True:
        print('\n1. What documents do I need to buy a new Prepaid/Postpaid connection?')
        print('2. How long will it take to activate my new connection?')
        print('3. Do I have to pay any activation/delivery charges for buying a SIM card?')
        print('4. What are the additional benefits of a connection?')
        print('5. Quit\n')
        
        faq_choice=int(input('Enter Query No. '))
        
        if faq_choice == 1:
            print('You need original Proof of Identity (POI) and Proof of Address (POA) document such as Aadhaar, Voter ID, Passport, or Driving License.')
            print('In case you are porting your number from another operator, you would additionally need Unique Porting Code (UPC) for switching your connection.')
            print('\n\nRedirecting to Main Menu...')
            time.sleep(5)
        elif faq_choice ==2:
            print ('It usually takes a few hours, post sharing valid documents, for your new SIM to get activated.')
            print('\n\nRedirecting to Main Menu...')
            time.sleep(5)
        elif faq_choice ==3:
            print('Getting a SIM card is completely free. There are no charges for home delivery, no activation charges, and no security deposit.')   
            print('\n\nRedirecting to Main Menu...')
            time.sleep(5)
        elif faq_choice ==4:
            print("\nWith a connection you get multiple benefits, few are as follows:")
            print('1. Faster data speeds and better voice quality owing to pan India 4G network')
            print('2. Most value for money prepaid plans')
            print('3. Unlimited voice calls to anywhere in India and across any network')
            print('\n\nRedirecting to Main Menu...')
            time.sleep(5)
        elif faq_choice == 5:
            print('Redirecting to Main Menu...')
            time.sleep(5)
            break
        else :
            print('\n\nInvalid Entry')
            print('\n\nRedirecting to Main Menu...')
            time.sleep(2)
        
            

            
#7 Function for Help Centre
def help_centre():
    
    while True:
        print("\nNeed guidance?\nWe'd love to help you.\n")
        print('1. Need Helpline No.')
        print('2. Type your Query')
        print('3. Close your Account')
        print('4. Leave\n')
    
        
        cust_choice=int(input('Enter No. '))
    
            
        if cust_choice==1:
            print('\nOur experts are available for your assistance 24X7')
            print('ONLY REGISTERED NUMBERS CAN CALL!')
            print('Helpline No.     - 1800-108-1800')
            print('For Queries      - 299')
            print('For Comaplaints  - 399')
            print('For Int. support - 499')
            print('\nHELPLINE FOR NON-REGISTERED NUMBERS - 1800-009-1800')
            print('\n\nRedirecting to Main Menu...')
            time.sleep(5)
        elif cust_choice==2:
            n=input('Enter Name :')
            e=input('Enter Email : ')
            no=input('Enter Phone Number : ')
            q=input('Enter Query[in Not More than 50 words] - ')
            print('\nQuery Submitted Successfully')
            print("Our Representatives our working 24X7, they'll contact you shortly")
            print('\n\nRedirecting to Main Menu...')
            time.sleep(5)
        elif cust_choice==3:
            file1=open('customer.dat','rb')
            file2=open('temp.dat','wb')
            cust_od=int(input('\nEnter to Confirm User ID: '))
            cust_id=int(input('\nRe-Enter to Confirm User ID: '))
            
            try:
                while True:
                    data=pickle.load(file1)
                    if data['User ID']==cust_id:
                        print('Account Deleted Peramanently')
                    else:
                        pickle.dump(data, file2)
            except EOFError:
                file1.close()
                file2.close()

            file1=open('customer.dat','wb')
            file2=open('temp.dat','rb')
            
            try:
                while True:
                    record=pickle.load(file2)
                    pickle.dump(record,file1)
            except EOFError:
                pass
            
            print('\n\nRedirecting to Main Menu...')
            time.sleep(5)
        
        elif cust_choice==4:
            print('Redirecting to Main Menu...')
            time.sleep(5)
            break
        
        else :
            print('\n\nInvalid Entry\n')
            print('\n\nRedirecting to Main Menu...')
            time.sleep(2)

#                     FUNCTION PART ENDS...



#                       MAIN PROGRAM 



#                        MAIN MENU 



while True:
    
    print('\n\n            WELCOME TO TELECOM\n\n')
    
    Ent_choice=int(input('To Proceed Enter 1\nTo Quit Press 2: '))
    
    if Ent_choice==1:
    
        print('\n\n1. Get a New Sim Card')
        print('2. Check Details')
        print('3. Discover Plans')
        print('4. Recharge/Pay Bill')
        print('5. Edit Details')
        print('6. FAQ')
        print('7. Help Centre')
        print('8. Quit\n\n')
        
        menu_choice = int(input("Enter Preferred Choice : "))
        
        if menu_choice==1:
            new_sim()
        
        elif menu_choice== 2:
            chk_det()
        
        elif menu_choice== 3:
            disc_plan()
        
        elif menu_choice==4:
            rec_pay()
        
        elif menu_choice==5:
            change_det()
        
        elif menu_choice==6:
            faq()
        
        elif menu_choice==7:
            help_centre()
        
        elif menu_choice==8:
            print('Thanks for Using')
            break
        
        else :
            print('\n\nInvalid Entry\nRe-Enter from given Choices\n\n')
            time.sleep(3)
    
    
    else:
        print('\nYou left too Soon...')
        time.sleep(1)
        break
        
#                         MAIN PART ENDS...


#                           PROGRAM ENDED
