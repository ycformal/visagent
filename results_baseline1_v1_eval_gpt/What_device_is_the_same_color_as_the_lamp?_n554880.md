Question: What device is the same color as the lamp?

Reference Answer: cell phone

Image path: ./sampled_GQA/n554880.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='lamp')
IMAGE0=CROP(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What color is the lamp?')
ANSWER1=EVAL(expr="SELECT(image=IMAGE,object='device',color={ANSWER0})")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Runtime error: name 'SELECT' is not defined

