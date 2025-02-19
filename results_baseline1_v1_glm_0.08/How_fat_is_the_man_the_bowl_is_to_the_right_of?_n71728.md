Question: How fat is the man the bowl is to the right of?

Reference Answer: thin

Image path: ./sampled_GQA/n71728.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='bowl')
IMAGE0=CROP_RIGHTOF(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='man')
ANSWER0=VQA(image=IMAGE1,question='How fat is the man?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: 'IMAGE1'

