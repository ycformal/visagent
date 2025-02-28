Question: What is the color of the closest building?

Reference Answer: yellow

Image path: ./sampled_GQA/552507.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='building')
IMAGE0=CROP_CLOSEST(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What color is the building?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: 'CROP_CLOSEST'

