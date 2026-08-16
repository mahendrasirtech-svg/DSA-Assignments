#1. Find maximum element.

nums=[12,5,6,20,13]
largest=nums[0]
for num in nums:
    if num>largest:
        largest=num
print("Largest:", largest)

#2. Find minimum element. 
smallest=nums[0]
for num in nums:
    if num<smallest:
        smallest=num
print("Smallest:", smallest)

#3. Find second largest element. 
largest=float('-inf')
second_largest=float('-inf')
for num in nums:
    if num>largest:
        second_largest=largest
        largest=num
    elif num>second_largest:
        second_largest=num
print("Second Largest:", second_largest)

#4. Find second smallest element. 
smallest=float('inf')
second_smallest=float('inf')
for num in nums:
    if num<smallest:
        second_smallest=smallest
        smallest=num
    elif num<second_smallest:
        second_smallest=num
print("Second Smallest:", second_smallest)

#5. Count even numbers. 
even_count=0
for num in nums:
    if num%2==0:
        even_count+=1
print("Even numbers:", even_count)

#6. Count odd numbers.
odd_count=0
for num in nums:
    if num%2!=0:
        odd_count+=1
print("Odd numbers:", odd_count) 
#7. Reverse an array.
for i in range(len(nums)//2):
    nums[i], nums[len(nums)-1-i] = nums[len(nums)-1-i], nums[i]
print("Reversed array:", nums)    
 
#8. Search an element.
search_element=20
found=False
for num in nums:
    if num==search_element:
        found=True
        break
if found:
    print(f"{search_element} found in the array.")
    
#9. Check if an array is sorted.
is_sorted=True
for i in range(len(nums)-1):
    if nums[i]>nums[i+1]:
        is_sorted=False
        break
if is_sorted:
    print("The array is sorted.") 
#10. Count occurrences of a target element.
target_element=20
count=0
for num in nums:
    if num==target_element:
        count+=1
print(f"Occurrences of {target_element}: {count}")

