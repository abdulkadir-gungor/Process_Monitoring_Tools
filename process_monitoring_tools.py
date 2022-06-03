#######################################################################################
#
#   process_monitoring_tools (process monitoring tools) [ Main Program ]
#   © 2022 ABDULKADİR GÜNGÖR All Rights Reserved
#   Contact email address: abdulkadir_gungor@outlook.com
#
#	Developper:	Abdulkadir GÜNGÖR (abdulkadir_gungor@outlook.com)
#	Date:	06/2022
#	All Rights Reserved (Tüm Hakları Saklıdır)
#
#######################################################################################
import pystray as pystray
from colorama import init, Fore, Back
from ctypes import Structure, c_int, byref, windll
import os, time, PIL.Image
from winreg import *
#
#
#
class SETTINGS:
    PROGRAM_TITLE:        str  = "Process Monitoring Tools"
    PROGRAM_NAME:         str  = "process_monitoring_tools.exe"
    SYSTEM_TRAY_ICON:     str  = "images\\systemtray.png"
    SYSTEM_TRAY_TITLE:    str  = "Process Monitoring Tools"
    WAIT_TIME:          float  = 0.01
    DEVELOPPER:           str  = "ABDULKADIR GUNGOR"
    PROCESS_CREATION:     list = ( "Process Creation", "programs\\process_creation.exe")
    PROCESS_DELETION:     list = ("Process Deletion", "programs\\process_deletion.exe")
    PROCESS_MONITOR:      list = ("Process Monitor", "programs\\ProcessMonitor\\Procmon64.exe")
    PROCESS_EXPLORER:     list = ("Process Explorer", "programs\\ProcessExplorer\\procexp64.exe")
    PROCESS_RAMMAP:       list = ("RAMMap", "programs\\RAMMap\\RAMMap64.exe")
    PROCESS_WINOBJ:       list = ("WinObj", "programs\\WinObj\\Winobj64.exe")
    PROCESS_AUTORUNS:     list = ("Autoruns","programs\\Autoruns\\Autoruns64.exe" )
    PROCESS_CMD:          list = ("CMD", "cmd")
#
#
#
def setCursor():
    class CONSOLE_CURSOR_INFO(Structure):
        _fields_ = [('dwSize', c_int),
                    ('bVisible', c_int)]
    STD_OUTPUT_HANDLE = -11
    hStdOut = windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
    cursorInfo = CONSOLE_CURSOR_INFO()
    cursorInfo.dwSize = 1
    cursorInfo.bVisible = 0
    windll.kernel32.SetConsoleCursorInfo(hStdOut, byref(cursorInfo))
#
def consoleTitle(title:str):
    os.system("echo off")
    os.system("title {title}".format(title=title))
#
def consoleClear():
    os.system("echo off")
    os.system("cls")
#
def consoleHide():
    windll.user32.ShowWindow(windll.kernel32.GetConsoleWindow(), 0)
#
def consoleShow():
    windll.user32.ShowWindow(windll.kernel32.GetConsoleWindow(), 1)
