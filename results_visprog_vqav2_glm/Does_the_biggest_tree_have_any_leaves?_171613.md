Question: Does the biggest tree have any leaves?

Reference Answer: no

Image path: ./sampled_GQA/171613.jpg

Program:

```
BOX0=LOC(image=IMAGE,objects='tree')
IMAGE0=CROP_LARGEST(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='Are there any leaves?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: 'object'

