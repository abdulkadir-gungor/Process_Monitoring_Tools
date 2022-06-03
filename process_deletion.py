#######################################################################################
#
#   process_deletion.py (Process Deletion) [ Main Program ]
#   © 2022 ABDULKADİR GÜNGÖR All Rights Reserved
#   Contact email address: abdulkadir_gungor@outlook.com
#
#	Developper:	Abdulkadir GÜNGÖR (abdulkadir_gungor@outlook.com)
#	Date:	06/2022
#	All Rights Reserved (Tüm Hakları Saklıdır)
#
#######################################################################################
from ctypes import Structure, c_int, byref, windll
from colorama import init, Fore
import wmi, os
#
def consoleTitle(title:str):
    os.system("echo off")
    os.system("title {title}".format(title=title))
#
def consoleClear():
    os.system("echo off")
    os.system("cls")
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
class ProcessWatcher():
    COLOR_DATE = Fore.RED
    COLOR_NAME = Fore.GREEN
    COLOR_OWNER = Fore.CYAN
    COLOR_ID = Fore.YELLOW
    COLOR_PRIORITY = Fore.YELLOW
    COLOR_SESSIONID = Fore.YELLOW
    COLOR_COMMANDLINE = Fore.WHITE
    #
    def __init__(self):
        self.__wmi   = wmi.WMI()
        self.__watch = self.__wmi.Win32_Process.watch_for("deletion")
    #
    def watch(self):
        try:
            tmp = self.__watch(timeout_ms=1)
        except:
            tmp = None
        if tmp != None:
            try:
                Process_Owner = tmp.GetOwner()
            except:
                Process_Owner = None
            Process_CreationDate = tmp.CreationDate
            Process_Id = tmp.ProcessId
            Process_Name = tmp.Name
            Process_CommandLine = tmp.CommandLine
            Process_Priority = tmp.Priority
            Process_SessionId = tmp.SessionId
            if Process_CreationDate is not None:
                p_year = Process_CreationDate[0:4]
                p_month = Process_CreationDate[4:6]
                p_day = Process_CreationDate[6:8]
                p_hour = Process_CreationDate[8:10]
                p_minute = Process_CreationDate[10:12]
                p_second = Process_CreationDate[12:14]
                str_time = "[" + p_day + "/" + p_month + "/" + p_year + " " + p_hour + ":" + p_minute + ":" + p_second + "]"
                str_time = ProcessWatcher.COLOR_DATE + str_time
            else:
                str_time = ProcessWatcher.COLOR_DATE + "[ ]"
            if Process_Name is not None:
                str_name = "[" + Process_Name + "]"
                str_name = ProcessWatcher.COLOR_NAME + str_name
            else:
                str_name = ProcessWatcher.COLOR_NAME + "[ ]"
            if Process_Owner is not None:
                if len(Process_Owner) == 3:
                    str_owner = ProcessWatcher.COLOR_OWNER + "[" + str(Process_Owner[0]) +" | "+str(Process_Owner[1])+" | "+str(Process_Owner[2])+"]"
                else:
                    str_owner = ProcessWatcher.COLOR_OWNER + "[ ]"
            else:
                str_owner = ProcessWatcher.COLOR_OWNER + "[ ]"
            if Process_Id is not None:
                str_id = "[id:" + str(Process_Id) + "]"
                str_id = ProcessWatcher.COLOR_ID + str_id
            else:
                str_id = ProcessWatcher.COLOR_ID + "[ ]"
            if Process_Priority is not None:
                str_priority = "[priority:" + str(Process_Priority) + "]"
                str_priority = ProcessWatcher.COLOR_PRIORITY + str_priority
            else:
                str_priority = ProcessWatcher.COLOR_PRIORITY + "[ ]"
            if Process_SessionId is not None:
                str_sessionId = "[sessionId:" + str(Process_Priority) + "]"
                str_sessionId = ProcessWatcher.COLOR_SESSIONID + str_sessionId
            else:
                str_sessionId = ProcessWatcher.COLOR_SESSIONID + "[ ]"
            if Process_CommandLine is not None:
                str_commandline = ProcessWatcher.COLOR_COMMANDLINE + "[Command Line] " + Process_CommandLine
            else:
                str_commandline = ProcessWatcher.COLOR_COMMANDLINE + "[Command Line] "
            str_return = " " + str_time + " "+ str_owner+" "+ str_name + " " + str_id + " " + str_priority + " " + str_sessionId + "\n"
            str_return += " " + str_commandline
            return str_return
        else:
            return None

###--- Main ---###
if __name__ == '__main__':
    consoleTitle("Process Deletion")
    consoleClear()
    setCursor()
    init(autoreset=True)
    pp = ProcessWatcher()
    setCursor()
    while True:
        res = pp.watch()
        if res is not None:
            print()
            print(res)
