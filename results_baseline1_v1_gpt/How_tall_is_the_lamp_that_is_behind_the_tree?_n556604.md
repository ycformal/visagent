Question: How tall is the lamp that is behind the tree?

Reference Answer: tall

Image path: ./sampled_GQA/n556604.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='tree')
IMAGE0=CROP_BEHIND(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='lamp')
ANSWER0=MEASURE(box=BOX1,property='height')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: 'MEASURE'

