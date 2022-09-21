import time


def greet():
    print('Hello...')
    time.sleep(1)  # blocking resource; database query, API call...
    print('... World!')


def main():
    for _ in range(4):
        greet()


if __name__ == '__main__':
    main()
