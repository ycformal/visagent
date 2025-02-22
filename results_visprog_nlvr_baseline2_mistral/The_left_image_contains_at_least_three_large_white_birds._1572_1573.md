Question: The left image contains at least three large white birds.

Reference Answer: False

Left image URL: http://1.bp.blogspot.com/-QCcEE7FyORw/UEFvQOtkLLI/AAAAAAAAZwE/f-8LPJAlXR0/s1600/DSC_4159.jpg

Right image URL: https://i.ytimg.com/vi/lViPmi08gSU/maxresdefault.jpg

Original program:

```
ANSWER0=VQA(image=LEFT,question='How many large white birds are in the image?')
ANSWER1=EVAL(expr='{ANSWER0} >= 3')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=LEFT,question='How many large white birds are in the image?')
ANSWER1=EVAL(expr='{ANSWER0} >= 3')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Answer: true

