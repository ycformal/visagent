Question: What is the device that is sitting beside the bag?

Reference Answer: laptop

Image path: ./sampled_GQA/n367944.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='bag')
IMAGE0=CROP_BESIDE(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What is the device?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Calculator

