# Mission 7 — How Computers Communicate

## 1. Task / objective
Explain basic network types and concepts, observe network lookup and connectivity information, and describe what happens when a website opens.

## 2. Work completed

### Task 7.1 - Explain network concepts
|Concept|Explaination in my words|Example| 
|---|---|---|
|LAN| A network in a small area | School |
|MAN| A network that covers a bigger area than LAN and less than WAN | An University|
|WAN| A network that covers a large area | International connections|
|DNS| Finds the network address linked to a website name | like phone contact list|
|Router| Sends data between networks | like traffic police |
|Protocol| Rules that devices follow to communicate |
|Packet switching| Splits data into small packets that travel across a network|
|Client-server| A client asks for something, and a server provides it | 

### Task 7.2 - Observe network information

I checked whether I could reach `eatclub.com` and looked up its DNS information.

- Connectivity check: `ping -c 4 eatclub.com` received all 4 replies with no packet loss
- DNS lookup: `nslookup eatclub.com` succeeded and returned address records. I have not included the IP addresses.
- DNS acts like the contact list in the phone. It converts a website name (domain name) into an IP address, that computers use to locate the website.

### Task 7.3 - What happens when I open a website

1. I enter a website address in my browser
2. DNS helps find the address for the website
3. My computer sends a request through the network
4. The website’s server receives the request
5. The server sends information back
6. My browser displays the page

## 3. Commands / tools used
- `ping -c 4 example.com`: checked whether the website responded
- `nslookup example.com`: checked DNS information


## 4. My understanding
Devices use networks to send information. DNS helps find websites by name, and a browser uses network requests to get a webpage from a server.

## 5. Difficulties faced
I don't know how DNS works.

## 6. How I resolved them
I saw a tutorial and came to know how it worked. 

## 7. Evidence / files
The privacy-safe results are recorded in [`evidence/mission-07-networking.txt`](evidence/mission-07-networking.txt)

## 8. Commit details
Commit message: `Explain networking concepts and website communication`
Status: Committed and pushed.