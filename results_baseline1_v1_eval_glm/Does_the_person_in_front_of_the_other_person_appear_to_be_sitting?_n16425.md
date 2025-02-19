Question: Does the person in front of the other person appear to be sitting?

Reference Answer: no

Image path: ./sampled_GQA/n16425.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='person')
IMAGE0=CROP_ABOVE(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='person')
ANSWER0=VQA(image=IMAGE1,question='Is the person sitting?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: 'IMAGE1'

