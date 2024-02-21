option=1

general_seats=23
ac_seats=11
price_of_each_G_seat = 100
price_of_each_AC_seat = 500
total_seats=general_seats+ac_seats
no_of_seats=0
del_seat=0
ticket_no=666666
users=[]
u=users
reg_users=0
y=[]
Gen_no=0
Ac_no=0
rest_seat=no_of_seats - del_seat

print("\n ====================================")
print(" ||   Welcome To Indian Railaway   ||")
print(" ====================================")


while True:
    print("================================")
    print("||  Press 1 for Book Seat     ||")
    print("||  Press 2 for Show Seat     ||")
    print("||  Press 3 for Delete Seat   ||")
    print("||  Press 4 for Show Tickets  ||")
    print("||  Press 5 for Exit          ||")
    print("================================")

    try:
        want=int(input("CHOOSE OPTION FROM ABOVE => "))
    except:
        print("\nYou have typed wrong number")
        print("Please type number between 1 to 4 for getting \"True\" information")
        continue


    if want==1:
        print("What type of seats you want to book")
        type=input("Press G for General & Press A for AC : ")

        if type=="A":
            print("\nThanks for choosing AC ")
            print("Available Seats in AC coach :",ac_seats)
            print("Price of each AC seat $ \b",price_of_each_AC_seat)
            print("How many seats you want to book ;")
    
            no_of_seats=int(input())
            for i in range(no_of_seats):
                name=str(input(f'\n{i+1} person Name : '))
                Age=int(input(f'{i+1} person Age : '))
                Gender=str(input(f'{i+1} person Gender : '))

                Ac_no+=1
                sno='A'+str(Ac_no)
                ticket_no+=1
                users.append([sno,ticket_no,name,Age,Gender])

            print("\n")

            for u in users:
                print(u)

            print("\n",no_of_seats," : seats have been booked")
            print("Total price of",no_of_seats,"seats is $","\b",no_of_seats*price_of_each_AC_seat)

            ac_seats = ac_seats-no_of_seats
            total_seats=ac_seats+general_seats
                
        elif type=="G":
            print("\nWelcome to General coach")
            print("Available Seats in General coach :",general_seats)
            print("Price of each AC seat $ \b",price_of_each_G_seat)
            print("How many seats you want to book ;")

            no_of_seats=int(input()) 

            for y in range(no_of_seats):
                
                name=str(input(f'\n{y+1} person Name : '))
                Age=int(input(f'{y+1} person Age : '))
                Gender=str(input(f'{y+1} person Gender : '))
                 
                Gen_no+=1
                sno='G'+str(Gen_no)
                ticket_no+=1
                users.append([sno,ticket_no,name,Age,Gender])

            print("\n")

            for u in users:
                print(u)        
                
            print("\n",no_of_seats," : seats have been booked")
            print("Total price of",no_of_seats,"seats is $ \b",no_of_seats*price_of_each_G_seat)

            general_seats= general_seats - no_of_seats
            total_seats=general_seats+ac_seats
        
        reg_users=[x for x in users]


    elif want==2:
        if del_seat==0:
            print("\nTotal Seats : ",total_seats)
            print("Available Seats in AC coach : ",ac_seats)
            print("Booked Seats in AC coach : ",Ac_no)
            print("Available Seats in General coach : ",general_seats)
            print("Booked Seats in General coach : ",Gen_no)

        else:
            total_seats=ac_seats+general_seats+del_seat
            print("\nTotal Seats : ",total_seats)

            if type=='A':       
                print("Available Seats in AC coach : ",ac_seats+del_seat) 
            else:            
                print("Available Seats in General coach : ",general_seats+del_seat)

        continue


    elif want==3:
        if no_of_seats==0:
            print("\nYou haven't booked any seat..") 

        else:
            print("\n",no_of_seats,"seats you have already booked is ")
            for u in users:
                print(u)
            print("How many seats you want to cancel : ")

            del_seat=int(input())
        
            if del_seat>no_of_seats:
                print("not possible, because no of seats is minimum than cancel ")

            elif del_seat==no_of_seats:
                del users
                print("All seats is cancelled")  

            elif del_seat<no_of_seats:     
                for x in range(del_seat):
                    ticket=int(input("Enter ticket number : \n"))
                    for i in range(len(users)):
                        if int(users[i][1])==int(ticket):
                            users[i][1]=0

                print(del_seat,"seats is now cancelled ;")
                print("Remaining Users:")
                for reg_users in users:
                    if reg_users[1]!=0:
                        print(reg_users)


    elif want==4:
        rest_seat=no_of_seats - del_seat

        if rest_seat==0:
            print("\nYou haven't booked any seat...")
        else:
            print("\nYour",rest_seat,"booked seat is")
            if rest_seat>=2:
                for r in reg_users:
                    print(r)
            elif rest_seat==1:
                print(reg_users)

    elif want==5:
        exit()
    
print("sourav chutiya hai")

