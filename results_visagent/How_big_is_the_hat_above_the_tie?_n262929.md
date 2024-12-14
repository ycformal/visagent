Question: How big is the hat above the tie?

Reference Answer: The hat is small.

Image path: ./sampled_GQA/n262929.jpg

Program:

```
 How big is A <spatial pos> B?
Program:
BOX0=LOC(image=IMAGE,object='tie')
IMAGE0=CROP_ABOVE(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='hat')
ANSWER0=SIZE(box=BOX1)
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: small

