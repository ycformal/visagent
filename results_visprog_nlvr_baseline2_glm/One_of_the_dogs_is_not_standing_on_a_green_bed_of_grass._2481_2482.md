Question: One of the dogs is not standing on a green bed of grass.

Reference Answer: False

Left image URL: http://elsto.weebly.com/uploads/7/3/8/9/7389672/2936358_orig.jpg

Right image URL: https://i.pinimg.com/236x/4a/a6/a7/4aa6a7b80763eada261ddb49d08241e2--afghans-afghan-hound.jpg

Original program:

```
The statement is False.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'One of the dogs is not standing on a green bed of grass.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'One of the dogs is not standing on a green bed of grass.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

