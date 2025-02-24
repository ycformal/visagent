Question: Is the toilet paper next to the toilet made of paper?

Reference Answer: yes

Image path: ./sampled_GQA/n417401.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='toilet')
IMAGE0=CROP_NEXTTO(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='toilet paper')
IMAGE1=CROP(image=IMAGE0,box=BOX1)
ANSWER0=VQA(image=IMAGE1,question='Is the toilet paper made of paper?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Yes, the toilet paper next to the toilet is made of paper.

