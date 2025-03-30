def main():
    message = str(input())
    convert(message)

def convert(message):
    print(message.replace(":)","🙂").replace(":(", "🙁"))

main()

#1- define function main
#2- created the variable message which takes user input
#3- covert(function)- takes input we got from variable- message
#5- defines the convert function that takes message input(user input)
#6- prints & does replacement