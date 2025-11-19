# Fuzzy

## A web fuzzer the solves my problems between (dirb, ffuf, dirbuster) by combining and adding functinality. 



This tool was build with customizablity in mind and supports many function to handle my needs. Stealth was a big goal so a few features were added to facilitale this. Along with some new functions like User-Agent and Proxy tumbling, this project focused on documentation and readability.

![alt text](https://github.com/MikeyPPPPPPPP/Fuzzy/blob/main/ran.png)
# Main fetures

1. Concurrentcy 
3. Multipule wordlists
4. Colored text toggling
5. Range Filtering
6. WAF Evasion

## Install

The easyiest way is to clone the repo and intsall the moduls.

```
git clone https://github.com/MikeyPPPPPPPP/Fuzzy.git
cd Fuzzy
pip3 install -r requirments.txt
```
## Usage

Basic Usage:
```
python3 fuzzy.py -u <url> -w <wordlis>
```

Youtube Demo <a href="https://www.youtube.com/watch?v=khkfAbuy5E8&t=580s&ab_channel=MichaelProvenzano">here</a>.

![alt text](https://github.com/MikeyPPPPPPPP/Fuzzy/blob/main/options.png)


## Workflow intigration

Two options assist tool chaining, the color and json output option. These options make it easier to parse they output by adding ansi color codes or outputing to a common format. By default their is no color added makingit ideal for worflow intigration.
```
-C Colored text
-j output to a json file
```

## Known issuse (Work in progress)

This project is ongoing and new feturs are going to be added as I think of them but for now here are a few.

```
-- add a Crtl + C stop filter updater
-- make core.setup able to detect previus configs and just update it instead of always makeing a new one
-- implement recurssion
        --depth
        --based on redirects 
        --403 forbidon
        --if it is not an endpoint
-- core.setSettings.changeSetting     do JSON -> edit -> File  instead of converting a json to dict back to json, no need to convert it to a dict.
```

## Contribute 

If you want to contribute download the repo and work localy. A good place to start is core.spammer.py as its the backbone of the project. Since readability is a big part please include well documented comments and doc string.

## Found a Bug

Please add the command, config file, and a sample of your wordlist or something similare so I can help solve the problem. 

## Donate

Donate to your local church because I'm not worth anything.
