#!/usr/bin/env python


from sample import Collection


def main():
    """
    Main Entry
    """
    samples = Collection("data")
    
    while True:
        sample = samples.next()
        if not sample:
            break;
        print(sample)


if __name__ == "__main__":
    main()
