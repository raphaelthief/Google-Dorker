import time
from colorama import init, Fore, Style
from googlesearch import search
from urllib.error import HTTPError



def start():
    init()

doIbrrrt = "HellNo"

########################################### Start Dorks search requests
def startX(datas):
    global doIbrrrt
    if datas == "brrrt":
        doIbrrrt = "HellYes"
    elif datas == "brrrtVERBOSE":
        doIbrrrt = "HellVerbose"
    else:
        doIbrrrt = "HellNo"


########################################### Print results
def printitX(datas):
    global doIbrrrt
    dorks_lines = datas.split('\n')
    for i in range(len(dorks_lines)):
        
        if doIbrrrt == "HellYes" or "HellVerbose":
            Dorksearch(dorks_lines[i])
        else:
            print("    " + dorks_lines[i])
    

########################################### Emails dorks
def mails(ent, mail):
    
    email_dorks = (
        f"""site:{ent} {mail}\n"""
        f"""site:{ent} intext:{mail}\n"""
        f"""site:{ent} intext:contact OR intext:info OR intext:support OR intext:admin\n"""
        f"""site:{ent} inurl:contact OR inurl:about OR inurl:info OR inurl:staff\n"""
        f"""site:{ent} inurl:email OR inurl:mail\n"""
        f"""site:{ent} filetype:txt OR filetype:csv OR filetype:xls OR filetype:xlsx intext:{mail}"""
    )
    print(f"\n{Fore.RED}[+] {Fore.YELLOW}Emails Dorks :{Fore.GREEN}")
    printitX(email_dorks)
    


########################################### Tor Ransomwares Links
def torch():
    # Get Ransomwares tor links
    tor_dorks = (
        f"""    {Fore.YELLOW}LockBit : {Fore.GREEN}lockbit7z2jwcskxpbokpemdxmltipntwlkmidcll2qirbu7ykg46eyd.onion\n"""
        f"""    {Fore.YELLOW}LockBit 3.0 : {Fore.GREEN}lockbit7z2jwcskxpbokpemdxmltipntwlkmidcll2qirbu7ykg46eyd.onion\n"""
        f"""    {Fore.YELLOW}INC Ransom : {Fore.GREEN}incblog7vmuq7rktic73r4ha4j757m3ptym37tyvifzp2roedyyzzxid.onion/blog/leaks\n"""
        f"""    {Fore.YELLOW}Ragnar_Locker : {Fore.GREEN}rgleaktxuey67yrgspmhvtnrqtgogur35lwdrup4d3igtbm3pupc4lyd.onion\n"""
        f"""    {Fore.YELLOW}Cuba Ransomware : {Fore.GREEN}cuba4ikm4jakjgmkezytyawtdgr2xymvy6nvzgw5cglswg3si76icnqd.onion\n"""
        f"""    {Fore.YELLOW}CLOP : {Fore.GREEN}santat7kpllt6iyvqbr7q4amdv6dzrh6paatvyrzl7ry3zm72zigf4ad.onion\n"""
        f"""    {Fore.YELLOW}Alphv : {Fore.GREEN}alphvmmm27o3abo3r2mlmjrpdmzle3rykajqc5xsj7j7ejksbpsa36ad.onion\n"""
        f"""    {Fore.YELLOW}Snatch : {Fore.GREEN}hl66646wtlp2naoqnhattngigjp5palgqmbwixepcjyq5i534acgqyad.onion\n"""
        f"""    {Fore.YELLOW}RansomEXX : {Fore.GREEN}rnsm777cdsjrsdlbs4v5qoeppu3px6sb2igmh53jzrx7ipcrbjz5b2ad.onion\n"""
        f"""    {Fore.YELLOW}Everest : {Fore.GREEN}ransomocmou6mnbquqz44ewosbkjk3o5qjsl3orawojexfook2j7esad.onion\n"""
        f"""    {Fore.YELLOW}Play : {Fore.GREEN}mbrlkbtq5jonaqkurjwmxftytyn2ethqvbxfu4rgjbkkknndqwae6byd.onion\n"""
        f"""    {Fore.YELLOW}Omega : {Fore.GREEN}omegalock5zxwbhswbisc42o2q2i54vdulyvtqqbudqousisjgc7j7yd.onion\n"""
        f"""    {Fore.YELLOW}Medusa : {Fore.GREEN}medusaxko7jxtrojdkxo66j7ck4q5tgktf7uqsqyfry4ebnxlcbkccyd.onion\n"""
        f"""    {Fore.YELLOW}Qilin : {Fore.GREEN}kbsqoivihgdmwczmxkbovk7ss2dcynitwhhfu5yw725dboqo5kthfaad.onion\n"""
        f"""    {Fore.YELLOW}RansomHouse : {Fore.GREEN}zohlm7ahjwegcedoz7lrdrti7bvpofymcayotp744qhx6gjmxbuo2yid.onion\n"""
        f"""    {Fore.YELLOW}Other links : {Fore.GREEN}ransomwr3tsydeii4q43vazm7wofla5ujdajquitomtd47cxjtfgwyyd.onion"""
    )
    print(f"\n{Fore.RED}[+] {Fore.YELLOW}Tor Ransomwares Links :{Fore.GREEN}")
    print(tor_dorks)


