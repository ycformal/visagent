Question: Which animal is seen most in this picture?

Reference Answer: giraffe

Image path: ./sampled_GQA/434735.jpg

Program:

```
ANSWER0=VQA(image=IMAGE,question='Which animal is seen most in this picture?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Which animal is seen most in this picture?')=<b><span style='color: green;'>giraffe</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>giraffe</span></b></div><hr>

Answer: giraffe

