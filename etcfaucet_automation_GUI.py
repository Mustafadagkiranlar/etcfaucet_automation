from tkinter import *
import pyautogui



def start_button_click():
    wallet_id= wallet_id_enter.get()
    tab_pos_x = 142
    tab_pos_y = 22

    google_app_x = 167
    google_app_y =  1066
    pyautogui.click(google_app_x, google_app_y)

    search_pos_x = 325
    search_pos_y = 57
    pyautogui.click(search_pos_x, search_pos_y, duration=1  )

    link = "https://etcfaucet.info"
    pyautogui.typewrite(link)
    pyautogui.typewrite(['enter'])

    pyautogui.PAUSE =3.0

    scroll_pos_x = 1913
    scroll_pos_y = 1038
    pyautogui.click(scroll_pos_x, scroll_pos_y)
    pyautogui.PAUSE = 0.1
    for i in range(6):
        pyautogui.click(scroll_pos_x, scroll_pos_y)

    etc_add_pos_x = 944
    etc_add_pos_y = 661
    pyautogui.click(etc_add_pos_x, etc_add_pos_y)
    pyautogui.typewrite(wallet_id)

    robot_test_pos_x = 805
    robot_test_pos_y = 771
    pyautogui.click(robot_test_pos_x, robot_test_pos_y)

    cont_but_pos_x = 952
    cont_but_pos_y = 875
    pyautogui.click(cont_but_pos_x, cont_but_pos_y,duration=10)

root = Tk()
root.geometry("610x90")

default_wallet_label = Label(root, text="Enter your wallet")
default_wallet_label.grid(row=1, column=1)

wallet_id_enter = Entry(root, width= 100)
wallet_id_enter.grid(row=2,column=1)

start_button = Button(root, text="Done!" ,padx=50, pady=10, command=start_button_click,)
start_button.grid(row=3,column=1)

root.mainloop()