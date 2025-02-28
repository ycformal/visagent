Question: What sport is represented on the red shirt of the man?

Reference Answer: baseball

Image path: ./sampled_GQA/369685.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='man')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='red shirt')
ANSWER0=VQA(image=IMAGE1,question='What sport is represented on the red shirt?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: 'IMAGE1'

