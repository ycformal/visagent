Question: Does the Light pole have a shadow?

Reference Answer: yes

Image path: ./sampled_GQA/254917.jpg

Original program:

```
BOX0=LOC(image=IMAGE,object='light pole')
IMAGE0=CROP(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='Does this object have a shadow?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Program:

```
BOX0=LOC(image=IMAGE,object='light pole')
IMAGE0=CROP(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='Does this object have a shadow?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Yes

