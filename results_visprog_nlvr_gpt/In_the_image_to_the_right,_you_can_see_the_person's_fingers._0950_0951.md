Question: In the image to the right, you can see the person's fingers.

Reference Answer: False

Left image URL: https://media-cdn.tripadvisor.com/media/photo-s/07/b5/7e/8e/seaworld-orlando.jpg

Right image URL: https://media-cdn.tripadvisor.com/media/photo-s/02/79/5e/89/filename-sea-world-1.jpg

Program:

```
ANSWER0=VQA(image=RIGHT,question='Can you see the person's fingers in the image?')
FINAL_ANSWER=RESULT(var=ANSWER0)
```
Answer: Runtime error: '?'

