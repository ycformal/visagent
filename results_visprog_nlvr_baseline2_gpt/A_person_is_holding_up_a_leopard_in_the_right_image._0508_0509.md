Question: A person is holding up a leopard in the right image.

Reference Answer: True

Left image URL: https://i.pinimg.com/736x/6f/a1/e9/6fa1e9930ce7e17f752e23a49eacd089--cheetahs-leopards.jpg

Right image URL: https://www.africahunting.com/hunting-pictures-videos/watermark.php?file=3080

Original program:

```
ANSWER0=VQA(image=RIGHT,question='Is a person holding up a leopard?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=RIGHT,question='Is a person holding up a leopard?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is a person holding up a leopard?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="True")=<b><span style='color: green;'>True</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>True</span></b></div><hr>

Answer: True

