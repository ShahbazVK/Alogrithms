processes=int(input("Enter number of processes: "))
memory=int(input("Enter total memory:"))
processes_arr=[]
for i in range(processes):
    user=int(input("Enter process size:"))
    processes_arr.append(user)
assigned_processes=[]
for i in range(processes):
    if processes_arr[i]<=memory:
        memory-=processes_arr[i]
        # print("Size",process_arr[i],"\n\tinternal fragmentation=",size_of_block- process_arr[i])
        assigned_processes.append(processes_arr[i])
    else:
        print(processes_arr[i],"allocated no space")
print("Processes",assigned_processes)
print("External fragmentation:",memory)
