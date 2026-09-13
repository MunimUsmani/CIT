YOU
 ↓
COMPUTER
 ↓
OPERATING SYSTEM
 ↓
NETWORK
 ↓
INTERNET
 ↓
DNS
 ↓
WEB SERVER
 ↓
WEBSITE
 ↓
BROWSER
 ↓
YOU SEE THE RESULT

Tell students:

"By the end of today's class, you should be able to explain every important part of this process."

4. Computer

Short definition

A computer is an electronic device that takes input, processes data, stores information, and produces output.

Simple model

Input → Processing → Output
           ↓
         Storage

Example

If the user enters:

5 + 10

The process is conceptually:

Keyboard
   ↓
Input
   ↓
CPU processes instructions
   ↓
Result = 15
   ↓
Screen
   ↓
Output

Ask students

What is an input?

What is an output?

Is a keyboard input or output?

Is a monitor input or output?

Answers

Input = data/instructions given to the computer

Output = information produced by the computer

Keyboard = input

Monitor = output

5. Hardware

Short definition

Hardware is the physical part of a computer that you can touch.

Examples

CPU
RAM
SSD/HDD
Motherboard
GPU
Keyboard
Mouse
Monitor
Network card
USB devices

Easy rule

Hardware = something physical that you can touch.

6. CPU — Central Processing Unit

Short definition

The CPU is the main processor that executes instructions and performs calculations.

Simple analogy

Think of the CPU as a worker.

Task
 ↓
CPU
 ↓
Processes instructions
 ↓
Result

For example:

Open Chrome
     ↓
CPU executes instructions
     ↓
Chrome runs

Important clarification

You can tell students:

"People often call the CPU the brain of the computer. That is a useful analogy, but technically the CPU is a processor that executes instructions."

7. RAM — Random Access Memory

Short definition

RAM is temporary working memory used by the computer for data and programs that are currently being used.

Best analogy

Imagine:

SSD = Cupboard
RAM = Work desk
CPU = Worker

The worker takes books out of the cupboard and puts them on the desk while working.

More RAM is like having a larger desk:

More RAM
 ↓
More working space
 ↓
More programs/data can be kept readily available

Important distinction

Ask:

"If my computer has 16 GB RAM, does it have 16 GB storage?"

Answer:

No. RAM and storage are different things.

8. Storage

Short definition

Storage is where a computer keeps data persistently, even after the computer is turned off.

Examples

SSD

HDD

USB flash drive

External drive

Stores things such as

Operating system
Applications
Documents
Photos
Videos
Games
Projects

Analogy

RAM = Work desk
Storage = Cupboard

9. GPU — Graphics Processing Unit

Short definition

A GPU is a processor designed to handle graphics and many parallel computations efficiently.

Examples

GPUs are commonly used for:

Games

3D graphics

Video rendering

Image processing

Some AI/ML workloads

For beginners, don't go deeply into GPU architecture unless the class asks.

10. Input

Short definition

Input is data or instructions given to a computer.

Examples

Keyboard typing
Mouse click
Microphone
Camera
Touchscreen

11. Output

Short definition

Output is information produced by a computer after processing.

Examples

Text on screen
Images
Sound
Printed documents
Video

12. Hardware vs Software

Hardware

Physical components that you can touch.

Examples:

CPU
RAM
SSD
Keyboard
Mouse
Monitor

Software

Programs and instructions that tell a computer what to do.

Examples:

Windows
Linux
Chrome
VS Code
Microsoft Word
Games

Easy rule

Hardware is what you can touch. Software is what you run.

13. Operating System

Short definition

An operating system is the main software that manages computer hardware and provides an environment for applications to run.

Examples

Windows
Linux
macOS
Android
iOS

14. Explain the Operating System With an Analogy

Use a restaurant analogy.

User
 ↓
Application
 ↓
Operating System
 ↓
Hardware

For example, Chrome needs:

CPU

RAM

Storage

Network

Display

The operating system helps applications use these resources.

Draw:

          APPLICATIONS
    ┌────────┬────────┬────────┐
   Chrome   Word    VS Code   Games
    └────────┴────────┴────────┘
                ↓
        OPERATING SYSTEM
                ↓
    ┌───────────┼───────────┐
   CPU          RAM       Storage
                ↓
             HARDWARE

15. What Does the OS Actually Do?

