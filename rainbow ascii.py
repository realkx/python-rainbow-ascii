import time
import os
import sys
from colorama import init, Fore

if os.name == 'nt':
    os.system('title  github.com/realkx')
else:  
    sys.stdout.write("\x1b]2; github.com/realkx\x07")
    sys.stdout.flush()

init()  

your_ascii = """
██╗   ██╗ ██████╗ ██╗   ██╗██████╗      █████╗ ███████╗ ██████╗██╗██╗
╚██╗ ██╔╝██╔═══██╗██║   ██║██╔══██╗    ██╔══██╗██╔════╝██╔════╝██║██║
 ╚████╔╝ ██║   ██║██║   ██║██████╔╝    ███████║███████╗██║     ██║██║
  ╚██╔╝  ██║   ██║██║   ██║██╔══██╗    ██╔══██║╚════██║██║     ██║██║
   ██║   ╚██████╔╝╚██████╔╝██║  ██║    ██║  ██║███████║╚██████╗██║██║
   ╚═╝    ╚═════╝  ╚═════╝ ╚═╝  ╚═╝    ╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝╚═╝
"""

colors = [Fore.GREEN, Fore.BLUE, Fore.RED, Fore.YELLOW, Fore.MAGENTA, Fore.CYAN]

try:
    while True:
        for color in colors:
            os.system('cls' if os.name == 'nt' else 'clear')  
            print(color + your_ascii)
            time.sleep(0.08)  # TIME BETWEEN CHANGING COLORS
except KeyboardInterrupt:
    print(Fore.RESET + "Goodbye!")
    sys.exit(0)