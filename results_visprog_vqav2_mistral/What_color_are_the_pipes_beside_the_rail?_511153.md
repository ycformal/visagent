Question: What color are the pipes beside the rail?

Reference Answer: green

Image path: ./sampled_GQA/511153.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='rail')
IMAGE0=CROP_BESIDE(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='pipes')
IMAGE1=CROP(image=IMAGE0,box=BOX1)
ANSWER0=VQA(image=IMAGE1,question='What color are the pipes?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: 'CROP_BESIDE'

