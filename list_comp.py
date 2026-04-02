if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    # This prints the final list directly
    print([[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n])
    # In Python, range(1) only gives you 0. Since the problem says 0≤i≤x, we need to include the actual value of x. Adding + 1 ensures the loop goes all the way to the number you typed.


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    array = set(arr)
    #this will list down the score list of all people join
    A = sorted(list(array))
    print(A[-2])
    #use set() on the arr list to remove all the duplicates and 
    #sorted() to arrange it from lowest to highest score
    #when using print, we want to get the runner-up which is 
    #the 2nd highest score so we use index [-2] to find it
    #we need to put a new line for array just because the problem
    #requires to list the scores as a list, not a set. If not
    #we can just A = sorted(set(arr)) and remove line 15