########################################### Linkedin dorks
def linkedinmedia(ent, mail):
    global doIbrrrt
    if ent is not None:
        data = (
            f"""site:media.licdn.com intitle:cv intext:{ent}\n"""
            f"""site:content.linkedin.com intext:cv intitle:{ent}\n"""
            f"""site:media.licdn.com {ent}"""
        )
        print(f"\n{Fore.RED}[+] {Fore.YELLOW}Entreprise Linkedin Dorks :{Fore.GREEN}")
        printitX(data)

    else:
        pass

    if mail is not None:
        data = (
            f"""site:media.licdn.com intitle:cv intext:{mail}\n"""
            f"""site:content.linkedin.com intext:cv intitle:{mail}\n"""
            f"""site:media.licdn.com {mail}"""
        )
        print(f"\n{Fore.RED}[+] {Fore.YELLOW}Email Linkedin Dorks :{Fore.GREEN}")
        printitX(data)
    else:
        pass


########################################### Doxing + Breach forums + Markets
def leakedforums(ent, mail):
    global doIbrrrt
    if ent is not None:
        ent2 = ent
        if "." in ent:
            ent2 = ent.split(".")[0]
        else:
            pass
        data = (
            f"""site:crackingx.com intext:{ent2}\n"""
            f"""site:patched.to intext:{ent2}\n"""
            f"""site:breachforums.cx intext:{ent2}\n"""
            f"""site:nulled.to intext:{ent2}\n"""
            f"""site:darkforums.me intext:{ent2}\n"""
            f"""site:doxbin.org intext:{ent2}\n"""
            f"""site:hackforums.net intext:{ent2}\n"""
            f"""site:demonforums.net intext:{ent2}\n"""
            f"""site:blackhatworld.com intext:{ent2}\n"""
            f"""site:instant-hack.to intext:{ent2}\n"""
            f"""site:sinister.ly intext:{ent2}\n"""
            f"""site:pastebin.com intext:{ent2}"""
        )
        print(f"\n{Fore.RED}[+] {Fore.YELLOW}Entreprise Breached Forums Dorks :{Fore.GREEN}")
        printitX(data)
        print(f"\n{Fore.RED}--> {Fore.GREEN}intext:{ent2} site:crackingx.com OR site:patched.to OR site:breachforums.cx OR site:nulled.to OR site:darkforums.me OR site:doxbin.org OR site:hackforums.net OR site:demonforums.net OR site:blackhatworld.com OR site:instant-hack.to OR site:sinister.ly OR site:pastebin.com\n")
    else:
        pass

    if mail is not None:
        data = (
            f"""site:crackingx.com intext:{mail}\n"""
            f"""site:patched.to intext:{mail}\n"""
            f"""site:breachforums.cx intext:{mail}\n"""
            f"""site:nulled.to intext:{mail}\n"""
            f"""site:darkforums.me intext:{mail}\n"""
            f"""site:doxbin.org intext:{mail}\n"""
            f"""site:hackforums.net intext:{mail}\n"""
            f"""site:demonforums.net intext:{mail}\n"""
            f"""site:blackhatworld.com intext:{mail}\n"""
            f"""site:instant-hack.to intext:{mail}\n"""
            f"""site:sinister.ly intext:{mail}\n"""
            f"""site:pastebin.com intext:{mail}"""
        )
        print(f"\n{Fore.RED}[+] {Fore.YELLOW}Email Breached Forums Dorks :{Fore.GREEN}")
        printitX(data)
        print(f"\n{Fore.RED}--> {Fore.GREEN}intext:{mail} site:crackingx.com OR site:patched.to OR site:breachforums.cx OR site:nulled.to OR site:darkforums.me OR site:doxbin.org OR site:hackforums.net OR site:demonforums.net OR site:blackhatworld.com OR site:instant-hack.to OR site:sinister.ly OR site:pastebin.com\n")
    else:
        pass


