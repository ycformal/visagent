Question: How long is the white bath towel near the toilet?

Reference Answer: The bath towel is long.

Image path: ./sampled_GQA/n141939.jpg

Program:

```
 How long is A <planar pos> B?
Program:
BOX0=LOC(image=IMAGE,object='toilet')
IMAGE0=CROP_LEFTOF(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='white bath towel')
ANSWER0=LENGTH(box=BOX1)
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: short

