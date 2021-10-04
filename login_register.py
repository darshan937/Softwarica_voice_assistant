""" This module manages passwords of many apps/websites of the users."""
from tkinter import *
from tkinter import messagebox
import sys
import sqlite3
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import smtplib
import random
import os

main_win = Tk()
main_win.title("Softwarica Voice assistant")
main_win.geometry("900x700")
main_win.iconbitmap("images/icon.ico")
main_win.resizable(0, 0)

con = sqlite3.connect("myDatabase.db")
c = con.cursor()
'''
c.execute("""CREATE TABLE IF NOT EXISTS myTable(
              first_name text,
              last_name text, 
              username text, 
              password text)""")

print("Table has been created.")
'''

con.commit()
con.close()

bg_img = PhotoImage(file="images/ai1.PNG")
for_bg_img = Label(main_win, image=bg_img)
for_bg_img.place(x=0, y=0, relwidth=1, relheight=1)
banner_name = Label(main_win, text="Welcome to Softwarica Voice Assistant", font=("copperplate", 30, "bold"), bg="yellow")
banner_name.pack(fill=X)

def clear_entries():

    username_entry.delete(0, END)
    password_entry.delete(0, END)


def open_register():
    main_win.withdraw()
    #show_register()

    # ------------------- GUI for registration starts from here -------------------------------------
    register = Toplevel()
    register.title("Registration")
    register.geometry("1200x630")
    register.iconbitmap("images/icon.ico")
    register.resizable(False, False)
    Label(register, text="REGISTRATION FORM", font=("copperplate", 32, "bold"),
          bg="green", fg="yellow").place(x=410, y=10)


    def go_back():
        clear_entries()
        main_win.deiconify()
        register.destroy()

    def check():
        selected_gender = gender_select.get()
        print(selected_gender)

        if full_name_en.get() == "" and last_name_en.get() == "" and \
                username_en.get() == "" and password_en.get() == "" and confirm_password_en.get() == "":
            messagebox.showerror("Invalid", "All boxes are empty.")

        elif full_name_en.get() == "":
            messagebox.showerror("Invalid", "Full name  box is empty.")

        elif last_name_en.get() == "":
            messagebox.showerror("Invalid", "Last name  box is empty.")

        elif selected_gender == "Choose options":
            messagebox.showerror("Invalid", "Choose gender.")

        elif username_en.get() == "":
            messagebox.showerror("Invalid", "Username box is empty.")

        elif password_en.get() == "":
            messagebox.showerror("Invalid", "Password box  is empty.")

        elif password_en.get() != confirm_password_en.get():
            messagebox.showerror("Invalid", "Password and Re-type password do not match.")

        else:

            con = sqlite3.connect("myDatabase.db")
            c = con.cursor()
            c.execute("INSERT INTO myTable VALUES (:f_name, :l_name, :username_type, :password_type)", {
                'f_name': full_name_en.get(),
                'l_name': last_name_en.get(),
                'username_type': username_en.get(),
                'password_type': password_en.get()
            })
            print("Records have been inserted into the database.")
            con.commit()
            con.close()
            messagebox.showinfo("Registration Successfully", "Thank you for your registration.")
            #messagebox.showinfo("Registration Successfully", "Thank you for your registration.")

            clear_entries()
            main_win.deiconify()
            register.destroy()

    # ----------------------- two frames are designed ------------------
    left_frame = Frame(register, bg="#042a44" )
    left_frame.place(x=20, y=70, height=600, width=500)

    right_frame = Frame(register, bg="#042a44")
    right_frame.place(x=610, y=70, width=574, height=500)

    # ------------------ image in left frame -------------------------

    left_img = PhotoImage(file="images/ai.PNG")
    img_label = Label(left_frame, image=left_img)
    img_label.place(x=0, y=0, relwidth=1, relheight=1)

    # ------------------------- labels and entries in right frame ----------------
    # labels
    full_name_la = Label(right_frame, text="First Name : ", font=("times", 22, "bold"), bg="yellow", fg="black")
    last_name_la = Label(right_frame, text="Last Name : ", font=("times", 22, "bold"), bg="yellow", fg="black")
    gender_la = Label(right_frame, text="Gender : ", font=("times", 22, "bold"), bg="yellow", fg="black")
    username_la = Label(right_frame, text="Username : ", font=("times", 22, "bold"), bg="yellow", fg="black")
    password_la = Label(right_frame, text="Password : ", font=("times", 22, "bold"), bg="yellow", fg="black")
    confirm_password_la = Label(right_frame, text="Re-type password : ", font=("times", 22, "bold"), bg="yellow",
                                fg="black")

    # arrangement/positions of the labels
    full_name_la.grid(row=0, column=0, padx=10, pady=10, sticky=W)
    last_name_la.grid(row=1, column=0, padx=10, pady=10, sticky=W)
    gender_la.grid(row=3, column=0, padx=10, pady=10, sticky=W)
    username_la.grid(row=4, column=0, padx=10, pady=10, sticky=W)
    password_la.grid(row=5, column=0, padx=10, pady=10, sticky=W)
    confirm_password_la.grid(row=6, column=0, padx=10, pady=10, sticky=W)

    # entries
    full_name_en = Entry(right_frame, font=("Times New Roman", 20, "italic"), bd=2, relief=SOLID, bg="black",
                         fg="white")
    last_name_en = Entry(right_frame, font=("Times New Roman", 20, "italic"), bd=2, relief=SOLID, bg="black",
                         fg="white")
    username_en = Entry(right_frame, font=("Times New Roman", 20, "italic"), bd=2, relief=SOLID, bg="black", fg="white")
    password_en = Entry(right_frame, font=("Times New Roman", 20, "italic"), bd=2, relief=SOLID, bg="black", fg="white",
                        show="*")
    confirm_password_en = Entry(right_frame, font=("Times New Roman", 20, "italic"), bd=2, relief=SOLID, bg="black",
                                fg="white", show="*")

    # positions of the entries
    full_name_en.grid(row=0, column=1, padx=10, pady=10)
    last_name_en.grid(row=1, column=1, padx=10, pady=10)
    username_en.grid(row=4, column=1, padx=10, pady=10)
    password_en.grid(row=5, column=1, padx=10, pady=10)
    confirm_password_en.grid(row=6, column=1, padx=10, pady=10)

    # Menu for gender

    gender_list = ["Male", "Female", "Others"]
    gender_select = StringVar()
    gender_select.set("Choose options")
    dropper_show = OptionMenu(right_frame, gender_select, *gender_list)
    dropper_show.grid(row=3, column=1, padx=20, pady=20)
    dropper_show.config(bg="green")

    # buttons with events

    register_btn = Button(right_frame, text="Register", font=("Copperplate", 25, "bold"), bg="green", fg="black",
                          command=check)
    back_btn = Button(right_frame, text="Back", font=("Copperplate", 25, "bold"), bg="green", fg="black",
                      command=go_back)

    register_btn.grid(row=7, column=0, padx=20, pady=20)
    back_btn.grid(row=7, column=1, padx=20, pady=20)
    register.mainloop()

    # ------------------- GUI for registration ends from here -------------------------------------

