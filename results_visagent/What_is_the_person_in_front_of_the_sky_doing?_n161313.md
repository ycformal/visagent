Question: What is the person in front of the sky doing?

Reference Answer: The person is jumping.

Image path: ./sampled_GQA/n161313.jpg

Program:

```
 What is A <spatial pos> B doing?
Program:
BOX0=LOC(image=IMAGE,object='sky')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE,object='person')
IMAGE1=CROP_FRONT(image=IMAGE,box=BOX1)
ANSWER0=VQA(image=IMAGE1,question='What is the person in front of the sky doing?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Snowboarding

