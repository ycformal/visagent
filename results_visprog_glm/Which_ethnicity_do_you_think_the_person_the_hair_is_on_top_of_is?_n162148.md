Question: Which ethnicity do you think the person the hair is on top of is?

Reference Answer: asian

Image path: ./sampled_GQA/n162148.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='hair')
IMAGE0=CROP_TOPOF(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='Which ethnicity do you think the person is?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: 'CROP_TOPOF'

