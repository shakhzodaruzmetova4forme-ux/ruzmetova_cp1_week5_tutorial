n = int(input("Enter the number of days: "))
measures = []
for i in range(n):
    m = int(input("Enter the measurement for next day: "))
    measures.append(m)
print(measures)

for i in range(n):
    print(f"Day {i+1}: {measures[i]} cm")

    print(f"First hight: {measures[0]} cm")
    print(f"Last hight: {measures[-1]} cm")
    print(f"Change: {measures[-1] - measures[0]} cm")


