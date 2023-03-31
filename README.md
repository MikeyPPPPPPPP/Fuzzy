# Fuzzy
This is a directory fuzzing tool I made to help get better at python
also because some fuzzers had options that others didnt 



I wanted to make a tool that was very customizable and useful. A few big parts of this tool are conccurentcy, filtering/filtering range,
User-Agent tumbling. There are also a lot of smaller setting like ssl, timeouts, delays, and tor. I have 
never seen a tool with User-Agent tumbling and I though if a sysadmin checked the logs it would be a little more random
at first glance. I will add proxy tumbling for firewall evasion. There will also be a smart extention finder, and waf detector.
Adding color to the output is a cool part becauser if you want another tool to parse they output it wont be ansied for easy grepping, 
I made a tool that greps they output of others and most of the outputs had to be unansied.

![alt text](https://github.com/MikeyPPPPPPPP/Fuzzy/blob/main/Screen%20Shot%202022-05-09%20at%204.35.32%20PM.png)

# Main fetures

options:
  -h, --help            show this help message and exit

basic options:
  -u URL, --url URL     this is the url you want to fuzz, add a FUZZ
  --headers HEADERS     add headers/change useragent:funman,host:home
  -P P                  use for a POST request data:1,data:2
  -w W                  wordlist you want to use
  -c C                  cookies you want to use data:1,data:2
  -C                    Colored text

filter options:
  -sc SC                status code to show 200,403
  -cc CC                charector count show
  -wc WC                word count show
  -rt RT                response time show "<0.31" or ">0.10"
  -xrt XRT              exclude response time
  -xsc XSC              exclude status code
  -xwc XWC              exclude word count
  -xcc XCC              exclude charector count show
  -re RE                check the page with a regex

proxy options:
  -t                    proxy through TOR (SLOW)
  -S S                  single proxy

tunning options:
  -ts TS                number of threads, default 2
  -r R                  follow redirects
  -tt TT                timeout, default none
  -d D                  delay to set befor every request, default None
  -v V                  what HTTP VERB do you want to use, (default GET) GET POST INFO etc
  -ssl                  set SSL verify (default False) GET POST INFO etc
  --userAgentTumbler    file of useragent



## Filtering

The filtering is pretty cool because besides filtering like 200,404,302  you can also filter with a > or < sign, unfortenently you need to seround the
argument in quots like this ">200" and you can only do this onec but I am working on makeing it like this ">200,<500" for mor spacific filtering.
The function that checks the > or < is checked on every filter except fo the regex so you can specify a range on status codes, response time, word count,
char count, and the exclueds of those.



## Tumbling

There is User-Agent tumbling to help with evading bands and trying to make it look like the traffic is comming from multipule computers. I have made a 
class for proxy tumbling but it needs to be implemented. Not many if any tools have User-Agent tumbling which I though was interesting but I already hade somthing like this in a different tool I made and thought it would be a uniq option for a fuzzer. 