Explain that an operating system handles many responsibilities, including:

Managing CPU time

Managing memory

Managing files and storage

Managing devices

Managing networking

Providing security mechanisms

Providing a user interface

Allowing applications to run

Example

Chrome needs memory:

Chrome
 ↓
Operating System
 ↓
RAM

Chrome needs to save a file:

Chrome
 ↓
Operating System
 ↓
Storage

Chrome needs to communicate over a network:

Chrome
 ↓
Operating System/network stack
 ↓
Network interface
 ↓
Network

16. Live OS Demonstration

Windows

Open:

Task Manager

Show students:

CPU

Memory

Disk

Network

Running applications

Explain:

"The operating system is managing and monitoring these resources while applications are running."

Linux

Try:

top

If htop is installed:

htop

Explain the CPU and memory information.

17. Application

Short definition

An application is a software program designed to perform a specific task for the user.

Examples

Chrome → Browse the web
Word → Create documents
VS Code → Write code
WhatsApp → Messaging
Calculator → Calculations

18. Network

Short definition

A network is a group of connected devices that can communicate and exchange data.

Simple example

Laptop ─── Router ─── Phone

Or:

Laptop ── Wi-Fi ── Router
Phone  ── Wi-Fi ── Router
TV     ── Wi-Fi ── Router

19. Wi-Fi

Short definition

Wi-Fi is a wireless networking technology used to connect devices to a local network.

Important

Wi-Fi is not the same thing as the internet.

Example:

Laptop
  ↓
Wi-Fi
  ↓
Router
  ↓
Internet

Wi-Fi can connect your laptop to your router even though the router's internet connection is a separate part of the setup.

20. Router

Short definition

A router is a network device that forwards data between networks and helps devices communicate with other networks.

Analogy

Think of a router as a traffic director.

Device
  ↓
Router
  ↓
Correct network/destination

Simple analogy

Cars = Data
Roads = Networks
Traffic director = Router

21. IP Address

Short definition

An IP address is a network address used to identify a device/interface and route IP traffic.

Example:

192.168.1.10

Explain:

"It is similar to an address used for network communication. It helps traffic know where it needs to go."

Don't teach subnetting in this lesson.

22. Private IP Address

Short definition

A private IP address is used within a local network such as a home, school, or office network.

Example:

192.168.1.10

Other common private IPv4 ranges include:

10.0.0.0/8
172.16.0.0/12
192.168.0.0/16

For beginners, simply remember:

Private IP = used inside a local network.

23. Public IP Address

Short definition

A public IP address is an IP address used for communication with the public internet.

You can explain:

Your Laptop
    ↓
Private IP
    ↓
Router
    ↓
Public IP
    ↓
Internet

Avoid going into NAT unless students ask.

24. Packet

Short definition

A packet is a small unit of data transmitted across a network.

Simple demonstration

Write:

HELLO MY FRIEND

Then conceptually divide it:

HEL
LO
MY
FRI
END

Explain:

"Real network packets contain headers and other information. This is just a simple illustration of the idea that data is transmitted in units."

Conceptually:

Large Data
    ↓
Packets
    ↓
Network
    ↓
Destination
    ↓
Data processed/reassembled

25. Internet

Short definition

The internet is a global network of interconnected networks that allows devices and systems to communicate.

Important distinction

Ask:

"Is Wi-Fi the internet?"

Answer:

No.

Wi-Fi
 ↓
Wireless connection to a local network

Internet
 ↓
Global interconnected network

26. ISP — Internet Service Provider

Short definition

An ISP is a company that provides internet connectivity to customers.

Examples students may know:

PTCL
StormFiber
Nayatel
Transworld

Simple flow:

Laptop
 ↓
Router
 ↓
ISP
 ↓
Internet

27. Browser

Short definition

A web browser is software used to access, retrieve, and display websites.

Examples:

Google Chrome
Mozilla Firefox
Microsoft Edge
Safari

28. Search Engine

Short definition

A search engine is a service that helps users find information and web pages on the internet.

Examples:

Google Search
Bing
DuckDuckGo

29. Browser vs Search Engine

This is an important beginner distinction.

Ask:

"Is Google Chrome Google?"

Answer:

No.

Chrome
 ↓
Browser

Google Search
 ↓
Search engine

Example:

Chrome
  ↓
