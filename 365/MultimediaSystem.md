# Introduction

### Why multimedia?

* Multimedia is cool
  * Media -> Multimedia
    * Media: any thing can convey information is a media. 
    * e.g. text, pictures, audio, video, AR, VR. 
    * Combine these together -> multimedia. 
    * Single one is just media, not multimedia, but boundary is not that clear. 
  * Everywhere
    * Everything captured in real world will transferred to signals.
  * Requires broad knowledge in mathematics, signal processing, communications, networking, software, hardware, ...
  * You are paid to watch movies at your office!
    * What kind of resolution in this movie? 
    * What kinds of coding in this movie?
    * What kind of camera using in this movie?
    * How many tracks of this sound?
* Job opportunities
  * Multimedia is a booming industry
  * Tons of opportunities created by next-generation standards and emerging applications:
    * image compression standard: JPEG / JPEG 2000 
      * PNG using the same underlying technique
    * video/audio compression standard: MPEG-1/2/4    H.264/265/HEVC    4K/8K UHD    3D/freeview
      * UHD = Ultra High Definition
    * Communication: 3G/4G/5G mobile communications
    * Multimedia-enabled smartphone, tablets
    * Social media, Cloud media, Crowd media
    * Cloud media - store things in cloud, interactive with cloud, like Zoom meeting. 
    * Crowd media - everyone can generate their own content, like Youtube, you can record a video by OBS and upload it.
    * Online gaming
      * much higher demand - computation, communication
      * sensitive to the quality, sensitive to delay

### Multimedia Example

* 1G / 2G around 2000
* audio is good enough in 2G
* Old: NTT DoCoMo 3G Mobile Phone:
  * launch in 2001
  * 99% coverage in Japan as of March 2004
  * Up to 384 kbps video downloading
  * 40 times faster than 2G network (comparable to ADSL)
  * Telus using ADSL
* New: 4G LTE Mobile Phone:
  * 100 Mbps stationary
  * allow 3D virtual reality and interactive video / hologram images 
  * Commercial service since in 2010
  * 97% of the population in Canada now
* Even newer: 5G
  * speed: 1 Gbps/s
  * less than 10~50 milliseconds delay
  * VR/AR/Car …
    * Augmented Reality 增强现实技术
* Web2.0/Media streaming (Internet TV)
  * difference with Web1.0: interaction (交互), user can generate their own content on Internet. 
  * YouTube, Netflix, Twitch, TikTok
  * 4K/8K/16K HD/UHD video? 
  * 3D/360 degree video ?
* E-commerce
  * Ebay, Amazon, Craigslist, Groupon
* Online game
  * PS, XBOX, Switch
* …
* Social networking (2004-)
  * Facebook, Twitter …
  * Instagram, TikTok …
  * WhatsApp, Wechat …
* AR/VR
* AI

### Multimedia Companies

* Microsoft
* Intel
* AMD
* Adobe
* Apple
* Amazon
* Google
* Facebook
* Twitter
* Zoom
* Sony
* NVidia
* Philips
* Twitch
* YouTube
* Netflix
* Huawei
* Qualcomm
* …

<img src="img/1.1.png" />

### What are the objectives of this course?

* Understand what behind the interface
  * Behind BluRay, HD TV, mp3, mp4, flac, raw, jpeg? ...
  * 3D, 4K/8K UHD TV?
  
* Process multimedia data by yourself (programming projects)

* Have fun!
  
  * What a life without multimedia?
  
    * A PC with black-white monitor only ...
  
    <img src="img/1.2.png" />
  
