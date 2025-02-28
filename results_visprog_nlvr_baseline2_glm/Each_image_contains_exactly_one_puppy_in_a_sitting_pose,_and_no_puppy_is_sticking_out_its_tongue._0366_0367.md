Question: Each image contains exactly one puppy in a sitting pose, and no puppy is sticking out its tongue.

Reference Answer: True

Left image URL: https://www.pupcdn.com/photo/puppy/523025/59e9476ea1b16-3915695.jpg

Right image URL: https://www.pupcdn.com/photo/puppy/526056/59ee46c3bdc90-3917815.jpg

Original program:

```
The program is not provided for this statement.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'Each image contains exactly one puppy in a sitting pose, and no puppy is sticking out its tongue.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'Each image contains exactly one puppy in a sitting pose, and no puppy is sticking out its tongue.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

