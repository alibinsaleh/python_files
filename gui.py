import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
                            
        # Create frame panels for labels, entries and buttons widgets
        self.frame1 = tkinter.Frame(self.main_window)
        self.frame2 = tkinter.Frame(self.main_window)
        self.frame3 = tkinter.Frame(self.main_window, width=45)
        
        # Contact widgets
        self.contact_label = tkinter.Label(self.frame1, text="Contact Name:", width=15)
        self.contact_entry = tkinter.Entry(self.frame1, width=30)
        # Cell Phone widgets
        self.cellphone_label = tkinter.Label(self.frame2, text="Cell Phone:", width=15)
        self.cellphone_entry = tkinter.Entry(self.frame2, width=30)
        # pack widgets of frame1
        self.contact_label.pack(side='left')
        self.contact_entry.pack(side='left')
        # pack widgets of frame2
        self.cellphone_label.pack(side='left')
        self.cellphone_entry.pack(side='left')
 


        # Create buttons widgets
        self.save_button = tkinter.Button(self.frame3, 
                                        text='Save To File', 
                                        width=23,
                                        command=self.save)
        self.quit_button = tkinter.Button(self.frame3, 
                                        text='Quit',
                                        width=23,
                                        command=self.main_window.destroy)


        # pack widgets of frame3
        self.save_button.pack(side='left')
        self.quit_button.pack(side='right')

        # pack all frames
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        
        
        tkinter.mainloop()                                                                                               

    def save(self):
        try:
            # open the file.
            with open('names.txt', 'a+') as f:
                f.write(self.contact_entry.get() + ', ' + self.cellphone_entry.get())
            tkinter.messagebox.showinfo('Result', f'Name ( {self.contact_entry.get()} ),  saved successfuly!')

        except IOError:
            tkinter.messagebox.showinfo('Warnning!', 'Something wrong happend, name ( {self.contact_entry.get()} ), is not saved!')
            

gui = MyGUI()
