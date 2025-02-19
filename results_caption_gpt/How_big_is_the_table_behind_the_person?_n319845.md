Question: How big is the table behind the person?

Reference Answer: small

Image path: ./sampled_GQA/n319845.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='person')
IMAGE0=CROP_BEHIND(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='table')
ANSWER0=SIZE(box=BOX1)
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: "runtime error"

