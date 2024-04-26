from queue import LifoQueue
backward_history = LifoQueue()
forward_history = LifoQueue()
current_page = None
#visit function
noOfVisists = int(input("Enter the number of the URL history: "))
print("Enter URLs to visit:")
for i in range(noOfVisists):
    url = intput("URL: ")
    print(f"visiting{url}")
    backward_history.put(current_page)
    current_page = url
    #display current page
 print(f"current page: {current_page}")
#go back
# while input("Do you want to go back? (yes/no:) ").lower() == 'yes':
if not backward

