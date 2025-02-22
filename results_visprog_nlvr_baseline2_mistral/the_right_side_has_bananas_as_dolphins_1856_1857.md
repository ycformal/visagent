Question: the right side has bananas as dolphins

Reference Answer: True

Left image URL: https://i.pinimg.com/736x/e5/2b/44/e52b446f6a02d62709601eea26944f3e--banana-art-vegetable-carving.jpg

Right image URL: http://1.bp.blogspot.com/-j8BL9SohSm4/VhcESy954HI/AAAAAAAACHI/ty_oDq5sDBY/s1600/DSC01595_2.jpg

Original program:

```
ANSWER0=VQA(image=RIGHT,question='Are there bananas as dolphins?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=RIGHT,question='Are there bananas as dolphins?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Are there bananas as dolphins?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="True")=<b><span style='color: green;'>True</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>True</span></b></div><hr>

Answer: True

