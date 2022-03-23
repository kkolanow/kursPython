from threading import BoundedSemaphore

maxconnections = 5
pool_sema = BoundedSemaphore(value=maxconnections)

with pool_sema:
    print("init connect")
    try:
        print("execute")
    finally:
        print("close")

