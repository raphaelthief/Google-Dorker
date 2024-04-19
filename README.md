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

## Pictures

![GoogleDORKER](https://github.com/raphaelthief/Google-Dorker/blob/main/Pictures/Help.JPG "GoogleDORKER")
![GoogleDORKER](https://github.com/raphaelthief/Google-Dorker/blob/main/Pictures/checklist.JPG "GoogleDORKER")
![GoogleDORKER](https://github.com/raphaelthief/Google-Dorker/blob/main/Pictures/api_tor.JPG "GoogleDORKER")
![GoogleDORKER](https://github.com/raphaelthief/Google-Dorker/blob/main/Pictures/Exemple.JPG "GoogleDORKER")