* To understand the methods for multimedia **representation** and **compression**

  * *Representation* (audio/video)
    * Digitization - input signal is analog, eg, audio from microphone, video from CCD
    * Quantization 量子化 - make the analog discrete numbers. The process is also called sampling. The data captured by this method can be quite big, eg, raw image. 
  * *Compression* (audio/video)
    * Transform - initial sample of each pixel of an image or video, if manipulate directly on these pixels, it would be difficult. So you need to transform them into frequency domain (频率范围，频域). For sound, you have time domain samples, so that the sound contains different frequencies, and these frequencies are easier to manipulate, and later compress.
    * Entropy Coding (平均信息量代码) - The representative of information in term of bits. Based on this, we know that how much information is redundant in original data representation, and how much information is necessary to recapture. 
    * Coding Standards - mp3, JEPG, mp4

* To study the issues in multimedia **communications**

  * QoS Requirements
    *  QoS (Quality of Service) is measure by delay, by bandwidth, by loss rate, etc.
  * Network Protocols
    * TCP, UDP, IP, RTP ...
  * Streaming Media

* Multimedia database

  * Organization
  * Retrieval - multimedia retrieval
    * based on tag, eg, Google search
    * Machine Learning, e.g. search pictures

* To help you survive a job interview in multimedia

  * Programming assignments
  * C, C++, Java, Matlab could be involved

## What is "media"?

* Information represented in different formats/media
  * **Discrete** media: time independent
    * text
    * graphics
    * images
  * **Continuous** media: time dependent
    * animation
    * audio
    * video
* Analog vs. Digital
  * analog format: the time-varying feature (variable) of the signal is a continuous representation of the input, i.e., analogous to the input audio, image, or video signal.
  * Physical world is analog!

### Hyper Text, Hypermedia

* A **hypertext** system: meant to be read nonlinearly, by following links that point to other parts of the document, or to other documents. 

  <img src="img/1.3.png" style="display: inline"/> <img src="img/1.4.png" style="display: inline"/>

* HTML / XML

```html
<HTML>
    <HEAD>
        <TITLE>A sample web page.</TITLE>
        <META NAME="Author" CONTENT="Professor" />
    </HEAD>
    <BODY>
        <P>
            We can put any text we like here, since this is a paragraph element.
        </P>
    </BODY>
</HTML>
```

* HyperMedia

  * not constrained to be text-based, can include other media, e.g., graphics, images, and especially the continuous media: sound and video. 
  * World Wide Web (WWW) --- the best example 

  <img src="img/1.5.png">

### Multimedia System

##### Multimedia

information represented through audio, graphics, images, video, and animation in an integrated and interactive manner (as contrast to traditional single-modality media, i.e., text and graphics drawing).

##### Multimedia system

the generation, manipulation, storage, presentation, and communication of multimedia information. 

### Digital Media

##### Multimedia digitized

* Captured, stored, transmitted, processing in digital (discrete) domain
* By general purpose computers or dedicated embedded computers
  * Today's digital cameras' have a number of CPUs inside, many of which are more powerful than a PC of 1990's or even 2000's.
* What do you mean by **digitized**?
* Why **digitized**?

### (Digital/Computer) Multimedia Systems

* Using computers to present and process multimedia information, in an integrated and interactive manner. 
* Examples of Multimedia Systems: 
  * Digital camera / camcord
  * World Wide Web
  * Video conferencing
  * Video-on-demand
  * Interactive TV
  * Online games
  * Virtual reality
  * Digital video editing and production systems
  * Multimedia Database systems
  * Social media

### Different Views

* Different views from different people
  * A PC vendor: a PC that has sound capability, a DVD/BluRay drive, and perhaps the superiority of multimedia-enabled CPU/GPU (Graphical Processing Unit) that understand additional multimedia instructions. 
  * A consumer entertainment vendor: interactive cable TV with hundreds of digital channels available, or a cable TV-like service delivered over a high-speed Internet/wireless connection. 
  * A computer Science (CS) student: applications that use multiple modalities, including text, images, drawings (graphics), animation, video, sound including speech; **integration** and **interactivity**. 
* Multimedia and Computer Science: 
  * Data representation compression
  * Graphics, visualization, computer vision
  * Networking, database systems

