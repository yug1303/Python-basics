# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    # printing stuff
    print("Hello World")
    # to comment line use contrl # simply
    # simply string define kar lo
    x="hhkj"
    print(x)
    #list-array bro
    c=['yug','qwe']
    print(c[0],c[1])
    print(c)
c.append('kdd')
print(c)
# c.append('kdd')
# print(c)
 #tuples
tup1=(1,2,3)
print(tup1[0])
#dictionaries (map valli chiz)
names={'jd':22 ,'mk':33}
print(names['jd'])
print(names.keys())
print(names.values())
#if else vagera
# number=int(input())
#
# if(number>90):
#     grade ='a'
# elif(number <90):
#     grade ='c'
# print(grade)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
#loops
# for i in range(0,10) :
#     print(i)
# python functions
def avg(n1,n2) :
  return (n1+n2)/2
print(avg(1,2))
# file reading
file1 =open("harry.txt","wb")
print(file1.mode)
print(file1.name)
file1.write(bytes("write thhis to my file","UTF8"))
file1.close()
