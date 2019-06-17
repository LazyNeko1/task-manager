import PySimpleGUI as sg
import psutil,time

# ----------------  Create Window  ----------------
sg.ChangeLookAndFeel('Black')
layout = [[sg.Text('')],
          [sg.Text('', size=(8, 2), font=('Helvetica', 20), justification='center', key='text')],
          [sg.ProgressBar(100, orientation='h', size=(10,10), key='membar')],
          [sg.ProgressBar(100, orientation='h', size=(10,10), key='rambar')],
          [sg.Exit(button_color=('white', 'firebrick4'), pad=((15, 0), 0))],
          [sg.Spin([x + 1 for x in range(10)], 1, key='spin'),
           sg.Text("Change Update time (s)")],
          
          [sg.Spin([x + 1 for x in range(10)], 1, key='transparency'),
          sg.Text("Change transparency")]]

window = sg.Window('Running Timer', layout, alpha_channel=1, no_titlebar=True, auto_size_buttons=False, keep_on_top=True,
                   grab_anywhere=True)

# ----------------  main loop  ----------------
while (True):
    # --------- Read and update window --------
    event, values = window.Read(timeout=0)

    # --------- Do Button Operations --------
    if event is None or event == 'Exit':
        break
    try:
        interval = int(values['spin'])
    except:
        interval= 1


    ram_percent = str(round(psutil.virtual_memory().percent))#(interval=interval)
    cpu_percent = str(round(psutil.cpu_percent(interval=0.1)))#(interval=interval)
    ram_1 = int(ram_percent)
    ram_2 = int(ram_percent)
    ram_3 = int(ram_percent)
    total=int(ram_1+ram_2+ram_3/3)
    # --------- Display timer in window --------

    window.Element('text').Update(f'MEM {ram_percent}%\nRAM {cpu_percent}%')
    window.Element('membar').UpdateBar(int(ram_percent))
    window.Element('rambar').UpdateBar(int(cpu_percent))
    transparency =  (int(values['transparency'])/10)
    f=open('transparency.txt', 'w')
    f.truncate(0)
    f.write(str(transparency))
    f.close()

# Broke out of main loop. Close the window.
window.Close()
