Question: Are the floor and the cupboard made of the same material?

Reference Answer: Yes, both the floor and the cupboard are made of wood.

Image path: ./sampled_GQA/2377561.jpg

Program:

```
ANSWER0=VQA(image=IMAGE,question='What material is the floor made of?')
ANSWER1=VQA(image=IMAGE,question='What material is the cupboard made of?')
ANSWER2=EVAL(expr="'yes' if {ANSWER0} == {ANSWER1} else 'no'")
FINAL_RESULT=RESULT(var=ANSWER2)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What material is the floor made of?')=<b><span style='color: green;'>wood</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What material is the cupboard made of?')=<b><span style='color: green;'>wood</span></b></div><hr><div><b><span style='color: blue;'>ANSWER2</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if ANSWER0 == ANSWER1 else 'no'")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if 'wood' == 'wood' else 'no'")=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER2</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: yes
