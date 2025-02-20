Question: What is the device that is sitting beside the bag?

Reference Answer: laptop

Image path: ./sampled_GQA/n367944.jpg

Original program:

```
BOX0=LOC(image=IMAGE,object='bag')
IMAGE0=CROP_BESIDE(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What is the device?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="What is the device that is sitting beside the bag?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What is the device that is sitting beside the bag?')=<b><span style='color: green;'>laptop</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>laptop</span></b></div><hr>

Answer: calculator

