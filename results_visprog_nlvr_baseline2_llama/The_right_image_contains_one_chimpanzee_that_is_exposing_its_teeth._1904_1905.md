Question: The right image contains one chimpanzee that is exposing its teeth.

Reference Answer: True

Left image URL: http://mmafitnessclub.weebly.com/uploads/1/8/2/2/1822368/gorilla-teeth.jpg

Right image URL: https://listverse.com/wp-content/uploads/2017/03/feature-6a-angry-chimp-122203715.jpg

Original program:

```
ANSWER0=VQA(image=RIGHT,question='Does the image contain one chimpanzee that is exposing its teeth?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=RIGHT,question='Does the image contain one chimpanzee that is exposing its teeth?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Does the image contain one chimpanzee that is exposing its teeth?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="True")=<b><span style='color: green;'>True</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>True</span></b></div><hr>

Answer: True