########################################### Search for files
def filesX(ent, mail):
    global doIbrrrt
    if ent is not None:
        ent2 = ent
        if "." in ent:
            ent2 = ent.split(".")[0]
        else:
            pass

        data = (
            f"""inurl:{ent2} filetype:doc OR filetype:docx OR filetype:ppt OR filetype:pptx OR filetype:xls OR filetype:xlsx OR filetype:pdf OR filetype:txt OR filetype:csv"""
        )
        print(f"\n{Fore.RED}[+] {Fore.YELLOW}Entreprise Files Dorks :{Fore.GREEN}")
        printitX(data)
    else:
        pass

    if mail is not None:
        data = (
            f"""inurl:{mail} filetype:doc OR filetype:docx OR filetype:ppt OR filetype:pptx OR filetype:xls OR filetype:xlsx OR filetype:pdf OR filetype:txt"""
        )
        print(f"\n{Fore.RED}[+] {Fore.YELLOW}Email Files Dorks :{Fore.GREEN}")
        printitX(data)
        print(f"\n{Fore.RED}--> {Fore.GREEN}intext:{mail} site:crackingx.com OR site:patched.to OR site:breachforums.cx OR site:nulled.to OR site:darkforums.me OR site:doxbin.org OR site:hackforums.net OR site:demonforums.net OR site:blackhatworld.com OR site:instant-hack.to OR site:sinister.ly\n")


########################################### Search for databases
def databases(ent):
    global doIbrrrt
    if ent is not None:
        data = (
            f"""site:{ent} intitle:"index of" ( database.sql OR database.bak OR database.sql.gz OR database.sql.zip OR database.mdb OR database.accdb OR database.sqlite OR database.db OR database.dbf OR database.mdf OR database.ldf OR database.ndf )\n"""
            f"""site:{ent} intitle:"index of" intext:*.sql OR intext:*.bak OR intext:*.sql.gz OR intext:*.sql.zip OR intext:*.mdb OR intext:*.accdb OR intext:*.sqlite OR intext:*.db OR intext:*.dbf OR intext:*.mdf OR intext:*.ldf OR intext:*.ndf """
        )
        print(f"\n{Fore.RED}[+] {Fore.YELLOW}Entreprise Databases Dorks :{Fore.GREEN}")
        printitX(data)
    else:
        pass


########################################### Search for config files
def configurationX(ent):
    global doIbrrrt
    if ent is not None:
        data = (
            f"""site:{ent} intitle:"index of" intext:*.config OR intext:*.conf OR intext:*.cfg OR intext:*.ini\n"""
            f"""site:{ent} intitle:"index of" ( inurl:htpasswd OR inurl:passwd OR inurl:htaccess)\n"""
            f"""site:{ent} ( intitle:index.of.etc.passwd OR intitle:index.of.passwd )\n"""
            f"""site:{ent} filetype:txt ( inurl:passwd OR inurl:htpasswd OR inurl:mdp OR inurl:pass )\n"""
            f"""site:{ent} intitle:index.of.config\n"""
            f"""site:{ent} inurl:robot.txt"""
        )
        data2 = (
            f"\n{Fore.YELLOW}Basic infos :{Fore.GREEN}\n"
            f"""    {ent}/robots.txt\n"""
            f"""    {ent}/sitemap.xml\n"""
            f"""    {ent}/crossdomain.xml\n"""
            f"""    {ent}/clientaccesspolicy.xml\n"""
            f"""    {ent}/.well-known/\n"""
        )
        print(f"\n{Fore.RED}[+] {Fore.YELLOW}Entreprise Config Dorks :{Fore.GREEN}")
        printitX(data)
        print(data2)
    else:
        pass


########################################### Search for logs files
def logsX(ent):
    global doIbrrrt
    if ent is not None:
        data = (
            f"""site:{ent} intitle:"index of" ( intext:*.log OR intext:syslog OR intext:auth.log OR intext:debug.log OR intext:app.log OR intext:error.log OR intext:access.log )"""
        )
        print(f"\n{Fore.RED}[+] {Fore.YELLOW}Entreprise Logs-files Dorks :{Fore.GREEN}")
        printitX(data)

    else:
        pass


