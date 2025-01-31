stack=[]
size=5
def display():
    print("stack items are:")
    for item in stack:
        print(item)
def push(item):
    print(f"push an item into the stack{item}")
    if len(stack)<size:
        stack.append(item)
    else:
        print("stack is full")
def pop():
    if len(stack)>0:
        print(f"pop an item from the list{stack.pop()}")
    else:
        print("STACK IS EMPTY")
def main():
    push(1)
    push(2)
    push(3)
    push(4)
    push(5)
    display()
    push(10)
    pop()
    pop()
    pop()
    display()
    pop()
    pop()
    pop()
if __name__ == "__main__":

    main()