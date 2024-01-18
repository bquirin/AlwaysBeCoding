"""
Stuttering function
Description: https://edabit.com/challenge/gt9LLufDCMHKMioh2
"""



def stutter(word):
    # first 2 letters, ellipsis, space first 2 letters ellipsis, space word
    
    prefix = word[0:2]
    ellipsis = "..."
    
    return f"{prefix}{ellipsis} {prefix}{ellipsis} {word}? "




def main():
    result = stutter("incredible")
    print(result)

if __name__ == "__main__":
    main()