Google Search
  ↓
Search results
  ↓
Website

30. Website

Short definition

A website is a collection of web pages and resources available through the web under a domain or web address.

Example:

youtube.com

A website can contain:

Text

Images

Videos

Buttons

Forms

Interactive applications

Other resources

31. Web Server

Short definition

A web server is a computer or software system that receives web requests and provides web content or services.

Simple diagram:

Browser
   ↓
Internet
   ↓
Web Server
   ↓
Response
   ↓
Browser

32. Domain Name

Short definition

A domain name is a human-readable name used to access a website or internet service.

Examples:

google.com
youtube.com
github.com

Humans prefer:

google.com

rather than remembering a numerical IP address.

33. DNS — Domain Name System

Short definition

DNS is a system that translates domain names into IP addresses and provides other information about internet domains.

Simple analogy

DNS is like a contacts list for internet names.

Your phone:

Ali
 ↓
Ali's phone number

DNS:

google.com
 ↓
IP address / DNS records

Important:

DNS does not deliver the website. It helps your system discover information needed to reach the service.

34. Live DNS Demonstration

Windows

Run:

nslookup google.com

Linux/macOS

Run:

nslookup google.com

If available:

dig google.com

Explain:

Domain name
     ↓
DNS query
     ↓
DNS response
     ↓
IP address/other records

35. URL — Uniform Resource Locator

Short definition

A URL is the address used to locate a resource on the web.

Example:

https://www.example.com/about

Break it down:

https://
   ↓
Protocol/scheme

www
   ↓
Subdomain

example
   ↓
Domain name

.com
   ↓
Top-level domain

/about
   ↓
Path

Don't spend too much time on URL anatomy in a beginner class.

36. Protocol

Short definition

A protocol is a set of rules that devices and software follow when communicating.

Examples:

HTTP
HTTPS
TCP
IP
DNS

Simple analogy:

Protocols are like agreed rules for communication.

37. HTTP

Short definition

HTTP is a protocol used for communication between web clients and web servers.

Simple:

Browser
   ↓
HTTP request
   ↓
Server
   ↓
HTTP response
   ↓
Browser

38. HTTPS

Short definition

HTTPS is HTTP carried over a secure TLS connection, providing encrypted communication between the client and server.

Simple:

HTTP
 ↓
Web communication

HTTPS
 ↓
Encrypted web communication

Important:

HTTPS helps protect communication, but HTTPS alone does not prove that a website is trustworthy.

39. How a Website Loads

This is the most important section.

Ask:

"What happens when you type google.com and press Enter?"

Walk through it slowly.

Step 1 — User enters a URL

https://google.com

Step 2 — Browser interprets the URL

The browser determines what resource it needs.

Step 3 — DNS lookup

The system/browser uses DNS to discover the address information associated with the domain.

google.com
    ↓
DNS
    ↓
IP address / records

Step 4 — Network communication begins

The computer sends traffic through its network connection.

Computer
 ↓
Wi-Fi/Ethernet
 ↓
Router

Step 5 — Traffic goes through the ISP

Router
 ↓
ISP
 ↓
Internet

Step 6 — Traffic reaches the service

Internet
 ↓
Google infrastructure

Step 7 — Server responds

The service sends data back.

Step 8 — Browser receives the response

The browser processes the returned web resources.

Step 9 — Browser renders the page

The browser displays the webpage to the user.

Complete diagram

YOU
 ↓
BROWSER
 ↓
DNS LOOKUP
 ↓
IP ADDRESS
 ↓
NETWORK INTERFACE
 ↓
ROUTER
 ↓
ISP
 ↓
INTERNET
 ↓
WEB SERVICE/SERVER
 ↓
RESPONSE
 ↓
INTERNET
 ↓
ISP
 ↓
ROUTER
 ↓
YOUR COMPUTER
 ↓
BROWSER
 ↓
WEBPAGE

Tell students:

"A lot more happens in a real web request, but this is the simplified mental model you need at this level."

40. Useful Network Commands

Windows

Show network configuration

ipconfig

More detailed network configuration

ipconfig /all

Test connectivity/reachability

ping google.com

Query DNS

nslookup google.com

Show network path

tracert google.com

Show system information

systeminfo

Linux

Show network interfaces

ip addr

Show IP address

hostname -I

Test connectivity/reachability

ping google.com

