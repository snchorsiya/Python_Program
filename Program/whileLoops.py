it = 10

while it > 1:
    if it == 9:
        it = it - 1
        continue
    if it == 3:
        break
    print(f"The loop is true: {it}")
    it = it-1
    # break
else:
    print("The loop is false")
