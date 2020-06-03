### What is the Internet

* Networks include many connected devices: 
  * workstations, laptops, tablets, mobile devices, TVs, other "Things" in the IOT (Internet of things)
    * IOT = smart devices connect to Internet, such as smart TV, smart washing machine, toaster, light switches, blender 
  * Routers, switches, servers, base stations ...
    * router, an equipment on the network, it allows information to be sent from one network to another, or from one part of the network to another.
    * Base Station 基站，又称基地台，是固定在一个地方的高功率、多信道、双向无线电发送机。
* The Internet is a collection of networks
* Networks of connected devices use protocols to communicate. 
* Communication = 
  * sending and receiving messages
  * taking actions on receiving or sending messages (or other events).

<img src="img/1.9.png" />

### End systems: the network edge 终端系统：网络边缘

* An end system (host) can be a source system, and/or a destination system at the edge of the Internet.
* 端系统 - 通常把与因特网相连的计算机和其他设备成为端系统。
  * 端系统也成为主机，因为它们容纳（即运行）应用程序。
* End systems connect to the network using <u>communication links</u> (通信链路). 
  * wired - Guided media 引导媒体: Copper wire (coaxial 同轴的, twisted pair 双绞线), optical fiber
    * loss a little bit power by going down the wire, but it's not spreading on all direction.
  * wirelessly - Unguided media: air (radio, microwave, IR ...)
    * by default, things will go all direction.
* End systems are also referred to as hosts(主机). They may clients and/or servers 
  * A **client** *consumes* a service - 非正式地等同于桌面PC、移动PC和智能手机等
  * A **server** *provides* a service - 非正式地等用于更为强大的机器，用于存储和发布Web页面、流视频、中继电子邮件等。
  * An end system can be a consumer of one service and a provider of another service. 

##### Examples of end systems

* Mobile phone
* Personal computer
* Server supporting a service
* Tablet
* TV
* Gaming Console
* GPS
* Others?

### Access Network 接入网

* 接入网 - 指将端系统连接到其边缘路由器(edge router)的物理链路。
* 边缘路由器 - 是端系统到任何其他远程端系统的路径上的第一台路由器。

##### 家庭接入：DSL、电缆、FTTH、拨号和卫星

###### 数字用户线 DSL - Digital Subscriber Line

* 住户从提供本地电话接入的本地电话公司处获得DSL因特网接入。（因此，使用DSL时，用户的本地电话公司也是他的ISP）
* 每个用户的DSL调制解调器使用现有的电话线（双绞铜线）与位于本地电话公司的本地中心局（CO）中的数字用户线接入复用器（DSLAM）来交换数据。
* 家庭的DSL标志解调器得到数字数据后将其转换为高频音，以通过电话线传输给本地中心局
* 来自许多家庭的模拟信号在DSLAM处被转换回数字形式

<img src="img/1.18.png" />



### Services the Internet provides

* **Communication** between end systems
* Communication supports many applications. Some applications include:
  * WWW (world wide web)
  * Email, chat, video
  * E-Commerce, E-banking
  * Games, social media

### Data Communications

* Many ways to transmit the information
  * Voice - in person, by telephone, Internet, physically sending recorded media, wireless
  * Data - on paper disk or tape, vocally(声音地) or digitally using LAN, WAN, internet, or wireless
* Want to send information from one location to another efficiently and accurately
* Many transmission methods have independently evolved for particular types of data. 
* Different transmission methods, used for voice, data, internet and video have converged(融合). 
* all this information translates to electrical signals.

### Source Systems, Transmission 源系统，传输

* **Source System**: Includes *data source* and *transmitting device* which encodes data into electromagnetic(电磁) signals suitable for transmission through the transmission medium. 
* Example of Source Systems
  * Smartphone
  * Personal Computer

### Destination Systems  目标系统

* **Destination System**: Includes a *receiver* to intercept the transmitted electromagnetic signals from the transmission system and to decode/demodulate the those signals into a form appropriate for the destination device. 

### Examples of Source and Destination Systems

