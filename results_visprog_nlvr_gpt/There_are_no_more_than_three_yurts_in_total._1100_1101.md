Question: There are no more than three yurts in total.

Reference Answer: True

Left image URL: http://cdn.newsapi.com.au/image/v1/40bb1907830629019edf4cb6ec65b4a0

Right image URL: https://i.pinimg.com/736x/c0/91/c1/c091c19020089cf50c0545df02ae253b--yurts-equestrian.jpg

Program:

```
ANSWER0=VQA(image=LEFT,question='How many yurts are in the image?')
ANSWER1=VQA(image=RIGHT,question='How many yurts are in the image?')
ANSWER2=EVAL(expr='{ANSWER0} + {ANSWER1} <= 3')
FINAL_ANSWER=RESULT(var=ANSWER2)
```
Answer: Runtime error: can only concatenate str (not "int") to str

