def momoization(func):
    saving={}
    def wrapper(*args):
        if tuple(args) not in saving:
            saving[tuple(args)]=func(*args)
        return saving[tuple(args)]
    return wrapper

@momoization
def fib(n:int):
    if n==0 or n ==1:
        return 1
    return fib(n-1)+fib(n-2)

if __name__ == "__main__":
    angka=50
    print(f"{fib(angka):,}")
