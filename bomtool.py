import sys
import math

#Tool for generating Digikey fast-add compatible BOMs
#from a copypasta in google sheets.

def main():
    print("Paste in your part numbers on separate lines")
    print("Enter a blank line to end input")
    lines = []
    while True:
        part = input(">")
        part = part.strip().upper()
        if part == "":
            print("Done!")
            break
        else:
            lines.append(part)
    print("How many copies of this BOM?")
    copies = int(input(">"))
    print("Safety margin? (.05 = 5%)")
    margin = float(input(">"))
    if margin < 1.0:
        margin += 1.0
    print("OK, here's your order.")
    result = count(lines, copies, margin)
    output(result)
    summarize(result)

def output(d):
    print("Digikey BOM")
    for k in d.keys():
        print("{},{}".format(d[k], k))
    print("Google sheets pasteable")
    for k in d.keys():
        print("{}\t{}".format(k, d[k]))

def summarize(d):
    count = 0
    for v in d.values():
        count += int(v)
    print("BOM contains {} unique parts, {} total parts.".format(
        len(d.keys()), count))

def count(items, quantity=1, margin=1.0):
    result = dict()
    for i in items:
        if i in result.keys():
            result[i] += 1
        else:
            result[i] = 1
    #Apply quantities
    for i in result.keys():
        q = result[i]
        q *= quantity
        q *= margin
        result[i] = math.ceil(q)
    return result
    
if __name__ == "__main__":
    sys.exit(main())
