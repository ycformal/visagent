Question: The right image shows one black, white, and brown puppy sitting and facing the camera

Reference Answer: True

Left image URL: http://www.warrenphotographic.co.uk/photography/bigs/20332-Tricolour-Cavalier-King-Charles-Spaniel-pup-white-background.jpg

Right image URL: https://www.warrenphotographic.co.uk/photography/bigs/37977-Tricolour-Cavalier-pup-white-background.jpg

Original program:

```
ANSWER0=VQA(image=RIGHT,question='Does the image show one black, white, and brown puppy sitting and facing the camera?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=RIGHT,question='Does the image show one black, white, and brown puppy sitting and facing the camera?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Does the image show one black, white, and brown puppy sitting and facing the camera?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="True")=<b><span style='color: green;'>True</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>True</span></b></div><hr>

Answer: True

