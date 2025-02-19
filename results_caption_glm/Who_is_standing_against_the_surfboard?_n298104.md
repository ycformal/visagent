Question: Who is standing against the surfboard?

Reference Answer: woman

Image path: ./sampled_GQA/n298104.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='surfboard')
IMAGE0=CROP_AGAINST(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='Who is standing against the surfboard?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: a young woman

