# Google DORKER

![GoogleDORKER](https://github.com/raphaelthief/Google-Dorker/blob/main/Pictures/Main.JPG "GoogleDORKER")

## Disclaimer 
This program aims to help businesses monitor the exposure of their infrastructures on the internet. I am not responsible for the misuse of the Dorks provided in this program. Please use this tool ethically and comply with the laws applicable in your respective countries.

## Usage 
Google Dorker aims to automate the generation of Dorks to observe the exposure of a company or a given email. This tool generates a series of Dorks according to the specified needs. These Dorks are a compilation of what I consider interesting for certain monitoring purposes and only represent my views. The goal is to automate the customization of a compilation of Dorks that I find useful for potential pentests and red team operations.

Through these generated Dorks, you will find some compilations from Hacktriks or DB-exploit. But you will also find unique Dorks that I have either designed myself or at least have not seen elsewhere.

I have also introduced the possibility of checking a presumed number of password uses based on breachdirectory through their API that I extracted.
The operation of the API is relatively simple, you just need to convert your word into SHA1 to compare it to their database. There doesn't seem to be any limit on the number of requests since the API call is made every time you trigger a keystroke on the search bar on their website :

```
https://api.breachdirectory.org/passsearch?hash={sha1_hash}
```

I have added two functions to the program that allow you to directly query to check whether or not there is a result for the different Dorks generated according to the parameters entered.
The --run function thus allows you to see whether or not the search displays certain results and if an error occurs, a generic message will be displayed. Conversely, the --runverbose function will not display generic messages but the complete error message.
Note that in most cases, this is a query problem. Google does not accept Boolean searches well.

## Pictures

![GoogleDORKER](https://github.com/raphaelthief/Google-Dorker/blob/main/Pictures/HelpV2.JPG "GoogleDORKER")
![GoogleDORKER](https://github.com/raphaelthief/Google-Dorker/blob/main/Pictures/checklist.JPG "GoogleDORKER")
![GoogleDORKER](https://github.com/raphaelthief/Google-Dorker/blob/main/Pictures/api_tor.JPG "GoogleDORKER")
![GoogleDORKER](https://github.com/raphaelthief/Google-Dorker/blob/main/Pictures/Exemple.JPG "GoogleDORKER")
