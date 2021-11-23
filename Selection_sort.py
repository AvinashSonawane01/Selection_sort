# Selection_sort


Percentage = []
number = int(input("Enter Total Number of Students:\n"))
for i in range(number):
    value = float(input("Enter Percentage:\n "))
    Percentage.append(value)

for i in range(len(Percentage)-1):
    m_ind=i
    for j in range(i+1,len(Percentage)):
        if Percentage[j]<Percentage[m_ind]:
            m_ind = j
    if Percentage[i] != Percentage[m_ind]:
        Percentage[i],Percentage[m_ind] = Percentage[m_ind],Percentage[i] 
     
print("Top five scores are:",Percentage)
minimum = len(Percentage)-6
maximum = len(Percentage)-1
index = 1
for i in range(maximum,minimum,-1):
    if i>=0:
        print(f"{index} Top Scorer:",Percentage[i],"\n")
        index+=16
