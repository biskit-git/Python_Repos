import os #line:1
import shutil #line:2
import time #line:3
from colorama import Fore ,Style #line:4
import win32api #line:5
import win32con #line:6
os .environ ['PYGAME_HIDE_SUPPORT_PROMPT']='1'#line:7
import pygame #line:8
from colorama import Fore ,Style ,init #line:9
init ()#line:10
def blue_green (OOOOO00000O000O0O ):#line:12
    O0O0O00O00O00OO00 =[Fore .BLUE ,Fore .CYAN ,Fore .LIGHTCYAN_EX ,Fore .LIGHTGREEN_EX ,Fore .GREEN ]#line:13
    OO0O00OO0OO00OOO0 =max (1 ,len (OOOOO00000O000O0O )//len (O0O0O00O00O00OO00 ))#line:14
    OO0000OOOOOO0OOO0 =""#line:16
    for OOO000OOOOO0000O0 ,O0OOO00OO000OO0OO in enumerate (OOOOO00000O000O0O ):#line:17
        O00OOO00OOOO00O0O =O0O0O00O00O00OO00 [min (OOO000OOOOO0000O0 //OO0O00OO0OO00OOO0 ,len (O0O0O00O00O00OO00 )-1 )]#line:18
        OO0000OOOOOO0OOO0 +=O00OOO00OOOO00O0O +O0OOO00OO000OO0OO #line:19
    return OO0000OOOOOO0OOO0 +Style .RESET_ALL #line:20
def blue_p (O0OO0OOO00O00OO0O ):#line:22
    OOO000OOOO0O000OO =[Fore .LIGHTRED_EX ,Fore .RED ,Fore .CYAN ,Fore .LIGHTCYAN_EX ,]#line:28
    OOOOO0O0O0O0O0000 =max (1 ,len (O0OO0OOO00O00OO0O )//len (OOO000OOOO0O000OO ))#line:29
    OOO000OOO00O00O00 =""#line:31
    for O0OOO0O000O0OO00O ,O00O00O0O0000OOOO in enumerate (O0OO0OOO00O00OO0O ):#line:32
        O0000O00OO00O0OOO =OOO000OOOO0O000OO [min (O0OOO0O000O0OO00O //OOOOO0O0O0O0O0000 ,len (OOO000OOOO0O000OO )-1 )]#line:33
        OOO000OOO00O00O00 +=O0000O00OO00O0OOO +O00O00O0O0000OOOO #line:34
    return OOO000OOO00O00O00 +Style .RESET_ALL #line:35
os .system ("cls")#line:37
def loading ():#line:39
 for OOOOOOOO00OO0O00O in range (3 ):#line:40
  O0O0O00OO000OO0O0 ="\033[0;32m*"*OOOOOOOO00OO0O00O #line:41
  print (f"\r\033[0mLoading Obfuscated Code {O0O0O00OO000OO0O0}",end ="")#line:42
  time .sleep (1.3 )#line:43
loading ()#line:44
os .system ("cls")#line:46
print (blue_green ("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"))#line:47
print (f"\033[1;35m: This Project Was A Reverse Engineering Script Edited And Decompiled By Controller Ascend, \033[38;5;45m@BisKit @Lonely : \033[0m")#line:48
print (blue_green ("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"))#line:49
time .sleep (4 )#line:50
os .system ('cls')#line:52
def main2 ():#line:54
 for OO00O0O000O000OOO in range (2 ):#line:55
  print (blue_p ("""
       
       ██████╗██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗      █████╗ ███████╗ ██████╗███████╗███╗   ██╗██████╗ 
      ██╔════╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗    ██╔══██╗██╔════╝██╔════╝██╔════╝████╗  ██║██╔══██╗
      ██║     ██████╔╝███████║██║     █████╔╝ █████╗  ██║  ██║    ███████║███████╗██║     █████╗  ██╔██╗ ██║██║  ██║
      ██║     ██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██║  ██║    ██╔══██║╚════██║██║     ██╔══╝  ██║╚██╗██║██║  ██║
      ╚██████╗██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██████╔╝    ██║  ██║███████║╚██████╗███████╗██║ ╚████║██████╔╝
       ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═════╝     ╚═╝  ╚═╝╚══════╝ ╚═════╝╚══════╝╚═╝  ╚═══╝╚═════╝ """))#line:63
  print ("\033[1;38;5;208m       @BisKit \033[1;38;5;226m@Lonely\033[0m\n")#line:64
  OO0O0OO00OOOOO00O =input (blue_p (f""" ['Enter Password To Access: """))#line:65
  if OO0O0OO00OOOOO00O =="9001":#line:66
    print ("")#line:67
    break #line:68
  else :#line:69
    os .system ("cls")#line:70
    print (f"\033[1;33mWrong Password, ['{1 - OO00O0O000O000OOO}'] \033[1;31mAttempts Left Untill Exiting, Cracked Ascend\033]0m")#line:71
 else :#line:72
    os .system ("cls")#line:73
    print (blue_p ("""                      
 _       _               
| |_ _ _| |_ ___ _ _ ___ 
| . | | | . | -_| | | -_|
|___|___|___|___|_  |___|
                |___|    

Used All Password Attempts.\n"""))#line:81
    time .sleep (2.1 )#line:82
    OO0O0OO00OOOOO00O =quit ()#line:83
main2 ()#line:84
def clear_screen ():#line:86
    OOOO0O0O0O000OOOO ='cls'if os .name =='nt'else 'clear'#line:87
    os .system (OOOO0O0O0O000OOOO )#line:88
def get_terminal_width ():#line:90
    return shutil .get_terminal_size ().columns #line:91
def color_text (O0O00O00000OO00OO ,color =Fore .WHITE ):#line:93
    OOOO00O000000OO00 =O0O00O00000OO00OO .split ('\n')#line:94
    O0O000O00OO0OO0O0 =get_terminal_width ()#line:95
    OO00O0O0000O00O0O =[color +O0OO0OOO00O00OO00 .center (O0O000O00OO0OO0O0 )+Style .RESET_ALL for O0OO0OOO00O00OO00 in OOOO00O000000OO00 ]#line:96
    return '\n'.join (OO00O0O0000O00O0O )#line:97
def center_text (OOO0OOOO0O0O0OOO0 ):#line:99
    OO0OO0O0OOOO000OO =shutil .get_terminal_size ().columns #line:100
    OO00O0O000OOO0OO0 =[OOOO0O00OOOO000OO .center (OO0OO0O0OOOO000OO )for OOOO0O00OOOO000OO in OOO0OOOO0O0O0OOO0 .split ('\n')]#line:101
    return '\n'.join (OO00O0O000OOO0OO0 )#line:102
def load_settings ():#line:104
    OOOOO000O0OO00O0O =20 #line:105
    OOO00O00OO0O0OO00 =20 #line:106
    OO0OO00O0O0OOO000 =20 #line:107
    O0000OO00OO0O0OO0 =24 #line:108
    return (OOOOO000O0OO00O0O ,OOO00O00OO0O0OO00 ,OO0OO00O0O0OOO000 ,O0000OO00OO0O0OO0 )#line:109
def display_banner (OOOO00O00O0O000O0 ,OOO0O000OO0OO0OOO ,OOO00O0OOOO00O0O0 ,OO0O00000OOO0O000 ):#line:111
 print (blue_green (""" 
       ██████╗██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗      █████╗ ███████╗ ██████╗███████╗███╗   ██╗██████╗ 
      ██╔════╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗    ██╔══██╗██╔════╝██╔════╝██╔════╝████╗  ██║██╔══██╗
      ██║     ██████╔╝███████║██║     █████╔╝ █████╗  ██║  ██║    ███████║███████╗██║     █████╗  ██╔██╗ ██║██║  ██║
      ██║     ██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██║  ██║    ██╔══██║╚════██║██║     ██╔══╝  ██║╚██╗██║██║  ██║
      ╚██████╗██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██████╔╝    ██║  ██║███████║╚██████╗███████╗██║ ╚████║██████╔╝
       ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═════╝     ╚═╝  ╚═╝╚══════╝ ╚═════╝╚══════╝╚═╝  ╚═══╝╚═════╝ """))#line:118
def mouse_motion ():#line:120
    win32api .mouse_event (win32con .MOUSEEVENTF_MOVE ,move_right ,move_down ,31 ,31 ,)#line:121
    time .sleep (0.01 )#line:122
    win32api .mouse_event (win32con .MOUSEEVENTF_MOVE ,-move_left ,-move_up ,-31 ,-31 )#line:123
def monitor_settings (O0O0OO0OOO0OOO00O ):#line:125
    return O0O0OO0OOO0OOO00O #line:126
def wait_for_controller ():#line:128
    while pygame .joystick .get_count ()==0 :#line:129
        clear_screen ()#line:130
        display_banner (move_right ,move_left ,move_up ,move_down )#line:131
        time .sleep (1 )#line:132
        pygame .joystick .quit ()#line:133
        pygame .joystick .init ()#line:134
    O00O0O0OO00OO0OOO =pygame .joystick .Joystick (0 )#line:135
    O00O0O0OO00OO0OOO .init ()#line:136
    clear_screen ()#line:137
    display_banner (move_right ,move_left ,move_up ,move_down )#line:138
    print ("\n\033[1;37m                     Works For Xbox + Ps4/5                             \033[0;36mLT + LR\033[0m or \033[0;35mL1 + L2\033[0m")#line:140
    print ("\n\033[1;37m                                             Project By \033[1;32m@BisKit \033[1;36m@Lonely\033[0m")#line:141
    print ("                                                [\033[1;33m'Jitter Activated'\033[1;33m\033[0m]")#line:142
    return O00O0O0OO00OO0OOO #line:143
move_right ,move_left ,move_up ,move_down =load_settings ()#line:145
current_settings =(move_right ,move_left ,move_up ,move_down )#line:146
pygame .init ()#line:148
pygame .joystick .init ()#line:149
controller =wait_for_controller ()#line:150
while True :#line:152
    for event in pygame .event .get ():#line:153
        if event .type ==pygame .QUIT :#line:154
            pygame .quit ()#line:155
            exit ()#line:156
    if pygame .joystick .get_count ()==0 :#line:158
        pygame .quit ()#line:159
        exit ()#line:160
    aim =controller .get_axis (4 )#line:162
    shoot =controller .get_axis (5 )#line:163
    if aim >0.0 and shoot >0.0 :#line:164
        mouse_motion ()#line:165
    if int (time .time ())%2 ==0 :#line:167
        updated_settings =monitor_settings (current_settings )#line:168
        if updated_settings !=current_settings :#line:169
            move_right ,move_left ,move_up ,move_down =updated_settings #line:170
            current_settings =updated_settings #line:171
            display_banner (move_right ,move_left ,move_up ,move_down )#line:172
    time .sleep (0.01 )
