print("""
Line 1
Line 2
Line 3
""")


#multiple line message
print("""
HKIS..
Intro to programming
..with Ms Mok! ..V1
""")

#Putting line message into function
def i2p_intro():
    print ("""
    HKIS..
    Intro to programming
    ..with Ms Mok! ..V1
    """)

print(i2p_intro())


int1 = input("type any number")
int2 = input("type any number")

def f_sum(int1,int2):


    """This function will add two numbers"""
    return (int1 + int2)


vtotal = f_sum(int1,int2)


print("The total is:",vtotal)


int3 = input("type any number")
int4 = input("type any number")

def f_print_largest(int3,int4):
    """This function will print the larger number"""
    if int3>int4:
        print(int3,"is larger")
    if int3<int4:
        print(int4,"is larger")

f_print_largest(int3,int4)


#int5 = input("type any number")
#int6 = input("type any number")

def f_larger(int5,int6):
    """"function will return largest number"""
    if int5>=int6:
        return int5
    else:
        return int6


x = 12
y = 24
z = 36
#print(f_larger(f_larger(x,y,z)))





