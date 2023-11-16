import tkinter as tk
import socket
import time

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

def update_ip():
    global ip_address
    new_ip = get_ip_address()
    if new_ip != ip_address:
        ip_address = new_ip
        label.config(text=f"IP Address: {ip_address}")
    root.after(1000, update_ip)  # Check every 10 seconds

root = tk.Tk()
root.title("IP Address")

ip_address = get_ip_address()
label = tk.Label(root, text=f"IP Address: {ip_address}", font=("Helvetica", 16))
label.pack(pady=20)

update_ip()  # Start the periodic IP check

root.mainloop()
