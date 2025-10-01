#Currrent page
current_state_url = "http://www.google.com/"
#To move forward
forward_stack = []
#To move backward
backward_stack = []


def visit_new_url(url):
    global current_state_url

    if (current_state_url != ""):
        #Push the current page on the top of the backward stack
        backward_stack.append(current_state_url)
    
    current_state_url = url
    forward_stack.clear()
    print(current_state_url)
#FORWARD
def forward():
    global current_state_url

    #If the forward stack is empty, the command is ignored
    if len(forward_stack) == 0:
        print("Ignored")
        return
    
    #Else push the current page on top of the backward stack
    backward_stack.append(current_state_url)

    #Pop the page fromt he top of the forward stack
    current_state_url = forward_stack.pop()
    print(current_state_url)

#BACK
def backward():
    global current_state_url

    #If the backward stack is empty, the command is ignored
    if len(backward_stack) == 0:
        print("Ignored")
        return

    #Else push the current page on top of the forward stack
    forward_stack.append(current_state_url)

    #Pop the page from the top of the backward stack
    current_state_url = backward_stack.pop()
    print(current_state_url)

def main():
    while True:
        try:
            command = input().strip()
            if not command:
                continue

            parts = command.split(maxsplit=1)
            action = parts[0].upper()

            if action == "QUIT":
                break
            elif action == "BACK":
                backward()
            elif action == "FORWARD":
                forward()
            elif action == "VISIT":
                if len(parts) < 2:
                    print("Ignored")
                else:
                    url = parts[1]
                    visit_new_url(url)
            else:
                print("Ignored")
        except EOFError:
            break
if __name__ == "__main__":
    main()



