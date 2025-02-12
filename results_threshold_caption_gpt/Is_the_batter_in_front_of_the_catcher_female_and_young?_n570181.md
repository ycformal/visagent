Question: Is the batter in front of the catcher female and young?

Reference Answer: no

Image path: ./sampled_GQA/n570181.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='catcher')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='batter')
IMAGE1=CROP_FRONT(image=IMAGE0,box=BOX1)
ANSWER0=VQA(image=IMAGE1,question='Is the batter female and young?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: No

