"""Pyramid"""
def main():
    """Main Func."""
    num = int(input())
    for i in range(1, num+1):
        print(" "*(num-i), end="")
        print("*" * ((2*i)-1))
main()
