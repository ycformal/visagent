Question: What color is the shirt near the shorts?

Reference Answer: The shirt is black.

Image path: ./sampled_GQA/n262929.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='shorts')
IMAGE0=CROP_NEAR(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='shirt')
ANSWER0=VQA(image=IMAGE0,question='What color is the shirt?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: black

