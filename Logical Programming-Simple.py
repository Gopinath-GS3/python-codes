print("***Welcome to the Triathlon Award Program***")
print("Enter the time taken by participant to complete following events in minutes")
s = int(input("Swimming: "))
c = int(input("Cycling: "))
r = int(input("Running: "))
total = s+c+r
print("Total timing taken to complete the triathlon: {} minutes".format(total))
if (total <= 100):
    print("Participant is qualifing to *Provincial Colours Award*")
elif (total <= 105):
    print("Participant is qualifing to *Provincial Half Colours Award*")
elif (total <= 110):
    print("Participant is qualifing to *Provincial Scroll Award*")
else:
    print("Participant is qualifing to no Award")