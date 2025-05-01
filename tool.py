# !/usr/bin/env python3

import socket
import threading
import udp_flood

def get_attack():
    print("Available attacks:")
    print("[1] Smart Lightbulb")
    print("[2] Router")
    print("[3] Smart Vacuum")
    attack_num = input("Enter the number of the device you'd like to target: ")
    try:
        attack_num = int(attack_num)
    except:
        print("Invalid attack choice. Try again.")
        quit()
    if attack_num in range(1, 4):
        if attack_num == 1:
            print("Smart lightbulb chosen.")
        elif attack_num == 2:
            print("Router chosen.")
        elif attack_num == 3:
            print("Smart vacuum chosen.")
        return int(attack_num)
    else:
        print("Invalid attack number. Try running again.")
        quit()

def main():
    print("<<<< <<<< <<<< <<<< METASPL-IOT >>>> >>>> >>>> >>>>")
    print("What kind of device would you like to attack?")
    attack = get_attack()
    if attack == 1:
        udp_flood.udp_flood()


if __name__ == "__main__":
    main()


