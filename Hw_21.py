#HW_21 -- python basic 1-7
#start
#1
l12_24: list[int] = [ i for i in range(12,24+1)]
print(l12_24)
#2
l7_31: list[int] = [ i for i in range(7,31+1, 3)]
print(l7_31)
#3
l10_20: list[int] = [ i for i in range(10,20+1,2)]
print(l10_20)
#4

for num in range(1,45+1):
    if num % 3 == 0 and num % 5 == 0:
        print(num, "FizzBuzz")
    elif num % 3 == 0:
        print(num,"Fizz")
    elif num % 5 == 0:
        print(num,"Buzz")

#5
def sum_list(x :list[int]) -> int:
    sum_x = 0
    for num in x:
        sum_x += num
    return sum_x
print(sum_list([2,6,8,10]))
#
# #6
def personal_details(x:list):
    x = {"id": input("Enter your id: "),"first_name": input("Enter your first name: "),
         "last name": input("last name:"),"age": input("Enter your age: "),"country":input("Enter your country: "),
        "city": input("Enter your city:") }

# how many student ?
#who i continue the function

print(personal_details([]))


#7
our_pets = [
{
"animal_type": "cat",
"names": [
"Meowzer",
"Fluffy",
"Kit-Cat"
]
},
{
"animal_type": "dog",
"names": [
"Spot",
"Bowser",
"Frankie"
]
}
]
for i in our_pets:
    if i["animal_type"] == "cat":
        print(i["animal_type"])

for i in our_pets:
    if i["names"]:
        print(i["names"])

for i in our_pets:
    if i["names"]:
        ["names"].insert(2,"boni")
print("ddd",{our_pets.index(["names"])})


for i in our_pets:
    if i["names"]:
        print(i["names"])
