Question: A dog is standing on all four feet facing to the left with its tail sticking out straight.

Reference Answer: False

Left image URL: http://buzzsharer.com/wp-content/uploads/2016/04/basset-hound-picture.jpg

Right image URL: http://www.bhcsc.com/basset-hound-standard/images/disqualifications/shape_pic-41.png

Program:

```
Statement: A dog is standing on all four feet facing to the left with its tail sticking out straight.
Program:
ANSWER0=VQA(image=LEFT,question='Is the dog standing on all four feet?')
ANSWER1=VQA(image=LEFT,question='Is the dog facing to the left?')
ANSWER2=VQA(image=LEFT,question='Is the dog tail sticking out straight?')
ANSWER3=EVAL(expr='{ANSWER0} and {ANSWER1} and {ANSWER2}')
FINAL_ANSWER=RESULT(var=ANSWER3)
```
Answer: Runtime error: 'A'