def close():
    user_response = messagebox.askyesno("Exit", "Do you want to exit ? ")
    if user_response == 1:
        sys.exit()
def hide_password():
    """
    This is for hiding password as clicked on checkbutton.
    :return: None
    """
    password_entry.configure(show="•")
    check_button.configure(command=show_my_password)

def clear_password(event):
    """
    This function clears the password entry as clicked on tab key or the entry.
    :param event: key
    :return: None
    """
    password_entry.delete(0, END)
    password_entry.configure(show="•")


def show_my_password():
    """
    This is for showing password as clicked on checkbutton.
    :return: None
    """

    password_entry.configure(show="")
    check_button.configure(command=hide_password)


def clear_username(event):
    """
    This function clears the username entry as clicked on tab key or the entry.
    :param event: key
    :return: None
    """
    username_entry.delete(0, END)

def submit_func():
    if (username_entry.get() == "" or username_entry.get() == "Enter username") and \
            (password_entry.get() == "" or password_entry.get() == "Enter password"):
        messagebox.showerror("Empty", "Sorry, you've not inserted your username and password.")

    elif username_entry.get() == "" or username_entry.get() == "Enter username":
        messagebox.showerror("Empty", "Sorry, you've not inserted your username.")

    elif password_entry.get() == "" or password_entry.get() == "Enter password":
        messagebox.showerror("Empty", "Sorry, you've not inserted your password.")

    else:
        con = sqlite3.connect("myDatabase.db")
        c = con.cursor()
        q = "Select * from myTable where username =? and password=?"

        c.execute(q, (username_entry.get(), password_entry.get()))
        some_data = c.fetchall()
        for i in some_data:
            myNAME = i
            break
        #print(myNAME[0])
        if len(some_data) > 0:
            messagebox.showinfo("Login successfully", "Login successfully. please go to the command line of pycharm!")

            engine = pyttsx3.init('sapi5')
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[0].id)

            def speak(audio):
                engine.say(audio)
                engine.runAndWait()

            def wishMe():
                hrs = int(datetime.datetime.now().hour)
                if hrs >= 0 and hrs < 12:
                    print('Hello! good morning' + str(myNAME))
                    speak("Hello! good morning")


                elif hrs >= 12 and hrs < 17:
                    print('Hello! good Afternoon ' + str(myNAME[0]))
                    speak("Hello! good Afternoon" + str(myNAME[0]))

                elif hrs >= 17 and hrs < 19:
                    print('Hello! Good Evening ' +str(myNAME[0]))
                    speak("Hello! Good Evening " + str(myNAME[0]))


                else:
                    print('Hello! good night ' + str(myNAME[0]))
                    speak("Hello! good night" + str(myNAME[0]))

                print('I am Softwarica, how can i help you? '+ str(myNAME[0]))
                speak("I am Softwarica, how can i help you? "+ str(myNAME[0]))

            # it takes microphone input from user and returns string output
            def takecommand():

                r = sr.Recognizer()
                with sr.Microphone() as source:
                    print("Listening...")
                    r.pause_threshold = 1
                    r.energy_threshold = 800

                    audio = r.listen(source)

                try:
                    print("Recognizing... ")
                    query = r.recognize_google(audio, language='en-nep')
                    print(f'user said: {query}\n')

                except Exception as e:
                    print('say that again please.....')
                    return "none"
                return query

            def sendEmail(to, content):
                server = smtplib.SMTP('smtp.gmail.com')
                server.ehlo()
                server.starttls()
                server.login('darshanbhusal41@gmail.com', '12+iphone')
                server.sendmail('darshanbhusal41@gmail.com', to, content)
                server.close()

            if __name__ == '__main__':
                wishMe()
                while True:
                    query = takecommand().lower()

                    # logic for executing task
                    if 'wikipedia' in query:
                        speak("Searching wikipedia.....")
                        query = query.replace("wikipedia", "")
                        results = wikipedia.summary(query, sentences=2)
                        speak("according to wikipedia ")
                        print(results)
                        speak(results)

                    elif 'open youtube' in query:
                        webbrowser.open('youtube.com')

                    elif 'open google' in query:
                        webbrowser.open('google.com')

                    elif 'open lms' in query:
                        webbrowser.open('https://lms.softwarica.edu.np/')

                    elif 'open teams' in query:
                        webbrowser.open('https://signup.microsoft.com/create-account/signup')

                    elif 'open campus ' in query:
                        webbrowser.open('https://campus.softwarica.edu.np/sign-in')

                    elif 'the time' in query:
                        strTime = datetime.datetime.now().strftime("%H:%M:%S")
                        print(f"sir the time is {strTime}")
                        speak(f"sir the time is {strTime}")

                    elif 'send email' in query:
                        try:
                            print('what should i say?')
                            speak('what should i say ?')
                            content = takecommand()
                            speak('whom should i send email?')
                            to = takecommand()
                            sendEmail(to, content)
                            print(f"email has been sent to {to} sucessfully.")
                            speak('email has been send sucessfully')
                        except Exception as e:
                            print(e)
                            speak('sorry my dear friend i cannot send this email.')

                    elif 'how are you' in query:
                        speak("I am great and what about you?")

                    elif "what's up" in query:
                        speak("I am great and what about you?")

                    elif 'play music' in query:
                        musicDir = 'C:\\Users\\dijac\\Music\\music\\fav'
                        songs = os.listdir(musicDir)
                        print(songs)
                        randomSong = random.randint(0, 6)
                        os.startfile(os.path.join(musicDir, songs[randomSong]))

                    elif "exit" in query:
                        exit()

                    else:
                        print('I can,t here anything')
                        speak('I can,t here anything so speak again  ')


        else:
            messagebox.showerror("Not registered", "Sorry, this account has not been registered yet.")



        #messagebox.showinfo("Login successfully", "Login successfully. Thank you!")




