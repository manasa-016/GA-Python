bookings=[]
trains={
    101:{
        "name":"Express",
        "fare":500,
        "seats":5
    },
    102:{
        "name":"Superfast",
        "fare":800,
        "seats":5
    },
    103:{
        "name":"Rajdhani",
        "fare":1500,
        "seats":5
    }
}
def display_trains():
    print("\n===========Available Trains===========")
    for train_no, details in trains.items():
        print(
            f"Train No:{train_no} |"
            f"Name:{details['name']} |"
            f"Fare:{details['fare']} |"
            f"Available Seats:{details['seats']}"
        )
def book_ticket():
    display_trains()
    train_no=int(input("Enter train number:"))
    if train_no not in trains:
        print("Invalid train number.")
        return
    if trains[train_no]["seats"]==0:
        print("No Seats Available")
        return

    name=input("Enter your name:")
    age=int(input("Enter your age:"))
    gender=input("Enter gender:")    
    mobile=input("Enter mobile number:")
    passengers=int(input("Enter number of passengers:"))
    if passengers>trains[train_no]["seats"]:
        print("Not enough seats.Please try again.")
        return
    total_fare=passengers*trains[train_no]["fare"]
    booking={
        "name":name,
        "age":age,
        "gender":gender,
        "mobile":mobile,
        "passengers":passengers,
        "total_fare":total_fare,
        "train_no":train_no,
        "train_name":trains[train_no]["name"]
    }
    bookings.append(booking)
    trains[train_no]["seats"]-=passengers
    print("Ticket booked successfully!")
    print(f"Total Fare:{total_fare}")
    
def view_bookings():
    if len(bookings)==0:
        print("No bookings made yet.")
        return
    print("\n===========Bookings Details===========")
    for booking in bookings:
        print("------------------------------------------")
        print("Passenger Name:",booking['name'])
        print("Train Name:",booking['train_name'])
        print("Train Number:",booking['train_no'])
        print("Total Fare:",booking['total_fare'])
        print("Age:",booking['age'])
        print("Gender:",booking['gender'])
        print("Mobile:",booking['mobile'])
        print("Passengers:",booking['passengers'])

def cancel_ticket():
    name=input("enter passenger name to cancel ticket:")
    for booking in bookings:
        if booking['name'].lower()==name.lower():
            trains[booking['train_no']]['seats']+=booking['passengers']
            bookings.remove(booking)
            print("ticket cancelled")
            return
    print("Booking Not Found")

while True:
    print("\n==========Train Ticket Booking System==========")
    print("1.Display Trains")
    print("2.Book Ticket")
    print("3.View Bookings")
    print("4.Cancel Ticket")
    print("5.Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        display_trains()
    elif choice==2:
        book_ticket()
    elif choice==3:
        view_bookings()
    elif choice==4:
        cancel_ticket()
    elif choice==5:
        break
    else:
        print("Invalid choice")        