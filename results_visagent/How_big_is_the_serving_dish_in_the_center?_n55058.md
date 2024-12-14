Question: How big is the serving dish in the center?

Reference Answer: The serving dish is small.

Image path: ./sampled_GQA/n55058.jpg

Program:

```
How big is A in the <spatial pos>?
Program:
BOX0=LOC(image=IMAGE,object='serving dish')
IMAGE0=CROP_CENTER(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='How big is the serving dish?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: small

