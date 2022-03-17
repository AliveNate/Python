from tkinter import *
import tkinter.messagebox

class PassWord_Vault(Frame, Text, Scrollbar):

    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        Text.__init__(self, parent)
        # Want a scrollbar in the text, box, but cannot find solution without using .pack()
        # Currently we have the program set with .grid()
        # Scrollbar.__init__(self, master)

        self.grid()
        self.master = parent

        self.close_button = Button(parent, text="Close", command=parent.quit)
        self.close_button.grid()
        self.deleteConfirm = False
        self.linecount = 0

        # This will be part of the dropdown box.
        # The dropdown was decided against.
        # self.studFiles = StringVar()  # Files will contain a string variable
        # self.studFiles.set('Choose')  # The files will be set empty by default.
        # options = ['Encrypt', 'Decrypt', 'Exit']  # List with The 2 options that we want in the drop down box.
        # self.choice = StringVar()
        # self.studDropDown = OptionMenu(parent, self.studFiles, *options, command=self.openFiles).grid(row=2)

        # Menu Labels
        # The primary labels for the program title
        # menuLabel1 = StringVar()
        menuLabel2 = StringVar()
        menuLabel3 = StringVar()
        menuLabel4 = StringVar()
        menuLabel5 = StringVar()
        # ==============================
        # menuLabel1.set("-----------------")
        # Set The primary labels for the program title
        menuLabel2.set("CyberNate")
        menuLabel3.set(" Password Encryption")
        # menuLabel4.set("")
        # menuLabel5.set("-----------")

# -------------------------------------------------
# State a global var and then define.
global theList
theList = []

# Format for a port being added to the list.
class portClass:
    # -------------------------------------------------
    def __init__(self, portProto, portNum, portTit, portDef):
        self.portProtocol = portProto
        self.portNumber = portNum
        self.portTitle = portTit
        self.portDefinition = portDef
        theList.append(self)
        print(self.portNumber)
        for x in range(len(theList)):
            print(theList[x].portProtocol)


