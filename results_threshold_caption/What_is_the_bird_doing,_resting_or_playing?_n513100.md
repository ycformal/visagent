Question: What is the bird doing, resting or playing?

Reference Answer: The bird is playing.

Image path: ./sampled_GQA/n513100.jpg

Program:

```
ANSWER0=VQA(image=IMAGE,question='What is the bird doing?')
ANSWER1=EVAL(expr="'resting' if {ANSWER0} == 'resting' else 'playing'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What is the bird doing?')=<b><span style='color: green;'>eating</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'resting' if ANSWER0 == 'resting' else 'playing'")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'resting' if 'eating' == 'resting' else 'playing'")=<b><span style='color: green;'>playing</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>playing</span></b></div><hr>

Answer: playing