Stop ping with:

Ctrl + C

Query DNS

nslookup google.com

or:

dig google.com

Show network path

traceroute google.com

Show system information

uname -a

Show RAM usage

free -h

Show disk usage

df -h

41. Hands-On Activity #1 — Find Your Computer Information

Give students approximately 10 minutes.

Ask them to find:

1. Operating System
2. CPU
3. RAM
4. Storage
5. IP address
6. Browser

Have them fill in:

Operating System: __________________

CPU: ______________________________

RAM: ______________________________

Storage: ___________________________

IP Address: ________________________

Browser: ___________________________

Windows

Use:

systeminfo

and:

ipconfig

Linux

Use:

uname -a

free -h

df -h

ip addr

42. Hands-On Activity #2 — Test the Network

Have students run:

ping google.com

Explain that ping can test whether a destination responds to ICMP echo requests and can show round-trip timing.

Then:

nslookup google.com

Ask:

"What IP address did DNS return?"

Then on Windows:

tracert google.com

or Linux:

traceroute google.com

Explain:

"This can show the path discovered toward the destination. It may not show every actual network device/path because routers and networks can filter or handle these probes differently."

43. Files

Short definition

A file is a stored collection of digital data.

Examples:

photo.jpg
assignment.pdf
program.py
video.mp4
resume.docx

44. Folder

Short definition

A folder is a container used to organize files and other folders.

Example:

Projects/
├── Python/
├── Web/
└── AI/

45. File Extension

Short definition

A file extension commonly indicates the format or type of a file.

Examples:

.pdf   → PDF document
.jpg   → Image
.png   → Image
.py    → Python source file
.docx  → Word document
.mp4   → Video
.xlsx  → Spreadsheet

46. File Path

Short definition

A file path tells the computer where a file or folder is located.

Example:

Documents/Projects/Python/app.py

On Windows, paths may look like:

C:\Users\Student\Documents\Projects\Python\app.py

47. Download

Short definition

Downloading means transferring data from a remote system to your device.

Internet/Server
      ↓
   Computer

Example:

Downloading a PDF from a website.

48. Upload

Short definition

Uploading means transferring data from your device to a remote system.

Computer
   ↓
Internet/Server

Example:

Uploading an assignment to Google Drive.

49. Why File Organization Matters

Show students this bad example:

Downloads/
├── final.pdf
├── final2.pdf
├── newfinal.pdf
├── newfinal2.pdf
├── assignment.pdf
├── image.png
├── random.zip
└── document.docx

Ask:

"Will you easily find the correct file six months from now?"

Explain:

"Good file organization makes files easier to find, manage, share, and back up."

50. Good Folder Structure

Create:

My_Work/
│
├── Education/
│   ├── Python/
│   ├── Web_Development/
│   └── Networking/
│
├── Projects/
│   ├── Project_1/
│   └── Project_2/
│
├── Documents/
│
├── Certificates/
│
└── Personal/

Explain that the exact structure can vary. The important thing is consistency.

51. File Naming

Bad names

final.pdf
final2.pdf
newfinal.pdf
newfinal2.pdf
assignmentfinalREAL.pdf

Better names

Networking_Assignment_01.pdf
Python_Loops_Quiz.pdf
CV_2026.pdf
Project_Report_v1.pdf
Project_Report_v2.pdf

Good file names should be

Descriptive

Consistent

Easy to search

Easy to understand later

For versions:

Report_v1
Report_v2
Report_v3

52. Downloads Folder

Teach students:

"The Downloads folder is where downloaded files often arrive. It does not have to be your permanent organization system."

Good workflow:

Download file
     ↓
Check file
     ↓
Rename if necessary
     ↓
Move to correct folder
     ↓
Back up important files

53. Cloud Storage

Short definition

Cloud storage is a service that stores files on remote servers and allows users to access them over a network, usually the internet.

Examples:

Google Drive
OneDrive
Dropbox
iCloud

Simple diagram:

Your Computer
      ↓
   Internet
      ↓
Cloud Service
      ↓
Remote Servers

54. Benefits of Cloud Storage

Access

Laptop → Files
Phone → Same files
Other computer → Same files

Sharing

You can share files with other people.

Availability

If your laptop stops working, a cloud copy may still be available.

Collaboration

Multiple people can sometimes work with shared documents/files.

