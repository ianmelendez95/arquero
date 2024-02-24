
import sys

# print("Tell me why: ", end='')
print("Tell me why: ", end='', flush=True)
response = sys.stdin.readline()
if response != "Ain't nothing but a heartache\n":
    print("Wrong! It's 'Ain't nothing but a heartache', not: " + response)
    exit(1)

print("Tell me why!: ", end='', flush=True)
response = sys.stdin.readline()
if response != "Ain't nothing but a mistake\n":
    print("Wrong! It's 'Ain't nothing but a mistake'")
    exit(1)

print("But I want it that way...")
