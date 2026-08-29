"""
Using names.txt, a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order.
Then working out the alphabetical value for each name,
multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth,
3 + 15 + 12 + 9 + 14 = 53 is the 938th name in the list.
So, COLIN would obtain a score of 938 * 53 = 49714.

What is the total of all the name scores in the file?
"""

letters = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
value = [i for i in range(1,26+1)] 
mappings = dict(zip(letters,value))
def load():
    with open("names.txt",'r') as file:
        text = file.read()
    text = text.replace("\"","")
    text = text.split(",")
    text.sort()
    return text

if __name__ == "__main__":
    names = load()
    total = 0
    for i in range(len(names)):
        score = 0
        for j in range(len(names[i])):
            score += mappings[names[i][j]]
        total += score * (i + 1)
    print(total)
