from playsound import playsound
from pygame import mixer
import pygame
import tkinter as tk
import keyboard
import sdl2
import threading
import time
import subprocess
import json
import os


path_sound = "soundboard\\sound\\"
path_json = 'soundboard\\setting.json'


global all_sounds_with_mp3
all_sounds_with_mp3 = os.listdir("soundboard\\sound\\")


print("\n", ('-' * 50), "\n")


def get_device(type_device):
    device = []
    mixer.init()
    for i in range(sdl2.audio.SDL_GetNumAudioDevices(type_device)):
        device.append(
            str(sdl2.audio.SDL_GetAudioDeviceName(i, type_device))[2:-1]
        )
    mixer.quit()
    return device


def get_device_select():
    device_selected = device_select.get()
    print('set output device :', device_selected)
    data = []
    with open(path_json, 'r') as json_r:
        data = json.load(json_r)
        data["output device"] = device_selected
        new_data = json.dumps(data, indent=4, sort_keys=False)
        with open(path_json, 'w') as json_w:
            json_w.write(new_data)
            json_w.close()
        json_r.close()
    _reload()


def get_volume_select():
    volume_selected = volume_select.get()
    print('set volume :', volume_selected)
    data = []
    with open(path_json, 'r') as json_r:
        data = json.load(json_r)
        data["volume"] = float(volume_selected)
        new_data = json.dumps(data, indent=4, sort_keys=False)
        with open(path_json, 'w') as json_w:
            json_w.write(new_data)
            json_w.close()
        json_r.close()
    _reload()


def get_json():
    data = []
    with open(path_json, 'r') as json_r:
        data = json.load(json_r)
        json_r.close()
    return data


def _reload():
    _reload.data_json = get_json()
    #print('data loaded',_reload.data_json)
    _reload_mixer()


def _reload_mixer():
    try:
        mixer.quit()
    finally:
        try:
            mixer.init(devicename=str(_reload.data_json["output device"]))
        except:
            print("  _output missing_ \n")


def playx(name_song):
    try:
        mixer.music.unload()
    except:
        pass
    finally:
        _reload_mixer()

    try:
        mixer.music.load(path_sound + name_song + ".mp3")
        mixer.music.set_volume(_reload.data_json["volume"])
        mixer.music.play()
        print("  _play " + name_song + ".mp3")
        # time.sleep(.05)
    except FileNotFoundError:
        print("  _ " + name_song + ".mp3\tnot found _ ")


def UI_window():
    pud = tk.Tk()
    pud.geometry("500x500")
    pud.minsize(0, 500)
    pud.maxsize(500, 1000)
    pud.title("Hello world")

    menubar = tk.Menu(pud)
    menu_input = tk.Menu(menubar, tearoff=0)
    menu_device = tk.Menu(menu_input, tearoff=0)

    device_name = get_device(0)
    global device_select
    device_select = tk.StringVar(
        None, _reload.data_json["output device"])
    for i in range(len(device_name)):
        menu_device.add_radiobutton(
            label=device_name[i],
            variable=device_select,
            value=str(device_name[i]),
            command=get_device_select
        )

    menu_input.add_cascade(
        label="output device", menu=menu_device, command=nothing
    )
    menubar.add_cascade(label="input", menu=menu_input)

    volumemenu = tk.Menu(menubar, tearoff=0)
    pikvolumemenu = tk.Menu(volumemenu, tearoff=0)

    global volume_select
    volume_select = tk.StringVar(
        None, float(_reload.data_json["volume"]))
    for i in range(101):
        pikvolumemenu.add_radiobutton(
            label=i,
            variable=volume_select,
            value=int(i)/100,
            command=get_volume_select
        )

    volumemenu.add_cascade(
        label="sound level", menu=pikvolumemenu, command=nothing
    )
    menubar.add_cascade(label="volume", menu=volumemenu)

    helpmenu = tk.Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Help Index", command=nothing)
    helpmenu.add_command(label="About...", command=nothing)
    menubar.add_cascade(label="Help", menu=helpmenu)

    i_row = 0
    i_colum = 0
    for i in range(len(all_sounds_with_mp3)):
        buttonz = tk.Button(
            text=all_sounds_with_mp3[i],
            command=lambda i=i: playx(str(all_sounds_with_mp3[i])[0:-4]),
            bd=1, height=2, width=12,
        ).grid(row=i_row, column=i_colum, padx=4, pady=4)

        if i_colum != 4:
            i_colum += 1
        else:
            i_row += 1
            i_colum = 0

    pud.config(menu=menubar)
    pud.mainloop()


def keyboard_match():
    while True:
        match keyboard.read_key():
            case '1':
                playx(_reload.data_json["_key"]['1'])
            case '2':
                playx(_reload.data_json["_key"]['2'])
            case '3':
                playx(_reload.data_json["_key"]['3'])
            case '4':
                playx(_reload.data_json["_key"]['4'])
            case '5':
                playx(_reload.data_json["_key"]['5'])
            case '6':
                playx(_reload.data_json["_key"]['6'])
            case '7':
                playx(_reload.data_json["_key"]['7'])
            case '8':
                playx(_reload.data_json["_key"]['8'])
            case '9':
                playx(_reload.data_json["_key"]['9'])
            case '0':
                playx(_reload.data_json["_key"]['0'])
            case _:
                pass


def keyboard_ifelse():
    while True:
        # print(keyboard.read_key())
        if keyboard.read_key() in _reload.data_json['_key'].keys():
            playx(_reload.data_json["_key"][keyboard.read_key()])


def error_():
    raise TypeError("  _stop it!_ ")


def nothing():
    print('nothing')


def main():
    _reload()
    subprocess.Popen('rundll32.exe Shell32.dll,Control_RunDLL Mmsys.cpl,,1')

    global typex_
    typex_ = ''

    while True:
        typex_ = input("\t- chose type : ")
        if (typex_ != '0' and typex_ != '1' and typex_ != '2' and typex_ != '3'):
            print("  _ not found _ ")
        else:
            break

    match typex_:
        case '1':
            while True:
                soundx = input(" -; ")
                playx(soundx)
        case '2':
            keyboard_match()
        case '3':
            UI_window()
        case '0':
            thread_UIWindow = threading.Thread(target=UI_window).start()
            thread_Keyboard = threading.Thread(target=keyboard_ifelse).start()
        case _:
            pass


if __name__ == '__main__':
    main()


print("\n", ('-' * 50), "\n")
