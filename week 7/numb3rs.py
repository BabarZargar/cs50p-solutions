import re

def main():
    ip = input("IPv4 Address: ").strip()
    print(validate(ip))


def validate(ip):
    if ip := re.search(r"^([1-9]?[0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]?[0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]?[0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]?[0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$", ip):
        return True
    else:
        return False


if __name__ == "__main__":
    main()
