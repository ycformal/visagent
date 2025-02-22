Question: The right image shows a woman with a gold-topped hypodermic needle in front of her.

Reference Answer: True

Left image URL: https://st2.depositphotos.com/1518767/7635/i/450/depositphotos_76352059-stock-photo-doctor-preparing-syringe.jpg

Right image URL: https://st.depositphotos.com/2249091/4964/v/450/depositphotos_49646305-stock-video-doctor-preparing-syringe-to-inject.jpg

Original program:

```
ANSWER0=VQA(image=RIGHT,question='Does the image show a woman with a gold-topped hypodermic needle in front of her?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=RIGHT,question='Does the image show a woman with a gold-topped hypodermic needle in front of her?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Does the image show a woman with a gold-topped hypodermic needle in front of her?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="True")=<b><span style='color: green;'>True</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>True</span></b></div><hr>

Answer: True

