Question: Who is in front of the person that is crouching?

Reference Answer: batter

Image path: ./sampled_GQA/n130638.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='person')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='crouching')
IMAGE1=CROP_FRONT(image=IMAGE0,box=BOX1)
ANSWER0=VQA(image=IMAGE1,question='Who is in front of the crouching person?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: The batter.

