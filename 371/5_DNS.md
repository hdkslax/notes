# DNS

### Host names 主机名

* Our computer can have more than 1 IP addresses depending on how many Interface cards we have and how many network we are connected to.
* In addition to identifying a host by the IP address of a connected interface we also identify the interface by an hostname
* Hostnames are easier for a human to use and remember than the IP address
* In the early Internet names were recorded at a central registry(登记处) at the Network Information Center (NIC) .
  * New hosts/names were submitted to the central registry and added to the hosts file
  * The hosts file was available for distribution to all other sites.
* This was a flat naming structure (平面命名结构)

### Hierarchical name space

* The central naming system worked well until the Internet grew larger than it could handle (soon after TCP/IP was adopted)
  * The central servers could no longer deal with the volume of traffic
  * The manual updating of names was slow, and maintaining network wide consistency was difficult
  * Enforcing the use of unique names became more difficult (then impossible) (强制使用唯一名称变得更加困难（当时不可能）)
* The hierarchical DNS name system was designed to replace this original flat namespace in which each machine had a unique name
  * Administration was decentralized using a distributed database
  * Local administrators were given responsibility for building and maintaining a database relating IP address and name for their designated groups of local networks

### DNS (Domain Name System)

* Application runs in the application layer
* The primary use of DNS is to answer queries requesting the IP address that corresponds to a given host name.
* Reverse queries, finding the name of a host with a particular IP address are also possible
* DNS can also support multiple, different names for the same host (computer, mail server, …).
  * The primary name of a host is the **canonical hostname** (规范主机名)
  * A host can be called by names other than it's canonical hostname, these alternate names are called **aliases**(别名)
* DNS can also support multiple IPs for the same canonical hostname (used to distribute load)

### Addresses and names

* IP address is a hierarchical system. (32 bits address, 8 bits for each part)
  * An IP address consists of four integers between 0 and 256 separated by .'s  (example 192.168.3.1) . 
  * As we scan each group starting at the left and proceeding towards the right we obtain more and more specific information
* DNS also uses a hierarchical classification system for domain names. 
  * Domain names may represent a network a sub network or even a host
  * Consists of . separated names. As we read from left to right each name represents a smaller and more localized network or even a single host

### DNS Name Tree

* Labels may have up to 63 characters
* Labels (names) may refer to domains (hosts + nets) hosts or networks 
* 最上面的那个点(**·**)是root
* 第二层叫做 top level domain
  * arpa = advanced research projects agency (高级研究规划局), com = commercial, edu, gov are separated by use.
  * us, uk, ca, fr are separated by country

<img src="img/3.14.png" />

* Children of different parents can have the same name
* All children of a given parent must have unique names

<img src="img/3.15.png" />

### Constructing names: name tree

1. Start at the leaves of the tree
2. The domain for the chosen leaf will be the first part of the name. 
3. Add a period to the first part of the name
4. Check the domain name of the root of the current position in the tree. 
   1. If it is not the root of the tree
      1. The domain name of the root of the current position in the tree is added after the period
   2. If it is the root of the tree the name is complete
5. Repeat steps 3 and 4 until the name is complete

###### example: jpl.nasa.gov.

<img src="img/3.16.png" />

### Fully Qualified Domain Name 全称域名

* DNS uses fully qualified domain names
* FQDNs are complete domain names including all parts of the domain name from the domain of interest up to the root 
  * Ends in a . to indicate root. For example fraser.sfu.ca.
  * The terminating . Indicates that the name is absolute  ( relative to root, not to any other position in the DNS tree)

###### Why is FQDN important?

* Because when we search an IP address to go with the domain, we need to start with the FQDN.
* Some of resolvers, a software on our local machines, can be used to make request will allow partial DNS names.

##### Domain Names: not fully qualified

* Domain names that are not fully qualified (do not end at root, like fraser.sfu) may be interpreted by **some** software as relative to some particular location (other than root) in the DNS tree. 
* Your host must be configured to tell these software applications how to complete a domain name that is not fully qualified (how to convert it to a fully qualified domain name). You must tell the software what locations these names may be relative to.  (LINUX /etc/resolv.conf)

### Knowing where to look

* First, we need a resolver - a tool that make DNS request, and try to find IP address by particular DNS name or make a reverse request.

* Dig and other applications that need to look up DNS information must know where to go to find or ask for the information

* The list of locations to look (on a Linux system) can be found in /etc/resolv.conf. The locations will be queried in the order given

  * /etc/resolv.conf.  is a system file
  *  /etc/resolv.conf.  is a local DNS server we can request names from.

