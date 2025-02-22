Question: There is one stand that is both glass top and wider than the TV it is holding.

Reference Answer: True

Left image URL: https://i5.walmartimages.com/asr/d35d63d6-79d4-4a84-933d-542e649b9002_1.6936c5f7e4007232a99897780eedfdac.jpeg?odnHeight=450&odnWidth=450&odnBg=FFFFFF

Right image URL: https://i5.walmartimages.com/asr/03e57ef1-aa63-48c8-897d-7ccbcd93fa6d_1.9f4a55e68648c660cb2fd7d955d8382d.jpeg?odnHeight=450&odnWidth=450&odnBg=FFFFFF

Original program:

```
The program provided does not contain a statement or a corresponding program to evaluate the statement.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is "{statement.replace('(','').replace(')','')}" true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is ')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

