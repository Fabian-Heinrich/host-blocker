from HostBlocker import HostBlocker

blocker = HostBlocker()

print("1: to activate, 2: to deactivate")
choice = int(input())

if choice == 1:
    blocker.activate()

if choice == 2:
    blocker.deactivate()