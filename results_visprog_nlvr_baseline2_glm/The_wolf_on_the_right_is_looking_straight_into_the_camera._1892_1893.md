Question: The wolf on the right is looking straight into the camera.

Reference Answer: True

Left image URL: https://images.fineartamerica.com/images-medium-large-5/gray-wolf-resting-north-america-tim-fitzharris.jpg

Right image URL: http://images5.fanpop.com/image/photos/25400000/Wolf-Resting-On-Grass-elemental-wolves-25425605-300-383.jpg

Original program:

```
The statement is True.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'The wolf on the right is looking straight into the camera.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'The wolf on the right is looking straight into the camera.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