########################################### Search for passwords
def passX(ent, mail):
    global doIbrrrt
    if ent is not None:

        data = (
            f"""db_password filetype:env site:{ent}\n"""
            f"""(site:jsonformatter.org | site:codebeautify.org) & (intext:password OR intext:username) & (intext:{ent})\n"""
            f"""intitle: index of /concrete/Password site:{ent}\n"""
            f"""site:pastebin.com & (intext:password OR intext:username) & (intext:{ent})"\n"""
            f"""intitle:"index of" ".ssh" OR "ssh_config" OR "ssh_known_hosts" OR "authorized_keys" OR "id_rsa" OR "id_dsa" site:{ent}"""
        )
        print(f"\n{Fore.RED}[+] {Fore.YELLOW}Entreprise Passwords Dorks :{Fore.GREEN}")
        printitX(data)
    else:
        pass
    
    if mail is not None:
        data = (
            f"""(site:jsonformatter.org | site:codebeautify.org) & (intext:password OR intext:username) & (intext:{mail})\n"""
            f"""site:pastebin.com & (intext:password OR intext:username) & (intext:{mail})"""
        )
        print(f"\n{Fore.RED}[+] {Fore.YELLOW}Email Passwords Dorks :{Fore.GREEN}")
        printitX(data)


########################################### Search for bad web config
def breakit(ent):
    global doIbrrrt
    if ent is not None:
        data = (
            f"""site:{ent} intitle:"index of" ( intext:.env OR intext:.env.example OR intext:config.php OR intext:wp-config.php OR intext:wp-config.php.bak OR intext:wp-config.php.old OR intext:wp-config.php.save OR intext:.git OR intext:.gitignore OR intext:.gitattributes OR intext:.git/config OR intext:.git/HEAD OR intext:.git/logs OR intext:.git/refs)\n"""
            f"""site:{ent} intitle:"index of" AND (intitle:"admin" OR intitle:"dashboard" OR intitle:"login" OR intitle:"control panel")\n"""
            f"""site:{ent} intitle:"index of" ( inurl:wp-admin OR intitle:"index of" inurl:wp-login.php)"""
        )
        print(f"\n{Fore.RED}[+] {Fore.YELLOW}Entreprise Web-config Dorks :{Fore.GREEN}")
        printitX(data)

    else:
        pass


########################################### Search for web cache
def cacheX(ent):
    global doIbrrrt
    if ent is not None:
        data = (
            f"""cache:{ent}"""
        )
        print(f"{Fore.RED}[+] {Fore.YELLOW}Entreprise Web-cache Dorks :{Fore.GREEN}")
        printitX(data)

    else:
        pass


########################################### Dorks requests (/!!!\ Fails requests goes brrrrrrt /!!!\)
def Dorksearch(data):
    pages = 0
    timeout = 5
    error_occurred = False
    
    try:
        for _ in search(data, lang="fr", timeout=timeout):
            pages += 1  # Increment the number of requests made
            if pages >= 1:
                break  # Break out of the loop if the maximum number of requests is reached

    except HTTPError as e:
        error_occurred = True
        if e.code == 429:
            print(f"    {data} {Fore.CYAN}| {Fore.RED}ERROR: Too Many Requests detected{Fore.GREEN}")
        else:
            print(f"    {data} {Fore.CYAN}| {Fore.RED}HTTPError : {e}{Fore.GREEN}")
    except Exception as ex: #print(ex) to see most of the errors '429 Client Error: Too Many Requests for url' 
        error_occurred = True
        if doIbrrrt == "HellVerbose":
            print(f"    {data} {Fore.CYAN}| {Fore.RED}{ex}{Fore.GREEN}")
        else:
            print(f"    {data} {Fore.CYAN}| {Fore.RED}Probably Too Many Requests for url ...{Fore.GREEN}")

    if error_occurred:
        pass
    else:
        if pages > 0:
            print(f"    {data} {Fore.CYAN}| {Fore.YELLOW}[YES]{Fore.GREEN}")
        else:
            print(f"    {data} {Fore.CYAN}| {Fore.RED}[NO]{Fore.GREEN}")
