Question: You can see the tongue hanging out of the mouth of the dog on the left.

Reference Answer: False

Left image URL: https://i.pinimg.com/736x/1a/5e/12/1a5e12c311137000b21849839464f16d--italian-greyhound-greek-yogurt.jpg

Right image URL: https://i.pinimg.com/736x/0b/43/33/0b43339f607ec409a0889028258fdc33--italian-greyhound-rescue-my-style.jpg

Program:

```
ANSWER0=VQA(image=LEFT,question='Can you see the tongue hanging out of the mouth of the dog?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Can you see the tongue hanging out of the mouth of the dog?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="True")=<b><span style='color: green;'>True</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>True</span></b></div><hr>

Answer: True

