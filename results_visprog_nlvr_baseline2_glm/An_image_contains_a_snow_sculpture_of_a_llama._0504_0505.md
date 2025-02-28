Question: An image contains a snow sculpture of a llama.

Reference Answer: False

Left image URL: https://i.pinimg.com/736x/c1/e3/4b/c1e34b4bb3994f4b24811195a8e4c4c7--boring-life-llama-llama.jpg

Right image URL: https://i.pinimg.com/736x/45/42/cd/4542cdc7e2cac5050d9d7e5c88e25ec5--llama-llama-llamas.jpg

Original program:

```
Statement: An image shows one bare hand with the thumb on the right holding up a belly-first, head-up crab, with water in the background.
Program:
ANSWER0=VQA(image=LEFT,question='Does the image shows one bare hand with the thumb on the right holding a crab?')
ANSWER1=VQA(image=RIGHT,question='Does the image shows one bare hand with the thumb on the right holding a crab?')
ANSWER2=VQA(image=LEFT,question='Is the crab belly-first and head-ups?')
ANSWER3=VQA(image=RIGHT,question='Is the crab belly-first and head-ups?')
ANSWER4=VQA(image=LEFT,question='Is there water in the background?')
ANSWER5=VQA(image=RIGHT,question='Is there water in the background?')
ANSWER6=EVAL(expr='{ANSWER0} and {ANSWER2} and {ANSWER4}')
ANSWER7=EVAL(expr='{ANSWER1} and {ANSWER3} and {ANSWER5}')
ANSWER8=EVAL(expr='{ANSWER6} xor {ANSWER7}')
FINAL_ANSWER=RESULT(var=ANSWER8)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'An image contains a snow sculpture of a llama.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAApAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwBqSKRnZQZoc4KgVkPbvbSGOaMxuDyrDmppLaJApeJDuGfX/PGK6bnPY0hLbkdqYZLb1GfrWaywDH7iPk/3ake2VFDNajkZHyUXHYtMYuoP61Czp18z9az7i+htJ4IDFhpjtQAY5yB/XNSs6kDKAZ9RTuFi5cSAxrzUayiqWJ3A4OKsQW7u6CQMEJG4jqB3rN0pcvMDqa2RbEmehqZCCM03UdI+w6bZXcFw8/2hmBGzATHQfU81mrcSxnDI35VnQjKdTlYpycTXkUMnFRRzmB6jiuCy8o35VFcS8cKfyr05YJrYhVe5rDW9gC7qK5SWSQyHCt+VFYvCTNPaI9DtNAg02W4uDFA6eVhcpk5znnNU4ktTqgjuII5YnYKA46E10xKtEyOCQwwR7VzsVuyakn2iNvJRiVIXrjpk/X+VYTXvKxUdncs614e06Sx2pGLZi4w0SjPf1rJh0RtSuZoRfPGFTCgrkdMdsV0Oo3EdxbjaxBVt3IrL02VVvhMCVUAn5hjOamXxocdInm3jBo7TW7aKOXzGtGILDPJB9z7V2NhpM17pdtcp5MqyRhlfzGBP1965Dx3pxXxTNNbqzw3ZDoQONxxlfrn+dek+H4Y9M0K1sDMHeMfMR0yTkgfnThF8zuVNqysWo9Jtgi5QZwM8UXNnbWtq8pX2AA7npVoXMI/jFQ381vLp8y+YMhdy/Uc03N2sTZEtnai88PQCTBEUz4z1xTW0e1bqg/KnaQ7NaNABhUAbr/e5/pV4qRUwdthtGb/ZVuo4QUo0q2bqgq81Ipwa19tPuTyohGhWZHMa/lRV5X4orP2s+5VkGykMKnqKkFKa3sY3Kj2kbjBUVSOj24YsqY+h4rXNMalyod2Y76VCeqA/UU9LKNcgKB7AVfbpUX8Y+o/nVJCMb+3tDRirappwKnBBukB/nTx4h0Hbzq2mj/t6j/xr5rv/APkI3P8A11f+ZqvXHznRY+ol8SaEIzjWtNGf+nqP/Gj/AISXQ/8AoNad/wCBSf418u0Uc4WPqA+JND/6DWnf+BSf400eJNDz/wAhrTv/AAKT/GvmGijnCx9QjxNoeP8AkNad/wCBSf40V8vUUuYLH//Z">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'An image contains a snow sculpture of a llama.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

