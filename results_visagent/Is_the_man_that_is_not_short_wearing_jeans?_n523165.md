Question: Is the man that is not short wearing jeans?

Reference Answer: No, the man is wearing shoes.

Image path: ./sampled_GQA/n523165.jpg

Program:

```
 Is A <attr> B?
Program:
BOX0=LOC(image=IMAGE,object='man')
IMAGE0=CROP(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='Is the man wearing jeans?')
ANSWER1=EVAL(expr="'yes' if {ANSWER0} else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>BOX0</span></b>=<b><span style='color: red;'>LOC</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>object</span></b>='man')=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>IMAGE0</span></b>=<b><span style='color: red;'>CROP</span></b>(<b><span style='color: darkorange;'>bbox</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">)=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCABkACMDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDmbzWgVCRSIG9D3rPbUCzsCdrH0PB/CsWWOYBZhE4jfOGIwD2ODWta2sN1YpFax+ZfbWZsn06DBqp1HuwhST0RLJrkkEBQYKN0HfNLYa06FTnCn73uarT6PdIitNDKkhJxGFHzDGeD3I9KqfYbmO3NwY2WEcs3936jrSVVvVahKmo6M6gavckAokbL2OetFc7EkzRKyqSCMggZoro/edmY+53Ea3u7mzhEamWJiyxgMfkz8xG08jpS29+Pt4jVWSSLlHUY3EdcGtZoJTO7CRNrLtyMhuDkHPrUViqRGUfbbW4e5XesUSMAgycgkjhs88dcVxp82rO1tRi4x6if8JJDGrR6mGRc7lBy2COmD61V8hFvBcRo8VrcJ5jJIrEyHn5iT9aSa7jW6nhtQqwM2WXaDg98Zzxn+dNu9QLS2vlRKHwVf5uH9Dj19qIWvZGkqTjBVJbEkb2VpGsEtneO6jlkyqt3yAOKKiS+t4UEbebkdcE4/mKK39pPuc/sqXZfeaGpW+u6Vqax3VqEtnLBJBhlcDvkcg+xqu7afb2sbC9+z3O1oyHQkc9+KfJ4gfW3Ek8m+ZRgIBgKue2Ky9Wi8y3RCrhQ+Tk+xrnlZPRFU220iays7Mu7SapHgjjC9/xqv5XnMD94JlwR3rOisohIrctg8L1Fa1pwGwDt6DIzilFpO6Oyvz+xtIybi+WO4dTaB8H728jNFOurNWuZCIzyfQ0Vv7RHm8jNsFM/dUHpkKAaW202LULyC2DPEHcAsrn+vFNcE88/TFavh63J1NXZXZUUsSRn2rCOrKu1qjfj8HaVACssUrRgBg3nkHPfOK5fUIrCLUHSyUJBG2B+8JLeuT3rsNVASxmksXAdYiGVVAAGPXufQV56xftuIx3FXOyG6s2rNsvNLEWJ8qP8P/r0VVA4/wBUf0orPmEOLRtwUDfiatWupXNiXFuV2twRINw/CsRNSQECWNgw64/wq3Dci4ZY4RvduAo6k+lOzQXOh03W5bu1ubBxGr4IxGuAQawiWUkHI+q5qbT7G6XxILcxNDM2CQ6nhfX6GtDXtHn0i43uweOVjyn8J64NDTepTtyruZWD6p+VFN3+oX86KmxF2QTWscgGULkd8kE1o6PqZ0U5t9Ps2kwR55BMoz71Et0mR/otuR6bT/jUv2xC3/HvbKOw8oMfzNF2thM2IvFUgn+0TWQnlRSIyZNu3J5zxyPasfUdRuNUnM94qs2TtVc7VH4/zoF3LuBxagY4xAM1J9qlLgeZGPXEKj+lNzb0KVjPyw6BcdvmFFX/ALRL3uFH0VR/SipGVCACV9KlVV3FdoxxRRTEiUxpg/IvBA6UbQPwOBRRSZXQZiiiimB//9k=">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is the man wearing jeans?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if ANSWER0 else 'no'")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if False else 'no'")=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: no
