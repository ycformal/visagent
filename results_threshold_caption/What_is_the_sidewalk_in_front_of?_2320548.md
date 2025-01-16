Question: What is the sidewalk in front of?

Reference Answer: The sidewalk is in front of the bench.

Image path: ./sampled_GQA/2320548.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='sidewalk')
IMAGE0=CROP_FRONT(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What is the sidewalk in front of?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: building

