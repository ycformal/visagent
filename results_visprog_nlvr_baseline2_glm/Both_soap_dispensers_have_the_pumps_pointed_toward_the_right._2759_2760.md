Question: Both soap dispensers have the pumps pointed toward the right.

Reference Answer: True

Left image URL: https://images-na.ssl-images-amazon.com/images/I/61IJDH-3rjL._SY355_.jpg

Right image URL: https://ae01.alicdn.com/kf/HTB1ZomCLpXXXXX5XFXXq6xXFXXXG/Antique-Brass-Crystal-Liquid-Soap-Dispenser-With-Silver-Finish-Europe-Frosted-Glass-Container-Bottle-Bathroom-Products.jpg

Original program:

```
Solution:
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'Both soap dispensers have the pumps pointed toward the right.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'Both soap dispensers have the pumps pointed toward the right.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

