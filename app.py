# from datetime import datetime
# t = open('app_vol/text.txt')
# print(t.read())
#
#
# t = open('app_vol/text.txt','a')
# def main():
#     today = datetime.today()
#     t.write("Previous running: ")
#     t.write(str(today))
#     t.write("\n")
#     print("App.py is running now :)")
#
# if __name__ == "__main__":
#     main()

# from datetime import datetime
#
# with open('app_vol/text.txt') as t:
#     print(t.read())
#
# def main():
#     today = datetime.today()
#     with open('app_vol/text.txt','a') as t:
#         t.write("Previous running: ")
#         t.write(str(today))
#         t.write("\n")
#         print("App.py is running now :)")
#
# if __name__ == "__main__":
#     main()

from datetime import datetime

def read_file(file_descriptor=None):
    print(file_descriptor.read())

def write_file(file_descriptor=None):
    today = datetime.today()
    file_descriptor.write("Previous running: ")
    file_descriptor.write(str(today))
    file_descriptor.write("\n")
    print("App.py is running now :)")

if __name__ == "__main__":
    with open('app_vol/text.txt', 'r+') as t:
        read_file(t)
        write_file(t)
