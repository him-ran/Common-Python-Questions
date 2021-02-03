# logparse
""" log parser
    Accepts a filename on the command line. The file is a Linux-like log file
    from a system you are debugging. Mixed in among the various statements are
    messages indicating the state of the device. They look like this:
        Jul 11 16:11:51:490 [139681125603136] dut: Device State: ON
    The device state message has many possible values, but this program cares
    about only three: ON, OFF, and ERR.

    Your program will parse the given log file and print out a report giving
    how long the device was ON and the timestamp of any ERR conditions.
"""

errorTimeList = []

def getontime():
    print("hello On function")


if __name__ == "__main__":
    count = 0
    with open("C:\\Users\\g521781\\Desktop\\Learning\\Python\\test.log", "r") as logFile:
        for i in logFile:
            status = (i.rstrip().split(":")[-1])
            if status == " ON":
                count = count + 1
            elif status == " ERR":
                errorTimeList.append(i.split("[")[0])
    logFile.close()
    print("Device was on for " +  str(count) + " seconds.")
    print("Timestamps of error events:")
    for i in errorTimeList:print(i)

