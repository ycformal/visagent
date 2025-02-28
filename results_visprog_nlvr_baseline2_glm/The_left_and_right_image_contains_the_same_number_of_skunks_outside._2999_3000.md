Question: The left and right image contains the same number of skunks outside.

Reference Answer: True

Left image URL: https://i.pinimg.com/736x/de/4f/61/de4f61d27aec16071f35fef9267a9a38--baby-skunks-animal-babies.jpg

Right image URL: https://i.pinimg.com/736x/7c/33/83/7c33839c877cb4f60d0724f745d40629--kundalini-after-dark.jpg

Original program:

```
Statement: The left and right image contains the same number of skunks outside.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'The left and right image contains the same number of skunks outside.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'The left and right image contains the same number of skunks outside.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

