time = input("Enter Amount in HH:MM Format-> ")

if time.partition(':')[2]:
    min = (int) (time.partition(':')[2]) + (int) (time.partition(':')[0]) * 60
min = (int) (time.partition(':')[0]) * 60

sessions = (int) (min / 25)
if sessions * 25 < min:
    sessions += 1

total = sessions * 30 + 25 * (int) (sessions / 4)

print(f"Expected amount of time using the method: {(int)(total/60)}:{total - 60 *(int)(total/60)}")
print("You will need %d regular 30 min sessions (which includes the 5 min break) and %d, 30 minute breaks!" % (sessions, (int) (sessions / 4)))


