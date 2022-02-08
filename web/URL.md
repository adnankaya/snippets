# Uniform Resource Locator (URL)

### Anatomy of a URL

- https://www.example.com/page1
- `https `: This basically tells the browser which protocol it should use. It can be http, https, ftp etc.
  - A protocol is a set of rules that the browser use for the communication over the internet.
  - https is a secure version. the information is exchanged in a secure way.
  - This protocol tells the browser to make a connection to the server using Transport Layer Security, or TLS. TLS is an encryption protocol to secure communications over the Internet
- `www.example.com` is a domain name. We use it to reach the server.
  - URL is a complete address. Whereas the domain name is part of a URL.
- Every domain name has an IP address which are stored in a database named DNS (domain name system)
- After hitting the URL, the first thing that needs to resolve the IP address associated with domain name. DNS helps to resolve it. DNS is like a phone book.
-  `page1` is the path on the server to the requested resource
  - Sometimes you’ll see this with a file extension like `.html` which indicates this is a static file on the server with HTML content.
  - Without an extension, like this URL, it usually indicates the server generated this content. For instance, a news site would show you customized, up to date, and local news content, which it can only do when it knows who you are or where the request came from.

#### DNS lookup to find IP address

1. After hitting the URL, the browser cache is checked. As browser maintains its DNS records for some amount of time for the web sites you have visited earlier. So firstly DNS query runs to find the IP address associated with domain name.
2. The second place where DNS query runs in OS cache followed by router cache.
3. If first and second steps are performed but DNS does not get resolved then it takes the help of resolver server. Resolver server is nothing but your Internet Service provider(ISP). The query is sent to ISP where DNS query runs in ISP cache
4. If 3rd steps as well no results found then request sends to top or root server of the DNS hierarchy. If you are seraching IP address of the top level domain(.com, .net, .gov, .org) the resolver search on TLD server(Top level domain)
5. Now resolver asks TLD server to give IP address of our domain name. TLD stores address information of domain name. It tells the resolver to ask it to Authoritative Name server.
6. The authoritative name server is responsible for knowing everything about the domain name. Finally resolver(ISP) gets the IP address associated with the domain name and sends it back to the browser.
7. After getting the IP address the resolver(ISP) stores it in its cache. The next time ISP does not have to go to all these steps again.

#### TCP connection initiates with the server by browser

- Once the IP address of the server is found, the browser initiates connection with it. To communicate over the network internet protocol is followed and TCP/IP protocol is most common.
- A connection is built between 2 using a process called TCP 3-way handshake. 
  - A -------------  SYN message (ie: are you ready for connection ) ----------------------- > B
  - A <----------- SYN and ACK(acknowledge message)(ie: yes I am ready)   -------------- B
  - A ------------------ ACK (ie: ok lets communicate)        ----------------------------------------> B

#### Communication Starts (Request Response Process)

- Finally the connection is built between client and server. Now they can communicate with each other and share information.



### For review, here are those six steps:

1. You type a URL in your browser and press Enter
2. Browser looks up IP address for the domain
3. Browser initiates TCP connection with the server
4. Browser sends the HTTP request to the server
5. Server processes request and sends back a response
6. Browser renders the content



##### Resources

1. https://www.freecodecamp.org/news/what-happens-when-you-hit-url-in-your-browser/
2. https://aws.amazon.com/blogs/mobile/what-happens-when-you-type-a-url-into-your-browser/