# demonstrating file handling in python using a daily study log

#writing to a file
with open("study_log.txt","a") as file:
    file.write("Day: Python internediate : file handling practiced \n")

print("study log updated succesfully")

#reading from the file
print("\n readin study log:")
with open("study_log.txt","r") as file:
    for line in file:
        print(line.strip())