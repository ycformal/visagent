Question: What is in the background of this picture?

Reference Answer: trees

Image path: ./sampled_GQA/448211.jpg

Original program:

```
BOX0=GET(image=IMAGE)
IMAGE0=CROP_BELOW(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='background')
ANSWER0=VQA(image=IMAGE0,question='What is in the background of this picture?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Program:

```
BOX0=GET(image=IMAGE)
IMAGE0=CROP_BELOW(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='background')
ANSWER0=VQA(image=IMAGE0,question='What is in the background of this picture?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: a wooden fence and trees