* Landline Telephone 固定电话
  * encodes/modulates voice or data into electrical signals to be carried through a line and a switching system. The switching system decides where to go next, and it takes the information to another switching system, ... , and eventually it will connect to the receiving phone. It forms a path, and all the information travel alone back and forth on that path. 
  * decodes/demodulates signals carried through a line and a switching system into voice or data.
  * most of the old phones are using analog signal.
  * nowadays, most of landline telephone are digital phones, that's why landline phone and Internet are same company, they are sharing a line. the way to transmit and encode will determine how the line is shared, and which part of the bandwidth or frequency are available.
* Cellular Telephone, Satellite or Radio
  * encodes/modulates voice or data into signals to be sent through an antenna(天线).
    * The information translate into binary data.
  * decodes/demodulates electromagnetic signals received by an antenna into voice or data. 
* Personal Computer
  * encodes/modulates a data stream of binary bits to a form that can be efficiently carried through a computer network. 
  * decodes/modulates an electromagnetic signals from a computer network and reconstructs the information that was sent. 

### Transmission of Information

* Information is sent from a source system to a destination system.
  * The information must be fed into the source system 
  * The information must be encoded into a form the source system can send (usually into an electromagnetic signal)
  * The information travels through some transmission medium to the destination system
  * The destination system must be able to interpret (decode) the received signal
  * The decoded signal must be translated into a form that the operator of the destination system can understand

### Simplified Communications Model

<img src="img/1.10.png" />

### Data Communication Networking

* The problem is more complex than point to point connection
  * Source and destination may be separated by large physical distances. 
  * Links may only be needed for a short time, dedicated links(专用链路) would be too expensive.
  * Many devices, any of which may be the source or destination at a given time. 
  * Multiple pairs of source and destination may wish to communicate through the same medium at the same time. 
* These problems are addressed using *networking protocols*
  * All devices communicate via a net of connections
  * Efficiency and accuracy is maintained using protocols

### What is a protocol?

**Network protocol** are sets of established rules that dictate how to format, transmit and receive data so computer network devices - from servers and routers to endpoints - can communicate regardless of the differences in their underlying infrastructures, designs or standards. 

一个**协议**定义了在两个或多个通信实体之间交换的报文格式和次序，以及报文发送和/或接收一条报文或其他事件所采取的的动作。

A **human protocol** and a **computer network** protocol:

<img src="img/1.11.png" />

### Why a Network  /  why do we use network

* The number of stations is large, it is not possible to have dedicated connections to all other end systems. 
* The distance between two stations may be long enough that the transmission media cannot carry the signal from the source to the receiver without introducing many errors, going through intermediate devices will fix this problem. 
  * as the signal travel down the cable, some energy radiated(放射).
* Worldwide connectivity is desired. 

### Station Interconnection  

* The number of station is large.

##### method 1: direct connection

* Direct connection between all stations is not practical: $n(n-1)/2$ connections are needed
* Connection using a shared bus limited by distance (long paths with loss of signal due to attenuations(衰减)). Bus can carry information, lacks redundancy(冗余) (any failure of link destroys connectivity), and allows only 1 message to travel at a time.

<img src="img/1.12.png" />



##### method 2: tree routes

* connection in a tree routes too much traffic through the root. 

  <img src="img/1.13.png" />

* Connection through a Partially Connected Network distributes traffic(流量) and provides redundancy. Also provides a mechanism for repeating signals to enable long distance propagation(传播). 

  * redundancy(冗余) - 信息的冗余度是指同一信息通过不止一种媒介披露，或通过同一媒介披露不止一次。

##### method 3: Station Interconnection

* Connection through a Partially Connected Network provides redundancy and intermediate stations along the path to act as repeaters(中继站).

* Why is a shorter wire better?

  * guided wave transmission. Stations going through wires. When a signal goes through wire, it lose power. If the wire is too long, then the signal will not have enough power at the end.

