class Star_Cinema:
    __hall_list=[]
    
    @classmethod
    def entry_hall(self,hall):
        self.__hall_list.append(hall)

class Hall(Star_Cinema):
    def __init__(self,rows,cols,hall_no) -> None:
        self.__seats={}
        self.__show_list=[]
        self.__rows=rows
        self.__cols=cols
        self.__hall_no=hall_no
        super().__init__()

    def entry_show(self,id: str,movie_name:str,time:str):
        tp=(id,movie_name,time)
        self.__show_list.append(tp)
        matrix=[[0 for _ in range(self.__cols)] for _ in range(self.__rows)]
        self.__seats[id]=matrix
    
    def book_seats(self,id: str, seat_list:list):
        if id in self.__seats:
            for num in seat_list:
                row,col=num
                if row<0 or row>= self.__rows or col<0  or col >= self.__cols:
                    print("\ninvalid seat number given")

                if self.__seats[id][row][col]==1:
                    print("\nseat already taken")
                else:
                    self.__seats[id][row][col]=1
                    print("\nyour seat is booked")
        else:
            print("\ninvalid id")

    def view_show_list(self):
        for show in self.__show_list:
            print(f"Movie Name: {show[1]} id:{show[0]} time:{show[2]}")
        print()
    def view_available_seats(self,id:str):
        if id not in self.__seats:
            print("\nNo such id found")
            return
        position=self.__seats[id]
        print()
        for row in position:
            print(row)
        print()

hl=Hall(5, 5,111)

hl.entry_show("1","inception","11.12")
hl.entry_show("2","django unchained","11.12")

run=True
while run:
    print("1 : View All Shows Today")
    print("2 : view available seats")
    print("3 : Book Ticket")
    print("4 : Exit")
    option=int(input("Enter Option: "))

    if option==1:
        print()
        hl.view_show_list()
    elif option==2:
        opt=input("enter id: ")
        hl.view_available_seats(opt)
    
    elif option==3:
        opt=input("enter id: ")
        t_num=int(input("no of tickets: "))
        seat_list=[]
        for _ in range(t_num):
            row=int(input("enter row no: "))
            col=int(input("enter col no: "))
            seat_list.append([row-1,col-1])
        
        hl.book_seats(opt,seat_list)

    elif option==4:
        run=False

        
