Question: Each image contains one empty bottle with a pump dispenser, and each image features a dispenser nozzle turned leftward.

Reference Answer: True

Left image URL: http://cdn8.bigcommerce.com/s-i17pk3h6/products/226/images/1219/bell-glass-soap-dispenser-antique-bronze-metal-well-pump-rail19-19__98138.1479316879.800.800.jpg?c=2

Right image URL: https://img.etsystatic.com/il/3fc78a/761172121/il_570xN.761172121_i92j.jpg?version=1

Original program:

```
The provided program does not contain any statement or question related to the given statement. Therefore, it is not possible to determine if the statement is true or false based on the given program.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is "{statement.replace('(','').replace(')','')}" true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is ')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

