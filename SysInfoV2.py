from tkinter import *
import platform
import psutil
from hurry.filesize import size
from datetime import datetime
import tkinter.scrolledtext as tkscrolled
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from psutil import cpu_percent

root = Tk()
root.title('SysInfoV2 by Juss Patel')
root.configure(background = "#1c1b19")
    
Header = Label(root , text = "SysInfoV2" ,fg = "white" ,bg = "#1c1b19", font = ("Courier New" , 25,"bold"))
Header.grid(row =0 ,column = 0 , columnspan = 3)
basic = LabelFrame(root , text = "Basic Info", fg = "white" ,bg = "#1c1b19",font = ("Microsoft PhagsPa" , 15))
basic.grid(row = 2 , column = 0)
boot = LabelFrame(root , text = "Boot time",fg = "white" ,bg = "#1c1b19", font = ("Microsoft PhagsPa" , 15))
boot.grid(row = 3 , column = 0)
memory = LabelFrame(root , text = "Memory Information", fg = "white" ,bg = "#1c1b19",font = ("Microsoft PhagsPa" , 15))
memory.grid(row = 4 , column = 0)
cpuinfo = LabelFrame(root , text = "CPU Information", fg = "white" ,bg = "#1c1b19",font = ("Microsoft PhagsPa" , 15))
cpuinfo.grid(row = 2 , column = 1)
disk = LabelFrame(root , text = "Disk Info",fg = "white" ,bg = "#1c1b19", font = ("Microsoft PhagsPa" , 15))
disk.place(x = 367 , y = 225)
basicnet = LabelFrame(root , text = "Basic Network Info",fg = "white" ,bg = "#1c1b19", font = ("Microsoft PhagsPa" , 15))
basicnet.grid(row = 5 , column =0)
graph = LabelFrame(root , text = "Basic Network Info",fg = "white" ,bg = "#1c1b19", font = ("Microsoft PhagsPa" , 15))
graph.place(x = 370 , y = 325)
T = Text(basic , height = 9 , width = 45 , bg = "black" , fg = "white")
T.pack()

  
uname = platform.uname()
T.insert(END,f"System: {uname.system}\n")
T.insert(END,f"Node Name: {uname.node}\n")
T.insert(END,f"Release: {uname.release}\n")
T.insert(END,f"Version: {uname.version}\n")
T.insert(END,f"Machine: {uname.machine}\n")
T.insert(END,f"Processor: {uname.processor}\n")

T2 = Text(boot , height = 2 , width = 45 , bg = "black" , fg = "white")
T2.pack()
boot_time_timestamp = psutil.boot_time()
bt = datetime.fromtimestamp(boot_time_timestamp)
T2.insert(END ,f"Boot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}\n")
T3 = Text(memory,  height = 11 , width = 45 , bg="black" , fg = "white")
T3.pack()
svmem = psutil.virtual_memory()
T3.insert(END , f"Total: {size(svmem.total)}\n")
T3.insert(END , f"Available: {size(svmem.available)}\n")
T3.insert(END , f"Used: {size(svmem.used)}\n")
T3.insert(END , f"Percentage: {svmem.percent}%\n\n")
T3.insert(END , "SWAP MEMORY\n\n")
swap = psutil.swap_memory()
T3.insert(END , f"Total: {size(swap.total)}\n")
T3.insert(END , f"Free: {size(swap.free)}\n")
T3.insert(END , f"Used: {size(swap.used)}\n")
T3.insert(END , f"Percentage: {swap.percent}%\n")

T4 = Text(cpuinfo , height = 9 , width = 44 , bg = "black" , fg = "white")
T4.pack()
T4.insert(END,"Total cores :"+ str(psutil.cpu_count(logical=True)) + '\n')

cpufreq = psutil.cpu_freq()
T4.insert(END,f"Max Frequency: {cpufreq.max:.2f}Mhz\n")
T4.insert(END,f"Min Frequency: {cpufreq.min:.2f}Mhz\n")
T4.insert(END,f"Current Frequency: {cpufreq.current:.2f}Mhz\n")

