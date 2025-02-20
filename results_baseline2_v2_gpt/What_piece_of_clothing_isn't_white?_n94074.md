Question: What piece of clothing isn't white?

Reference Answer: suit

Image path: ./sampled_GQA/n94074.jpg

Original program:

```
ANSWER0=VQA(image=IMAGE,question='What color is the piece of clothing?')
ANSWER1=EVAL(expr="'shirt' if {ANSWER0} == 'white' else 'pants'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question='What color is the piece of clothing?')
ANSWER1=EVAL(expr="'shirt' if {ANSWER0} == 'white' else 'pants'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What color is the piece of clothing?')=<b><span style='color: green;'>white</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'shirt' if ANSWER0 == 'white' else 'pants'")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'shirt' if 'white' == 'white' else 'pants'")=<b><span style='color: green;'>shirt</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>shirt</span></b></div><hr>

Answer: shirt

