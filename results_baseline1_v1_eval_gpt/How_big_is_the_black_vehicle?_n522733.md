Question: How big is the black vehicle?

Reference Answer: large

Image path: ./sampled_GQA/n522733.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='black vehicle')
ANSWER0=SIZE(box=BOX0)
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: 'SIZE'

