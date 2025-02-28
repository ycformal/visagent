Question: What is the man standing next too?

Reference Answer: sign

Image path: ./sampled_GQA/323827.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='man')
IMAGE0=CROP_NEXTTO(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What is the man standing next too?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: 'CROP_NEXTTO'

