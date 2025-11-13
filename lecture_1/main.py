from colorama import init, Fore, Back, Style

# Initialize colorama for cross-platform colored terminal output
init()

# Print colored Hello World
print(f"{Fore.RED}{Back.YELLOW}Hellow World!{Style.RESET_ALL}")
print(f"{Fore.GREEN}Hellow World in Green!{Style.RESET_ALL}")
print(f"{Fore.BLUE}{Style.BRIGHT}Hellow World in Bright Blue!{Style.RESET_ALL}")
print(f"{Fore.MAGENTA}{Back.CYAN}Hellow World with Magenta text and Cyan background!{Style.RESET_ALL}")
