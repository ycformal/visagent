Question: Why is the photo blurry?

Reference Answer: camera moved

Image path: ./sampled_GQA/402778.jpg

Original program:

```
ANSWER0=VQA(image=IMAGE,question='Why is the photo blurry?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question='Why is the photo blurry?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Why is the photo blurry?')=<b><span style='color: green;'>movement</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>movement</span></b></div><hr>

Answer: movement

