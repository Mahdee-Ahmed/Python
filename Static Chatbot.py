import webbrowser
from datetime import datetime




def greet():
    name = (input('Enter your name : ').lower())
    print('')
    print("Hello,", name.upper())
    print('How are you doing,',name.upper(),'?')
    if name== 'mahdee':
        print('The answer is matched',1)
    elif name!= 'mahdee':
        print('The answer is not matched',0)

def conversation():
        name_conversation = str(input('Enter your name : '))
        print('')
        print("hello", name_conversation, '.', 'Do you want to learn today ', name_conversation, '?')
        answer = str(input('YES or NO : ').lower())
        print('')
        if answer == 'yes' or answer=='y':
            course=str(input('Excel, Wordpress, Python, R, HTML, Graphics design : ').lower())
            if course=='excel':
                print(webbrowser.open('https://www.w3schools.com/excel'))
            if course=='wordpress':
                print(webbrowser.open('https://wordpress.com'))
            if course == 'python':
                print(webbrowser.open('https://www.w3schools.com/python/default.asp'))
            if course == 'html':
                print(webbrowser.open('https://www.w3schools.com/html/default.asp'))
            if course == 'graphics' or course =='graphics design' or course=='design':
                print(webbrowser.open('https://www.domestika.org/en'))

        elif answer == 'no':

            print('Okay,bye')
def today():
    now = datetime.now()
    formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
    print("Today is:", formatted_date)



print('PRESS 1 FOR GREET')
print('PRESS 2 FOR CONVERSATION')
print('PRESS 3 FOR INFORMATION ABOUT TODAY')
print('')
user = str(input('greet or conversation : '))
if user =='1':
    greet()
if user =='2':
    conversation()
if user =='3':
    today()








