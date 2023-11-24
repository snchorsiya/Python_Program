ItemsInCart = 0
# 2 items will be added to cart

if ItemsInCart != 2:  # raise Exception("Product Cart Count not matching")
    pass

assert (ItemsInCart == 0)

try:
    with open("asdsds.txt", "r") as reader:
        print(reader.read())

except:
    print("Some how i reached this block there is failure in try block")


try:
    with open("54knf.txt", "r") as reader:
        print(reader.read())

except Exception as e:
    print(e)

finally:
    print("This is a finally block")

