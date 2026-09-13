# Computer Basics — Class Guide

A beginner-friendly walkthrough of how computers, networks, and the web work — from hardware, to the internet, to file organization.

> **Goal for students:** By the end of class, be able to explain every part of this diagram:

```
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
```

---

## Table of Contents

1. [Computer](#1-computer)
2. [Hardware](#2-hardware)
3. [CPU — Central Processing Unit](#3-cpu--central-processing-unit)
4. [RAM — Random Access Memory](#4-ram--random-access-memory)
5. [Storage](#5-storage)
6. [GPU — Graphics Processing Unit](#6-gpu--graphics-processing-unit)
7. [Input](#7-input)
8. [Output](#8-output)
9. [Hardware vs Software](#9-hardware-vs-software)
10. [Operating System](#10-operating-system)
11. [What Does the OS Actually Do?](#11-what-does-the-os-actually-do)
12. [Live OS Demonstration](#12-live-os-demonstration)
13. [Application](#13-application)
14. [Network](#14-network)
15. [Wi-Fi](#15-wi-fi)
16. [Router](#16-router)
17. [IP Address](#17-ip-address)
18. [Private IP Address](#18-private-ip-address)
19. [Public IP Address](#19-public-ip-address)
20. [Packet](#20-packet)
21. [Internet](#21-internet)
22. [ISP — Internet Service Provider](#22-isp--internet-service-provider)
23. [Browser](#23-browser)
24. [Search Engine](#24-search-engine)
25. [Browser vs Search Engine](#25-browser-vs-search-engine)
26. [Website](#26-website)
27. [Web Server](#27-web-server)
28. [Domain Name](#28-domain-name)
29. [DNS — Domain Name System](#29-dns--domain-name-system)
30. [Live DNS Demonstration](#30-live-dns-demonstration)
31. [URL — Uniform Resource Locator](#31-url--uniform-resource-locator)
32. [Protocol](#32-protocol)
33. [HTTP](#33-http)
34. [HTTPS](#34-https)
35. [How a Website Loads](#35-how-a-website-loads)
36. [Useful Network Commands](#36-useful-network-commands)
37. [Hands-On Activity #1 — Find Your Computer Information](#37-hands-on-activity-1--find-your-computer-information)
38. [Hands-On Activity #2 — Test the Network](#38-hands-on-activity-2--test-the-network)
39. [Files](#39-files)
40. [Folder](#40-folder)
41. [File Extension](#41-file-extension)
42. [File Path](#42-file-path)
43. [Download](#43-download)
44. [Upload](#44-upload)
45. [Why File Organization Matters](#45-why-file-organization-matters)
46. [Good Folder Structure](#46-good-folder-structure)
47. [File Naming](#47-file-naming)
48. [Downloads Folder](#48-downloads-folder)
49. [Cloud Storage](#49-cloud-storage)
50. [Benefits of Cloud Storage](#50-benefits-of-cloud-storage)
51. [Sync vs Backup](#51-sync-vs-backup)
52. [Hands-On Activity #3 — Build a Digital Workspace](#52-hands-on-activity-3--build-a-digital-workspace)
53. [Hands-On Activity #4 — Organize a Messy Folder](#53-hands-on-activity-4--organize-a-messy-folder)
54. [Final Practical Challenge](#54-final-practical-challenge)
55. [Final Big Picture](#55-final-big-picture)
56. [Quick Definitions — Student Cheat Sheet](#56-quick-definitions--student-cheat-sheet)
57. [Command Cheat Sheet](#57-command-cheat-sheet)
58. [10-Minute Quiz](#58-10-minute-quiz)
59. [Questions to Ask During Class](#59-questions-to-ask-during-class)
60. [Common Beginner Misconceptions](#60-common-beginner-misconceptions)

---

## 1. Computer

**Short definition:** A computer is an electronic device that takes input, processes data, stores information, and produces output.

**Simple model:**

```
Input → Processing → Output
           ↓
         Storage
```

**Example** — if the user enters `5 + 10`:

```
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
```

**Ask students:**
- What is an input?
- What is an output?
- Is a keyboard input or output?
- Is a monitor input or output?

**Answers:**
- Input = data/instructions given to the computer
- Output = information produced by the computer
- Keyboard = input
- Monitor = output

---

## 2. Hardware

**Short definition:** Hardware is the physical part of a computer that you can touch.

**Examples:** CPU, RAM, SSD/HDD, Motherboard, GPU, Keyboard, Mouse, Monitor, Network card, USB devices

> **Easy rule:** Hardware = something physical that you can touch.

---

## 3. CPU — Central Processing Unit

**Short definition:** The CPU is the main processor that executes instructions and performs calculations.

**Simple analogy** — think of the CPU as a worker:

```
Task
 ↓
CPU
 ↓
Processes instructions
 ↓
Result
```

Example:

```
Open Chrome
     ↓
CPU executes instructions
     ↓
Chrome runs
```

> **Important clarification:** People often call the CPU the "brain" of the computer. That's a useful analogy, but technically the CPU is a processor that executes instructions.

---

## 4. RAM — Random Access Memory

**Short definition:** RAM is temporary working memory used by the computer for data and programs currently in use.

**Best analogy:**

| Analogy | Real thing |
|---|---|
| Cupboard | SSD |
| Work desk | RAM |
| Worker | CPU |

The worker takes books out of the cupboard and puts them on the desk while working.

```
More RAM
 ↓
More working space
 ↓
More programs/data can be kept readily available
```

**Important distinction — ask:** "If my computer has 16 GB RAM, does it have 16 GB storage?"
**Answer:** No. RAM and storage are different things.

---

## 5. Storage

**Short definition:** Storage is where a computer keeps data persistently, even after the computer is turned off.

**Examples:** SSD, HDD, USB flash drive, External drive

**Stores things such as:** Operating system, Applications, Documents, Photos, Videos, Games, Projects

**Analogy:** RAM = Work desk · Storage = Cupboard

---

## 6. GPU — Graphics Processing Unit

**Short definition:** A GPU is a processor designed to handle graphics and many parallel computations efficiently.

**Examples:** Games, 3D graphics, Video rendering, Image processing, Some AI/ML workloads

> For beginners, don't go deeply into GPU architecture unless the class asks.

---

## 7. Input

**Short definition:** Input is data or instructions given to a computer.

**Examples:** Keyboard typing, Mouse click, Microphone, Camera, Touchscreen

---

## 8. Output

**Short definition:** Output is information produced by a computer after processing.

**Examples:** Text on screen, Images, Sound, Printed documents, Video

---

## 9. Hardware vs Software

| Hardware | Software |
|---|---|
| Physical components you can touch | Programs and instructions that tell a computer what to do |
| CPU, RAM, SSD, Keyboard, Mouse, Monitor | Windows, Linux, Chrome, VS Code, Microsoft Word, Games |

> **Easy rule:** Hardware is what you can touch. Software is what you run.

---

## 10. Operating System

**Short definition:** An operating system is the main software that manages computer hardware and provides an environment for applications to run.

**Examples:** Windows, Linux, macOS, Android, iOS

**Analogy diagram:**

```
User
 ↓
Application
 ↓
Operating System
 ↓
Hardware
```

For example, Chrome needs: CPU, RAM, Storage, Network, Display — the operating system helps applications use these resources.

```
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
```

---

## 11. What Does the OS Actually Do?

The operating system handles many responsibilities, including:

- Managing CPU time
- Managing memory
- Managing files and storage
- Managing devices
- Managing networking
- Providing security mechanisms
- Providing a user interface
- Allowing applications to run

**Examples:**

Chrome needs memory:
```
Chrome → Operating System → RAM
```

Chrome needs to save a file:
```
Chrome → Operating System → Storage
```

Chrome needs to communicate over a network:
```
Chrome → Operating System/network stack → Network interface → Network
```

---

## 12. Live OS Demonstration

**Windows** — Open **Task Manager**. Show students: CPU, Memory, Disk, Network, Running applications.

> "The operating system is managing and monitoring these resources while applications are running."

**Linux** — Try:

```bash
top
```

If `htop` is installed:

```bash
htop
```

Explain the CPU and memory information shown.

---

## 13. Application

**Short definition:** An application is a software program designed to perform a specific task for the user.

| Application | Purpose |
|---|---|
| Chrome | Browse the web |
| Word | Create documents |
| VS Code | Write code |
| WhatsApp | Messaging |
| Calculator | Calculations |

---

## 14. Network

**Short definition:** A network is a group of connected devices that can communicate and exchange data.

**Simple example:**

```
Laptop ─── Router ─── Phone
```

Or:

```
Laptop ── Wi-Fi ── Router
Phone  ── Wi-Fi ── Router
TV     ── Wi-Fi ── Router
```

---

## 15. Wi-Fi

**Short definition:** Wi-Fi is a wireless networking technology used to connect devices to a local network.

> **Important:** Wi-Fi is not the same thing as the internet.

```
Laptop
  ↓
Wi-Fi
  ↓
Router
  ↓
Internet
```

Wi-Fi can connect your laptop to your router even though the router's internet connection is a separate part of the setup.

---

## 16. Router

**Short definition:** A router is a network device that forwards data between networks and helps devices communicate with other networks.

**Analogy:** Think of a router as a traffic director.

```
Device
  ↓
Router
  ↓
Correct network/destination
```

| Analogy | Real thing |
|---|---|
| Cars | Data |
| Roads | Networks |
| Traffic director | Router |

---

## 17. IP Address

**Short definition:** An IP address is a network address used to identify a device/interface and route IP traffic.

**Example:** `192.168.1.10`

> "It is similar to an address used for network communication. It helps traffic know where it needs to go."

*Don't teach subnetting in this lesson.*

---

## 18. Private IP Address

**Short definition:** A private IP address is used within a local network such as a home, school, or office network.

**Example:** `192.168.1.10`

Other common private IPv4 ranges:

```
10.0.0.0/8
172.16.0.0/12
192.168.0.0/16
```

> For beginners, simply remember: **Private IP = used inside a local network.**

---

## 19. Public IP Address

**Short definition:** A public IP address is an IP address used for communication with the public internet.

```
Your Laptop
    ↓
Private IP
    ↓
Router
    ↓
Public IP
    ↓
Internet
```

*Avoid going into NAT unless students ask.*

---

## 20. Packet

**Short definition:** A packet is a small unit of data transmitted across a network.

**Simple demonstration** — write: `HELLO MY FRIEND`, then conceptually divide it:

```
HEL
LO
MY
FRI
END
```

> "Real network packets contain headers and other information. This is just a simple illustration of the idea that data is transmitted in units."

```
Large Data
    ↓
Packets
    ↓
Network
    ↓
Destination
    ↓
Data processed/reassembled
```

---

## 21. Internet

**Short definition:** The internet is a global network of interconnected networks that allows devices and systems to communicate.

**Ask:** "Is Wi-Fi the internet?" → **Answer: No.**

```
Wi-Fi     → Wireless connection to a local network
Internet  → Global interconnected network
```

---

## 22. ISP — Internet Service Provider

**Short definition:** An ISP is a company that provides internet connectivity to customers.

**Examples students may know:** PTCL, StormFiber, Nayatel, Transworld

```
Laptop → Router → ISP → Internet
```

---

## 23. Browser

**Short definition:** A web browser is software used to access, retrieve, and display websites.

**Examples:** Google Chrome, Mozilla Firefox, Microsoft Edge, Safari

---

## 24. Search Engine

**Short definition:** A search engine is a service that helps users find information and web pages on the internet.

**Examples:** Google Search, Bing, DuckDuckGo

---

## 25. Browser vs Search Engine

An important beginner distinction.

**Ask:** "Is Google Chrome Google?" → **Answer: No.**

```
Chrome        → Browser
Google Search → Search engine
```

```
Chrome → Google Search → Search results → Website
```

---

## 26. Website

**Short definition:** A website is a collection of web pages and resources available through the web under a domain or web address.

**Example:** `youtube.com`

A website can contain: Text, Images, Videos, Buttons, Forms, Interactive applications, and other resources.

---

## 27. Web Server

**Short definition:** A web server is a computer or software system that receives web requests and provides web content or services.

```
Browser
   ↓
Internet
   ↓
Web Server
   ↓
Response
   ↓
Browser
```

---

## 28. Domain Name

**Short definition:** A domain name is a human-readable name used to access a website or internet service.

**Examples:** `google.com`, `youtube.com`, `github.com`

Humans prefer `google.com` rather than remembering a numerical IP address.

---

## 29. DNS — Domain Name System

**Short definition:** DNS is a system that translates domain names into IP addresses and provides other information about internet domains.

**Simple analogy** — DNS is like a contacts list for internet names:

```
Your phone:  Ali → Ali's phone number
DNS:         google.com → IP address / DNS records
```

> **Important:** DNS does not deliver the website. It helps your system discover information needed to reach the service.

---

## 30. Live DNS Demonstration

**Windows / Linux / macOS:**

```bash
nslookup google.com
```

Linux/macOS also has:

```bash
dig google.com
```

**Explain:**

```
Domain name
     ↓
DNS query
     ↓
DNS response
     ↓
IP address/other records
```

---

## 31. URL — Uniform Resource Locator

**Short definition:** A URL is the address used to locate a resource on the web.

**Example:** `https://www.example.com/about`

| Part | Meaning |
|---|---|
| `https://` | Protocol/scheme |
| `www` | Subdomain |
| `example` | Domain name |
| `.com` | Top-level domain |
| `/about` | Path |

*Don't spend too much time on URL anatomy in a beginner class.*

---

## 32. Protocol

**Short definition:** A protocol is a set of rules that devices and software follow when communicating.

**Examples:** HTTP, HTTPS, TCP, IP, DNS

> Simple analogy: Protocols are like agreed rules for communication.

---

## 33. HTTP

**Short definition:** HTTP is a protocol used for communication between web clients and web servers.

```
Browser
   ↓
HTTP request
   ↓
Server
   ↓
HTTP response
   ↓
Browser
```

---

## 34. HTTPS

**Short definition:** HTTPS is HTTP carried over a secure TLS connection, providing encrypted communication between the client and server.

```
HTTP  → Web communication
HTTPS → Encrypted web communication
```

> **Important:** HTTPS helps protect communication, but HTTPS alone does not prove that a website is trustworthy.

---

## 35. How a Website Loads

**This is the most important section.**

**Ask:** "What happens when you type `google.com` and press Enter?" — walk through it slowly.

| Step | What happens |
|---|---|
| 1. User enters a URL | `https://google.com` |
| 2. Browser interprets the URL | The browser determines what resource it needs |
| 3. DNS lookup | The system/browser uses DNS to discover address information for the domain |
| 4. Network communication begins | The computer sends traffic through its network connection |
| 5. Traffic goes through the ISP | Router → ISP → Internet |
| 6. Traffic reaches the service | Internet → Google infrastructure |
| 7. Server responds | The service sends data back |
| 8. Browser receives the response | The browser processes the returned web resources |
| 9. Browser renders the page | The browser displays the webpage to the user |

**Complete diagram:**

```
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
```

> "A lot more happens in a real web request, but this is the simplified mental model you need at this level."

---

## 36. Useful Network Commands

### Windows

| Task | Command |
|---|---|
| Show network configuration | `ipconfig` |
| More detailed network configuration | `ipconfig /all` |
| Test connectivity/reachability | `ping google.com` |
| Query DNS | `nslookup google.com` |
| Show network path | `tracert google.com` |
| Show system information | `systeminfo` |

### Linux

| Task | Command |
|---|---|
| Show network interfaces | `ip addr` |
| Show IP address | `hostname -I` |
| Test connectivity/reachability | `ping google.com` (stop with `Ctrl+C`) |
| Query DNS | `nslookup google.com` or `dig google.com` |
| Show network path | `traceroute google.com` |
| Show system information | `uname -a` |
| Show RAM usage | `free -h` |
| Show disk usage | `df -h` |

---

## 37. Hands-On Activity #1 — Find Your Computer Information

Give students ~10 minutes to find:

1. Operating System
2. CPU
3. RAM
4. Storage
5. IP address
6. Browser

**Worksheet:**

```
Operating System: __________________
CPU:              __________________
RAM:              __________________
Storage:          __________________
IP Address:       __________________
Browser:          __________________
```

- **Windows:** use `systeminfo` and `ipconfig`
- **Linux:** use `uname -a`, `free -h`, `df -h`, `ip addr`

---

## 38. Hands-On Activity #2 — Test the Network

1. Run `ping google.com` — explain that ping tests whether a destination responds to ICMP echo requests and can show round-trip timing.
2. Run `nslookup google.com` — ask: *"What IP address did DNS return?"*
3. Run `tracert google.com` (Windows) or `traceroute google.com` (Linux).

> "This can show the path discovered toward the destination. It may not show every actual network device/path because routers and networks can filter or handle these probes differently."

---

## 39. Files

**Short definition:** A file is a stored collection of digital data.

**Examples:** `photo.jpg`, `assignment.pdf`, `program.py`, `video.mp4`, `resume.docx`

---

## 40. Folder

**Short definition:** A folder is a container used to organize files and other folders.

**Example:**

```
Projects/
├── Python/
├── Web/
└── AI/
```

---

## 41. File Extension

**Short definition:** A file extension commonly indicates the format or type of a file.

| Extension | Type |
|---|---|
| `.pdf` | PDF document |
| `.jpg` / `.png` | Image |
| `.py` | Python source file |
| `.docx` | Word document |
| `.mp4` | Video |
| `.xlsx` | Spreadsheet |

---

## 42. File Path

**Short definition:** A file path tells the computer where a file or folder is located.

**Example:** `Documents/Projects/Python/app.py`

On Windows, paths may look like: `C:\Users\Student\Documents\Projects\Python\app.py`

---

## 43. Download

**Short definition:** Downloading means transferring data from a remote system to your device.

```
Internet/Server
      ↓
   Computer
```

*Example: Downloading a PDF from a website.*

---

## 44. Upload

**Short definition:** Uploading means transferring data from your device to a remote system.

```
Computer
   ↓
Internet/Server
```

*Example: Uploading an assignment to Google Drive.*

---

## 45. Why File Organization Matters

Show students this bad example:

```
Downloads/
├── final.pdf
├── final2.pdf
├── newfinal.pdf
├── newfinal2.pdf
├── assignment.pdf
├── image.png
├── random.zip
└── document.docx
```

**Ask:** "Will you easily find the correct file six months from now?"

> Good file organization makes files easier to find, manage, share, and back up.

---

## 46. Good Folder Structure

```
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
```

*The exact structure can vary — the important thing is consistency.*

---

## 47. File Naming

**Bad names:**
```
final.pdf
final2.pdf
newfinal.pdf
newfinal2.pdf
assignmentfinalREAL.pdf
```

**Better names:**
```
Networking_Assignment_01.pdf
Python_Loops_Quiz.pdf
CV_2026.pdf
Project_Report_v1.pdf
Project_Report_v2.pdf
```

**Good file names should be:**
- Descriptive
- Consistent
- Easy to search
- Easy to understand later

For versions: `Report_v1`, `Report_v2`, `Report_v3`

---

## 48. Downloads Folder

> "The Downloads folder is where downloaded files often arrive. It does not have to be your permanent organization system."

**Good workflow:**

```
Download file
     ↓
Check file
     ↓
Rename if necessary
     ↓
Move to correct folder
     ↓
Back up important files
```

---

## 49. Cloud Storage

**Short definition:** Cloud storage is a service that stores files on remote servers and allows users to access them over a network, usually the internet.

**Examples:** Google Drive, OneDrive, Dropbox, iCloud

```
Your Computer
      ↓
   Internet
      ↓
Cloud Service
      ↓
Remote Servers
```

---

## 50. Benefits of Cloud Storage

- **Access** — Laptop, Phone, and other computers can all reach the same files
- **Sharing** — you can share files with other people
- **Availability** — if your laptop stops working, a cloud copy may still be available
- **Collaboration** — multiple people can sometimes work with shared documents/files

---

## 51. Sync vs Backup

An important concept.

**Synchronization** — keeps data or files consistent across multiple locations or devices:

```
Laptop ↕ Cloud ↕ Phone
```

**Backup** — an additional copy of important data kept so it can be restored if the original is lost or damaged.

> **Warning:** Sync is not automatically the same as backup. If a synchronized file is deleted and the deletion propagates, the cloud copy may also be deleted.

**Recommended approach:**

```
Important file
     ↓
Local copy
     +
Cloud copy
     +
Separate backup when appropriate
```

---

## 52. Hands-On Activity #3 — Build a Digital Workspace

Give students 20–30 minutes.

1. Create a folder: `Computer_Class`
2. Inside it, create:
   ```
   Computer_Class/
   ├── Notes/
   ├── Assignments/
   ├── Projects/
   └── Resources/
   ```
3. Inside `Assignments`, create:
   ```
   Assignments/
   ├── Assignment_01/
   └── Assignment_02/
   ```
4. Create a file `My_Computer_Info.txt` containing:
   ```
   Operating System:
   CPU:
   RAM:
   Browser:
   ```
5. Save it in `Computer_Class/Notes/`
6. Upload it to their cloud storage
7. Open the file from the cloud

Students have now practiced: **Files → Folders → File naming → Local storage → Cloud storage**

---

## 53. Hands-On Activity #4 — Organize a Messy Folder

Give students these imaginary files:

```
resume.pdf
python_notes.pdf
family_photo.jpg
assignment.docx
movie.mp4
certificate.pdf
project.zip
```

Ask them to create these folders and move each file to the appropriate one:

```
Documents/
Education/
Photos/
Videos/
Certificates/
Projects/
```

---

## 54. Final Practical Challenge

**Tell students:** "You type `youtube.com` into your browser and press Enter. Explain what happens."

A good beginner answer should look like:

```
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
```

---

## 55. Final Big Picture

```
                         COMPUTER
                             │
               ┌─────────────┴─────────────┐
               │                            │
           HARDWARE                     SOFTWARE
               │                            │
       CPU / RAM / SSD               APPLICATIONS
               │                            │
               └─────────────┬──────────────┘
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
```

---

## 56. Quick Definitions — Student Cheat Sheet

Keep this section available during revision.

| Topic | Short Definition |
|---|---|
| Computer | Electronic device that takes input, processes data, stores information, and produces output. |
| Hardware | Physical parts of a computer that can be touched. |
| Software | Programs and instructions that tell a computer what to do. |
| CPU | Processor that executes instructions and performs calculations. |
| RAM | Temporary working memory used by programs and the operating system. |
| Storage | Persistent place where files, applications, and data are stored. |
| GPU | Processor specialized for graphics and parallel computations. |
| Input | Data or instructions given to a computer. |
| Output | Information produced by a computer. |
| Operating System | Software that manages hardware and provides an environment for applications. |
| Application | Software designed to perform a specific task. |
| Network | Connected devices that communicate and exchange data. |
| Wi-Fi | Wireless technology for connecting devices to a local network. |
| Router | Device that forwards traffic between networks. |
| IP Address | Network address used to identify a device/interface and route IP traffic. |
| Private IP | IP address used inside a local/private network. |
| Public IP | IP address used for communication with the public internet. |
| Packet | Small unit of data transmitted across a network. |
| ISP | Company that provides internet connectivity. |
| Internet | Global network of interconnected networks. |
| Browser | Software used to access and display websites. |
| Search Engine | Service that helps users find information on the web. |
| Website | Collection of web pages/resources available through the web. |
| Web Server | Computer/software system that provides web content or services. |
| Domain Name | Human-readable name used to access an internet service. |
| DNS | System that provides information about domains, including resolving names to IP addresses. |
| URL | Address used to locate a resource on the web. |
| Protocol | Rules that devices/software follow to communicate. |
| HTTP | Protocol used for web communication. |
| HTTPS | HTTP communication protected by TLS encryption. |
| File | Stored collection of digital data. |
| Folder | Container used to organize files and folders. |
| File Extension | Suffix that commonly indicates a file's format/type. |
| File Path | Location of a file or folder in a filesystem. |
| Download | Transfer data from a remote system to your device. |
| Upload | Transfer data from your device to a remote system. |
| Cloud Storage | Storage provided on remote servers and accessed over a network. |
| Sync | Keeps data/files consistent across multiple locations. |
| Backup | Additional copy of data kept for recovery. |

---

## 57. Command Cheat Sheet

| Task | Windows | Linux |
|---|---|---|
| Show IP/network information | `ipconfig` | `ip addr` |
| Show detailed network info | `ipconfig /all` | `ip addr` |
| Show IP address | `ipconfig` | `hostname -I` |
| Test connectivity | `ping google.com` | `ping google.com` |
| DNS lookup | `nslookup google.com` | `nslookup google.com` |
| Alternative DNS tool | — | `dig google.com` |
| Trace network path | `tracert google.com` | `traceroute google.com` |
| System information | `systeminfo` | `uname -a` |
| RAM information | Task Manager | `free -h` |
| Disk usage | File Explorer/Settings | `df -h` |

---

## 58. 10-Minute Quiz

<details>
<summary><strong>Q1.</strong> What is hardware?</summary>

A. Programs&nbsp;&nbsp;B. Physical computer components&nbsp;&nbsp;C. Internet data&nbsp;&nbsp;D. Websites

**Answer: B**
</details>

<details>
<summary><strong>Q2.</strong> Which component executes instructions?</summary>

A. SSD&nbsp;&nbsp;B. Monitor&nbsp;&nbsp;C. CPU&nbsp;&nbsp;D. Keyboard

**Answer: C**
</details>

<details>
<summary><strong>Q3.</strong> What is RAM primarily used for?</summary>

A. Permanent file storage&nbsp;&nbsp;B. Temporary working memory&nbsp;&nbsp;C. Printing&nbsp;&nbsp;D. Internet connectivity

**Answer: B**
</details>

<details>
<summary><strong>Q4.</strong> Which one is an operating system?</summary>

A. Chrome&nbsp;&nbsp;B. Google Search&nbsp;&nbsp;C. Windows&nbsp;&nbsp;D. YouTube

**Answer: C**
</details>

<details>
<summary><strong>Q5.</strong> What does a router primarily do?</summary>

A. Store photos&nbsp;&nbsp;B. Forward network traffic between networks&nbsp;&nbsp;C. Run Word documents&nbsp;&nbsp;D. Display images

**Answer: B**
</details>

<details>
<summary><strong>Q6.</strong> What does DNS help with?</summary>

A. Converting domain names into network address information&nbsp;&nbsp;B. Increasing RAM&nbsp;&nbsp;C. Editing photos&nbsp;&nbsp;D. Creating folders

**Answer: A**
</details>

<details>
<summary><strong>Q7.</strong> Which one is a web browser?</summary>

A. Google Search&nbsp;&nbsp;B. Chrome&nbsp;&nbsp;C. DNS&nbsp;&nbsp;D. IP address

**Answer: B**
</details>

<details>
<summary><strong>Q8.</strong> Is Wi-Fi the same as the internet?</summary>

A. Yes&nbsp;&nbsp;B. No

**Answer: B**
</details>

<details>
<summary><strong>Q9.</strong> What is a packet?</summary>

A. A computer monitor&nbsp;&nbsp;B. A unit of data transmitted across a network&nbsp;&nbsp;C. A type of folder&nbsp;&nbsp;D. An operating system

**Answer: B**
</details>

<details>
<summary><strong>Q10.</strong> What is a backup?</summary>

A. A browser&nbsp;&nbsp;B. A network protocol&nbsp;&nbsp;C. An additional copy of data kept for recovery&nbsp;&nbsp;D. A type of CPU

**Answer: C**
</details>

---

## 59. Questions to Ask During Class

Instead of continuously lecturing, stop and ask:

**Hardware**
- "Can you touch software?" → No.
- "Is RAM storage?" → No.
- "Which component executes instructions?" → CPU.

**Operating Systems**
- "Can Chrome normally run without an operating system?" → Explain that applications rely on the operating system and underlying system software to access hardware/resources.

**Networking**
- "Is Wi-Fi the internet?" → No.
- "What device normally connects your local network to another network?" → Router.
- "What identifies/addresses network interfaces for IP communication?" → IP address.

**Web**
- "Is Chrome a search engine?" → No.
- "What does DNS do?" → Provides domain-related information, including resolving domain names to IP addresses.
- "Where does website content/services come from?" → From servers/services on the network.

---

## 60. Common Beginner Misconceptions

| # | Misconception | Correction |
|---|---|---|
| 1 | "CPU is the whole computer." | CPU is one important component inside a computer. |
| 2 | "RAM stores files permanently." | RAM is temporary working memory. Storage such as an SSD keeps data persistently. |
| 3 | "Google Chrome is Google." | Chrome is a browser. Google Search is a search engine. |
| 4 | "Wi-Fi is the internet." | Wi-Fi is a wireless networking technology. It can connect your device to a local network, which may then connect to the internet. |
| 5 | "DNS is the internet." | DNS is a naming system used to look up information about domains. |
| 6 | "A website is stored inside my browser." | The browser retrieves web resources from servers/services and renders them on your device. |
| 7 | "Cloud means my files are nowhere." | Cloud storage means files are stored on remote computers/servers operated by a service and accessed over a network. |
| 8 | "Sync and backup are exactly the same." | Synchronization keeps copies aligned; a backup is a separate recovery copy. Sync alone is not necessarily a sufficient backup. |
