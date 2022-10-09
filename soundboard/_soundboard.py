from pynput.keyboard import Key, KeyCode, Listener
from playsound import playsound
import tkinter as tk
import threading
import time
import json
import subprocess
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from pygame import mixer
import sdl2


path_sound = "soundboard\\sound\\"
path_json = 'soundboard\\setting.json'

global all_sounds_with_mp3
all_sounds_with_mp3 = os.listdir("soundboard\\sound\\")


def get_device(type_device):
    device = []
    mixer.init()
    for i in range(sdl2.audio.SDL_GetNumAudioDevices(type_device)):
        device.append(
            str(sdl2.audio.SDL_GetAudioDeviceName(i, type_device))[2:-1])
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


def get_json(path):
    data = []
    with open(path, 'r') as json_r:
        data = json.load(json_r)
        json_r.close()
    return data


def _reload():
    _reload.data_json = get_json(path_json)
    print('data loaded',_reload.data_json)
    _reload_mixer()


def _reload_mixer():
    try:
        mixer.quit()
    finally:
        try:
            mixer.init(devicename=str(_reload.data_json["output device"]))
            mixer.music.set_volume(_reload.data_json["volume"])
        except:
            print("  _something error_ \n")


def playx(name_song):
    try:
        mixer.music.unload()
    except:
        _reload_mixer()

    try:
        mixer.music.load(path_sound + name_song + ".mp3")
        mixer.music.play()
        print("  _ play " + name_song + ".mp3 ♪")
    except:
        print("  _ {:<20} not found _ ".format(str(name_song) + ".mp3"))


def error_():
    raise TypeError("  _stop it!_ ")


def nothing_():
    print('nothing')


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

    menu_input.add_cascade(label="output device", menu=menu_device, command=nothing_)
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

    volumemenu.add_cascade(label="sound level", menu=pikvolumemenu, command=nothing_)
    menubar.add_cascade(label="volume", menu=volumemenu)

    menu_quit = tk.Menu(menubar, tearoff=0)
    menu_quit.add_command(label="quit...", command=pud.destroy)
    menubar.add_cascade(label="Help", menu=menu_quit)

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


list_pressed_key = []
NUMPAD0 = KeyCode(0x60)
NUMPAD1 = KeyCode(0x61)
NUMPAD2 = KeyCode(0x62)
NUMPAD3 = KeyCode(0x63)
NUMPAD4 = KeyCode(0x64)
NUMPAD5 = KeyCode(0x65)
NUMPAD6 = KeyCode(0x66)
NUMPAD7 = KeyCode(0x67)
NUMPAD8 = KeyCode(0x68)
NUMPAD9 = KeyCode(0x69)

_HOTKEYS = {
    frozenset([Key.alt_l, NUMPAD0]): lambda: playx(_reload.data_json['_key']['0']),
    frozenset([Key.alt_l, NUMPAD1]): lambda: playx(_reload.data_json['_key']['1']),
    frozenset([Key.alt_l, NUMPAD2]): lambda: playx(_reload.data_json['_key']['2']),
    frozenset([Key.alt_l, NUMPAD3]): lambda: playx(_reload.data_json['_key']['3']),
    frozenset([Key.alt_l, NUMPAD4]): lambda: playx(_reload.data_json['_key']['4']),
    frozenset([Key.alt_l, NUMPAD5]): lambda: playx(_reload.data_json['_key']['5']),
    frozenset([Key.alt_l, NUMPAD6]): lambda: playx(_reload.data_json['_key']['6']),
    frozenset([Key.alt_l, NUMPAD7]): lambda: playx(_reload.data_json['_key']['7']),
    frozenset([Key.alt_l, NUMPAD8]): lambda: playx(_reload.data_json['_key']['8']),
    frozenset([Key.alt_l, NUMPAD9]): lambda: playx(_reload.data_json['_key']['9']),
}


def get_vk(key):
    return key.vk if hasattr(key, 'vk') else key.value.vk


def is_combination_pressed(combination):
    return all([get_vk(key) in list_pressed_key for key in combination])


def func_on_press(key):
    vk = get_vk(key)
    if vk not in list_pressed_key:
        list_pressed_key.append(vk)
    for combination in _HOTKEYS:
        if is_combination_pressed(combination):
            _HOTKEYS[combination]()
            del list_pressed_key[1:]


def func_on_release(key):
    vk = get_vk(key)
    if vk in list_pressed_key:
        list_pressed_key.remove(vk)


def _Hotkey():
    with Listener(on_press=func_on_press, on_release=func_on_release) as listener:
        listener.join()


def main():
    _reload()
    thread_Window = threading.Thread(target=UI_window).start()
    thread_HotKey = threading.Thread(target=_Hotkey).start()


if __name__ == '__main__':
    main()
