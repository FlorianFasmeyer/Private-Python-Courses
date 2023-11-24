import time as t


def countdown(second):
    if second == 0:
        print("finished")
        return
    else:
        print(f"{second} seconds left")
        t.sleep(1)
        countdown(second - 1)
        return


countdown(10)
