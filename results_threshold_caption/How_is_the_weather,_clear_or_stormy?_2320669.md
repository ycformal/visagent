Question: How is the weather, clear or stormy?

Reference Answer: It is stormy.

Image path: ./sampled_GQA/2320669.jpg

Program:

```
ANSWER0=VQA(image=IMAGE,question='How is the weather?')
ANSWER1=EVAL(expr="'clear' if {ANSWER0} == 'clear' else 'stormy'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='How is the weather?')=<b><span style='color: green;'>cloudy</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'clear' if ANSWER0 == 'clear' else 'stormy'")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'clear' if 'cloudy' == 'clear' else 'stormy'")=<b><span style='color: green;'>stormy</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>stormy</span></b></div><hr>

Answer: stormy

