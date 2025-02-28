Question: a dog is in the snow staring at the camera

Reference Answer: False

Left image URL: https://i.pinimg.com/736x/48/e8/79/48e879ae2a83b967abf934c2e5c40419--collie-puppies-rough-collie.jpg

Right image URL: https://i.pinimg.com/736x/a3/2a/0b/a32a0b8e7b5acef965ee0900f848c7c2--my-favourite-rough-collie.jpg

Original program:

```
Solution:
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'a dog is in the snow staring at the camera' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'a dog is in the snow staring at the camera' true or false?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: False

