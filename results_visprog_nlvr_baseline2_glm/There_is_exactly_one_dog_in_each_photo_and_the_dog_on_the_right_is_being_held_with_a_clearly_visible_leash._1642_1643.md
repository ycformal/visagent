Question: There is exactly one dog in each photo and the dog on the right is being held with a clearly visible leash.

Reference Answer: True

Left image URL: https://i.pinimg.com/736x/ed/3c/f6/ed3cf68f95b0e25ce78b171e922fe390--red-doberman-pinscher-german-dogs.jpg

Right image URL: http://www.dogwallpapers.net/wallpapers/doberman-pinscher-side-view-photo.jpg

Original program:

```
The program is not provided for this statement.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'There is exactly one dog in each photo and the dog on the right is being held with a clearly visible leash.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'There is exactly one dog in each photo and the dog on the right is being held with a clearly visible leash.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

