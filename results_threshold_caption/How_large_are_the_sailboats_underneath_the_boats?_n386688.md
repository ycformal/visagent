Question: How large are the sailboats underneath the boats?

Reference Answer: The sailboats are small.

Image path: ./sampled_GQA/n386688.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='boats')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='sailboats')
ANSWER0=SIZE(box=BOX1)
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: small

