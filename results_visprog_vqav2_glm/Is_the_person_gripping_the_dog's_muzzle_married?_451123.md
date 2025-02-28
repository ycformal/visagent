Question: Is the person gripping the dog's muzzle married?

Reference Answer: no

Image path: ./sampled_GQA/451123.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='dog')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='muzzle')
IMAGE1=CROP_GRIPPING(image=IMAGE0,box=BOX1)
BOX2=LOC(image=IMAGE1,object='person')
ANSWER0=VQA(image=IMAGE2,question='Is the person married?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: 'CROP_GRIPPING'

