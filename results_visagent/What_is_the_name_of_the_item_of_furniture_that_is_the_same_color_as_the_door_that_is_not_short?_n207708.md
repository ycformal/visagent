Question: What is the name of the item of furniture that is the same color as the door that is not short?

Reference Answer: The piece of furniture is a bookcase.

Image path: ./sampled_GQA/n207708.jpg

Program:

```
 What is the name of A that is <attr> as B that is not <attr>?
Program:
BOX0=LOC(image=IMAGE,object='door')
IMAGE0=CROP(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What color is the door?')
BOX1=LOC(image=IMAGE,object='furniture')
IMAGE1=CROP(image=IMAGE,box=BOX1)
ANSWER1=VQA(image=IMAGE1,question='What is the name of the furniture?')
ANSWER2=EVAL(expr="'yes' if {ANSWER0} == {ANSWER1} and {ANSWER2} != 'short' else 'no'")
FINAL_RESULT=RESULT(var=ANSWER2)
```
Answer: chair

