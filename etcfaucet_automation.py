import pyautogui
#google chrome position Point(x=167, y=1066)
#tab position Point(x=142, y=22)
#search bar position Point(x=325, y=57)
#scroll button Point(x=1913, y=1038)
#etc adress enter Point(x=944, y=661)
#robot test pos Point(x=805, y=771)
#continue button pos Point(x=952, y=875)
#print(pyautogui.position()) #takes positions
#pyautogui.PAUSE = 0.7 (increase wait time)


wallet_id= "0x6e956921596DeA1f55E1154338B43D8E248e7807"
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

