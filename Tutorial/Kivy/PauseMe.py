from functools import partial
import tkinter as tk
import threading
import time
#import vlc

global videoscreen_button_num
videoscreen_button_num = 0

global button_timer
global show_button
button_timer = 0
show_button = False


class video_window:
    def __init__(self, master, channel):  # create the windows
        self.master = master

        self.frame = tk.Frame(self.master)

        reset_encoder = tk.Button(self.frame, text='Reset Encoder', width=25, command=self.close_windows)  # create buttons to control the video
        reset_video = tk.Button(self.frame, text='Refresh Video', width=25, command=self.close_windows)
        return_button = tk.Button(self.frame, text='Return to Main Menu', width=25, command=self.close_windows)

        return_button.grid(row=0, column=0)
        reset_video.grid(row=0, column=1)
        reset_encoder.grid(row=0, column=2)

        unselected_colour = "SteelBlue1"
        selected_colour = "RoyalBlue1"

        return_button.config(background=selected_colour)
        reset_video.config(background=unselected_colour)
        reset_encoder.config(background=unselected_colour)

        self.frame.pack()

        self.video_button_ids = []
        self.video_button_ids.append(reset_encoder)
        self.video_button_ids.append(reset_video)
        self.video_button_ids.append(return_button)

        #Instance = vlc.Instance()  # '--verbose 2'.split())
        # self.player = Instance.media_player_new()
        # Media = Instance.media_new(channel)
        # Media.get_mrl()
        # self.player.set_media(Media)
        # player.set_fullscreen(False)
        # self.player.play()
        # self.player.set_fullscreen(True)

        master.attributes('-topmost', 'true')  # force the window to be infront

        time.sleep(5)  # give player time to load before spawning the control buttons

        master.bind('<Key>', partial(self.press_button))

        master.mainloop()

        self.timed_opacity_thread = threading.Thread(target=self.timed_opacity)  # make a thread which manage when the opacity of the buttons will turn on and off
        self.timed_opacity_thread.start()


    def press_button(self, event):  # tells the program what to do if a button is pressed
        print("pressed button in video screen")

        if show_button == True:  # if the opacity is set to be visable simple extend the time
            global button_timer
            button_timer = time.perf_counter()
        else:  # if the opacity is off turn it back on and place it into a thread to that other tasks can be performed at the same time.
            self.timed_opacity_thread = threading.Thread(target=self.timed_opacity)
            self.timed_opacity_thread.start()

        global videoscreen_button_num
        old_button_num = videoscreen_button_num
        print("button pressed", event.keycode)
        if event.keycode == 40:  # up button
            if videoscreen_button_num == 2:
                videoscreen_button_num = 0
            else:
                videoscreen_button_num = videoscreen_button_num + 1

        if event.keycode == 38:  # down
            if videoscreen_button_num == 0:
                videoscreen_button_num = 2
            else:
                videoscreen_button_num = videoscreen_button_num - 1

        if event.keycode == 37:  # right
            if videoscreen_button_num == 2:
                videoscreen_button_num = 0
            else:
                videoscreen_button_num = videoscreen_button_num + 1

        if event.keycode == 39:  # left
            if videoscreen_button_num == 0:
                videoscreen_button_num = 2
            else:
                videoscreen_button_num = videoscreen_button_num - 1

        if event.keycode == 13:  # enter
            print("pressed enter")
            self.video_button_ids[videoscreen_button_num].invoke()

        print("old button = ", old_button_num)
        print("new button = ", videoscreen_button_num)

        print("old object = ", self.video_button_ids[old_button_num])
        print("new object = ", self.video_button_ids[videoscreen_button_num])

        unselected_colour = "SteelBlue1"
        selected_colour = "RoyalBlue1"

        self.video_button_ids[old_button_num].config(background=unselected_colour)
        self.video_button_ids[videoscreen_button_num].config(background=selected_colour)

        print("")

    def timed_opacity(self):  # make the buttons fade when no user input is detected for a while and then reappear when a user input is detected
        self.master.attributes('-alpha', 1)

        global button_timer
        global show_button
        button_timer = time.perf_counter()
        show_button = True
        while time.perf_counter() - button_timer < 10:
            pass

        self.master.attributes('-alpha', .5)
        show_button = False

    def close_windows(self):
        self.player.stop()
        global show_button

        self.master.destroy()  # get rid of window, app still runs, not sure how to kill app

    def refresh_video(self):
        print("refresh video funtion")
        self.player.Refresh()


def main():
    root = tk.Tk()
    app = video_window(root, 'rtsp://192.168.8.20/4')  # the location of the video you wish to play
    root.mainloop()


if __name__ == '__main__':
    main()