55. Sync vs Backup

This is an important concept.

Synchronization

Short definition

Synchronization keeps data or files consistent across multiple locations or devices.

Example:

Laptop
  ↕
Cloud
  ↕
Phone

Backup

Short definition

A backup is an additional copy of important data kept so it can be restored if the original is lost or damaged.

Important warning

Sync is not automatically the same as backup.

If a synchronized file is deleted and the deletion propagates, the cloud copy may also be deleted.

Therefore:

Important file
     ↓
Local copy
     +
Cloud copy
     +
Separate backup when appropriate

56. Hands-On Activity #3 — Build a Digital Workspace

Give students 20–30 minutes.

Step 1

Create:

Computer_Class

Step 2

Inside it create:

Computer_Class/
├── Notes/
├── Assignments/
├── Projects/
└── Resources/

Step 3

Inside Assignments:

Assignments/
├── Assignment_01/
└── Assignment_02/

Step 4

Create a file:

My_Computer_Info.txt

Put:

Operating System:
CPU:
RAM:
Browser:

Step 5

Save it in:

Computer_Class/Notes/

Step 6

Upload it to their cloud storage.

Step 7

Open the file from the cloud.

Students have now practiced:

Files
 ↓
Folders
 ↓
File naming
 ↓
Local storage
 ↓
Cloud storage

57. Hands-On Activity #4 — Organize a Messy Folder

Give students these imaginary files:

resume.pdf
python_notes.pdf
family_photo.jpg
assignment.docx
movie.mp4
certificate.pdf
project.zip

Ask them to create:

Documents/
Education/
Photos/
Videos/
Certificates/
Projects/

Then move each file to the appropriate folder.

58. Final Practical Challenge

Tell students:

"You type youtube.com into your browser and press Enter. Explain what happens."

A good beginner answer should contain something like:

I open a browser
        ↓
I enter youtube.com
        ↓
The domain needs to be resolved
        ↓
DNS provides address information
        ↓
My computer sends network traffic
        ↓
Traffic goes through my router
        ↓
My ISP connects me to the internet
        ↓
The traffic reaches YouTube's infrastructure
        ↓
The server/service sends a response
        ↓
The response comes back
        ↓
The browser processes the data
        ↓
The browser renders the webpage
        ↓
I see the website

59. Final Big Picture

Draw this on the board:

                         COMPUTER
                             │
               ┌─────────────┴─────────────┐
               │                           │
           HARDWARE                    SOFTWARE
               │                           │
       CPU / RAM / SSD              APPLICATIONS
               │                           │
               └─────────────┬─────────────┘
                             │
                     OPERATING SYSTEM
                             │
                     NETWORK INTERFACE
                             │
                          ROUTER
                             │
                            ISP
                             │
                         INTERNET
                             │
                       DNS / SERVERS
                             │
                       WEB SERVER
                             │
                          BROWSER
                             │
                           USER

60. Quick Definitions — Student Cheat Sheet

Keep this section available during revision.

Topic

Short Definition

Computer

Electronic device that takes input, processes data, stores information, and produces output.

Hardware

Physical parts of a computer that can be touched.

Software

Programs and instructions that tell a computer what to do.

CPU

Processor that executes instructions and performs calculations.

RAM

Temporary working memory used by programs and the operating system.

Storage

Persistent place where files, applications, and data are stored.

GPU

Processor specialized for graphics and parallel computations.

Input

Data or instructions given to a computer.

Output

Information produced by a computer.

Operating System

Software that manages hardware and provides an environment for applications.

Application

Software designed to perform a specific task.

Network

Connected devices that communicate and exchange data.

Wi-Fi

Wireless technology for connecting devices to a local network.

Router

Device that forwards traffic between networks.

IP Address

Network address used to identify a device/interface and route IP traffic.

Private IP

IP address used inside a local/private network.

Public IP

IP address used for communication with the public internet.

Packet

Small unit of data transmitted across a network.

ISP

Company that provides internet connectivity.

Internet

Global network of interconnected networks.

Browser

Software used to access and display websites.

Search Engine

Service that helps users find information on the web.

Website

Collection of web pages/resources available through the web.

Web Server

Computer/software system that provides web content or services.

Domain Name

Human-readable name used to access an internet service.

DNS

System that provides information about domains, including resolving names to IP addresses.

