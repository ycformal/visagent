Question: Is there any short grass in the picture?

Reference Answer: Yes, there is short grass.

Image path: ./sampled_GQA/n98540.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='grass')
ANSWER0=VQA(image=IMAGE,question='Is there any short grass in the picture?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>BOX0</span></b>=<b><span style='color: red;'>LOC</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCABkAFADASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDgv7Q1zU7OWWOSVreEDzDGoVVB+la+j2+panbF31JkSOaONVVRnJ78eladp4Z1Czikg+3RR2753BWIJPv26VHDobabco0WpxhWkXKpyR6H8KVrA5t9R2reD9TaykmXWZHZBkK5Kg+2c1R0bwffSQGae8WOSTPlsjCRWA6/ka1/E1ndXvh2aGHULmeVGV9gjIDYPPIH4/hXMeH9TXR5LS2DO+6YF5JGwse4gMVHrjua0j7NrUm1R7GxP4MuIWE0syT5IXIj+7nvSW3g+6uUnhiliHkSlGYqcnv+ArvczXVu628JkzwG3DFRWmn6nam5dBAhmlMmGye3tWbkloPkb1OOXwXqFs4eOWHeBjaNwH51VOj366gltPIolcfKFc4HtmvQBp+sSn5r+GPP9yHP8zT08Mhrj7RcXsss2MBtirge3FS6kRqlI4t/CM0oO+dUb+8XJxj2xUdjo8WleItNf7Wtw8k4B6fKe1d7JoFmeJGlkB4wZOP0pLfw/pFu5ZLGEHudtL2qKVFk8elacvS2i9csuf51OE0+3AH7hP8AvkV5891cSj95I7D0LEg1XZjjqOK522Htktkdj4n1gWegXT6dmS4b91G0SlgrHuT0GBk14jbYe8jEsm1Q2WJBbpzzjmu8tteutDklunjluLVASYBJhHzx8ynqP85ri9J1KNvEzXbxIoIeQxtwqn/DmuzDuny3l0FNt7M7zwff6xqEZu7KJJ5Y5PLnnHyIRnIDdiSCOvI611V54nhW2t54UWVZlJwH5Rh1VuOo9q8/j8bf2fq9xc6TFEv2mPbLFjEIZR8rgDqRz+dXvD+n3B06+s70SLdWyC6gVgRvicbiQD2PUH2qsTWVSPNJa6W/4IoRlHSLOhPiq5IzHDGvr3qJvE+oFfv4P+yoFYYcDvTGkycAc15/MT7ST6mqddvpODJJ7/PULajcE/M5PHUsTVFQ55Cj8aHDEEtj6UcxLkyXKpxnPvTWdGPyr+tSeQDgYUe5pogBb7w/Ci4iOWJZYnjdCVdSp+hrzbVtOk03UJIWJKkAq3qteoiBD2PTrVW50y2u2ZbmCJgF/dSj76k9a2oz5XqUlqeeadFL9ogDW7yRyHAXkZHr9K9K0q/FnPG15NK0UMDQ7sj5UI6Ek8AcY/8Ar1TjtI7WNI1LYj4G45P51m3Wl3OqakZFnZbQAb0bpvxztH5c11yacOVlJtSujZRkkDmLcYw5VSR94A9aXZknJPHqK9Cs9LsvE3hK1t7ZoY9Qs02queW9VbPJz1z61yE1tFbSPFcOyyIxVkKkEH0NcNSnyslozlGD0JoYZONtWnaP7sbAjryOajyMYLDPbio5WKw/crciM4HGQaUAKMt6dM1UQ4bjn8ak8wsDgqoHIosMkMqrzkAmoy4c42Nz0Pao5JPkzu61Pb2t5dY8q1kYE8NjAotYEm9iGdCyE7Tkeo61d0O0F7a30CY89I/Pj56leo/EH9KtxeHbp2Bu5lUf3UOT/hVNX/4RvW0mz90kpuYKGHqfb1ropTT91mkqcuW7G219JZyrdQF1kiO7cDjp3J9Ktz+KNG8T6tDGzn+0nXFw648p2H3Qv4VvWF5aatYi9tlTyZy2VVAATkgjHpXnPifwNLor/wBr6I0hijbzHgHLRDOcqe6+3UVdOcW3TqlOk0lNancrpVsoH7hSfcmriWUMCApAmfVV6VT8P6imuaPBeRMSxGJFHOGHWtUQy8YVsdgBXNOEoScX0OqCha6OYg8OahKq+YyQjuM5P6Vch8LW0YBmmklb/Z+UV0Lbl4UGmgSM4/dsRntUEqjBdDPttFsbVspbpkf3uf51oDA5IOPY1cjtnIHygY9abcC0tRm4lVPYnaP1quVlXitioHLDJGMdOayvEnhqDxJpYtziO5jy1vLj7reh/wBk960X13R7blEaZh/zz5/U8Vn3fiwM3+i2caHuzncfyGBTXuu9zOVWFrM5nwFfSaVd3fh3VQLW4jffGJTgZPUA+/BBr0Jkt7c5uLmNABzuYCvJfG091ftb6puP2i2+VmUAfJ1HA9/51c0/VY9Ys1vVkJckLKv9xvStajjJc636mMarirIq+ITeaDrU8Xhy8Z9JupRN5MQwqydxnGcenOMHFdDpXivWk08LfiJ52OQecr7H1qixCg/MOarkc8PWUqza1M+ZrVHpN3r+j2zHzLmJiOy81g3fj6yj3LbiAHs0kg/kK4q701b2ctPKfK/hRFwfxNJHplhAwK2seQP4hk/rQ5JFSqyZtXXju4nyo1CONTxiJdtZUutwTZeW4eQ/3irH9cUoggz8kEePZBUwT5MbMLjHFZuSIbb3Kqa7ZFSPMZ/XKkfqamS8jk5idfp5g/xqJLO3hcvFbRoT3xTwiseUUH1xSunsIc0gkVkZVdWGGG8YINZ2naVb6Rc3EkV0wilAHlMRhccjn861lRDjC5P0FDxJg52+pyAaaUtrgMjmilb5ZFYd9pBqXywBncvt2qssMMcm8QICO6qM1OSzZwDj1IpcqAM4VuBwKAA/LcmiikSKkYz1I+lOi+aQA9qKKFuAlw5zgYHHYVEjMX6ng44oorRlEjSFWAwp46kUqyEsRgDiiigEIoLDJZunrTHHBBJPOOT7miipA//Z">, <b><span style='color: darkorange;'>object</span></b>='grass')=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is there any short grass in the picture?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: Yes.
