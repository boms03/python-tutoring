# List

## Creat
<p align=center>
    <img src="img_1.png" width="800">
</p>
- Create a list using [ ] to store data

## Pick
<p align=center>
    <img src="img_2.png" width="800">
</p>

- A list is useful because it can be manipulated
- Use index position inside [] to pick a data from the list


<details>
    <summary>What did you notice?</summary>

    Yes, a list starts at index position 0, so the first item in a list is 0, the second is 1, and the third is 2.

</details>

## Change
<p align=center>
    <img src="img_3.png" width="800">
</p>

- You can also change an item in a list using []

## Subset

<p align=center>
    <img src="img_4.png" width="800">
</p>

- use a colon (:) inside [] to show a subset of items in the list
- “show the items from index position 2 up to (but not including) index position 5”

## Type
- A list can store all sorts of items

<p align=center>
    <img src="img_5.png" width="800">
</p>

<p align=center>
    <img src="img_6.png" width="800">
</p>

<p align=center>
    <img src="img_7.png" width="800">
</p>

- A list can have mixture of number and strings

<p align=center>
    <img src="img_14.png" width="800">
</p>

- A list can store other lists

## Add items

<p align=center>
    <img src="img_8.png" width="800">
</p>

- Use the append function to add items to the end of a list
- A function is a chunk of code that tells Python to do something

<p align=center>
    <img src="img_9.png" width="800">
</p>

- Keep adding like this

## Quiz 1

fruits_list =  ['apple','banana']

(blank 1)

(blank 2)

print(fruits_list)

result: ['apple','banana', 'grape', 'grape']

**Fill in the blanks to get the result**

<details>
    <summary>Answer</summary>

fruits_list.append('grape')

fruits_list.append('grape')

</details>

## Remove items

- Use the del command to remove items from a list

<p align=center>
    <img src="img_10.png" width="800">
</p>

- Remember that positions start at zero
- wizard_list[5] refers to the sixth item in the list

## Quiz 2

fruits_list =  ['apple','banana', 'grape', 'grape']

(blank 1)

(blank 2)

print(fruits_list)

result: ['apple','banana']

**Fill in the blanks to get the result**

<details>
    <summary>Answer</summary>

del fruits_list[3]

del fruits_list[2]


</details>

## List Arithmetic

- join lists just + sign

<p align=center>
    <img src="img_12.png" width="800">
</p>

- join list1 and list2 by using + sign

- You can multiply a list by a number to repeat the list

<p align=center>
    <img src="img_13.png" width="800">
</p>

- This is telling Python to repeat list1 five times


## Challenge

tutor_information =  ['-','Beomsu','Seoul',24,'-']

You will create tutee_information list with your information

1. Get rid of all '-' using **a colon** in tutor_information
2. **Clone** tutor_information to tutee_information
3. **Replace** name, region, age with your information
4. **Combine** tutor_information and tutee_information to all_information list

