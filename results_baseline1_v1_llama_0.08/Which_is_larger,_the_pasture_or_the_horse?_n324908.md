Question: Which is larger, the pasture or the horse?

Reference Answer: pasture

Image path: ./sampled_GQA/n324908.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='horse')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='pasture')
ANSWER0=COUNT(box=BOX1)
ANSWER1=VQA(image=IMAGE0,question='What color is the pasture?')
ANSWER2=EVAL(expr="'pasture' if {ANSWER0} > {ANSWER1} else 'horse'")
FINAL_RESULT=RESULT(var=ANSWER2)
```
Answer: Runtime error: '>' not supported between instances of 'int' and 'str'

