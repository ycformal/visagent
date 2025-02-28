Question: There are only women in the left image.

Reference Answer: True

Left image URL: https://marketplace.canva.com/MAA8BQVtJZM/1/screen/canva-group-of-smiling-people-working-out-with-dumbbells-MAA8BQVtJZM.jpg

Right image URL: https://st2.depositphotos.com/1046535/7980/i/950/depositphotos_79806238-stock-photo-fitness-people-in-gym-working.jpg

Original program:

```
ANSWER0=VQA(image=LEFT,question='Are there only women in the image?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=LEFT,question='Are there only women in the image?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Are there only women in the image?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="True")=<b><span style='color: green;'>True</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>True</span></b></div><hr>

Answer: True

