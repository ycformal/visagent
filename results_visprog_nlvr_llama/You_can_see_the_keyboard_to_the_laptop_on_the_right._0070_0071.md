Question: You can see the keyboard to the laptop on the right.

Reference Answer: True

Left image URL: https://www.kv.by/sites/default/files/user535/asus_taichi_31.jpg

Right image URL: http://insmart.cz/wp-content/uploads/2017/05/hp-laptop.jpg

Program:

```
ANSWER0=VQA(image=RIGHT,question='Can you see the keyboard to the laptop?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Can you see the keyboard to the laptop?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="True")=<b><span style='color: green;'>True</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>True</span></b></div><hr>

Answer: True

