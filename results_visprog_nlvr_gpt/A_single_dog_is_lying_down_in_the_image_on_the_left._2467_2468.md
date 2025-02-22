Question: A single dog is lying down in the image on the left.

Reference Answer: True

Left image URL: http://www.warrenphotographic.co.uk/photography/bigs/20332-Tricolour-Cavalier-King-Charles-Spaniel-pup-white-background.jpg

Right image URL: https://www.warrenphotographic.co.uk/photography/bigs/37977-Tricolour-Cavalier-pup-white-background.jpg

Program:

```
ANSWER0=VQA(image=LEFT,question='How many dogs are lying down?')
ANSWER1=EVAL(expr='{ANSWER0} == 1')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='How many dogs are lying down?')=<b><span style='color: green;'>1</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0 == 1")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="1 == 1")=<b><span style='color: green;'>True</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>True</span></b></div><hr>

Answer: True

