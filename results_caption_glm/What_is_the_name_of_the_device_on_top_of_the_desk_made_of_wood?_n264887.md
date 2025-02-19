Question: What is the name of the device on top of the desk made of wood?

Reference Answer: monitor

Image path: ./sampled_GQA/n264887.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='desk')
IMAGE0=CROP_TOPOF(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='device')
ANSWER0=VQA(image=IMAGE1,question='What is the name of the device on top of the desk made of wood?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: runtime error

