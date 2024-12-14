Question: What is the dessert that is the same shape as the large container called?

Reference Answer: The dessert is a brownie.

Image path: ./sampled_GQA/n28996.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='large container')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='dessert')
ANSWER0=VQA(image=IMAGE0,question='What shape is the large container?')
ANSWER1=VQA(image=IMAGE0,question='What shape is the dessert?')
ANSWER2=EVAL(expr="'The dessert is called {ANSWER1} and it is the same shape as the large container, which is a {ANSWER0}.'")
FINAL_RESULT=RESULT(var=ANSWER2)
```
Answer: Runtime error: invalid syntax (<string>, line 1)

