'''
🇮🇳🇮🇳🇮🇳 BY~DHRUV AGRAWAL , INDIA 🇮🇳🇮🇳🇮🇳
'''

def tower_of_Hanoi(num_disks , source , auxillary , destination):
    if num_disks==0:
        return

    elif num_disks==1:
        print(f"{source} {destination}")

    else:
        tower_of_Hanoi(num_disks-1 , source , destination , auxillary)
        print(f"{source} {destination}")
        tower_of_Hanoi(num_disks-1 , auxillary , source , destination)

def num_of_disks(num_disks):
    tower_of_Hanoi(num_disks, 'S', 'A', 'D')

num=int(input("ENTER NUMBER OF TOWERS:"))
num_of_disks(num)