username_label = Label(main_win, text="Username", font=("times", 25, "bold"), bg="blue", fg="white")
password_label = Label(main_win, text="Password", font=("times", 25, "bold"), bg="blue", fg="white")

username_entry = Entry(main_win, width=30, font=("times new roman", 20, "italic"), bd=3)
username_entry.insert(0, "Enter username")
username_entry.bind("<FocusIn>", clear_username)

password_entry = Entry(main_win, width=30, font=("times new roman", 20, "italic"), bd=3, )
password_entry.insert(0, "Enter password")
password_entry.bind("<FocusIn>", clear_password)

# arranging the position of labels and entries
username_label.place(x=430, y=90)
username_entry.place(x=280, y=140)
password_label.place(x=430, y=190)
password_entry.place(x=280, y=240)

check_button = Checkbutton(main_win, text="Show password", fg="white", bg="blue",
                           command=show_my_password, font=("times", 20, "bold"))
check_button.deselect()
check_button.place(x=410, y=300)

submit_btn = Button(main_win, text="LogIn", font=("times", 20, "bold"), bg="green", fg="black",
                    command=submit_func)
submit_btn.place(x=440, y=360)

create_acc = Button(main_win, text="Create an account",  font=("times", 20, "bold"), bg="purple",
                     fg="black", command=open_register)
create_acc.place(x=360, y=420)

close_win = Button(main_win, text="EXIT",  font=("times", 20, "bold"), bg="red", fg="black", command=close)
close_win.place(x=450, y=485)
main_win.mainloop()