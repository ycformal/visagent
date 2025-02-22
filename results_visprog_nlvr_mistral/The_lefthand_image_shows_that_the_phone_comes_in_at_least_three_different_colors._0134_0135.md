Question: The lefthand image shows that the phone comes in at least three different colors.

Reference Answer: False

Left image URL: http://s7d2.scene7.com/is/image/SamsungUS/Pdpkeyfeature-sm-g928rzkausc-600x600-C1-062016?$product-details-jpg$

Right image URL: https://images-na.ssl-images-amazon.com/images/I/51S5gBPBHsL._SL500_AC_SS350_.jpg

Program:

```
ANSWER0=VQA(image=LEFT,question='How many different colors does the phone come in?')
ANSWER1=EVAL(expr='{ANSWER0} >= 3')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='How many different colors does the phone come in?')=<b><span style='color: green;'>4</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0 >= 3")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="4 >= 3")=<b><span style='color: green;'>True</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>True</span></b></div><hr>

Answer: True

