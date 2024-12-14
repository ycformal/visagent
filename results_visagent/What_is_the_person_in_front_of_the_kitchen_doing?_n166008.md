Question: What is the person in front of the kitchen doing?

Reference Answer: The man is eating.

Image path: ./sampled_GQA/n166008.jpg

Program:

```
 What is A <spatial pos> B doing?
Program:
BOX0=LOC(image=IMAGE,object='kitchen')
IMAGE0=CROP_FRONT(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='person')
ANSWER0=VQA(image=IMAGE0,question='What is the person in front of the kitchen doing?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: eating

