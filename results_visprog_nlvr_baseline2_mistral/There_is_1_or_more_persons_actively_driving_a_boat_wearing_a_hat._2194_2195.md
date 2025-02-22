Question: There is 1 or more persons actively driving a boat wearing a hat.

Reference Answer: True

Left image URL: https://s-media-cache-ak0.pinimg.com/originals/c9/c4/41/c9c441e8e265cf82c6db40aaeb9e6cdf.jpg

Right image URL: http://2.bp.blogspot.com/_h0fJxJvtYDc/TUVdNHfUH5I/AAAAAAAACMw/tHW1qwafz8s/s1600/IMG_0043.JPG

Original program:

```
ANSWER0=VQA(image=LEFT,question='How many persons are actively driving a boat wearing a hat?')
ANSWER1=VQA(image=RIGHT,question='How many persons are actively driving a boat wearing a hat?')
ANSWER2=EVAL(expr='{ANSWER0} + {ANSWER1} >= 1')
FINAL_ANSWER=RESULT(var=ANSWER2)
```
Program:

```
ANSWER0=VQA(image=LEFT,question='How many persons are actively driving a boat wearing a hat?')
ANSWER1=VQA(image=RIGHT,question='How many persons are actively driving a boat wearing a hat?')
ANSWER2=EVAL(expr='{ANSWER0} + {ANSWER1} >= 1')
FINAL_ANSWER=RESULT(var=ANSWER2)
```
Answer: true

