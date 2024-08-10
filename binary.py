video_titles = [
    "The Art of Coding",
    "Exploring the Cosmos",
    "Cooking Masterclass: Italian Cuisine",
    "History Uncovered: Ancient Civilizations",
    "Fitness Fundamentals: Strength Training",
    "Digital Photography Essentials",
    "Financial Planning for Beginners",
    "Nature's Wonders: National Geographic",
    "Artificial Intelligence Revolution",
    "Travel Diaries: Discovering Europe"
]

def bubble_sort(list):
    n = len(list)
    # print(n)
    for i in range(n):
        # print (range(n))
        for j in range(0, n-i-1):
            # print(range(0, n-i-1))
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
        
# bubble_sort(video_titles)
# print("Sorted Videos")
# print(video_titles)


def binary_search (list, target):
    low = 0
    high = len(list)-1

    # print (high)
    while low <= high:
        mid = (low + high)//2 
        if list[mid] == target:
            return mid
        elif list[mid] < target:
            low = mid + 1
        else: 
            high = mid - 1

    return None


# print(f"This is the index")

# print(binary_search(video_titles, "Digital Photography Essentials"))