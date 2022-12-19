import socket
import tkinter as tk

def send(signal,ipaddr="127.0.0.1"):
    if signal=='2':
        send_data = 'SIGNAL2'
    elif signal=='1':
        send_data = 'SIGNAL1'
    else:
        send_data = signal
    #  create a udp socket
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #   senddata(data, (ip, port))
    udp_socket.sendto(send_data.encode("utf-8"), (ipaddr, 8888))
    #  close socket
    udp_socket.close()
    print("Sent successfully")


if __name__ == '__main__':
    window = tk.Tk()
    
    window.title('Control Panel')
    
    window.geometry('300x400') 
    
    var = tk.StringVar()  
    l = tk.Label(window, textvariable=var, bg='green', fg='white', font=('Arial', 12), width=30, height=2)
    l.pack()
    
    on_hit = False
    def cap():
        global on_hit
        if on_hit == False:
            on_hit = True
            ipaddr = change_state()
            send('2',ipaddr=ipaddr)
            var.set('excuted')
        else:
            on_hit = False
            var.set('')

    def block():
        global on_hit
        if on_hit == False:
            on_hit = True
            ipaddr = change_state()
            send('1',ipaddr=ipaddr)
            var.set('excuted')
        else:
            on_hit = False
            var.set('')

    def func_sig1long():
        global on_hit
        if on_hit == False:
            on_hit = True
            ipaddr = change_state()
            send('SIGNAL1_LONG',ipaddr=ipaddr)
            var.set('excuted')
        else:
            on_hit = False
            var.set('')

    def func_sig2long():
        global on_hit
        if on_hit == False:
            on_hit = True
            ipaddr = change_state()
            send('SIGNAL2_LONG',ipaddr=ipaddr)
            var.set('excuted')
        else:
            on_hit = False
            var.set('')

    def func_sig1major():
        global on_hit
        if on_hit == False:
            on_hit = True
            ipaddr = change_state()
            send('SIGNAL_1_MAJOR',ipaddr=ipaddr)
            var.set('excuted')
        else:
            on_hit = False
            var.set('')

    def func_sig2major():
        global on_hit
        if on_hit == False:
            on_hit = True
            ipaddr = change_state()
            send('SIGNAL_2_MAJOR',ipaddr=ipaddr)
            var.set('excuted')
        else:
            on_hit = False
            var.set('')

    def func_allbind():
        global on_hit
        if on_hit == False:
            on_hit = True
            ipaddr = change_state()
            send('ALLBLIND',ipaddr=ipaddr)
            var.set('excuted')
        else:
            on_hit = False
            var.set('')

    def func_allbind_release():
        global on_hit
        if on_hit == False:
            on_hit = True
            ipaddr = change_state()
            send('ALLBLIND_RELEASE',ipaddr=ipaddr)
            var.set('excuted')
        else:
            on_hit = False
            var.set('')

    def func_blank():
        global on_hit
        if on_hit == False:
            on_hit = True
            ipaddr = change_state()
            send('BLANK',ipaddr=ipaddr)
            var.set('excuted')
        else:
            on_hit = False
            var.set('')

    def exitt():
        exit(0)

    

    b = tk.Button(window, text='Send SIGNAL1 camera block', font=('Arial', 12), width=100, height=1, command=block)
    b.pack()

    p = tk.Button(window, text='Send SIGNAL2 camera protection', font=('Arial', 12), width=100, height=1, command=cap)
    p.pack()

    sig1long = tk.Button(window, text='Send SIGNAL1_LONG', font=('Arial', 12), width=100, height=1, command=func_sig1long)
    sig1long.pack()

    sig2long = tk.Button(window, text='Send SIGNAL2_LONG', font=('Arial', 12), width=100, height=1, command=func_sig2long)
    sig2long.pack()

    sig1major = tk.Button(window, text='Send SIGNAL_1_MAJOR', font=('Arial', 12), width=100, height=1, command=func_sig1major)
    sig1major.pack()

    sig2major = tk.Button(window, text='Send SIGNAL_2_MAJOR', font=('Arial', 12), width=100, height=1, command=func_sig2major)
    sig2major.pack()

    allbind = tk.Button(window, text='ALLBLIND', font=('Arial', 12), width=100, height=1, command=func_allbind)
    allbind.pack()

    allbind_release = tk.Button(window, text='ALLBLIND_RELEASE', font=('Arial', 12), width=100, height=1, command=func_allbind_release)
    allbind_release.pack()

    blank = tk.Button(window, text='Send signal BLANK', font=('Arial', 12), width=100, height=1, command=func_blank)
    blank.pack()




    entry = tk.Entry(window,width=20)
    entry.pack()

    def change_state():
        var = entry.get()		# Call the get() method to get the content in the Entry
        if len(var)<2:
            var = '127.0.0.1'
        return var
    button = tk.Button(window,text='Apply',command=change_state).pack()


    

    e = tk.Button(window, text='exit', font=('Arial', 12), width=10, height=1, command=exitt)
    e.pack()

    

    window.mainloop()