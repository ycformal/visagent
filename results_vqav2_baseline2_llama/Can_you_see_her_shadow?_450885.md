Question: Can you see her shadow?

Reference Answer: no

Image path: ./sampled_GQA/450885.jpg

Original program:

```
BOX0=LOC(image=IMAGE,object='woman')
IMAGE0=CROP_BELOW(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='shadow')
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Can you see her shadow?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCABDAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDibG8ksbhZ4rZbl8FREzEA59xzXY2PxK1nQLKCOHw9YRLKm4N5rFn+pz19q5nw5bQXmt2sNzII4d25pMZKgDOR78cViXN+NK1bULa0VrmLzGSK5lJSQLnnoTg+49/WnK1zkw3N7Pyuein4369JGyJp1mrkEK25jg9jjPNU9F+KOraQJZZbFLy8nYmW7uXYu3+yMcKo9BXB6bqsmkT/AG5XQyANHjPz/Mp+cDpwf51pXF1NrGkfboGeSK3AE7TyjeHPVQP4hwCDTehvZs9JtPjHr17MsFvo9m8jAkAuw6DJ5LYFc14i1C88R3H2i8N0VkVWVRlkTPJCZB4qOOwjtdGWOGecvPHCzuGA2k5JCEDIHOD/ALtUNaRv7VADIUWJMMzDJ4HX/PenbS4pO2glrYx2zGTyJJOwEqZA+gwKv3s0BUJHarGDGoYhMNnHUEHim/8ACM6h/Y9xqBFvHHF8zJNMiSFcZ3BSc/h1Paqt4y3lwojki3CNMgtjoDmiLfQiajF+8RSyksWBcHnu/wD8VUdlcyG/jEnmMN2MAt3+r4qqYHkgmZWi+RGc/OOn+NJp1rLFfLdM8QjjkBfEgzimrkSlC2heuZXeV2AkjDScKXPHPT/WipJlPkMGYHA/iYf1krNlhD3Nxcb4mjMjY+bn5jnP0qV0tXtpHR4QBleSARnv9Kepi5bJEptzJggRkYxn5P8AE0UWiWT24JurVCOCHYAmilYPavsWfB0MF14ltYLgM0UgdWCY3H5D0qv8QLa3i8SF4Lb7MZI9zpuzlgSC344BrBtdWv7SdZoZwsi9G8scfpT73V9Q1GZJru7eWRE2Bjwce/HJqX5GlGooQcZGbgNkH1rc0lJrWR7TzyLa9sTcHyhtaMh9vDeuAfwNZnmy/wDPV/8Avo1PDfXULxssznywQATngkEj6HFBoq8T0SPTZ5InWNgFVYypkJ6YPXjjrWRp3hmPWNTubi+uJVjEyriEcODwoLHhMkYyR2plz46H2PbBFMZiQR5uNqEdOn3sfhTPBV3qd1rNzBCZ7l7mPfKoOc7WDbj9P61EpTcWzSDpuoonY6loFrDZSpqdpOkCyBEKyA7WBBDA9SO3PvXAX1hE10YU0ZTIkx3SeZgyDsPbsa9W+IP2seA7hhgFZIhIQOQu7r+eK8W8+bvNJ/32a0jTjDRGGMqynJf8H/MvSWCSXMcaaEEdGKyKJc72+vtVe4to/tUJttH8pkzHJH5md7Hvn9KhFxN/z2l/Bz/jSGR2bJklB9nYf1qtDlUmuv5/5jpYfMmWOHRFidMxMvmZ3Nn379qbJbvJcpHHo6I6jymXf1YHnr37UheXORPN/wB/W/xpoaQNu86bOc58xuT+dFyuZf1/w5UvIzNdOBbQ2pjPltGOxHX8aKsyAu25nkJ7neeaKWpaqRKYRv8Anm34L/8AXp21h/Aw/wCAH/Guuj8Dj5Q7EeuSM/pVyHwHarwZZWPqQDXO68EdH1aXc4UkAc8fVSP60gcdmH+fxr0618FafbuZEdnlK7T5iqy4+mMVbHhjSz/rbZHP+zGi/wDstJ4mIvqz7nkrHP516N8HLi2i8U3QuJo42ktGSNXXlzuU4H4AmtL/AIRTSWfizQc5xx/hU8PhjT7e4WaG3WOVT8rJjI/Sl9aj0RUaDTWp3fiSGLU/D2r2CSRuJLV8FOfmA3D9QK+cA4IByf8Av21en6jJ5txa2gc72kMciKeCCKRvBmmEcQlf91jQsWnujXF4RxaszzHcPX/xw/4UoYev6GvSx4L070m/77NJ/wAITYdjcj/toar61DzON4aZ5ruHrRmvR28D2J6S3K/9tDUDeBbTPF3dD8Qf6UfWoC+rTPPifcfnRXfN4EgJ+W8uQP8AgP8AhRR9aph9Xmbqs/cgDvgVMNxIOf1qRYhwNzfiasRJg+p/OuCx6CTIkUD/ABzUiQqfb8atJbu56CrMdiCeXXPvVKI+UppCnc/gKW6sLmW1QWqbDK2wSnovqa10tEC+/tT2BaFYS58tTkLtXOfr1q1DuXHR3RzmmeHEj1Ga6kbzViOyLa2fqx9yfyrcFlEADtP0qVLaIcKSo6kDgZp/lRjJyTn0p8iWxUpOTvIjWwhIyWI/Cn/2fbqB+8OfalKADlv51G2zqQfwosibDjY22fvMPpUTabCx/wBYR+FPBjGQFY/WnAkDAxj3oTg+qCyK/wDZsY6OT+FFaEcLyIGVGI9hxRV+z8haHJRcls81pRABAQBn6UUVzxBFuFiVGf5VaTlOQPyoorWIxzHjGBj6UPxtAwM57UUUwGMxDYGOnoKcnzDJ9cUUUAPZFUkAcfWoZkVTwKKKoBmxSq/KOR6VcsLeKW5VXQEelFFVDcmWxBqF9dR3siJMyIpwFXgCiiiplJ3YJKx//9k=">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Can you see her shadow?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: No

