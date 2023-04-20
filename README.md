# DataDiode
## The task's goal: Tranfer file from Sender to Enduser on a one way direction and make safe and secure internal network that data can't go out.
## Components:
- Sender: Calculates the md5 hash of the file and sends it to Proxy1. After that starts sending the file to Proxy1. Both actions using TCP protocol.
- Proxy1: Receives the file's packets from Sender using TCP protocol. Sends them to Proxy2 through data diode using UDP protocol. Also sends the sequences of the packets to   Proxy3 using TCP. He will send the packets of the file with their sequences to Proxy2 only if Proxy3 will allow it.
- Data diode: Receives packets from Prxoy1 and immediately sends them to Proxy2. Both operations using UDP.
- Proxy2: Recieves packets from the data diode using UDP. Splites the packets to their sequence and data. The sequences are sent to Proxy3 with TCP, And if he will allow,   The data will be sent to EndUser with TCP.   
- Prxoy3: Get the sequences of the packets from both proxies. Compares between them and sends instractions to proxies accordingly. If Proxy2 got the packet from Proxy1,     Proxy2 will send it to EndUser and Proxy1 will send the next packet. Otherwise, Proxy1 will send the same packet again and Proxy2 will not do anything.
- EndUser: Receives all the packets from Proxy2 using TCP. Compares the md5 hash that he got with the md5 hash of the file from the packets. If they are the same, the       network is a safe and secure with a reliable tranfer. 

![Screenshot 2023-04-19 231323](https://user-images.githubusercontent.com/117903915/233189428-5ffd7720-923c-4985-97fe-8f1f27f11731.png)
