Question: Who is in front of the person that is crouching?

Reference Answer: batter

Image path: ./sampled_GQA/n130638.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='person', pose='crouching')
IMAGE0=CROP_FRONT(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='Who is in front of the person?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: 'CROP_FRONT'

