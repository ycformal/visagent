Question: There are 3 phones on the left and two phones on the right.

Reference Answer: True

Left image URL: https://i.ebayimg.com/images/g/3VwAAOSwYHxWGB9q/s-l300.jpg

Right image URL: http://s7d2.scene7.com/is/image/SamsungUS/Pdpkeyfeature-sm-g920rzkausc-600x600-C1-062016?$product-details-jpg$

Original program:

```
Statement: There are 3 phones on the left and two phones on the right.
Program:
ANSWER0=VQA(image=LEFT,question='How many phones are in the image?')
ANSWER1=VQA(image=RIGHT,question='How many phones are in the image?')
ANSWER2=EVAL(expr='{ANSWER0} == 3 and {ANSWER1} == 2')
FINAL_ANSWER=RESULT(var=ANSWER2)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'There are 3 phones on the left and two phones on the right.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'There are 3 phones on the left and two phones on the right.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