### Multimedia Research Topics and Projects

To the computer science researcher, multimedia consists of a wide variety of topics: 

1. **Multimedia processing and coding**
   * multimedia content analysis
   * content-based multimedia retrieval
   * multimedia security
   * audio/image/video processing 
   * compression
2. **Multimedia system support and networking**
   * network protocols 
   * Internet
   * operating systems
   * servers and clients
   * quality of service (QoS)
   * databases
3. **Multimedia tools, end-systems and applications**
   * hypermedia systems
   * user interfaces
   * authoring systems
4. **Multi-modal interaction and integration**
   * web-everywhere devices
   * multimedia education including Computer Supported Collaborative Learning
   * design and applications of virtual environments

### History of Multimedia

1. **Newspaper**
   * perhaps the first mass communication medium, uses text, graphics, and images.
2. **Motion pictures**
   * conceived of in the 1830's in order to observe motion too rapid for perception by the human eye. 
3. **Wireless radio transmission**
   * Gugliemo Marconi, at Pontecchio, Italy, in 1895.
4. **Television**
   * the new medium for the 20th century, established video as a commonly available medium and has since changed the world of mass communications.
5. **Computers**
   * the connection between computers and ideas about multimedia covers what is actually only a short period: 1945 -- Vannevar Bush wrote a landmark article describing what amounts to a hypermedia system called Memex. 

