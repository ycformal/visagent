Question: How is the weather?

Reference Answer: It is cloudless.

Image path: ./sampled_GQA/2375358.jpg

Program:

```
ANSWER0=VQA(image=IMAGE,question='How is the weather?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='How is the weather?')=<b><span style='color: green;'>sunny</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>sunny</span></b></div><hr>

Answer: sunny

