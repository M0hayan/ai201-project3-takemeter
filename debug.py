import os

for root, dirs, files in os.walk("data_q"):
    print(root)
    for f in files:
        print(" ", f)

for root, dirs, files in os.walk("data_c"):
    print(root)
    for f in files:
        print(" ", f)