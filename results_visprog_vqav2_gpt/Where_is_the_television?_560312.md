Question: Where is the television?

Reference Answer: on wall

Image path: ./sampled_GQA/560312.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='television')
ANSWER0=EVAL(expr="'left' if {BOX0[0]} < IMAGE.width/2 else 'right'")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: name 'IMAGE' is not defined

