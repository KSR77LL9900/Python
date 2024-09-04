#INTRODUCTON TO APIs
#An API, or Application Programming Interface, is a set of rules that determine how different software components should interact with each other. An API acts as an intermediary between different systems, allowing them to communicate with each other and share data and functionality.
#APIs are an important part of modern software development, as they allow developers to easily integrate their own systems with other systems and services. This can save a lot of time and effort, as it avoids the need to build everything from scratch.

#In the context of APIs, an HTTP request is a request that is sent to an API over the internet using the Hypertext Transfer Protocol (HTTP). HTTP is a protocol that is used to transmit data over the web, and it defines a set of rules for how clients (such as web browsers) and servers (such as web servers) should communicate with each other.


#HTTP request in API
#When making an HTTP request to an API, a client (such as a web browser) sends a request to a server (such as a web server) asking it to perform a specific action. For example, the client might send a request to the server asking it to retrieve some data from a database or to create a new resource on the server

#GET REQUESTS
#In this analogy, the different databases and online services are like APIs, and the "GET" requests are like the requests you send to these APIs to retrieve information. Just like a detective, an API client can use "GET" requests to gather information from different sources in order to accomplish a specific task.

import requests
import json
data=requests.get('http://api.weatherapi.com/v1/current.json?key=caeeb2235f1d4c5782e103637240409&q=China&aqi=no')
txt=json.loads(data.text)
print(txt)