* What would power loss look like in the signal?

  * as the power lose, the difference between the two signals gets closer and closer, then it's hard to tell the difference.

  ```
  ---------------------------
  						|									-----------------
  						|							==>      				 |
  						|													|
  						|													---------------
  						-------------------------								
  		high power, high amplitude									low power, low amplitude
  ```

  

<img src="img/1.15.png" />



### Wide Area Networks (WAN) 广域网

* A WAN covers a large geographical area
* A WAN often uses common carrier or public right-of-ways. (广域网通常使用公共运营商或公共通行权)
* A WAN uses internal nodes to move data through network. 

<img src="img/1.14.png" />

### Local Area Networks (LAN)

* A LAN interconnects a variety of devices in a small area: Building or campus scope.
* LAN is usually owned / controlled and managed by one organization. 
* Most common types of LANs are 
  * Ethernet 以太网 (TCP/IP)
  * ATM = Asynchronous Transfer Mode 异步传输模式 (protocols used mostly by phone companies)
  * Wireless 

### Travel through a network

* Does all data in a message take the same path? No.
* What happens to data between each hop, what does each station do to the data passing through it?
  * hop - a step from one station to another.
    * e.g., station 11 ~ 9, 13 ~ 6 (相邻)
  * The stations do calculations to figure out which of the possible wires connected to it is the best to send the signal through to get the destination fastest.
* Data can travel along different paths from one station to another through the network.
* Which device chooses which path is faster?
  * normally it's the router. 
  * It can be a hardware, like the one we usually use at home.
  * It can be a software on a computer.
  * The hardware is faster, but both work.
  * There are lists, routing table and forwarding table, and the forwarding table will figure out where the data goes.
* If a router determines the fastest path, does it mean that each router knows the locations of all other router?
  * No. The way it determines the fastest path is called routing. Algorithms will supply either the information about neighbour that the closest, or the information about all routers in the local networks. That information can be used to make the forwarding table, which determines the interface we should send out of.
* e.g. from station 1 ~ 6:
  * there are more than one path
  * the time it takes to travel one station to another through a path is strongly related to the number of hops.
  * so, the blue path should be faster than the red path.
  * but, the data are divided into small packets, different packets may transmitted on different path, so the receiver does not always receive packages in order that we sent them.
  * If there is no congestion in the network, and there's no conflicting algorithms affecting things, it will always use the blue path, because it's faster.
  * If there's another application sending and receiving data from station 1~6, and it defined only use the blue path. Then it may be more efficient to send information along the red path, because the other one is very congestion.

<img src="img/1.16.png" />

### Approached to network travel

We can take different approaches to managing data

* **Circuit switching (电路交换)**: make a connection along a particular path and send all data in the message through that path.  
  * dedicated connection
  * as the data go through each stations, we are going to decide this is the path that everything will take. 
  * like going through an old telephone switching network. You get to the central switch, and it makes a physical connection, and send the signal to next switch, and that switch makes the physical connection to next switch, until it gets to the final destination.
* **Packet switching (分组交换)**: break the message into pieces and send each piece separately along its own path.
  * shared connection
  * How does a message divide into packets?
    * TCP/IP has a protocol, it defines the max size of a packet. It divide the packets to its max size. The last packets may not be the max size. It may send together with next message, depends on whether it send to the same place or they are the same software.
* **Virtual circuit switching (虚拟电路交换)**: break the message into pieces, use software to simulate a connection in a packet switched network.
  * **虚拟电路**（英语：Virtual circuit，缩写为 VC），又称为**虚电路**、**虚连接**或**虚通道**，在*分组交换*的计算机网络上，交换数据的传输方式之一。它是一种预接式（connection-oriented），或线路交换式（circuit-switched）的数据传输方法，在两个终端系统（End system）间，创建一条连线，来进行数据交换。在使用虚拟电路之前，必须先在两个节点或软件应用程序间创建连线。在创建连线之后，两个节点之间，就可以进行数据流的交换。概念来自于电路交换，其运作方式就如同在两个端点间，创建起专用的物理层线路连线一般，因此又称为虚拟连线（virtual connection）或虚拟通道（virtual channel）。

