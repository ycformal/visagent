Question: There are people in the right image.

Reference Answer: False

Left image URL: https://i.pinimg.com/236x/00/46/f5/0046f510a99d98a87b1f79086bd28419--barbershop-ideas-barber-shop.jpg

Right image URL: https://i.pinimg.com/736x/be/29/58/be2958e3795bab37e025c178756d72bb--barber-shop-interior-shop-interior-design.jpg

Original program:

```
ANSWER0=VQA(image=RIGHT,question='Are there people in the image?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=RIGHT,question='Are there people in the image?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Are there people in the image?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="False")=<b><span style='color: green;'>False</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>False</span></b></div><hr>

Answer: False

