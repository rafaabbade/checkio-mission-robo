"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
           {
        "input": [8, 8, 3, [1, -1, 1, 1, 1, -1, 1, 1]],
        "answer": 2
    },
    {
        "input": [5, 4, 1, [1, 1, 1, 1]],
        "answer": 1
    },
    {
        "input": [2, 1, 1, [1]],
        "answer": 1
    },
    {
        "input": [4, 4, 4, [-1,1,1,1]],
        "answer": 1
    },
    {
        "input": [4, 6, 2, [1,1,1,1,1,1]],
        "answer": 2
    }    
    ]
}