#### Circuit Switching 电路交换

* Connection Oriented
  * A path or circuit, or series of hops through the network, from the sending station to the receiving station is established, used as dedicated link, then disconnected. 
  * The communications links used for the dedicated link are not available to other users for making other connections. 
* Origin: analog telephone networks
* A path or circuit through the network is established. This path consists of a series of hops between nodes or switches, then a final hop to the receiver. 
* Every time it gets to the switch, it gets amplified, so that it won't lose power.
* The switches have the intelligence to help determine a path through the network and allocate available resources.
* Once the circuit is established it is used as dedicated link. 
* Data is transferred through that circuit, flow control is end to end (not hop by hop).
  * we create the path hop by hop, but not transfer information.
* If data is in the form of a series of bursts, the time between bursts is not utilized. The utilization of the connection will be low if the data is a series of bursts. 
* When the session is over the circuit is closed. 

###### Advantages

* provides a dedicated link
* efficient for continuous transmission
* do not have delay of waiting for packets to arrive before data can be forwarded along the next hop of the path.
* easier to implement control for quality of service
* guaranteed bandwidth

###### Problems

* inefficient when data comes in bursts, during the time between bursts the connection is allocated but not being used.  (not use the full power of the available connection)
* overhead required to establish and break circuit
* connection must be reestablished if there is a problem with any switch along the established path. 
* cannot send at a rate higher than your allocated share of resources even if you are the only user. (即使您是唯一的用户，也无法以高于分配的资源份额的速率发送(信息)。)

### Packet Switching

* Packet Switching: Connectionless
* the message sent is broken into small pieces called packets.
* each packet is sent through the network separately and can take a different path through the network. 
* At each hop the packet must be forwarded to the next host along the path to the destination.
* each packet is transferred 1 hop at a time, the intermediate stations need only wait for the end of the packet not the end of the message.
* the communications links used to send the packet are not reserved for any particular connection and are available to all end systems.
* No call setup or call termination required.
* Each packet, referred to as a datagram(数据电报), is sent individually, and is routed through the network individually. 
* packets with the same source and destination may take different paths through the network, and thus may arrive at the receiver out of order. 
* flexible reaction to congestion and failure. (对拥塞和故障的灵活反应。)
* robust delivery of packets, less loss of information in lost packet than in broken virtual connection when a node fails. (可靠的数据包传送，与节点故障时断开的虚拟连接相比，丢失的数据包中的信息丢失更少。)

###### Packet travel times

* packet travel time - the time from the packet left the sender, until it arrives the destination.
  * it includes the time to encode and decode the message to bits.
* packets can travel along different paths from one station to another
* different paths have different travel times
* packets that leave in order A-B-C may arrive in any order, because they travel along different paths with different travel times
* having more than one available path provides a more reliable transmission system. If one path fails, a different path can be used. 
* binary information in the packet need to be translated bit by bit into electrical signal, then it goes into a wire or the air. So it takes particular length of time to send a single bit, and if we multiply the length of the packets in bits by the time to send a bit, then we get the time to send/push the packet into a wire or the air. This usually equals to the time for the receiver to receive and decode the packet. 
  * This time is significantly larger than the travel time. 

###### Store and Forward node

* A network node that 
  * receives and stores incoming packets.
  * checks incoming packets for bit level errors
  * forwards the correct packets to the next store and forward node
* important: think of each hop as a separate communication.
  * source sends packet
  * receiver receives packet and queues it
    * if the queue is full, the receiver drops the packet
  * receiver checks the packet for correctness.
    * if a packet is not correct, the receiver may drop the packet (best effort transmission 尽力而为传输)
  * otherwise the receiver then passes packet on to another connection. 
* at each store and forward node, delay is introduced
  * waiting for the whole packet to arrive before forwarding the packet.
  * checking the packet for transmission errors.
  * waiting for the system to check the packet for transmission errors.

### Virtual Circuit Switching