URL

Address used to locate a resource on the web.

Protocol

Rules that devices/software follow to communicate.

HTTP

Protocol used for web communication.

HTTPS

HTTP communication protected by TLS encryption.

File

Stored collection of digital data.

Folder

Container used to organize files and folders.

File Extension

Suffix that commonly indicates a file's format/type.

File Path

Location of a file or folder in a filesystem.

Download

Transfer data from a remote system to your device.

Upload

Transfer data from your device to a remote system.

Cloud Storage

Storage provided on remote servers and accessed over a network.

Sync

Keeps data/files consistent across multiple locations.

Backup

Additional copy of data kept for recovery.

61. Command Cheat Sheet

Task

Windows

Linux

Show IP/network information

ipconfig

ip addr

Show detailed network info

ipconfig /all

ip addr

Show IP address

ipconfig

hostname -I

Test connectivity

ping google.com

ping google.com

DNS lookup

nslookup google.com

nslookup google.com

Alternative DNS tool

—

dig google.com

Trace network path

tracert google.com

traceroute google.com

System information

systeminfo

uname -a

RAM information

Task Manager

free -h

Disk usage

File Explorer/Settings

df -h

62. 10-Minute Quiz

Question 1

What is hardware?

A. Programs
B. Physical computer components
C. Internet data
D. Websites

Answer: B

Question 2

Which component executes instructions?

A. SSD
B. Monitor
C. CPU
D. Keyboard

Answer: C

Question 3

What is RAM primarily used for?

A. Permanent file storage
B. Temporary working memory
C. Printing
D. Internet connectivity

Answer: B

Question 4

Which one is an operating system?

A. Chrome
B. Google Search
C. Windows
D. YouTube

Answer: C

Question 5

What does a router primarily do?

A. Store photos
B. Forward network traffic between networks
C. Run Word documents
D. Display images

Answer: B

Question 6

What does DNS help with?

A. Converting domain names into network address information
B. Increasing RAM
C. Editing photos
D. Creating folders

Answer: A

Question 7

Which one is a web browser?

A. Google Search
B. Chrome
C. DNS
D. IP address

Answer: B

Question 8

Is Wi-Fi the same as the internet?

A. Yes
B. No

Answer: B

Question 9

What is a packet?

A. A computer monitor
B. A unit of data transmitted across a network
C. A type of folder
D. An operating system

Answer: B

Question 10

What is a backup?

A. A browser
B. A network protocol
C. An additional copy of data kept for recovery
D. A type of CPU

Answer: C

63. Questions to Ask During Class

Instead of continuously lecturing, stop and ask:

Hardware

"Can you touch software?"

No.

"Is RAM storage?"

No.

"Which component executes instructions?"

CPU.

Operating Systems

"Can Chrome normally run without an operating system?"

Explain that applications rely on the operating system and underlying system software to access hardware/resources.

Networking

"Is Wi-Fi the internet?"

No.

"What device normally connects your local network to another network?"

Router.

"What identifies/address network interfaces for IP communication?"

IP address.

Web

"Is Chrome a search engine?"

No.

"What does DNS do?"

Provides domain-related information, including resolving domain names to IP addresses.

"Where does website content/services come from?"

From servers/services on the network.

64. Common Beginner Misconceptions

Misconception 1

"CPU is the whole computer."

Correction:

CPU is one important component inside a computer.

Misconception 2

"RAM stores files permanently."

Correction:

RAM is temporary working memory. Storage such as an SSD keeps data persistently.

Misconception 3

"Google Chrome is Google."

Correction:

Chrome is a browser. Google Search is a search engine.

Misconception 4

"Wi-Fi is the internet."

Correction:

Wi-Fi is a wireless networking technology. It can connect your device to a local network, which may then connect to the internet.

Misconception 5

"DNS is the internet."

Correction:

DNS is a naming system used to look up information about domains.

Misconception 6

"A website is stored inside my browser."

Correction:

The browser retrieves web resources from servers/services and renders them on your device.

Misconception 7

"Cloud means my files are nowhere."

Correction:

Cloud storage means files are stored on remote computers/servers operated by a service and accessed over a network.

Misconception 8

"Sync and backup are exactly the same."

Correction:

Synchronization keeps copies aligned; a backup is a separate recovery copy. Sync alone is not necessarily a sufficient backup.
