Question: What is the color of the rightmost cell phone?

Reference Answer: silver

Image path: ./sampled_GQA/568367.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='cell phone')
IMAGE0=CROP_RIGHTMOST(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What color is the cell phone?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: 'CROP_RIGHTMOST'