| Year | 事件                                                         |
| ---- | ------------------------------------------------------------ |
| 1960 | Ted Nelson coined the term **hypertext**.                    |
| 1967 | Nicholas Negroponte formed the **Architecture Machine Group**. |
| 1968 | Douglas Engelbart demonstrated the **On-Line System (NLS)**. |
| 1969 | Nelson and van Dam at Brown University created an early hypertext editor called **FRESS**. |
| 1976 | The MIT Architecture Machine Group proposed a project entitled **Multiple Media**: resulted in the Aspen Movie Map, the first hypermedia videodisk, in 1978. |
| 1985 | Negroponte and Wiesner co-founded the **MIT Media Lab**.     |
| 1989 | Tim Berners-Lee proposed the **World Wide Web**              |
| 1990 | Kristina Hooper Woolsey headed the **Apple Multimedia Lab**. |
| 1991 | **MPEG-1** was approved as an international standard for digital  video - led to the newer standards, **MPEG-2**, **MPEG-4**, and further **MPEGs** in the 1990s. |
| 1991 | The introduction of **PDAs** in 1991 began a new period in the use  of computers in multimedia. |
| 1992 | **JPEG** was accepted as the international standard for digital  image compression - led to the new JPEG2000 standard. |
| 1992 | The first **MBone** audio multicast on the Net was made.     |
| 1993 | The University of Illinois National Center for  Supercomputing Applications produced **NCSA Mosaic  -**the first full fledged browser. |
| 1994 | Jim Clark and Marc Andreessen created the **Netscape**       |
| 1995 | The **JAVA** language was created for platform-  independent application development. |
| 1996 | **DVD video** was introduced; high quality full-length  movies were distributed on a single disk. |
| 1998 | **XML** 1.0 was announced as a W3C Recommendation.           |
| 1998 | **Hand-held MP3 devices** first made inroads into  consumerist tastes in the fall of 1998, with the  introduction of devices holding 32MB of flash memory. |
| 2000 | WWW size was estimated at over **1 billion pages**.          |
| 2001 | The first peer-to-peer file sharing system, Napster, was shut down by court order. First commercial 3G wireless network. |
| 2003 | Skype: free peer-to-peer voice over the Internet.            |
| 2004 | Web 2.0 promotes user collaboration and interaction. Examples include social networking, blogs, wikis. |
| 2004 | Facebook founded                                             |
| 2004 | Flickr founded                                               |
| 2005 | YouTube created                                              |
| 2005 | Google launched online maps                                  |
| 2006 | Twitter created: 500 million users in 2012, 340 million tweets/day. |
| 2006 | Amazon launched its cloud computing platform.                |
| 2006 | Nintendo introduced the Wii home video game console -- can detect movement in three dimensions. |
| 2007 | Apple launched iPhone, running the iOS mobile operating system. . |
| 2007 | Google launched Android mobile operating system.             |
| 2009 | The first LTE (Long Term Evolution) network was set, an important step toward 4G wireless networking. |
| 2009 | James Cameron's film, Avatar, a surge on the interest in 3D video. |
| 2010 | Netflix migrated its infrastructure to the Amazon's cloud computing platform. |
| 2010 | Microsoft introduced Kinect, a horizontal bar with full-body 3D motion capture, facial recognition and voice recognition capabilities, for its game console Xbox 360. |
| 2012 | HTML5 subsumes the previous version, HTML4. Able to run on low powered devices such as smartphones and tablets. |
| 2013 | Twitter offered Vine, a mobile app that enables its users to create and post short video clips. |
| 2013 | Sony released its PlayStation 4, a video game console, which is to be integrated with Gaikai, a cloud-based gaming service. |
| 2013 | 4K resolution TV started to be available in the consumer market. |
| 2015 | YouTube launched support for publishing and viewing 360-degree videos. |
| 2015 | AlphaGo, a computer program that plays the board game Go, became the first program to beat a human professional player. The event attracted significant attention from the general public, particular on its core technology, deep learning, which, in the coming years, has seen success in multimedia content understanding and generation. |
| 2016 | HoloLens, a pair of mixed reality smartglasses developed and manufactured by Microsoft, started to be available in the market. |
| 2016 | Pokémon Go, an augmented reality (AR) mobile game, was released and credited with popularizing location-based and AR technologies. |
| 2016 | Netflix completely migrated to the Amazon AWS cloud platform, so for Skype to move to the Microsoft Azure platform. |
| 2017 | TikTok, a video-sharing social networking service for creating and sharing short lip-sync, comedy, and talent videos, was launched for the global market (it's Chinese version, Douyin, was launched in 2016). |
| 2018 | World's first 16K Ultra High Definition (UHD) short video film, Prairie Wind, was created. |
| 2019 | 5G cellular systems started deployment, providing enhanced mobile broadband and ultra low latency access. |
| 2019 | WiFi 6 (802.11ax) standard was released, offering theoretical maximum throughput of 1 Gbps. |
| 2020 | Due to the outbreak of coronavirus (COVID-19) around the world, work/study from home became a norm in early 2020. Multimedia-empowered online meeting and teaching tools, e.g., Zoom, Google Class, and Microsoft Teams, have seen booming use during this period. |

* Year 2000 - your time ...
* Image/Audio
  * Huge/cheap HDD/SSD
  * High bandwidth/unlimited data plan
    * 3G/4G/5G
    * ADSL. Fiber
  * Cloud/data center
  * No worry anymore?
    * 4K-8K UHD (ultra-high definition) - 48-200 Gbps uncompressed
    * VR/AR
      * 16K video
      * Near zero delay

### Past Decade

* Skype/YouTube/Netflix
  * Replacing phone, movie theatre, TV!
* AR/VR immersive media
  * Pokémon Go!
  * MS HoloLens
* Cloud gaming
  * OnLive
  * Gaikai
  * Sony
* Livecast
  * Twitch.tv
  * eSports broadcast
* Drone/car
* Deep learning

<img src="img/1.6.png" style="display:inline"/> <img src="img/1.7.png" style="display:inline"/> <img src="img/1.8.png" style="display:inline"/> <img src="img/1.9.png" style="display:inline"/> <img src="img/1.10.png" style="display:inline"/><img src="img/1.11.png" style="display:inline"/> <img src="img/1.12.png" style="display:inline"/> 

### Digital Media Timeline

<img src="img/1.13.png" />

<img src="img/1.14.png" />

