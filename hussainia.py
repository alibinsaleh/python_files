import datetime
from tkinter import *

class ColorText:
    # Colourise - colours text in shell. Returns plain if colour doesn't exist.
    def colourise(colour, text):
        if colour == "black":
            return "\033[1;30m" + str(text) + "\033[1;m"
        if colour == "red":
            return "\033[1;31m" + str(text) + "\033[1;m"
        if colour == "green":
            return "\033[1;32m" + str(text) + "\033[1;m"
        if colour == "yellow":
            return "\033[1;33m" + str(text) + "\033[1;m"
        if colour == "blue":
            return "\033[1;34m" + str(text) + "\033[1;m"
        if colour == "magenta":
            return "\033[1;35m" + str(text) + "\033[1;m"
        if colour == "cyan":
            return "\033[1;36m" + str(text) + "\033[1;m"
        if colour == "gray":
            return "\033[1;37m" + str(text) + "\033[1;m"
        if colour == "white":
            return "\u001b[37m" + str(text) + "\u001b[0m"
        return str(text)
    
    # Highlight - highlights text in shell. Returns plain if colour doesn't exist.
    def highlight(colour, text):
        if colour == "black":
            return "\033[1;40m" + str(text) + "\033[1;m"
        if colour == "red":
            return "\033[1;41m" + str(text) + "\033[1;m"
        if colour == "green":
            return "\033[1;42m" + str(text) + "\033[1;m"
        if colour == "yellow":
            return "\033[1;43m" + str(text) + "\033[1;m"
        if colour == "blue":
            return "\033[1;44m" + str(text) + "\033[1;m"
        if colour == "magenta":
            return "\033[1;45m" + str(text) + "\033[1;m"
        if colour == "cyan":
            return "\033[1;46m" + str(text) + "\033[1;m"
        if colour == "gray":
            return "\033[1;47m" + str(text) + "\033[1;m"
        return str(text)

# Sessions class
class Session:
    def __init__(self, session_time, reciter_name, capacity=3):
        self.session_time = session_time
        self.reciter_name = reciter_name
        self.capacity = capacity
        self.remaining_seats = self.capacity
        self.attendees = {}
            
    def show_attendees(self):
        for k, v in self.attendees.items():
            print(k, v)     
            
    def inspect_attendee(self, person):
        self.attendees[person].info()

            
