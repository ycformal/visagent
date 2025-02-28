Question: An image shows a store display with upright bottles on open-fronted wooden shelves divided into rectangular compartments.

Reference Answer: True

Left image URL: https://archive.sltrib.com/images/2016/0810/dabc_westvalleystore_081116~1.jpg

Right image URL: http://www.wlevradio.com/wp-content/uploads/sites/500/2016/06/beer.jpg

Original program:

```
Statement: An image shows a store display with upright bottles on open-fronted wooden shelves divided into rectangular compartments.
Program:
ANSWER0=VQA(image=LEFT,question='Does the image show a store display with upright bottles on open-fronted wooden shelves divided into rectangular compartments?')
ANSWER1=VQA(image=RIGHT,question='Does the image show a store display with upright bottles on open-fronted wooden shelves divided into rectangular compartments?')
ANSWER2=EVAL(expr='{ANSWER0} and {ANSWER1}')
FINAL_ANSWER=RESULT(var=ANSWER2)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'An image shows a store display with upright bottles on open-fronted wooden shelves divided into rectangular compartments.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'An image shows a store display with upright bottles on open-fronted wooden shelves divided into rectangular compartments.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

