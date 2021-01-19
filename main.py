import tkinter as tk
import winsound

root = tk.Tk()
root.rowconfigure([0, 1, 2], minsize=150, weight=1)
root.columnconfigure([0, 1], minsize=200, weight=1)
root.wm_title('Two Timer')
font_family = 'Tahoma'


def break_time_decrease():
    number = int(lbl_break_time["text"])
    lbl_break_time["text"] = str(number - 1)


def break_time_increase():
    number = int(lbl_break_time["text"])
    lbl_break_time["text"] = str(number + 1)


frm_break_time = tk.Frame(master=root)
frm_break_time.rowconfigure([0, 1, 2], weight=1)
frm_break_time.columnconfigure([0, 1], weight=1)
frm_break_time.grid(row=0, column=0)
lbl_break_time_description = tk.Label(master=frm_break_time,
                                      text='Break Length',
                                      font=font_family + ' 16')
lbl_break_time_description.grid(row=0, column=0, columnspan=2)
lbl_break_time = tk.Label(master=frm_break_time, text="5", font=font_family + ' 20')
lbl_break_time.grid(row=1, column=0, columnspan=2)
btn_break_time_decrease = tk.Button(master=frm_break_time,
                                    text='-',
                                    font=font_family + ' 16',
                                    command=break_time_decrease)
btn_break_time_decrease.grid(row=2, column=0)
btn_break_time_increase = tk.Button(master=frm_break_time,
                                    text='+',
                                    font=font_family + ' 16',
                                    command=break_time_increase)
btn_break_time_increase.grid(row=2, column=1)


def session_time_decrease():
    number = int(lbl_session_time["text"])
    if lbl_activity['text'] == 'Session' and lbl_timer['text'].split(':')[0] == lbl_session_time['text']:
        lbl_session_time["text"] = str(number - 1)
        lbl_timer['text'] = lbl_session_time['text'] + ':00'
    else:
        lbl_session_time["text"] = str(number - 1)


def session_time_increase():
    number = int(lbl_session_time["text"])
    if lbl_activity['text'] == 'Session' and lbl_timer['text'].split(':')[0] == lbl_session_time['text']:
        lbl_session_time["text"] = str(number + 1)
        lbl_timer['text'] = lbl_session_time['text'] + ':00'
    else:
        lbl_session_time["text"] = str(number + 1)


frm_session_time = tk.Frame(master=root)
frm_session_time.rowconfigure([0, 1, 2], weight=1)
frm_session_time.columnconfigure([0, 1], weight=1)
frm_session_time.grid(row=0, column=1)
lbl_session_time_description = tk.Label(master=frm_session_time,
                                        text='Session Length',
                                        font=font_family + ' 16')
lbl_session_time_description.grid(row=0, column=0, columnspan=2)
lbl_session_time = tk.Label(master=frm_session_time, text="25", font=font_family + ' 20')
lbl_session_time.grid(row=1, column=0, columnspan=2)
btn_session_time_decrease = tk.Button(master=frm_session_time,
                                      text='-',
                                      font=font_family + ' 16',
                                      command=session_time_decrease)
btn_session_time_decrease.grid(row=2, column=0)
btn_session_time_increase = tk.Button(master=frm_session_time,
                                      text='+',
                                      font=font_family + ' 16',
                                      command=session_time_increase)
btn_session_time_increase.grid(row=2, column=1)

frm_timer = tk.Frame(master=root)
frm_timer.rowconfigure([0, 1], weight=1)
frm_timer.grid(row=1, column=0, columnspan=2)

lbl_activity = tk.Label(master=frm_timer, text='Session', font=font_family + ' 23')
lbl_activity.grid(row=0)
lbl_timer = tk.Label(master=frm_timer, text=lbl_session_time['text'] + ':00', font=font_family + ' 48')
lbl_timer.grid(row=1)


def start_timer():
    if btn_start_timer['text'] == 'Start':
        btn_start_timer['text'] = 'Pause'
    else:
        btn_start_timer['text'] = 'Start'


def reset_timer():
    btn_start_timer['text'] = 'Start'
    lbl_timer['text'] = lbl_session_time['text'] + ':00'
    lbl_activity['text'] = 'Session'


btn_start_timer = tk.Button(master=root, text='Start', command=start_timer, font=font_family + ' 16')
btn_start_timer.grid(row=2, column=0)
btn_reset_timer = tk.Button(master=root, text='Reset', command=reset_timer, font=font_family + ' 16')
btn_reset_timer.grid(row=2, column=1)


def update_timer():
    if btn_start_timer['text'] == 'Pause':
        remaining_time = str(lbl_timer['text']).split(':')
        remaining_seconds = int(remaining_time[0]) * 60 + int(remaining_time[1])
        if remaining_seconds > 0:
            remaining_seconds -= 1
        else:
            if lbl_activity['text'] == 'Session':
                lbl_activity['text'] = 'Break'
                remaining_time = str(lbl_break_time['text'])
                remaining_seconds = int(remaining_time) * 60
                winsound.PlaySound('c:\\windows\\Media\\Alarm01.wav', winsound.SND_ASYNC)
            else:
                lbl_activity['text'] = 'Session'
                remaining_time = str(lbl_session_time['text'])
                remaining_seconds = int(remaining_time) * 60
                winsound.PlaySound('c:\\windows\\Media\\Alarm01.wav', winsound.SND_ASYNC)
        lbl_timer['text'] = str(remaining_seconds//60) + ':' + str(remaining_seconds % 60).rjust(2, '0')
    root.after(1000, lambda: update_timer())


update_timer()
root.mainloop()