for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
    T4.insert(END,f"Core {i}: {percentage}%\n")
T4.insert(END,f"Total CPU Usage: {psutil.cpu_percent()}%")
T5 = Text(disk , height = 14 , width = 44 , bg = "black" , fg = "white")
T5.pack()
partitions = psutil.disk_partitions()
for partition in partitions:
    T5.insert(END,f" Drive: {partition.device} \n")
    T5.insert(END,f"  Mountpoint: {partition.mountpoint}\n")
    T5.insert(END,f"  File system type: {partition.fstype}\n")
    try:
        partition_usage = psutil.disk_usage(partition.mountpoint)
    except PermissionError:
        continue
    T5.insert(END,f"  Total Size: {size(partition_usage.total)}\n")
    T5.insert(END,f"  Used: {size(partition_usage.used)}\n")
    T5.insert(END,f"  Free: {size(partition_usage.free)}\n")
    T5.insert(END,f"  Percentage: {partition_usage.percent}%\n\n")
disk_io = psutil.disk_io_counters()
T5.insert(END,f"Total read: {size(disk_io.read_bytes)}\n")
T5.insert(END,f"Total write: {size(disk_io.write_bytes)}\n")
T6 = Text(basicnet , height = 3 , width = 45 , bg = "black" , fg = "white")
T6.pack()
net_io = psutil.net_io_counters()
fig = plt.Figure()
def cputusage():
    frame_len = 200
    y = []

    def animate(i) :
        x = psutil.cpu_times()
        z = x.user
        #print(z)
        y.append(z)
        if len(y) <= frame_len:
            plt.cla()
            plt.plot(y , 'r' , label = "CPU")
            
        plt.tight_layout()
    ani = FuncAnimation(plt.gcf() , animate , interval = 1000)
    plt.show()
def memusage():
    frame_len = 200
    y = []

    def animate(i) :
        x = psutil.cpu_freq()
        z = x.current
        y.append(z)
        if len(y) <= frame_len:
            plt.cla()
            plt.plot(y , 'r' , label = "CPU")
            
        plt.tight_layout()
    ani = FuncAnimation(plt.gcf() , animate , interval = 1000)
    plt.show()
def cpuusage():
    #newWindow = Toplevel(root)
    frame_len = 200
    y = []
    def animate(i) : 
        y.append(cpu_percent())
        if len(y) <= frame_len:
            plt.cla()
            plt.plot(y , 'r' , label = "CPU")
            
        plt.tight_layout()
    ani = FuncAnimation(plt.gcf() , animate , interval = 1000)
    plt.show()
def statsusage():
    frame_len = 200
    y = []

    def animate(i) :
        x = psutil.cpu_stats()
        z = x.ctx_switches
        
        y.append(z)
        
        if len(y) <= frame_len:
            plt.cla()
            plt.plot(y , 'r' , label = "CPU")
          
        plt.tight_layout()
    ani = FuncAnimation(plt.gcf() , animate , interval = 1000)
    plt.show()

        

T6.insert(END , f"Total Bytes Sent: {size(net_io.bytes_sent)}\n")
T6.insert(END , f"Total Bytes Received: {size(net_io.bytes_recv)}\n")
b1 = Button(root,text = "Check Current Cpu Usage\n         " , command = cpuusage ,width = 25 ).place(x = 370 , y = 540 )
b2 = Button(root,text = "Check Current Cpu \nFrequency (Mhz)" , command = memusage,width = 24 ).place(x = 550 , y = 490)
b3 = Button(root,text = "Check No. of Context \nSwitches since boot" , command = statsusage,width = 24 ).place(x = 550 , y = 540)
b4 = Button(root,text = "          Check time spent by \nprocesses executing in user mode" , command = cputusage, width = 25 ,).place(x = 370 , y = 490)

root.mainloop()
