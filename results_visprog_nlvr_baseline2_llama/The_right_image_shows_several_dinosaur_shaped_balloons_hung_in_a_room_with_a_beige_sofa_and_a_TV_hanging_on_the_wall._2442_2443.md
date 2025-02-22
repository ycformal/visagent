Question: The right image shows several dinosaur shaped balloons hung in a room with a beige sofa and a TV hanging on the wall.

Reference Answer: False

Left image URL: https://78.media.tumblr.com/3bc35f6ff2bb8d1d391857cd83838ce1/tumblr_p4b28lKXwG1swr6ulo1_500.jpg

Right image URL: http://media.tumblr.com/tumblr_m55mipcVP21qk7849.jpg

Original program:

```
ANSWER0=VQA(image=RIGHT,question='Does the image show several dinosaur shaped balloons hung in a room with a beige sofa and a TV hanging on the wall?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=RIGHT,question='Does the image show several dinosaur shaped balloons hung in a room with a beige sofa and a TV hanging on the wall?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Does the image show several dinosaur shaped balloons hung in a room with a beige sofa and a TV hanging on the wall?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="False")=<b><span style='color: green;'>False</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>False</span></b></div><hr>

Answer: False

