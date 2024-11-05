import dearpygui.dearpygui as dpg
import ctypes
import zipfile
import sys
import pathlib
import os
import shutil
import PyBass.bass as bass_z
import time
import FontInfo as font
def PlayMusic_Unk():
    bass_z.BASS_INIT(device=-1, freq=48000, flags=0, win=0, dsguid=0)
    bass_z.BASS_START()
    str_create = bass_z.BASS_StreamCreateFile(mem=0, filename=bytes("UnknownMusic_MafRemix.mp3", "utf-8"), offset=0, length=0, flags=0x4)
    bass_z.BASS_ChannelPlay(str_create, False)
def StopMusic():
    if(bass_z.BASSFree()):
        bass_z.BASSStop()
        print("Successfully Stopped This Music!!!")
    else:
        print("Failed to Stop Music!!!")
def GetMaxSize_X64():
    return int(2147483647)
def DPG_GetValue() -> str:
    return dpg.get_value("foldervalue")
def DPG_GetValue_ArchType():
    return dpg.get_value("archtype_windows")
def CheckIfSteamAPIX86IsDetected_Extract():
    steam_detect = pathlib.Path(str(DPG_GetValue() + "\\steam_api.dll")).is_file()
    if(steam_detect == False):
        print("Not Founded Steamworks API DLL File!!!")
        os._exit(1321)
    else:
        steam_apix86 = str(DPG_GetValue() + "\\steam_api.dll")
        shutil.copyfile(steam_apix86, str(DPG_GetValue() + "\\steam_api_o.dll"))
        os.remove(str(steam_apix86))
        with zipfile.ZipFile(str(os.getcwd() + "\\DLCMethod\\SmokeAPI.zip")) as zipf:
            if(zipf.extractall(path=str(DPG_GetValue())) == True):
                print("ALL GOOD!!! YOU CAN NOW USE THIS METHOD(CREAMAPI) -> X86 Edition")
                time.sleep(14)
                exit(554)
            else:
                print("WOOPSIE DOOPSIE!!! THIS NOT WORKED OR NOT FOUNDED ZIPFILE!!!")
                time.sleep(6)
                exit(155)

def CheckIfSteamAPIX64IsDetected_Extract():
    steam_detectx64 = pathlib.Path(str(DPG_GetValue() + "\\steam_api64.dll")).is_file()
    if(steam_detectx64 == False):
        print("Not Founded Steamworks API DLL File!!!")
        os._exit(1321)
    else:
        steam_apix64 = str(DPG_GetValue() + "\\steam_api64.dll")
        shutil.copyfile(steam_apix64, str(DPG_GetValue() + "\\steam_api64_o.dll"))
        os.remove(str(steam_apix64))
        with zipfile.ZipFile(str(os.getcwd() + "\\DLCMethod\\SmokeAPI.zip")) as zipf:
            if(zipf.extractall(path=str(DPG_GetValue())) == True):
                print("ALL GOOD!!! YOU CAN NOW USE THIS METHOD(SMOKEAPI) -> X64 Edition")
                time.sleep(14)
                exit(554)
            else:
                print("WOOPSIE DOOPSIE!!! THIS NOT WORKED OR NOT FOUNDED ZIPFILE!!!")
                time.sleep(6)
                exit(155)

class MainGUI:
    def Extract_DLCUnlocker_x86():
        CheckIfSteamAPIX86IsDetected_Extract()
    def Extract_DLCUnlocker_x64():
        if(sys.maxsize < GetMaxSize_X64()):
            CheckIfSteamAPIX64IsDetected_Extract()
        else:
            print("You have 64-bit arch... Pls Choose X86 Arch Type for steam_api.dll(x86 edition)!!!")
            time.sleep(18)
            os._exit(122)
    def IfArchIsX64BitOrX86():
        if(dpg.get_value("archtype") == str("64bit")):
            MainGUI.Extract_DLCUnlocker_x64()
        elif(dpg.get_value("archtype") == str("86bit")):
            MainGUI.Extract_DLCUnlocker_x86()
        else:
            print("Unknown or It's Linux-Type Architecture...")
            time.sleep(14)
            os._exit(4432)
    def MainThread():
        MainGUI.IfArchIsX64BitOrX86()
    def Main():
        PlayMusic_Unk()
        dpg.create_context()
        with dpg.font_registry():
            font_sourcecodepro = dpg.add_font(font.FontDir_String(), size=13)
        with dpg.window(label="SteamXL", height=700, width=700, tag="mainwindow") as window:
            dpg.bind_font(font_sourcecodepro)
            dpg.add_text("It's my First Serious Project for Unlocking DLC(Downloading Content)... So Enjoy to use this!!!")
            dpg.add_input_text(label="Folder for Extract DLC Methods(Only Available SmokeAPI Method)", tag="foldervalue")
            dpg.add_input_text(label="Architecture Type", tag="archtype")
            dpg.add_button(label="Unlock DLC", callback=MainGUI.MainThread)
            dpg.add_button(label="Stop Music" ,callback=StopMusic)
        dpg.create_viewport(title='SteamXL by RiritoXXL', width=555, height=555)
        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.set_primary_window("mainwindow", True)
        dpg.start_dearpygui()
        dpg.destroy_context()