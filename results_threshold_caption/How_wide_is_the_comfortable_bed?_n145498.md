Question: How wide is the comfortable bed?

Reference Answer: The bed is wide.

Image path: ./sampled_GQA/n145498.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='bed')
IMAGE0=CROP(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='How wide is the bed?')
ANSWER1=EVAL(expr="'comfortable' if {ANSWER0} > 0 else 'not comfortable'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: queen

