import time
timestamp= time.strftime("%H:%M:%S")
print("The current time is: ",timestamp)
# https://docs.python.org/3/library/time.html#time.strftime
# if(timestamp<"12:00:00"):
#     print("!!Good Morning!!")
# elif(timestamp>"12:00:00" and timestamp<"18:00:00"):
#     print("!!Good Afternoon!!")
# elif(timestamp>"18:00:00" and timestamp<"21:00:00"):
#     print("!!Good Evening!!")
# else:
#     print("!!Good Night!!")

if(int(time.strftime("%H"))<12):
    print("!!Good Morning!!")
elif(int(time.strftime("%H"))>12 and int(time.strftime("%H"))<18):
    print("!!Good Afternoon!!")
elif(int(time.strftime("%H"))>18 and int(time.strftime("%H"))<21):
    print("!!Good Evening!!")
else:
    print("!!Good Night!!")