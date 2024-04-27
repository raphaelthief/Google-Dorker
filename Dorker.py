import os, argparse
from modules import DB, passcheck
from colorama import init, Fore, Style

init()

menu = (
    f"{Fore.GREEN}"
    f"  ____                   _       {Fore.RED} ____   ___  ____  _  _______ ____  {Fore.GREEN}\n"
    f" / ___| ___   ___   __ _| | ___  {Fore.RED}|  _ \ / _ \|  _ \| |/ / ____|  _ \ {Fore.GREEN}\n"
    f"| |  _ / _ \ / _ \ / _` | |/ _ \ {Fore.RED}| | | | | | | |_) | ' /|  _| | |_) |{Fore.GREEN}\n"
    f"| |_| | (_) | (_) | (_| | |  __/ {Fore.RED}| |_| | |_| |  _ <| . \| |___|  _ < {Fore.GREEN}\n"
    f" \____|\___/ \___/ \__, |_|\___| {Fore.RED}|____/ \___/|_| \_\_|\_\_____|_| \_\\{Fore.YELLOW} V1.0{Fore.GREEN}\n"
    f"                   |___/                          {Fore.CYAN}< By raphaelthief > {Fore.GREEN}\n\n"
    f"{Fore.YELLOW}For more CTI links and tools : {Fore.RED}https://start.me/p/kvvGLO/cti-osint{Fore.GREEN}"

)

def cleanit():
    os.system('cls' if os.name == 'nt' else 'clear') # Linux or Windows OS detection & compatibility
    print(menu)
    print(f"{Fore.YELLOW}Usage : {Fore.GREEN}dorker.py [-h] [-check CHECK] [-checklist CHECKLIST] [-e ENTREPRISE] [-m MAIL] [-L] [-li] [-f] [-db] [-c] [-l] [-p] [-b] [-C] [-t] [-r] [-rr]")
    print("\n------------------------------------------------------------------------------\n")

def main():
    cleanit()
    parser = argparse.ArgumentParser(description=f"{Fore.GREEN}Google{Fore.RED} DORKER{Fore.GREEN} - {Fore.BLUE}Cyber Threat Intelligence{Fore.GREEN}")
    parser.add_argument("-check", "--check", help="Check how many times a password is used (breach directory)") # ok
    parser.add_argument("-checklist", "--checklist", help="Check how many times a password is used (breach directory) from a file list") # ok
    parser.add_argument("-e", "--entreprise", help="Set entreprise site name (exemple.com)") # ok
    parser.add_argument("-m", "--mail", help="Search for an email (exemple@dns.fr or @dns.fr)") # ok
    parser.add_argument("-L", "--leaks", action="store_true", help="Search for leaks") # ok
    parser.add_argument("-li", "--linkedin", action="store_true", help="Search for employees exposure on Linkedin") # ok
    parser.add_argument("-f", "--files", action="store_true", help="Search for files (doc, docx, ppt, pptx, xls, xlsx, pdf, csv, txt)") # ok
    parser.add_argument("-db", "--database", action="store_true", help="Search for sql databases") # ok
    parser.add_argument("-c", "--config", action="store_true", help="Search for config files (.config, .cfg, .ini, robots.txt, htpasswd, htaccess, etc...)") # ok
    parser.add_argument("-l", "--logs", action="store_true", help="Search for logs files") # ok
    parser.add_argument("-p", "--passwords", action="store_true", help="Search for passwords") # ok
    parser.add_argument("-b", "--breaks", action="store_true", help="Search for bad website config or vulnerability") # ok
    parser.add_argument("-C", "--cache", action="store_true", help="Search for cache website") # ok
    parser.add_argument("-t", "--tor", action="store_true", help="Get tor links of actual ransomwares") # ok
    parser.add_argument("-r", "--run", action="store_true", help="Launch a Dorks search to see if there are some results aviable with timeout 5 (Danger : requests errors goes brrrrrrt !)") # ok
    parser.add_argument("-rr", "--runverbose", action="store_true", help="Same as --run but display realtime errors (not estetic, display large errors messages") # ok
    args = parser.parse_args()


    if not any(vars(args).values()):
        exit()

    # init DB and passcheck colorama
    DB.start()
    passcheck.start()
    
    # Only one without necessary args --> get tor links
    if args.tor and not args.entreprise:
        DB.torch() # Show only Ransomwares .onion links
        if not args.check:
            exit()
    else:
        pass

    # Password checker
    if args.check and not args.entreprise:
        passcheck.checkit(args.check)
        exit()
        
    # Password checker - list
    if args.checklist and not args.entreprise:
        passcheck.checklist(args.checklist)
        exit()
        
    # No args, no dorks
    if not args.entreprise:
        print("--entreprise argument needed !")
        exit()
    
    if args.run and not args.runverbose:
        DB.startX("brrrt")
    elif args.runverbose and not args.run:
        DB.startX("brrrtVERBOSE")
    elif args.runverbose and args.run:
        print("--run and --runverbose can't be run together")
        exit()


    ########### Start db exploit
    if args.mail: # Mails
        DB.mails(args.entreprise, args.mail)
    
    if args.linkedin: # LinkedIn
        DB.linkedinmedia(args.entreprise, args.mail)
    
    if args.leaks: # DB breach + Doxs + Leaks
        DB.leakedforums(args.entreprise, args.mail)
    
    if args.leaks: # Search for files
        DB.filesX(args.entreprise, args.mail)

    if args.database: # Search for DB
        DB.databases(args.entreprise)

    if args.config: # Search for config files
        DB.configurationX(args.entreprise)

    if args.logs: # Search for logs files
        DB.logsX(args.entreprise)

    if args.passwords: # Search for passwords
        DB.passX(args.entreprise, args.mail)

    if args.breaks: # Search for bad web config
        DB.breakit(args.entreprise)
        
    if args.cache: # Search for cache
        DB.cacheX(args.entreprise)

    if args.tor: # Show Ransomwares .onion links
        DB.torch() 
    

if __name__ == "__main__":
    main()
