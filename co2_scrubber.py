import pandas as pd

#print(len('110011111011')) #12

txt = pd.read_csv('power_consump.txt', header=None, dtype = str)
#print(txt)
#print(type(txt))

#convert dataframe to series dtype:objects
txt.columns = ['0']

#convert int to str
data = txt['0'].astype(str)
#print(type(txt))

#convert into split list series to dataframe
oxygen = data.apply(list).apply(pd.Series)
#print(data.apply(list))
#print(type(data.apply(list)))
#print(oxygen)
#print(type(oxygen))

n = 0
print("Bit = ", n)

#df version
more = oxygen[n].value_counts().to_frame()
print("Df counts are \n", more)

a = more.loc['0'].values
b = more.loc['1'].values
print("0, 1 counts are ", a, b)

if a == b:
    index = 1
    print("Index is ", index)
    print(type(index))
else:
    index = more.idxmax().apply(int).values
    print("Index is ", index)
    print(type(index))


for n in range(0,11): #0-'10+1' bit+1
    if index == 0:
        #df column 0 [0], index 0 ['0']
        oxygen = oxygen.loc[lambda oxygen: oxygen[n] == '0']
        #print(oxygen)
        print("Bit+1 = ", n+1)
        more = oxygen[n+1].value_counts().to_frame()
        print("Value_counts are \n", more)

        try:
            #df column 0 [0], index 0 ['0']
            a = more.loc['0'].values
            b = more.loc['1'].values
            print("0, 1 counts are ", a, b)

            if a == b:
                index = 1
                print("Index is ", index)
                print(type(index))
            else:
                index = more.idxmax().apply(int).values
                print("Index is ", index)
                print(type(index))

            continue

        except:
            print("Breaking at bit: ", t+1)
            break


    elif index == 1:
        oxygen = oxygen.loc[lambda oxygen: oxygen[n] == '1']
        #print(oxygen)
        print("Bit+1 = ", n+1)
        more = oxygen[n+1].value_counts().to_frame()
        print("Value_counts are \n", more)

        try:
            a = more.loc['0'].values
            b = more.loc['1'].values
            print("0, 1 counts are ", a, b)

            if a == b:
                index = 1
                print("Index is ", index)
                print(type(index))
            else:
                index = more.idxmax().apply(int).values
                print("Index is ", index)
                print(type(index))

            continue

        except:
            print("Breaking at bit: ", t+1)
            break

#convert into split series to dataframe
co2 = data.apply(list).apply(pd.Series)

t = 0
print("Bit = ", t)

less = co2[t].value_counts().to_frame()
print("Df counts are \t", less)

c = less.loc['0'].values
d = less.loc['1'].values
print("0, 1 counts are ", c, d)

if c == d:
    idx = 0
    print("Idx is ", idx)
    print(type(idx))
else:
    idx = less.idxmin().apply(int).values
    print("idx is ", idx)
    print(type(idx))

for t in range(0,11): #0-'10+1' bit+1
    if idx == 0:
        #df column 0 [0] index 0 ['0']
        co2 = co2.loc[lambda co2: co2[t] == '0']
        #print(co2)
        print("Bit+1 = ", t+1)
        less = co2[t+1].value_counts().to_frame()
        print("Value_counts are \n", less)

        try:
            #df column 0 [0] index 0 ['0']
            c = less.loc['0'].values
            d = less.loc['1'].values
            print("0, 1 counts are ", c, d)

            if c == d:
                idx = 0
                print("Idx is ", idx)
                print(type(idx))
            else:
                idx = less.idxmin().apply(int).values
                print("Idx is ", idx)
                print(type(idx))

            continue

        except:
            print("Breaking at bit: ", t+1)
            break

    elif idx == 1:
        co2 = co2.loc[lambda co2: co2[t] == '1']
        #print(co2)
        print("Bit+1 = ", t+1)

        less = co2[t+1].value_counts().to_frame()
        print("Value_counts are \n", less)

        try:
            c = less.loc['0'].values
            d = less.loc['1'].values
            print("0, 1 counts are ", c, d)
            if c == d:
                idx = 0
                print("Idx is ", idx)
                print(type(idx))
            else:
                idx = less.idxmin().apply(int).values
                print("Idx is ", idx)
                print(type(idx))

            continue

        except:
            print("Breaking at bit: ", t+1)
            break

print("Oxygen sumfor is ", oxygen)  #000111111101
print(type(oxygen))

o1 = oxygen.values #to_numpy()
print(o1)
print(type(o1)) #array

#array index 0 [0]
o2 = o1[0]

i = 0
o3 = o2[0]
for i in range(1,12):
        o3 += o2[i]
        i+=1
        print("Oxygen binary number is ", o3)
        print(type(o3))

print("Carbon Dioxide sumfor is ", co2)  # 101010000101
print(type(co2))

co1 = co2.values #to_numpy()
print(co1)
print(type(co1)) #array

#array index 0 [0]
co = co1[0]

i = 0
co3 = co[0]
for i in range(1,12):
        co3 += co[i]
        i+=1
        print("Carbon Dioxide binary number is ", co3)
        print(type(co3))

o2_dec = int(o3, 2)
print("Binarytodec val is ", o2_dec) #509

co2_dec = int(co3, 2)
print("Binarytodec val is ", co2_dec) #2693

life_sup = o2_dec * co2_dec
print("Life_sup is ", life_sup)
