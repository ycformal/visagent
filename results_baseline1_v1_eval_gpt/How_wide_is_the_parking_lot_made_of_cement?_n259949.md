Question: How wide is the parking lot made of cement?

Reference Answer: wide

Image path: ./sampled_GQA/n259949.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='parking lot')
IMAGE0=CROP(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='How wide is the parking lot?')
ANSWER1=EVAL(expr="'cement' if {ANSWER0} > 0 else 'not cement'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Runtime error: '>' not supported between instances of 'str' and 'int'

