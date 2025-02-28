Question: Each image contains a single dog, and the right image shows a basset hound facing forward with an open mouth showing its tongue.

Reference Answer: True

Left image URL: https://s-media-cache-ak0.pinimg.com/736x/0f/75/83/0f7583a000da5d01d232ca7c3da58ef6.jpg

Right image URL: https://i.pinimg.com/736x/8e/ce/ae/8eceaecfd4ec198c143dacbc89289380--fat-puppies-basset-puppies.jpg

Original program:

```
The statement is True.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'Each image contains a single dog, and the right image shows a basset hound facing forward with an open mouth showing its tongue.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'Each image contains a single dog, and the right image shows a basset hound facing forward with an open mouth showing its tongue.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

