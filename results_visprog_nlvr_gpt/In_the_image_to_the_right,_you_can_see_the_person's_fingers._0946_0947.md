Question: In the image to the right, you can see the person's fingers.

Reference Answer: True

Left image URL: https://i.ytimg.com/vi/EyVXlVFA_-I/hqdefault.jpg

Right image URL: https://s-media-cache-ak0.pinimg.com/originals/2a/b4/11/2ab411151cb378fa17b76d8b1bf9bccb.jpg

Program:

```
ANSWER0=VQA(image=RIGHT,question='Can you see the person's fingers in the image?')
FINAL_ANSWER=RESULT(var=ANSWER0)
```
Answer: Runtime error: '?'

