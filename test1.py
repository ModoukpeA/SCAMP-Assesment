# This function displays the fibbonnaci sequence of a given number
print("\n ***** Fibbonacci's sequence of a given number ***** \n")

# nterms is the number of terms in the sequence
# number1 is 0 and number2 is 1: These are are the first digits displayed in any fibonacci sequence
# next takes the value of the last number in the sequence

nterms = int(input("\t Enter a number : "))
number1 = 0
number2 = 1

print("\n The fibbonacci's sequence is :")
print("\n\t", number1, "|", number2, end=" | ")

for i in range(2, nterms):
    next = number1 + number2
    print(next, end=" | ")
    number1 = number2
    number2 = next