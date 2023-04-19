# DataDiode
## The task's goal: Tranfer file from Sender to Enduser on a one way dirction and make safe and secure internal network that data can't go out.
## components:
- Sender: Calculates the md5 hash of the file and sends it to Proxy1 using TCP protocol.
- Proxy1: Receives the file's packets from Sender using TCP protocol. Sends them to Proxy2 throw data diode using UDP protocol. Also sends the sequences of the packets to   Proxy3 using TCP. He will send the packets of the file with their sequences to Proxy2 only if Proxy3 will allow it.
- Data diode: Receives packets from Prxoy1 and immediately sends them to Proxy2. Both operations using UDP.
- Proxy2: Recieves packets from the data diode using UDP. Splites the packets to their sequence and data. The sequences are sent to Proxy3 with TCP, And if he will allow,   The data  will be sent to EndUser with TCP.   

