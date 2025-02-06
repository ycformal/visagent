Question: How old is the girl that is wearing a sweatshirt?

Reference Answer: young

Image path: ./sampled_GQA/n159802.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='sweatshirt')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='girl')
ANSWER0=VQA(image=IMAGE1,question='How old is the girl that is wearing a sweatshirt?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: 'IMAGE1'