# ---------------------------------------------
# Hussainia class
class Hussainia:
    def __init__(self, name, area="", capacity=50, location=""):
        self.name = name
        self.area = area
        self.capacity = capacity
        self.location = location
        
        self.hussainia_sessions = []
        
    def info(self):
        print(f'Hussainia Name: {self.name}\nCapacity: {self.capacity}\nArea: {self.area}\nLocation: {self.location}\n')
        
    
    def add_session(self, s):
        self.info()
        self.hussainia_sessions.append(s)
        self.show_sessions()
        
    def del_session(self, s):
        self.hussainia_sessions.remove(s)
        
    def sessions_count(self):
        return len(self.hussainia_sessions)
    
    def show_sessions(self):
        print("#".ljust(3, ' '),"Session Time".ljust(15,' '),"Reciter Name".ljust(30, ' '), "Available Seats".ljust(20, ' '))
        for counter, item in enumerate(self.hussainia_sessions):
            #print(f"\033[44;33m{counter}\033[m".ljust(4, ' '), f"{item.session_time}".ljust(15,' '), f"{item.reciter_name}".ljust(30, ' '), f"{self.hussainia_sessions[counter].remaining_seats}".ljust(20, ' '))
            print(ColorText.highlight("cyan", ColorText.colourise("black", f"{counter}".ljust(3, ' '))), \
                  ColorText.highlight("blue", ColorText.colourise("white", f"{item.session_time}".ljust(15,' '))), \
                  ColorText.highlight("red", ColorText.colourise("white", f"{item.reciter_name}".ljust(30, ' '))), \
                  ColorText.highlight("green", ColorText.colourise("white", f"{self.hussainia_sessions[counter].remaining_seats}".ljust(20, ' '))))

    def book(self, person):
        """ Used to book a seat in this Hussainia's  sessions."""
        while True:
            
            # display sessions to choose from.
            self.show_sessions()
            
            
            # ask user to select a session.
            print('Select session by session # or q.')
            choice = input()
            if choice.upper() == 'Q':
                break
            else:
                choice = int(choice)
                # check if user selection is valid and in range.
                if (choice > self.sessions_count()-1) or choice < 0: # if not in range:
                    print('Sorry, out of sessions range, try again.')
                    #self.show_attendees(choice)
                else: # if in range:
                    # check if there is an available seat in the session selected (choice)
                    if self.hussainia_sessions[choice].remaining_seats > 0: # if seat available:
                        # check if booking person already booked in this (choice) session:
                        if person.name in self.hussainia_sessions[choice].attendees: # already booked
                            print(f"Sorry {person.name}, you are already booked in this session.")
                        else: # not booked
                            # add this person into session's attendees' attribute.
                            self.hussainia_sessions[choice].attendees[person.name] = self.hussainia_sessions[choice].session_time
                            # add this session (choice) to this person's my_sessions list attribute.
                            person.my_sessions.append(self.hussainia_sessions[choice])
                            # display a message confirmming booking
                            print(f"My condolences {person.name.split(' ')[0]}, don't forget the session time ({self.hussainia_sessions[choice].session_time})")
                            # update session's remaining_seats attribute by -1
                            self.hussainia_sessions[choice].remaining_seats -= 1

                    else: # if there no seat available
                        print(f"Sorry {person.name.split(' ')[0]}, no seats available.")

    def unbook(self, person):
        while True:
            for c, s in enumerate(person.my_sessions):
                print('\033[44;33m'+str(c)+'\033[m', s.session_time, s.reciter_name)

            # ask user to select a session.
            print('Select session by session #.')
            choice = int(input())

            if (choice > len(person.my_sessions)-1) or choice < 0: # if not in range:
                print('Sorry, out of sessions range, try again.')
                break
            else:
                self.hussainia_sessions[choice].attendees.pop(person.name)
                self.hussainia_sessions[choice].remaining_seats += 1
                print(f"Successfully removed {person.name} from {self.hussainia_sessions[choice].session_time}")
                self.hussainia_sessions[choice].show_attendees()
                break
    
#     def get_remaining_seats(self, s):
#         return self.hussainia_sessions[s].remaining_seats
            
    def inspect_attendee(self, person):
        self.attendees[person].info()
    
# ---------------------------------------------   
    
# Class Person
class Person:
    def __init__(self, gov_id, name, sex='male'):
        self.gov_id = gov_id
        self.name = name
        self.sex = sex
        self.my_sessions = []
        
    def info(self):
        print(f'ID: {self.gov_id}\nName: {self.name}\nSex: {self.sex}\n')
        
 

if __name__ == "__main__":
    h1 = Hussainia('Albandar')
    h2 = Hussainia('Umalbaneen')

    h1.add_session(Session('07:15:00', 'Ali'))
    h1.add_session(Session('09:00:00', 'Mohammed'))
    h2.add_session(Session('08:00:00', 'Abbass'))
    h2.add_session(Session('11:00:00', 'Abdulraouf'))
    h2.add_session(Session('05:30:00', 'Nabeel'))


    p1 = Person('1001', 'Ali Almohammed Saleh')
    p2 = Person('1002', 'Essam Annajar')
    p3 = Person('1003', 'Saleem Faris')

    print(p1.info())
    h1.book(p1)
    print(p2.info())
    h1.book(p2)
    print(p3.info())
    h1.book(p3)
    print('removing', p1.name)
    h1.unbook(p1)


    