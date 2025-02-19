Question: What kind of animal is looking at the sky?

Reference Answer: bear

Image path: ./sampled_GQA/n335542.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='sky')
IMAGE0=CROP_BELOW(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object)
ANSWER0=VQA(image=IMAGE0,question='What kind of animal is looking at the sky?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: bear

