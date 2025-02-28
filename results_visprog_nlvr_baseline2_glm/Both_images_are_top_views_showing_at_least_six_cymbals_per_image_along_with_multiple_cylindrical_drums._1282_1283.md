Question: Both images are top views showing at least six cymbals per image along with multiple cylindrical drums.

Reference Answer: True

Left image URL: https://i.pinimg.com/736x/db/06/7b/db067b3bf79988a24bc3862ca32b9e01--double-bass-drums.jpg

Right image URL: https://s-media-cache-ak0.pinimg.com/originals/ae/10/f2/ae10f2189197b07633a46c61642e1ebc.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'Both images are top views showing at least six cymbals per image along with multiple cylindrical drums.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAAmAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDzF7mUX6y3LYyzYZuuanNyjRcSRq3QFumf6VrJptzq+qWlpZCG4undgo3gbTt6c8etVb/w5cWNwbCexMV4gO5fvZ4yDx2x3BpSd2WkkjL/ALQmikMbOFx3Bz+RrqPD2pSWMtrexXsMB83hlQlgR3x+P41nrpCbIjtjjdgjorDIfj1zxW5aRvaQW062WmE/dLlmLxZHdQAeOeeam47Fee/+2Xxm1C5n2SSFna32yMBnk7CRWn4h8Oponh631G2mcyX0g+zRuNjlfUr2OOvPGRUkqX39nwpaxW8Vxkhp23LyTkj5xgjHPAwc1F4k1RdevxDDKRBCAvByASSDgE4yTnp2qXJvUaSvY82u13+IjJqMMuwlfN2th+g5Fdxp+m6dd6Qmp27RQQWjh3e7kOWUHBXJ4ZmHYDjHet3StA0t0eZ9PW/u3YKvnSbY0UDHTB5475qv4w0bTLGwitC9tHfTcxxxfKMDrx6e5qJ+9qVG60OY8Q3Mf+mSWkJFvNGRkeYH25GAzD5SOOn1zisiPxTrjRuftiwJFEUDwxKjuvA6gdMdx616IfBOvax4Ta4W2V/kDRL521pBtwSEGB2GM81l+FvhKniDwkms6hqjwyTozQQxxA7QCRlvfIPAp04pRtIKkm3dHBa7r9xrktvJdTSsqtgyPKzfkGyR+vPSurufDdxcWtpqF1dx3cM0YaJ7ciRSvt0OR3BHWtvTNBstOEcCwRtEgOX2gszdM5x69qZqdpAJIGgjfbCrcABRk9cY5H4HB9K002RKT6nDt4bEjEy365HC7QOn4kd80V6JFp+YUJNvgqCMoQcfiKKXMyuRHBaKuo29iJ8fZ0fDQTMCGJ7Fcc475/nV29bWbu5jnvprie4ZQ0cjgybhggEH0IB/Ws3RtXubNzZXMK3llEflidirKCeit1A9R0+h5rbtr3Xp57wwKpkm5cqMhRjGEHbC9B7VU5JbmcU2tDX8KX/hG5Mya6JYJNi7XjjwjnPVdoypxj60s+t6Q2rTRWEE8UIYrFKzEZQ+oBznP4Vx8cUemX0n22QtMyYRQpbvjPbHT9a6Cy01RrEV1ZTFl8v5ARtPPqDxk9KUpKIlG7Nuz1ANpf2S6t5tatrScSxiW5YQ4x90oSBge3vU2oTaVaQnVXS2t7tphKywgKi8cKqf1/Wsd4VAnlmnkgn5LJx+Yz2GcVDY3GmjTJTc2MDtblmjYpktx3Pc5PeknFr1HZr5GFPfa3NcSajb3k8EMrk5VjlieeB0JxUCx3Go6jbXdyJooEcNPcTsWOV+8eep9hUiaxdWETQ2imDfIF3ZwoB5I56gEZ4H+FXfD2qNdeM4dV1BJ5tGs7nzXZo/3cBYYXA7DODjqcZ7VWwbnbW/xG8R6LoUdpJoFw9uo8q31KdHVQP4Sw744GcjNcvpeo+K7RYNNsdauWk1NxsWWDCxMzHflj93gE/L6ivXtU8V6DZ6NLJcX1tcwzRlEjicSGUsMAADnkmvEb7xPd3yRqsEkIjYMsu/Jyp7Ee4qYu/QbVjrb7wRrGm6dcT2Os3SSrEWKr/q3wOuDnB96p2uqyfaIomVJAQqDeQu5gOSD3Jq34R1DVPGd1Pp+vaxLLYRxBnhQCJpjuwAzLzj1rpdW8CWENr9t0dHhubUGSNC5dGx1GGzg470m+jKiYP/AAmdogCtYkYyBvcDOCRxx0yDRXnk+hTefIFmZgGP3s8Z5/rRTtA0946DwxZ6Tqtrd3LpMLlGGQyAoVOcY5yDwc/Wui0/TBbMs8U8hQ8GNzkc/qKKK5Jv3mhI5nxXZj+0f7TRFbOFdGYj7vHGPwrb0yxNxCk91JiU/KiRD5I1XPHPJ5JJPvRRWrk/ZpGdlzXMbWrCaW4tXW4PkzSfKjdVPAx9KpajbtE1voyyfPJJ5gbaNozwAfX34ooohq0VJ2Ri2GlPcyG+uZFKJKqbU6sSM9e315q1HqUl0HiBMPlgqoj4TceN23pu9T1NFFdHUzJrSARosmAJEbhgPUdvSrMlun2VQuQQ7Ak9+hoopFx6j9IurzSL5L3T5VS4jBxvBKsD1DDuK3r/AOKWq3umXNiLS2tJmjIeWEs2VwcgZxtJ6Z5xmiii12GyPPB4jutq+RHGqgc7yWJNFFFVyoz5mf/Z">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'Both images are top views showing at least six cymbals per image along with multiple cylindrical drums.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

