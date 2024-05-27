from queue import LifoQueue

backward_history =LifoQueue()
forward_history = LifoQueue()
current_page = None 

#visit function 
NoOfVisists= int(input("Enter the number of url history: "))
print("Enter URLs to visit:")
for i in range (NoOfVisists):
    url= input ("URL:")
    print(f"Visiting {url}")
    backward_history.put(current_page)
    current_page=url

#display current page 
print(f"current page : {current_page}")

#go back 
while input ("Do you want to go back? (yes/no)").lower() =='yes':
    if not backward_history.empty():
        forward_history.put(current_page)
        current_page = backward_history.get()
        print(f"Going back to {current_page}")
    else:
        print("No previous page available")

#go forward 
while input ("Do you want to go forward? (yes/no): ").lower() =='yes':
    if not forward_history.empty():
        backward_history.put(current_page)
        current_page = forward_history.get()
        print(f"Going forward t {current_page}")
    else:
        print("No for ward page available")