* used in packet switched networks
* uses software to simulate a connection
* at any time any station can have multiple virtual circuit connections to the same or different destinations. 
* virtual circuits allow retransmission of data packets that arrive with errors. 
* Error / Flow control is associated with the virtual circuit. 
* at the beginning of each data exchange between a source and a receiver, a single path or virtual circuit from the source to the receiver is established and all packets in the exchange follow this path. Since packets follow the same path they arrive in order. 
* the virtual circuit is not dedicated. Each packet will be queued for transmission at each hop along with any other traffic traveling cross that particular link. Thus, when the virtual circuit connection is not being used by the source and receiver in this exchange it may be used by other exchanges. 

### What is a hop

*  hop - a step from one station to another.

<img src="img/1.17.png" />

### Queuing delay

* as the packet travels to each intermediate or final destination there are possible additional delays
* each time a packet arrives at a host or router or switch there is a possibility that it must enter a queue of packets waiting to be processed. 
* the time the packet resides in this queue, before the processing of the packet begins is the queuing delay. 
* when a packet arrives at a store and forward node, if the store an forward node is busy processing another packet it will be placed in a queue waiting for its turn. 
* unlike other delays, different for different packets because variations in the length of the queue independent of the packet (队列长度的变化与数据包无关).
* usually analyze queuing delays statistically

### Processing delay

* when a packet reaches a store and forward node
  * its header must be read and analyzed
  * its contents must be checked for bit level errors. 
* the time taken to do such checks is the processing delay.

### Transmission delay

* when a packet is sent the hardware used translates one bit at a time and inserted it onto the transmission medium
  * consider the link can send R bits per second
* the time taken for all L bits in the packet to be inserted into the transmission medium is the transmission delay, L/R.

### Propagation delay 传播延迟

* each bit must travel from the source to the destination through the transmission medium.

* the time taken by each bit to travel distance $d$ from the source to the destination is the propagation delay.

* This time is short (travels near light speed)

  $d_{prop} = d/v$ 	velocity $v$ is $2-3*10^8$

  

Difference between router and switch?

* a router is in the network layer, and it takes cares of addressing and getting things to the right place according to IP addresses. 
* a switch is something more general, it can exist in different layers, there are different kinds of switches, and switches are simpler
* a switch in a network layer is very similar to a router.
* a switch can be in a lower layer working with hardware addresses instead. 

two main things to cause corrupted:

* attenuation (衰变，稀释) - if the data come through a long wire, it radiate a little power. By the time it gets the destination, the total amplitude may be small enough, it is hard to tell the difference between levels (0 or 1).
* every wire access an antenna(天线), we use antenna both to send and receive signals. The attenuation is sending the signal out of wire. 
  * The wire can also pick up other signals, if this happens, the other signals will add to the signal on the wire already. 

what happens if a packet missed?

* Depends on protocols it uses.
* TCP - if a packet missed, the missed packet will be request again and resent, hopefully this time it will be received successfully, it may be request and resent for several times to make sure it received successfully.
* UDP - best effort protocol. It's not the responsibility for UDP to recover and resend the packet if it doesn't get there. 
  * so your application should be designed to check it.
  * or the application allows miss the data without damage.

What does the term "burst" mean?

* Burst is a term used in a number of information technology contexts to mean a specific amount of data sent or received in one intermittent operation. It can be contrasted with streamed, paced, or continuous.
* Considering sending data from source, it will be sending at a continuous rate, one packet after another, unless we have applications that are competing (let's ignore this).
* So the data leaves the source at a evenly spaced sequence of packets, but as it traverse through the network, it can be broken into chunks. We may have a series of packets that arrived and a few packets missing. We need to wait for those missed packets, which means by the time we get those missed packets, it took a long time to get there or to resend, we have a whole large chunk of packets that are ready to process.
* If we get a large burst, because we are waiting for a packet. When all the data has arrived, or they generate a large bunch, then that burst will all go through it at the same time. 
* The problem comes when the burst is big enough, that the real time reception and processing has a break where no packets are available because the burst is been put together. 
* Then we get a blank space in the transmission, so we get a corrupted piece of video or silence audio.