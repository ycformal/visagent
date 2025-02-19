Question: How is the piece of furniture that is made of same material as the brown chair called?

Reference Answer: side table

Image path: ./sampled_GQA/n83784.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='brown chair')
IMAGE0=CROP(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What material is the brown chair made of?')
ANSWER1=EVAL(expr="'It is called a {ANSWER0} chair.'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Runtime error: invalid syntax (<string>, line 1)