def portDef():
    # ----------------------------------
    ftp = portClass("File Transfer Protocol (FTP1)", "20/21", "TCP",
               "FTP is one of the most commonly used file transfer protocols on the Internet and within private networks. An FTP server can easily be set up with little networking knowledge and provides the ability to easily relocate files from one system to another. FTP control is handled on TCP port 21 and its data transfer can use TCP port 20 as well as dynamic ports depending on the specific configuration.")

    # ----------------------------------
    ssh = portClass("Secure Shell (SSH)", "22", "TCP",
               "SSH is the primary method used to manage network devices securely at the command level. It is typically used as a secure alternative to Telnet which does not support secure connections.")

    # ----------------------------------
    telnet = portClass("Telnet", "23", "TCP",
               "Telnet is the primary method used to manage network devices at the command level. Unlike SSH which provides a secure connection, Telnet does not, it simply provides a basic unsecured connection. Many lower level network devices support Telnet and not SSH as it required some additional processing. Caution should be used when connecting to a device using Telnet over a public network as the login credentials will be transmitted in the clear.")

    # ----------------------------------
    smtp = portClass("Simple Mail Transfer Protocol (SMTP)", "25", "TCP",
               "SMTP is used for two primary functions, it is used to transfer mail (email) from source to destination between mail servers and it is used by end users to send email to a mail system.")

    # ----------------------------------
    dns = portClass("Domain Name System (DNS)", "53", "TCP",
               "The DNS is used widely on the public internet and on private networks to translate domain names into IP addresses, typically for network routing. DNS is hieratical with main root servers that contain databases that list the managers of high level Top Level Domains (TLD) (such as .com). These different TLD managers then contain information for the second level domains that are typically used by individual users (for example, cisco.com). A DNS server can also be set up within a private network to private naming services between the hosts of the internal network without being part of the global system.")

    # ----------------------------------
    dhcp = portClass("Dynamic Host Configuration Protocol (DHCP)", "67", "UDP",
               "DHCP is used on networks that do not use static IP address assignment (almost all of them). A DHCP server can be set up by an administrator or engineer with a poll of addresses that are available for assignment. When a client device is turned on it can request an IP address from the local DHCP server, if there is an available address in the pool it can be assigned to the device. This assignment is not permanent and expires at a configurable interval; if an address renewal is not requested and the lease expires the address will be put back into the poll for assignment.")

    # ----------------------------------
    tftp = portClass("Trivial File Transfer Protocol (TFTP)", "69", "UDP",
           "TFTP offers a method of file transfer without the session establishment requirements that FTP uses. Because TFTP uses UDP instead of TCP it has no way of ensuring the file has been properly transferred, the end device must be able to check the file to ensure proper transfer. TFTP is typically used by devices to upgrade software and firmware; this includes Cisco and other network vendors? equipment.")

    # ----------------------------------
    http = portClass("Hypertext Transfer Protocol (HTTP)", "80", "TCP",
               "HTTP is one of the most commonly used protocols on most networks. HTTP is the main protocol that is used by web browsers and is thus used by any client that uses files located on these servers.")

    # ----------------------------------
    pop = portClass("Post Office Protocol (POP) version 3", "110", "TCP",
               "POP version 3 is one of the two main protocols used to retrieve mail from a server. POP was designed to be very simple by allowing a client to retrieve the complete contents of a server mailbox and then deleting the contents from the server.")

    # ----------------------------------
    ntp = portClass("Network Time Protocol (NTP)", "123", "UDP",
           "One of the most overlooked protocols is NTP. NTP is used to synchronize the devices on the Internet. Even most modern operating systems support NTP as a basis for keeping an accurate clock. The use of NTP is vital on networking systems as it provides an ability to easily interrelate troubles from one device to another as the clocks are precisely accurate.")

    # ----------------------------------
    netbios = portClass("NetBIOS", "137/138/139",  "TCP/UDP",
               "NetBIOS itself is not a protocol but is typically used in combination with IP with the NetBIOS over TCP/IP (NBT) protocol. NBT has long been the central protocol used to interconnect Microsoft Windows machines.")

    # ----------------------------------
    imap = portClass("Internet Message Access Protocol (IMAP)", "143", "TCP",
               "IMAP version3 is the second of the main protocols used to retrieve mail from a server. While POP has wider support, IMAP supports a wider array of remote mailbox operations which can be helpful to users.")

    # ----------------------------------
    snmp = portClass("Simple Network Management Protocol1 (SNMP)", "161/162", "TCP/UDP",
               "SNMP is used by network administrators as a method of network management. SNMP has a number of different abilities including the ability to monitor, configure and control network devices. SNMP traps can also be configured on network devices to notify a central server when specific actions are occurring. Typically, these are configured to be used when an alerting condition is happening. In this situation, the device will send a trap to network management stating that an event has occurred and that the device should be looked at further for a source to the event.")

    # ----------------------------------
    bgp = portClass("Border Gateway Protocol (BGP)", "179", "TCP",
               "BGP version 4 is widely used on the public internet and by Internet Service Providers (ISP) to maintain very large routing tables and traffic processing. BGP is one of the few protocols that have been designed to deal with the astronomically large routing tables that must exist on the public Internet.")

    # ----------------------------------
    ldap = portClass("Lightweight Directory Access Protocol (LDAP)", "389", "TCP/UDP",
               "LDAP provides a mechanism of accessing and maintaining distributed directory information. LDAP is based on the ITU-T X.500 standard but has been simplified and altered to work over TCP/IP networks.")

    # ----------------------------------
    https = portClass("Hypertext Transfer Protocol over SSL/TLS (HTTPS)", "443", "TCP",
               "HTTPS is used in conjunction with HTTP to provide the same services but doing it using a secure connection which is provided by either SSL or TLS.")

    # ----------------------------------
    ldaps = portClass("Lightweight Directory Access Protocol over TLS/SSL (LDAPS)", "636", "TCP/UDP",
               "Just like HTTPS, LDAPS provides the same function as LDAP but over a secure connection which is provided by either SSL or TLS.")

    # ----------------------------------
    ftp_overTLS_SSL = portClass("FTP over TLS/SSL", "989/990", "TCP",
               "Again, just like the previous two entries, FTP over TLS/SSL uses the FTP protocol which is then secured using either SSL or TLS.")

    #----------------------------------

#----------------------------------

#----------------------------------

#----------------------------------









# ==============
quizbox.mainloop()
portDef()

# This works
# print("\n---\n", theList[2].portProtocol)
# ===============