#
def screenEntry():
    line_c     = Fore.MAGENTA
    default_c  = Fore.LIGHTWHITE_EX
    tag_c      = Fore.CYAN
    print('')
    print( '\t'+line_c+'/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\' )
    print( '\t'+line_c+'\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/')
    print( '\t'+line_c+'/\/\\'+default_c+'                                                      '+line_c+'/\/\\')
    print( '\t'+line_c+'\/\/ '+tag_c+'<Program>'+default_c+'  Process Monitoring Tools v1.1  '+tag_c+'</Program> '+line_c+'\/\/')
    print( '\t'+line_c+'/\/\\               '+tag_c+'<Date>'+default_c+'  06/2022 '+tag_c+'</Date>                '+line_c+'/\/\\')
    print( '\t'+line_c+'\/\/'+default_c+'                                                      '+line_c+'\/\/')
    print( '\t'+line_c+'/\/\\      '+tag_c+'<Developer>'+default_c+' Abdulkadir GÜNGÖR '+tag_c+'</Developer>      '+line_c+'/\/\\')
    print( '\t'+line_c+'\/\/   '+tag_c+'<Email>'+default_c+'  abdulkadir_gungor@outlook.com '+tag_c+'</Email>    '+line_c+'\/\/')
    print( '\t'+line_c+'/\/\\'+default_c+'                                                      '+line_c+'/\/\\')
    print( '\t'+line_c+'\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/')
    print( '\t'+line_c+'/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\')
    print('')
#
def strOK():
    return '['+Back.GREEN+Fore.LIGHTWHITE_EX+'OK!'+Back.BLACK+Fore.WHITE+']'
#
def strERROR():
    return '['+Back.RED+Fore.LIGHTWHITE_EX+'ERROR!'+Back.BLACK+Fore.WHITE+']'
#
def strCHECK():
    return '['+Back.YELLOW+Fore.LIGHTWHITE_EX+'CHECK!'+Back.BLACK+Fore.WHITE+']'
#
def loadUpdate( total_int, value_int, bar_type:str, text_type:str ):
    fill_padding  = '█'
    fill_dash     = ' '
    bar_long      = 62
    text_long     = 28
    setCursor()
    nn_number   = 100/bar_long
    percent = int(100*(value_int/total_int))
    bar_padding = int(percent/nn_number)
    bar_dash    = bar_long - bar_padding
    bar = (Fore.YELLOW + Back.BLACK + str(fill_padding * bar_padding)) + (
                Fore.BLACK + Back.LIGHTWHITE_EX + str(fill_dash * bar_dash)) + (Fore.WHITE + Back.BLACK)
    if bar_type.lower() == 'error':
        bar = (Fore.RED+Back.BLACK+str(fill_padding * bar_padding)) + (Fore.BLACK+Back.LIGHTWHITE_EX+str(fill_dash * bar_dash)) + (Fore.WHITE+Back.BLACK)
    elif bar_type.lower() == 'ok':
        bar = (Fore.GREEN+Back.BLACK+str(fill_padding * bar_padding)) + (Fore.BLACK+Back.LIGHTWHITE_EX+str(fill_dash * bar_dash)) + (Fore.WHITE+Back.BLACK)
    elif bar_type.lower() == 'check':
        bar = (Fore.YELLOW+Back.BLACK+str(fill_padding * bar_padding)) + (Fore.BLACK+Back.LIGHTWHITE_EX+str(fill_dash * bar_dash)) + (Fore.WHITE+Back.BLACK)
    text_str = strCHECK() + ' '
    if text_type.lower() == 'error':
        text_str = strERROR()+' '
    elif text_type.lower()  == 'ok':
        text_str = '   ' + strOK() + ' '
    elif text_type.lower() == 'check':
        text_str = strCHECK() + ' '
    percent = "{0: >2}".format(str(percent))
    tmp_str_format = "{0: <" + str(text_long) + "}"
    txt_str = tmp_str_format.format(str(text_str))
    print( ''' %s%s %s%%''' % (txt_str, bar, percent), end='\r' )
#
def textUpdate(text:str, type:str, newline:bool=False):
    setCursor()
    text_long = 68
    #
    if newline:
        print()
    symbol = strCHECK() + " "
    if type.lower() == 'error':
        symbol = strERROR() + " "
    elif type.lower() == 'ok':
        symbol = "   "+strOK() + " "
    elif type.lower() == 'check':
        symbol = strCHECK() + " "
    tmp_str_format = "{0: <" + str(text_long) + "}"
    txt_str = tmp_str_format.format(str(text))
    #
    print(''' %s%s''' % (symbol,txt_str), end='\r')
#
def isAdmin():
    try:
        return windll.shell32.IsUserAnAdmin()
    except:
        return False
#
def on_clicked_Tools(icon, item):
    cd = os.getcwd()
    if str(item) == SETTINGS.PROCESS_CREATION[0]:
        program = cd + "\\" + SETTINGS.PROCESS_CREATION[1]
        os.startfile(program)
    elif str(item) == SETTINGS.PROCESS_DELETION[0]:
        program = cd + "\\" + SETTINGS.PROCESS_DELETION[1]
        os.startfile(program)
    elif str(item) == SETTINGS.PROCESS_MONITOR[0]:
        program = cd + "\\" + SETTINGS.PROCESS_MONITOR[1]
        os.startfile(program)
    elif str(item) == SETTINGS.PROCESS_EXPLORER[0]:
        program = cd + "\\" + SETTINGS.PROCESS_EXPLORER[1]
        os.startfile(program)
    elif str(item) == SETTINGS.PROCESS_RAMMAP[0]:
        program = cd + "\\" + SETTINGS.PROCESS_RAMMAP[1]
        os.startfile(program)
    elif str(item) == SETTINGS.PROCESS_WINOBJ[0]:
        program = cd + "\\" + SETTINGS.PROCESS_WINOBJ[1]
        os.startfile(program)
    elif str(item) == SETTINGS.PROCESS_AUTORUNS[0]:
        program = cd + "\\" + SETTINGS.PROCESS_AUTORUNS[1]
        os.startfile(program)
    elif str(item) == SETTINGS.PROCESS_CMD[0]:
        os.startfile(SETTINGS.PROCESS_CMD[1])
#
def on_clicked_Startup(icon, item):
    try:
        cd   = os.getcwd()
        reg_value = cd + "\\" + str(SETTINGS.PROGRAM_NAME)
        reg_key   = SETTINGS.PROGRAM_TITLE
        startup = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Run'
        try:
            key0 = OpenKey(HKEY_CURRENT_USER, startup, 0, KEY_WRITE)
        except:
            key0 = CreateKey(HKEY_CURRENT_USER, startup)
        if str(item) == "On":
            SetValueEx(key0, reg_key, 0, REG_SZ, reg_value)
        elif str(item) == "Off":
            DeleteValue(key0,reg_key)
        CloseKey(key0)
    except:
        pass
#
def on_clicked_Visible(icon, item):
    if str(item) == "On":
        consoleShow()
    elif str(item) == "Off":
        consoleHide()
#
def on_clicked_Exit(icon, item):
    icon.stop()
#
def pysTray():
    image = os.path.abspath(SETTINGS.SYSTEM_TRAY_ICON)
    image = PIL.Image.open(image)
    icon  = pystray.Icon( SETTINGS.SYSTEM_TRAY_TITLE, image, menu=pystray.Menu(
        pystray.MenuItem("Tools", pystray.Menu
        (
            pystray.MenuItem(SETTINGS.PROCESS_CREATION[0], on_clicked_Tools),
            pystray.MenuItem(SETTINGS.PROCESS_DELETION[0], on_clicked_Tools),
            pystray.MenuItem(SETTINGS.PROCESS_MONITOR[0], on_clicked_Tools),
            pystray.MenuItem(SETTINGS.PROCESS_EXPLORER[0], on_clicked_Tools),
            pystray.MenuItem(SETTINGS.PROCESS_RAMMAP[0], on_clicked_Tools),
            pystray.MenuItem(SETTINGS.PROCESS_WINOBJ[0], on_clicked_Tools),
            pystray.MenuItem(SETTINGS.PROCESS_AUTORUNS[0], on_clicked_Tools),
            pystray.MenuItem(SETTINGS.PROCESS_CMD[0], on_clicked_Tools)
        )),
        pystray.MenuItem("Startup", pystray.Menu
        (
            pystray.MenuItem("On", on_clicked_Startup),
            pystray.MenuItem("Off", on_clicked_Startup)
        )),
        pystray.MenuItem("Visible", pystray.Menu
        (
           pystray.MenuItem("On",  on_clicked_Visible),
           pystray.MenuItem("Off", on_clicked_Visible)
        )),
         pystray.MenuItem("Exit", on_clicked_Exit)
    ))
    return icon

###--- Main ---###
if __name__ == '__main__':
    consoleTitle(SETTINGS.PROGRAM_TITLE)
    consoleClear()
    init(autoreset=True)
    setCursor()
    screenEntry()
    print()
    # Animation 0
    textUpdate("Checking program requirements",type=strCHECK(), newline=True)
    time.sleep(SETTINGS.WAIT_TIME)
    time.sleep(SETTINGS.WAIT_TIME)
    # Animation 1
    loadUpdate( 100, 0, bar_type="OK", text_type="OK" )
    time.sleep(SETTINGS.WAIT_TIME)
    loadUpdate( 100, 5, bar_type="OK", text_type="OK" )
    time.sleep(SETTINGS.WAIT_TIME)
    loadUpdate( 100, 10, bar_type="OK", text_type="OK" )
    time.sleep(SETTINGS.WAIT_TIME)
    if isAdmin():
        loadUpdate(100, 40, bar_type="OK", text_type="OK")
        time.sleep(SETTINGS.WAIT_TIME)
        loadUpdate(100, 60, bar_type="OK", text_type="OK")
        time.sleep(SETTINGS.WAIT_TIME)
        loadUpdate(100, 90, bar_type="OK", text_type="OK")
        time.sleep(SETTINGS.WAIT_TIME)
        loadUpdate(100, 100, bar_type="OK", text_type="OK")
        time.sleep(SETTINGS.WAIT_TIME)
        textUpdate("Admin authority is available",type="OK",newline=False)
    else:
        loadUpdate(100, 40, bar_type="ERROR", text_type="ERROR")
        time.sleep(SETTINGS.WAIT_TIME)
        loadUpdate(100, 60, bar_type="ERROR", text_type="ERROR")
        time.sleep(SETTINGS.WAIT_TIME)
        loadUpdate(100, 90, bar_type="ERROR", text_type="ERROR")
        time.sleep(SETTINGS.WAIT_TIME)
        loadUpdate(100, 100, bar_type="ERROR", text_type="ERROR")
        time.sleep(SETTINGS.WAIT_TIME)
        textUpdate("Admin authority is not available",type="ERROR",newline=False)
    # Animation 2
    textUpdate("The necessary components for the system tray are being loaded",type=strCHECK(), newline=True)
    time.sleep(SETTINGS.WAIT_TIME)
    time.sleep(SETTINGS.WAIT_TIME)
    # Animation 3
    loadUpdate( 100, 0, bar_type="OK", text_type="OK" )
    time.sleep(SETTINGS.WAIT_TIME)
    loadUpdate( 100, 5, bar_type="OK", text_type="OK" )
    time.sleep(SETTINGS.WAIT_TIME)
    loadUpdate( 100, 10, bar_type="OK", text_type="OK" )
    time.sleep(SETTINGS.WAIT_TIME)
    loadUpdate( 100, 30, bar_type="OK", text_type="OK" )
    time.sleep(SETTINGS.WAIT_TIME)
    loadUpdate( 100, 40, bar_type="OK", text_type="OK" )
    icon = pysTray()
    loadUpdate( 100, 60, bar_type="OK", text_type="OK" )
    time.sleep(SETTINGS.WAIT_TIME)
    loadUpdate( 100, 70, bar_type="OK", text_type="OK" )
    time.sleep(SETTINGS.WAIT_TIME)
    loadUpdate( 100, 95, bar_type="OK", text_type="OK" )
    time.sleep(SETTINGS.WAIT_TIME)
    loadUpdate( 100, 100, bar_type="OK", text_type="OK" )
    time.sleep(SETTINGS.WAIT_TIME)
    textUpdate("Installed required components for system tray", type="OK", newline=False)
    print()
    time.sleep(SETTINGS.WAIT_TIME)
    consoleHide()
    icon.run()

