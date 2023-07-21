import tkinter as tk
from tkinter import filedialog


#User Input
input = input("Enter a list of numbers Seperated by one space: ")

#Splitting Numbers
number_list = input.split()



array1 = number_list

#Insertion Sort algorithm uses Outer for loop and inner while loop
# Best O(n) Worst O(n^2)
def insertionSort(array1):
    for i in range(1, len(array1)):
        val = array1[i]
        j = i - 1
        while j >= 0 and array1[j] > val:
            array1[j + 1] = array1[j] 
            j = j - 1
        array1[j + 1] = val
    


#Call Insertion Sort Function Outputs result
def sort_numbers():
    input_str = entry.get()
    number_list = [int(num) for num in input_str.split()]
    insertionSort(number_list)
    result.config(text="Sorted List: " + " ".join(map(str, number_list)))


# GUI Title
root = tk.Tk()
root.title("Number Sorter")

# GUI Size
canvas = tk.Canvas(root, width=600, height=300)
canvas.pack()

# GUI Instructions
instructions = tk.Label(root, text="Enter a list of numbers separated by one space:")
instructions.pack(pady=20)

#GUI Entry
entry = tk.Entry(root, width=50)
entry.pack(pady=5)

#GUI Sort Button
sort_button = tk.Button(root, text="Sort", command=sort_numbers)
sort_button.pack(pady=5)

#GUI Result
result = tk.Label(root, text="Sorted List: ")
result.pack(pady=10)

#GUI Exit Button
root.mainloop()