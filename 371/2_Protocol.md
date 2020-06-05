## What is a Protocol?

* A set of definitions and rules defining the method by which data is transferred between two or more entities or systems. 
* The key elements of a protocol are:
  * **Syntax:** definitions of data format, size and content of messages or packets (headers and data)
    * how big is the packet?
    * What part of the packet is data
    * What part of the packet is header
    * What information is in the header
    * How is that information used
    * it is like the grammar
  * **Semantics:** control, responses to messages or packets, coordination, error handling
    * how are we controlling the package
    * how do we determine where the packet go
    * how do we determine which packet have precedence(优先权)
    * how do we define the list of questions and answers that made up the protocol
  * **Timing/Synchronization:** maintaining synchronization between the communicating entities (speed matching, sequencing, recovery from timing related errors )

### Characteristics of Protocols

##### 分类方法一：direct / indirect

* Direct: data (directly)passes from source to destination without active intervention(介入) (point to point or multipoint link)
  * e.g. Transport layer, which is right below the application, we can think of the source is directly send from the source to the destination.
  * e.g. a protocol send data from one router to another is a direct protocol

<img src="C:/Users/shirl/Desktop/notes/371/img/1.36.png" />

* Indirect: data from source must pass through intermediate active entities to reach the destination (switched networks)
  * e.g. a protocol that through all the way from source to the destination like TCP is indirect

<img src="C:/Users/shirl/Desktop/notes/371/img/1.37.png" />

##### 分类方法二：Monolithic / Structured (!important)

​	this is the reason why very complicated system of the Internet can be dealt with using protocols that are understandable, implementable, and supportable.

* **Monolithic(整体的):** Single protocol for all aspects of data transfer
  * it's impossible to have all the functionality in a single protocol and keep track on that huge protocol of everything they are happening.
* **Structured**: uses a set of protocols interacting based on a chosen architecture. (Layered, client server …)
* Consider computer networks, A lot of complexity
  * Hosts , routers, switches, applications, varied hardware and software, varied communication needs
  * Our Internet use Structured protocol
  * Layers will only communicate with json layers
  * Any chance a single monolithic protocol is the best way to organize and manage the Internet?

##### 分类方法三：Symmetric / Asymmetric 

* **Symmetric:** communications between peers that is the same regardless of which entity is source and which is destination (peer to peer)

<img src="C:/Users/shirl/Desktop/notes/371/img/1.38.png" />

* **Asymmetric**: unequal source and receiver (client – server)
  * server -> client

<img src="C:/Users/shirl/Desktop/notes/371/img/1.39.png" />

* Internet needs to support both

##### 分类方法四：Standard / Nonstandard

* **Standard:** independent of hardware and application

  * Used by all members of network, no need for translation
  * Operates in a given layer regardless of operating system or system hardware (may require multiple implementations)

* **Nonstandard:** designed for specific hardware or application

  * Must translate between nonstandard protocols increasing load on system rapidly as number of nonstandard systems increases

    (随着非标准系统数量的增加，必须在非标准协议之间转换，从而迅速增加系统负载)

### Internet Protocol Choices

* **Structured (layered):** uses a set of protocols, several different protocols per layer
* Standardized: uses same protocols, may use different implementation on different hardware
  * any host, router, server will run the same protocols
  * if their hardware is different, or they are running different OS, they may use different implementations of the protocol, but the implementations are just codes that support the rules in the protocol
* Application layer: applications are implemented in the application layer. 
  * some of these applications want to send data to other hosts/processes, so we have these communications.
  * can call transport layer routines that we can use to ask to send information from one process on one host to another process
* Transport layer: contains the protocols that defines how the data/message go from one process on one host to another process.
  * tells us how the packets will be broken up and sent
  * tells us how to determine whether or not the packets will arrive if we want to have guaranteed delivery
  * tells us whether we are going to have guaranteed delivery
  * have a transition to Network layer
* Network layer: how we get packets from the source to the destination through a series of one-hop transition through the network

<img src="C:/Users/shirl/Desktop/notes/371/img/1.40.png" />

### Layered Protocol Architecture

* Flexible protocols can become very complicated very quickly. 
  * Reduce complexity, separate communication functions into modules(模块).
  * Layer these modules using clean interfaces 
  * Each module becomes a separate protocol layer
  * Each layer provides services to the layer above through an interface that hides the complexities of how the service is implemented.
  * With one or more protocols per layer the complete network architecture is known as a *protocol stack* (协议栈)

### Standardization

* Clearly defined functions for each layer allow for independent and simultaneous development of multiple layers (Lower layers = more detail)
* *Protocol specification* (协议规范) for each layer and for interfaces between layers must be exact
  * Format of data units
  * allowed sequence of PDUs (协议数据单元(Protocol Data Unit))
  * Semantics (meanings) of all fields
* Particular operations are localized in a given layer regardless of operating system or system hardware (may require multiple implementations for different OS or system hardware)
* *Service Definition*: standards for services provided by a layer, using a given set of protocols, to the layer above it
* *Addressing*: Provide the defined services to entities with particular addresses

### Layered models

