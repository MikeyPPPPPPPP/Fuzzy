# Fuzzy
This is a directory fuzzing tool I made to help get better at python
also because some fuzzers had options that others didnt 



I wanted to make a tool that was very customizable and useful. A few big parts of this tool is conccurentcy, filtering/filtering range,
User-Agent tumbling. There are also a lot of smaller setting like ssl, timeouts, delays, and tor. I have 
never seen a tool with User-Agent tumbling and I though if a sysadmin checked the logs it would be a little more random
at first glance. I also add proxy tumbling for firewall evasion. Adding color to the output is a cool part becauser if you want another tool to parse they output it wont be ansied for easy grepping, I made a tool that greps they output of others and most of the outputs had to be unansied.

![alt text](https://github.com/MikeyPPPPPPPP/Fuzzy/blob/main/ran.png)

# Main fetures
![alt text](https://github.com/MikeyPPPPPPPP/Fuzzy/blob/main/options.png)


## Filtering

The filtering is pretty cool because besides filtering like 200,404,302  you can also filter with a > or < sign, unfortenently you need to seround the
argument in quots like this ">200" and you can only do this onec but I am working on makeing it like this ">200,<500" for mor spacific filtering.
The function that checks the > or < is checked on every filter except fo the regex so you can specify a range on status codes, response time, word count,
char count, and the exclueds of those.



## Tumbling

There is User-Agent tumbling to help with evading bands and trying to make it look like the traffic is comming from multipule computers. Not many if any tools have User-Agent tumbling which I though was interesting but I already hade somthing like this in a different tool I made and thought it would be a uniq option for a fuzzer. 


