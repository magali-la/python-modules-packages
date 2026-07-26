# Requires colorama; install with: pip install colorama
from colorama import init, Fore, Style

# this config ensure that it won't print everything in that color chosen for the specific line in the whole terminal for the rest of the script, it'll add an invisible reset automatically rather then you have to include that flag
init(autoreset=True)

print(Fore.GREEN + "This line is green!")
print("This line goes back to normal color.")
# this adds another style to the color chosen
print(Fore.GREEN + Style.DIM + "This line is a dim green!")
print("This line goes back to normal color.")