* Each layer performs a different set of communications functions. 
* Each layer encapsulates and hides complexity from the layer above it
* Each layer uses the layer below it the perform more primitive and detailed functions
* Clear interfaces between layers make independent changes in one layer independent of the other layers

### Encapsulation

* The addition of control information to data before passing the resulting frame to the next protocol level
  * A PDU (protocol data unit) may or may not contain data but will contain control information such as
    * Addresses
    * Error detection checksums or redundancy checks
    * Sequence numbers
      * put the not-in-order packets in order
    * Other control information

### The OSI Environment

OSI = open systems interconnection 开放系统互连

<img src="C:/Users/shirl/Desktop/notes/371/img/1.41.png" />

### TCP/IP Protocol Suite

* TCP/IP is the most commonly used protocol stack on the Internet
* TCP/IP uses a layered structure, with fewer layers than the OSI model 
* TCP/IP protocols for a given layer use the services available from lower levels to complete the tasks they are responsible for 

### OSI 和 TCP/IP 的比较

<img src="C:/Users/shirl/Desktop/notes/371/img/1.42.png" />

### Application Layer

* **Application Layer:**  Working environment / support for applications
  * Provides services used directly by applications 
  * Hides the complexities of services provided by the other layers from the user
  * Provides an **interface to** communications between processes or applications on separate hosts

##### Some Application layer Protocols 

* Users most commonly directly use application layer protocols like Hypertext Transfer Protocol (HTTP), File Transfer Protocol (FTP)(largely replaced by safer protocol), Simple Mail Transfer Protocol (SMTP); Telnet (用于远程联接服务的标准协议或者实现此协议的软件),
* Other common application layer protocols help facilitate the use and management of TCP/IP networks (Not only in Application layer but also in other layers): These include Domain Name System (DNS), the Routing Information Protocol (RIP), the Simple Network Management Protocol (SNMP).

### Transport Layer

* Manages exchange of application data between end systems 
* Connection oriented reliable delivery (TCP)
  * Manages connections and error free, In sequence, loss and duplication free data transfer
  * watch if packet has been delivered or lost (re-send)
* Best effort delivery (UDP)
  * Packet oriented, connectionless
  * UDP usually have a checksum
* Process level addressing, Segmentation, Multiplexing / De-multiplexing

### Network Layer

* manages how data moves from one host to another in a network
  * Hides specifics of network technology from higher levels
  * Addressing, forwarding and routing in the network. How to get your packet from A to B
  * Fragmentation / Reassembly(重新组装)
  * Error detection and handling

### Link Layer

* Data Link Layer: making the physical link reliable and usable
  * Operates on frames containing messages sent between directly connected devices.
  * Bit level error detection and handling (finds corruption that happens during transmission)
  * Link control and management, Link level addressing
  * Media access control, sharing the physical media between multiple devices
  * this is how we control each hop, since this layer add the Ethernet address

### Physical Layer

* Physical Layer: raw bit stream service. Operates on bits
  * **Mechanical:** properties of connection to network (connector) 
  * **Electrical:** representation of bits as voltages (encoding and signaling)
    * encode: translate the binary bits to electrical signals
    * decode: translate the electrical signals to binary bits
  * **Functional:** Defines functions performed by particular circuits at the interface between the system and the transmission media
  * **Procedural:** Defines how bit streams are exchanged through the physical media

### TCP-IP Protocol Architecture

* dotted lines indicate that the connection here is conceptual, the data not actually go this way.
* middle blue box is a router in between  

<img src="C:/Users/shirl/Desktop/notes/371/img/1.43.png" />

### Encapsulation PDUs for TCP/IP

Encapsulation at each level

* Transport layer use socket programming.
* Ethernet is hardware, if we are using wifi, blue-tooth, wireless connections, we are using a different protocol than this.

<img src="C:/Users/shirl/Desktop/notes/371/img/1.44.png" />

###### Is each wireless protocol its own layer?

No. The wireless protocol would normally be a different kind of Data Link interface / protocol. So the "Ethernet" header position will not always be Ethernet.

### Encapsulation: PDU Headers

* TCP segment: User data +Transport Header (Transport Layer)
  * Destination and source process address of each occurrence of an application, called a port 
  * Sequence Number used to manage packet flow, deliver packets in the correct order
  * Checksum preserves reliability of data transfer and assure delivery to correct destination (校验和保留了数据传输的可靠性，并确保将数据传递到正确的目的地)
    * but problems could occur even it passed these lower test.
  * Lengths, flags …

* IP Datagram: TCP segment + IP Header
  * Destination and/or source network address (IP address)
  * Protocol Identification
    * Indicate transport protocol used
  * Flow and error control information (including fragmentation)
  * Error detection (header only) information
* Ethernet Frame: IP Datagram + Ethernet header
  * Next hop and source Ethernet address 
  * May be hardware specific (works for hardwares other than Ethernet)
  * Flow and sharing for the physical media
  * Error detection information

### Using a relay (router)

<img src="C:/Users/shirl/Desktop/notes/371/img/1.45.png" />

### Using a relay (level 2 switch)

<img src="C:/Users/shirl/Desktop/notes/371/img/1.46.png" />

### History

(Please be sure to read the excellent summary in your text book)