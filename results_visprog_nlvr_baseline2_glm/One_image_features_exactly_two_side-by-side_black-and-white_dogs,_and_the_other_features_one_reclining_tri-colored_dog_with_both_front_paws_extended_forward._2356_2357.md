Question: One image features exactly two side-by-side black-and-white dogs, and the other features one reclining tri-colored dog with both front paws extended forward.

Reference Answer: True

Left image URL: https://s3.amazonaws.com/pet-uploads.adoptapet.com/3/9/b/84923231.jpg

Right image URL: https://i.pinimg.com/236x/88/29/c0/8829c0d192d0d8d2ab789e3d249fac2e--black-tri-australian-shepherd-miniature-australian-shepherds.jpg

Original program:

```
Statement: One image features exactly two side-by-side black-and-white dogs, and the other features one reclining tri-colored dog with both front paws extended forward.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'One image features exactly two side-by-side black-and-white dogs, and the other features one reclining tri-colored dog with both front paws extended forward.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'One image features exactly two side-by-side black-and-white dogs, and the other features one reclining tri-colored dog with both front paws extended forward.' true or false?')=<b><span style='color: green;'>same</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>same</span></b></div><hr>

Answer: same

