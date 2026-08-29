"""
If the numbers 1 to 5 are written out in words:
one, two, three, four, five, then there are
3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000(one thousand) inclusive were written out in words,
how many letters would be used?

NOTE: Do not count spaces or hyphens. For example,
(three hundred and forty-two) contains 23 letters and
(one hundred and fifteen) contains 20 letters.
The use of "and" when writing out numbers is in compliance with British usage.
"""

parseMap = {
       1  :"one",    11 :"eleven",     20 :"twenty",
       2  :"two",    12 :"twelve",     30 :"thirty",
       3  :"three",  13 :"thirteen",   40 :"forty",
       4  :"four",   14 :"fourteen",   50 :"fifty",
       5  :"five",   15 :"fifteen",    60 :"sixty",
       6  :"six",    16 :"sixteen",    70 :"seventy",
       7  :"seven",  17 :"seventeen",  80 :"eighty",
       8  :"eight",  18 :"eighteen",   90 :"ninety",
       9  :"nine",   19 :"nineteen",
       10 :"ten",           
            }
# for 1 < number < 9999
# I've de
def parse(number):
    ones = number%10
    tens = (number%100)//10
    hundreds = (number%1000)//100
    thousands = (number%10000)//1000
    text = ""
    if thousands:
        text += parseMap[thousands] +" thousand "
    if hundreds:
        text += parseMap[hundreds] + " hundred "
    if tens:
        if hundreds:
            text += "and "
        if tens == 1:
            text += parseMap[tens*10 + ones]
            ones = 0
        else:
            text += parseMap[tens * 10]
    if ones:
        if tens:
            text += "-"
        elif thousands or hundreds:
            text += "and "

        text += parseMap[ones]

    return text
if __name__ == "__main__":
    total = 0
    for i in range(1,1001,1):
        text = parse(i)
        print(text)
        text = text.replace(" ","")
        text = text.replace("-","")
        total += len(text)
    print(total)
