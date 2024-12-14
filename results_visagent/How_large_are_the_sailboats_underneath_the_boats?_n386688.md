Question: How large are the sailboats underneath the boats?

Reference Answer: The sailboats are small.

Image path: ./sampled_GQA/n386688.jpg

Program:

```
 How <attr> are A <spatial pos> B?
Program:
BOX0=LOC(image=IMAGE,object='boats')
IMAGE0=CROP_UNDERNEATH(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='sailboats')
ANSWER0=VQA(image=IMAGE0,question='How large are the sailboats underneath the boats?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: small