* /etc/resolv.conf Will look something like

  ```
  search cs.sfu.ca css.sfu.ca ensc.sfu.ca math.sfu.ca 
  nameserver 199.60.1.1
  nameserver 142.58.103.1
  nameserver 142.58.103.2
  ```

* If we have a partial name, it is going to look in some of the local networks. 

  * In this case, it will look at cs.sfu.ca
  * if it does find it there, it will look at css.sfu.ca
  * ...

* We can use partial names if our systems can properly configure to deal with partial names. 

#### resolv.conf: search

* search followed by a series of domain names (defaults are generated, in addition you can set the list yourself in versions 4.9 and later)
  * If a query for the address of draconis is made, since draconis is not fully qualified it will not be found
  * Then the resolver will append the first domain name in the search list (usually the domain of the host making the request.) to the requested name, and then make a request for then if the query for draconis.cs.sfu.ca. That request will produce a result
  * If that request did not produce a result the resolver would make requests for draconis with each of the domain names in the search list (in the same order as the list is given) and would stop if and when one of those requests produced a match

### Authority for the DNS namespace (DNS名称空间的权限)

* The central internet authority was ICANN (Internet corporation for assigned numbers and names) and is now IANA (Internet assigned numbers authority). 

  * Responsibility for the root level **.** domain rests with IANA
  * TLDs, top level directories for the internet namespace
    * include generic TLDs (gTLDs) like .com or .org for classification of domain names by type of use
    * include country code TLDs (ccTLDs) like .ca or .us for geographical classification of domain names
  * Responsibility for administering the TLDs has been delegated to other contractors by IANA. (IANA已将管理顶级域名（TLD）的职责委托给其他承包商)

* Any organization to which responsibility for a DNS domain is delegated 

  * must provide at least two independent DNS servers to service that domain 
    * These DNS servers must be geographically separated
    * These servers must be configured to provide continuous service
  * may delegate authority for parts of the DNS domain for which they are responsible to other organizations.

* Each DNS server must know the name/address of the servers it has delegated responsibility to.

  * The delegator of authority need not inform all organizations it delegates to of changes made by other such organizations. This is an unreasonable load in a rapidly growing/changing internet.

  * The delegated authority has a responsibility to inform the delegator if address or name of the DNS name server changes. This is necessary to guarantee that address queries can be passed down the tree.

### DNS Name Tree: Domains

* Root domain 只包含第二级的domain names

<img src="img/3.17.png" />

###### Examples of delegation(授权)

* TLD .ca delegates authority to sfu to manage the domain sfu.ca
* TLD .ca delegates authority to BC to manage top level domain .bc
* Domain .bc delegates authority to the BC government to manage domain gov.bc.ca

<img src="img/3.18.png" />

### How many DNS servers?

* Extrapolating this model we discussed before would have a DNS server for each domain
* What is the smallest domain?
  * 1 host, host name = domain name
    * Clearly this makes too many servers
  * 1 local network = 2 DNS servers
    * Still too many (lots of small networks)
* At some reasonable point we need to stop delegating authority

### Domain Name System

* A DNS domain is a sub tree 
  * The name of the domain is the domain name of the node at the root of the sub tree
  * The domain includes all domains and hosts below the root of the sub tree
    * us domain, includes .ca domain and .ny domain
    * mycomp domain include .mynet domain and host .myhost
  * The administrative responsibility for the domain and its subdomains may be arranged in different ways

### Dividing Authority

* What about domains that include both hosts and multiple sub-domains?
  * Can delegate the sub-domains, what about the hosts?
  * What if you want to delegate only some of the sub-domains?
* Need some more flexible administrative unit, the zone

### Zone

* An administrative division (rather than a logical division) of the domain name tree
  * Each zone is the responsibility of one administrative authority
  * A zone may include hosts and sub-domains 
  * Sub domains in a zone may or may not have authority delegated to other administrative authorities. Any subset of sub-domains may be delegated
  * The domain name of the zone is the domain name of domain with the same root domain name

###### DNS Name Tree: zones

<img src="img/3.19.png" />

### Domain Name System - zone

* A DNS zone is a subtree 
  * Any delegated subtree
  * The administrative authority for the zone must maintain at least two completely independent DNS servers for the zone
  * A given zone will have a corresponding zone in the arpa subtree to be used for inverse queries
  * A zone may delegate some of its sub domains and not other

### Authority for the DNS namespace

* A particular DNS name server will service a zone. Its database of name information will contain 
  * entries for any hosts in the zone 
  * delegation information for domains or zones that have been delegated to other authorities
    * Includes the address of (pointer to) the DNS servers for the delegated domains or zones
    * excludes information about further delegation of authority in delegated zones or hosts in delegated domains
  * Root servers contain the delegation information for all TLDs

### Domain Server Message

