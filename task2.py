# task 1

import random
mood = ["happy", "sad", "angry", "tired"]
day = [1, 2, 3, 4, 5, 6, 7]
time = input("Is it morning, afternoon, or evening? ")

for day in range(1, 8):
    if day == 1:
        if time == "morning":
            print("On Sunday morning you were " + random.choice(mood))
        elif time == "afternoon":
            print("On Sunday afternoon you were " + random.choice(mood))
        elif time == "evening":
            print("On Sunday evening you were " + random.choice(mood))
    if day == 2:
        if time == "morning":
            print("On Monday morning you were " + random.choice(mood))
        elif time == "afternoon":
            print("On Monday afternoon you were " + random.choice(mood))
        elif time == "evening":
            print("On Monday evening you were " + random.choice(mood))
    if day == 3:
        if time == "morning":
            print("On Tuesday morning you were " + random.choice(mood))
        elif time == "afternoon":
            print("On Tuesday afternoon you were " + random.choice(mood))
        elif time == "evening":
            print("On Tuesday evening you were " + random.choice(mood))
    if day == 4:
        if time == "morning":
            print("On Wednesday morning you were " + random.choice(mood))
        elif time == "afternoon":
            print("On Wednesday afternoon you were " + random.choice(mood))
        elif time == "evening":
            print("On Wednesday evening you were " + random.choice(mood))
    if day == 5:
        if time == "morning":
            print("On Thursday morning you were " + random.choice(mood))
        elif time == "afternoon":
            print("On Thursday afternoon you were " + random.choice(mood))
        elif time == "evening":
            print("On Thursday evening you were " + random.choice(mood))
    if day == 6:
        if time == "morning":
            print("On Friday morning you were " + random.choice(mood))
        elif time == "afternoon":
            print("On Friday afternoon you were " + random.choice(mood))
        elif time == "evening":
            print("On Friday evening you were " + random.choice(mood))
    if day == 7:
        if time == "morning":
            print("On Saturday morning you were " + random.choice(mood))
        elif time == "afternoon":
            print("On Saturday afternoon you were " + random.choice(mood))
        elif time == "evening":
            print("On Saturday evening you were " + random.choice(mood))