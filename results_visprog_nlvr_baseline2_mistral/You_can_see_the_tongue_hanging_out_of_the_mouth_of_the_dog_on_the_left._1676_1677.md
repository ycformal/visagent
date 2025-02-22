Question: You can see the tongue hanging out of the mouth of the dog on the left.

Reference Answer: True

Left image URL: https://i.pinimg.com/736x/68/0c/b4/680cb436e4d04735372bc0cea9fa8b8f--italian-greyhound-frappucino.jpg

Right image URL: https://i.pinimg.com/236x/88/f6/a7/88f6a74f1819b663b47d6fe97003e011--italian-greyhound-whippet-dog.jpg

Original program:

```
ANSWER0=VQA(image=LEFT,question='Can you see the tongue hanging out of the mouth of the dog?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=LEFT,question='Can you see the tongue hanging out of the mouth of the dog?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Can you see the tongue hanging out of the mouth of the dog?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="True")=<b><span style='color: green;'>True</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>True</span></b></div><hr>

Answer: True

