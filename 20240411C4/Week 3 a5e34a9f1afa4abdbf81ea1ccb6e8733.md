# Week 3

Dates: April 11
Topics: CH3

# Tuple

- A tuple is like a list that uses parentheses

![Screenshot 2024-04-11 at 11.23.50 AM.png](Week%203%20a5e34a9f1afa4abdbf81ea1ccb6e8733/Screenshot_2024-04-11_at_11.23.50_AM.png)

- The main difference between a tuple and a list is that a tuple cannot change once you’ve created it

# Replace

![Screenshot 2024-04-11 at 11.24.39 AM.png](Week%203%20a5e34a9f1afa4abdbf81ea1ccb6e8733/Screenshot_2024-04-11_at_11.24.39_AM.png)

- Use tuple if you know can never change

# Map (Dictionary)

- A map or dictionary is a collection of things, like lists and tuples.

![Screenshot 2024-04-11 at 11.26.43 AM.png](Week%203%20a5e34a9f1afa4abdbf81ea1ccb6e8733/Screenshot_2024-04-11_at_11.26.43_AM.png)

<aside>
💡 If I asked you what Rebecca Clarke’s favorite sport is, you could skim through that list and find the answer is netball. But what if the list included 100 (or many more) people?

</aside>

![Screenshot 2024-04-11 at 11.27.03 AM.png](Week%203%20a5e34a9f1afa4abdbf81ea1ccb6e8733/Screenshot_2024-04-11_at_11.27.03_AM.png)

- The difference between maps and lists or tuples is that each item in a map has **a key and a
corresponding value**

![Screenshot 2024-04-11 at 11.41.37 AM.png](Week%203%20a5e34a9f1afa4abdbf81ea1ccb6e8733/Screenshot_2024-04-11_at_11.41.37_AM.png)

- This is a table representation of the favorite_sports

## Access

![Screenshot 2024-04-11 at 11.42.42 AM.png](Week%203%20a5e34a9f1afa4abdbf81ea1ccb6e8733/Screenshot_2024-04-11_at_11.42.42_AM.png)

- We access our map favorite_sports using her name as the key

<aside>
💡 Did you realize the index is different in a map?

</aside>

## Delete

- To delete a value in a map, use its key

![Screenshot 2024-04-11 at 11.46.07 AM.png](Week%203%20a5e34a9f1afa4abdbf81ea1ccb6e8733/Screenshot_2024-04-11_at_11.46.07_AM.png)

## Replace

- To replace a value in a map, we also use its key

![Screenshot 2024-04-11 at 11.46.38 AM.png](Week%203%20a5e34a9f1afa4abdbf81ea1ccb6e8733/Screenshot_2024-04-11_at_11.46.38_AM.png)

## Join

- You can’t join maps with the plus operator (+) like we did in list

![Screenshot 2024-04-11 at 11.48.06 AM.png](Week%203%20a5e34a9f1afa4abdbf81ea1ccb6e8733/Screenshot_2024-04-11_at_11.48.06_AM.png)

# Challenge 1

Create a list and map that contain this week’s date and day

Ex. ‘4.11 : Thursday’

# If Statements

- An if statement might be written in Python like this

![Screenshot 2024-04-12 at 8.18.26 AM.png](Week%203%20a5e34a9f1afa4abdbf81ea1ccb6e8733/Screenshot_2024-04-12_at_8.18.26_AM.png)

- An if statement is made up of the if keyword, followed by a condition and a colon (:)

# Block

- A block of code is a grouped set of programming statements
- For example, when if age > 20: is true, you might want to do more

![Screenshot 2024-04-12 at 8.20.07 AM.png](Week%203%20a5e34a9f1afa4abdbf81ea1ccb6e8733/Screenshot_2024-04-12_at_8.20.07_AM.png)

- Whitespace, such as a tab (inserted when you press
the tab key) or a space (inserted when you press the spacebar), is
meaningful.
    
    ![Screenshot 2024-04-12 at 8.21.03 AM.png](Week%203%20a5e34a9f1afa4abdbf81ea1ccb6e8733/Screenshot_2024-04-12_at_8.21.03_AM.png)
    

# Quiz1

Will it work?

![Screenshot 2024-04-12 at 8.21.14 AM.png](Week%203%20a5e34a9f1afa4abdbf81ea1ccb6e8733/Screenshot_2024-04-12_at_8.21.14_AM.png)

- Answer
    
    No! It is not part of a block. Use consistent spacing!
    
    ![Screenshot 2024-04-12 at 8.22.02 AM.png](Week%203%20a5e34a9f1afa4abdbf81ea1ccb6e8733/Screenshot_2024-04-12_at_8.22.02_AM.png)
    

# Conditions

![Screenshot 2024-04-12 at 8.23.38 AM.png](Week%203%20a5e34a9f1afa4abdbf81ea1ccb6e8733/Screenshot_2024-04-12_at_8.23.38_AM.png)

- Be sure to use a double equal sign (==) when defining an equal-to
condition
- equal sign (=) is an assignment operator!

![Screenshot 2024-04-12 at 8.24.58 AM.png](Week%203%20a5e34a9f1afa4abdbf81ea1ccb6e8733/Screenshot_2024-04-12_at_8.24.58_AM.png)

# If and Else

- “If something is true, then do this”
    
    ![Screenshot 2024-04-12 at 8.26.00 AM.png](Week%203%20a5e34a9f1afa4abdbf81ea1ccb6e8733/Screenshot_2024-04-12_at_8.26.00_AM.png)
    

# If and Elif

![Screenshot 2024-04-12 at 8.26.45 AM.png](Week%203%20a5e34a9f1afa4abdbf81ea1ccb6e8733/Screenshot_2024-04-12_at_8.26.45_AM.png)

![Screenshot 2024-04-12 at 8.26.56 AM.png](Week%203%20a5e34a9f1afa4abdbf81ea1ccb6e8733/Screenshot_2024-04-12_at_8.26.56_AM.png)

- Elif means else if
- You can add more conditions using elif

# Challenge 2

Suppose we need to assign different grades to students based on their scores.

1. If a student scores above **90**, assign grade **A → print(’A’)**
2. If a student scores above **75**, assign grade **B → print(’B’)**
3. If a student scores above **65**, assign grade **C → print(’C’)**
4. Below, assign grade **D → print(’D’)**