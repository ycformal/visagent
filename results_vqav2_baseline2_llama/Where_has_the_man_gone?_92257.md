Question: Where has the man gone?

Reference Answer: bathroom

Image path: ./sampled_GQA/92257.jpg

Original program:

```
BOX0=LOC(image=IMAGE,object='man')
IMAGE0=CROP_BELOW(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='man')
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'below' if {ANSWER0} > 0 else 'above'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Program:

```
BOX0=LOC(image=IMAGE,object='man')
IMAGE0=CROP_BELOW(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='man')
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'below' if {ANSWER0} > 0 else 'above'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>BOX0</span></b>=<b><span style='color: red;'>LOC</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>object</span></b>='man')=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>IMAGE0</span></b>=<b><span style='color: red;'>CROP_BELOW</span></b>(<b><span style='color: darkorange;'>bbox</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">)=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCABeASwDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDqbTwnfz4/0WOPPQ3Upz/3yvNUdY8P3uisDOY3jJ4dGH6r1FPu/F+rXKmOGVbSI/wW67T+LdaxHkZmLO7M7dWY5J/GuKThayOhKXUkDUm7mo91BakgJw9TI1U91TI1aIll9ZPlqCeb5DTBJwapzy8Hmqk9CLakAfFq3+3Ix/IAf1NV5h5iFd7r7qcGh5Q0MajtkH67jUZaskakDpN5YUOkoXoJByevf+tQhmgZW2zwjPPlneuOD+tTSBiPusPociowzr0fJ9CKYwF6+3cJopcnAB+Q/QU4OsysXhCt74OR6gimlt3LoCRzkAGq4t4+kTvGODtVun4dqNAJBAiuGGeDnrVhWy+fRTVZI5EJ3Ss644BA4/GnpuBbPTFIaK86qJjuB6DAppG2M7RjnvzS3Dp5zYyTntUJclQAvBP1NCGPByCWbccVGzEgYb8M4p+4BSDgEjjJ5/SmD2BPuFpoQ8YySTn2obtj0pF4OSBn/abFEkqpOqFQNxA3EgDpxgGmOxp6Nn7QDxwwrvBLXC6Z/rgNwIzxgY9fYV1sUuY1PtTT1M6iNASUpeqYkp/mcVdzKxKz1kXyEXYdCMyDnIJ6VeZ6pXJzNH9D/SonsXHcislzcSSOfmQYGBgc/wD6qj1S4EqiLGI4uo/vN6mpLdsTTfUf1rPvTnzPcmkn7pVveM95AhIaMqScDIxVeRspcEYxwP0rdeNX1JAwDKIcYIyOlU9UjRfLVVCqVxgDHeolsXF6mHCTnmrPGOKj8vZIRink4HtWbLRQkG2WUnHJ6God2S2M4Hekml3Ekkkk+nApjHA6bj/KoPWgmopCPgt90BR1qMxgnO1aa5G4Er+VR5/2QfrTSKO5k1OJTtiUyv8A7PA/OpIDNKBLO/OeI14A/wAarJCqbcACraHAxVo8Z7E2aC1M3U0tVkEu6pI35xVXdSo/zCqQi20mKpTycmpJHqhPJVvYjqQiX5GyfuvSiQHv+dURO0c7Y5HXFSm8gDYkO09i3T86zuaJN7FwN9Kqm7PAmgJPqnzClXa3zRuCP9k5FITuPIUjsaB2E+0QSHasg3H+HPP5GnAlehBHuKi2KGzsII7kUbgf4h6UAStJSIxLOc54qIk0qHAbPqKQypKQZmJYAbj0FIxVQOrZH8R/pTdjOSQM9amNtJtDMNqgdWIX+dMCMMUjdsqgGOemBQpzICXzxkc57U2c2At3hkv4V38NtO7AqS3u9NJAjleZlXBOwjjGPamNJiRxgnLA4780l/O9tJFKgGz7oYKCSfTJqz9steiwyEehxTl1CJGwYGb/AIFgUXK5H2L2lGWVTLIpQjvtxxzg4NdBBLhAM5xWFBdxnO2NlLD+97VoQy/LSvqZTNQSU/zOKoLJUgk4rRMyLLSe9VpWHnJn0P8ASkL1BcBpEGw4deVz/KplsVHcmtmb7U4TO7qMD61Tu5FbhwdzcDKnk1B9qZH+eN1f/dNSoZJZFklBVF5APU1F9LGlrO4+Fm+2AP8AeEWDmq+pnJh+v9azba/vX1vy5fJ2HcCU5BAHBBq3qEyhogzKMHuack0hReox4Q4BHXFUbweVA59sVpQuDgVU1JEMMit93H/6qiSNKb95GCG3Kx29+p5prE4C/KBnqBUiRDPOSfxNSm3Xrg/981ketdlORflwCTiowvotXGiVTn+eaTbH7D6NTQNnWjtTwaizyKXPWrR5BIWpM00mmlqsgfnikDYIqMtxTN3vTQE0r1Qnep5HqlO1adCHuUnb/SPwqOV8ye+KSRv34qKU5cYPOKxZvSdpA5x8yZVvUcVJHe3KxkFw/wDvjNQFuPapEAwfyoRu0mWoJ3ljPmIqkAcxsR+hp5nC9JZBxjDLkVnoxUcHBHFSmboQM/WrVmcrumW/NBHymNvbG2hbm3hbbMkzA8gRKzZ/LpVdb0L1Q/nUg1MDpGfzp2QXZZbUIQpEGn3fPquz+ZFZU9k11IWNqsee7ylj+Q/xq42pM/8AAPzqM3Lt3A+gp7C1Ei0WzEX7zezH0bA/KiOzt7eZhDHt4GcnJNW4/lQAnnuTVUS5DP0JNZt3ZrT3GnAb681Hv+cY7UO+M+9NjAaVU7lhSNm7I2Im2sB6AVqQSfLWOGw9XoJMUI5GaaycVJ5nFVFfinb+K1RBZ8yjfVffS7qTGiff700nPB71Fuo3cVAzmdGf/iZRxJGQkYcb8YBx7dqraw8EuqSKqyBhKFkyeDgdR9a6tFzcyY5JHYVy2r6ZfHWnYRqEeQMpBGCMD7w9eKtSTC2pt2z9KrarcBfkAyTyakgP7wjtmsuf97cOzHjcRyaxmzrwsLyu+gKFQZKHPfPanGXBwFX6EUHHAx0qOUlRgHBNYnppaDGnYsQUx9DTROh/iYfhTCTkjdz16U3yd3JAqhbnX55pxPNRk9KVjz+FaHjDiaaTSE00mqJFJphNBNNJ4qkIY71TnbrU7t1qrKRg1fQllKQ/vR9aZPlSjfhVmNEkuAGX5R8x+goupEltXVYYlJGQQOR3qOW5SlZlJj0xTlfFVg+5dvccinBiCe1I6rliNHkkYIpbjJwKc0Ey/wAGPqcVAlwI33O20YxSNebuQmVPQ1pGNznqaMN3JB4I6im7uajSRbmUquMqOcHpUphccYptW0IuKrVcto9xDnp296rxWzSYBBAroIrpo0VUjiUAADCCpY7lGZjHbyOB0U1mmUBQBWvrF7O2muhk+VioIAwOtc+GyB71NrGtMnaQD6Vd0i1a7meXcirGMZdscmslm681pWd3b2tqoZmLN8zYXPNCRVRu2hrz2jRfOHV16Eqc4+tJE2D1qrbaqjTZiz0wyOOGH09KvtAskRubXJjH34z96P8AxHvS5bbGHqTI/FSb6pI9SCTmrRLRZ30u+q4el30mMsB6duqvupQ1SMV4vmLI7Lnk4qo+ftCozliik5P+feru7IrOdz50jyRsCTngVLKQ+IYkassn52J6jOea1IZFdNw/Ws6aMpM44IJzzUSOzCtJtEQJzgn8BUbneSSfbmpC3PygkD3qGTJIO3GOOag70wEW9i2CB2xQflOA9NEgU9Dz1xSl143KM/WgdjqCflFKx6fSmZ+Sgn5RWp4gE03dSE8UzNUSOJpjNSE0w9KpCIZH5qrJIeankPWqrjIqhDwDHplzcE4LERKfryf0rEEsjg/vXx6bq6HV1FtptnanAJUzOD6t0/SsPOFwMUm7aFQV9SFCQpHORxUrPgnHSmEchj3HNKQdnPakbx2IZmywHTmoHiDdTx7mpZWRCGkYKueSe1RPPabc/aIz6Yaq16EStfU1NKgRIvMCgeYQBx1ArV2LuGaqWjwyWsBgkVwqDO05xVktk1SMGWotvoKxJZ5EnlTzZBtYg/PWtE1ZmpWzG6DqOJP51MioblO4ZzGu4k5brnNICcZp728vkrgZRDnjtmkKYTHaktjeIzG8gZ6n9KmxkYxx/Km2+1juOCD0INWlWLHbNRJ6huRRIAwYHDDvmt3T7x4nEkbBZF645BH+FZB2+nPbA4p0ZMbAqcMtCbRLjc6preO9iaezULIozJAP5r7e1UM1DZXp3qytsmXng/qK2SkWrKWjCxXw5KdFl9x6GtbX1Ri7x0ZnBqcGqJgyOUZSrA4IPUUA1DGT7qUNUIanZpDJg1I3zDB6UwNTs0AVyvlOQOhrN1V/KtmuVj8xkx8ucZBOP61rSDctZl7A9xbtCuPmIzn0zk0rK+pSk1qtyra3SzWBuxGQOQyZ5GKiGpWpXBDj6rmrVnZfZLd4iwKsc4HbI5rIaLGcEYqZRjfQ7KFWcl7xfS/slH3zn3U0K9s4yZ4j+NZuwHijy8dqXKjpU2duD8hoz+7H1piHgj2oB/dmmeSITTSabmmk1QhSaaTwaQmmk8UxEMp4NP0+1N5fQwD+Jhn6VHJWroIES3l51aGAlR7nitIq7FJ2Rj+ILhbjU52BAQNsTjPA4rI+XGMnj2q5cIWbJwazdQuDZxjCguxwvoPrUO8paGsbRjqJdzJDbyAttyu0HuT04rNXUbiwc291CWZeMk4JH9agt993qcQlbdufLE9wOf6Vt+IWjOmFjGC5cBWx93uf5VryqL5X1MfaSeqKseoaXcQyi6eVWZCAuzgH6iueANJmjNbxilsZSk5O7HLI8Lh43ZGHdTg1p2/iG+hwHZZl/wBsc/mKytxqUoCRjqRnpQ0uok2dBH4sKjmzyfaTj+VVrvxLc3LKVhijAGADlqxdh3beKGjK9SOaXJEak0dhoviG0jtNt9Ptn3EnMZxjtjAqDVdbs5p/JsIo3LDmVjtQH9M1ymPerFvCJZACeByfpS5I7jU5GxoczsZYHCvGgyr+hz0/HrW0pCnO0Zzya599V+ylYIIwuCM5AxjPpXQbzj29q5qq1v3Oik9LdiXfz04+lNk2ZXGM+5qLB37Sc4NO2r0NZJWNtyYI6uHyqFeQc1q20/mKrBgrjn5T+orHWTbGeOFH6VJETxJGSD1BNaRdiJa7nViSLVkEc7LHeAYWU8B/Zv8AGsuaGW2laKVCjr1BpkMhkTOMMMZxWzauuqoLO5BMij91MOo9j6itGuYw+ExgacGouIWt53iYglGKkiowayLJgacDUANOBoAkJqJ1Gc0/NNNIEVpm8uNmPYZrk795Fa32sVLykHBxxj/69dXdJvt5F6ZU1yt5819ZL28xv6U4bnRD+G/kUrS5uWmdTMzbf73NXfMmJyHOPYCs20bF1MD3yf1rUAwMGrqWTNKDvHVn/9k="></div><hr><div><b><span style='color: blue;'>BOX1</span></b>=<b><span style='color: red;'>LOC</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAAfAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwCzdanBeOPs9rBAqcfuiTn6knmoo5sMOaz0YIuBwKQzY5zXDF9TpaL2oXuFUE1jTMrfPkD3zUOp3Jxwe9Zn2+YPjhhn+Kqk9QhBvY0ixY8uCv8Atc/lUFzL8y9zt61XW8UqM4GevoKSWWN1+Vo9/TcTu/TFFhjtwLDFbvhmYRXczA/7J9q50s8GSJySQCfkVf5CtDS7yTgu5IJOM0uYqUfdud6bzK9ayZ3wlxtIG4c/TJqst2dvWmMyuxbJye2eKqTMYooX1oNsZQsSSTgn0NYd9JiYr3Uc1oCW5gubWCTJXYzM3UZLetULiRZLiWXaME9/Ssamh3YRNyuZrM248CipjLzxHx7UVB6Gp1JfAqJ5PemM/wAtQM9axPFZVunErBcn3+lZD3KNKTHkL1Ga1nGLW6m7hRGv1b/6wNc3LOTLJHCFaSJDI4bgYHbPrV2uOD5dWWxdebIkKR/MTjdmr8MK22Zrg7o1PQetccdYnS4Etudgx91wG57/AIVebxPcNbvFJaxMWHJ3HH5Vr7N2M3ONzYu7sS3EjRgqnQA/StOxvI38uAx+XtGBJ6n3rlU1aK4eHy7fyQmGmZmyD9B2rbDDpjJrKacdzZNTWh0pkeMhX9MgjoR6inrOfWs6xvA6fZ58uv8ACR1X6f55qxKjQOASCrDcrDuPWh7GdrOw+b74YAbe+Kw5nRWkUyKCrbTuOOeo/StgSZGKxtZAhs3dFXczAkkdT2rNxudFCq4S0IvMTs0Z+jCisWGZ5IlYqmT7UVPszvVa6uf/2Q==">, <b><span style='color: darkorange;'>object</span></b>='man')=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>COUNT</span></b>(<b><span style='color: darkorange;'>bbox</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAAfAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwCzdanBeOPs9rBAqcfuiTn6knmoo5sMOaz0YIuBwKQzY5zXDF9TpaLGrXKu9urgMoLcEZ521kzJCRuCRgdM4xUeqXBJU56Gs37fMHxwwz/FQ7czOlSqKEFF20/9uZoBEzxs2+4BqC4ZAy4Rfu88VCt4pUZwM9fQUkssbr8rR7+m4nd+mKfKuxHt6n8z+9i5UsMCtbQ2RLxXAG5ZlBOOnWsUs8GSJySQCfkVf5Crun3ch8su5I8wEZNS7W2NqdSo2ryevmegfbMp1rJnfCXG0gbhz9Mmqy3Z29aYzK7FsnJ7Z4rSTOCKKF9aDbGULEkk4J9DWHfSYmK91HNaAluYLm1gkyV2MzN1GS3rVC4kWS4ll2jBPf0rGpod2ETcrmazNuPAoqYy88R8e1FQehqdSXwKieT3pjP8tQM9axPFZVumErBcn3+lZD3KNKTHkL1Ga1JNwimdRkkeWPYn/wCsDWJNFc7iIYgzKu47mwCPT60OUbtNnZDD1pwhOEG1bom/tMkF15siQpH8xON2avwwrbZmuDujU9B61zZbVUuBLbw7AB91yjc9/wAKunUtUa3aKTT4mLDk+YMflmtLxtuvvMnhMTf+HL/wF/5Fy7uxLcSNGCqdAD9K0bK8STyoPLEYXGJP55rDDzzSQBLHyduDKzSAg+uAOlaQBAOR265rKcorS6Omlha903CSS8mdEZHjIV/TII6Eeop6zn1rOsbwOn2efLr/AAkdV+n+easSo0DgEgqw3Kw7j1rR7HnWs7D5vvhgBt74rDmdFaRTIoKttO4456j9K2BJkYrG1kCGzd0VdzMCSR1Pas3G50UKrhLQi8xOzRn6MKKxYZnkiViqZPtRU+zO9Vrq5//Z">)=<b><span style='color: green;'>1</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'below' if ANSWER0 > 0 else 'above'")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'below' if 1 > 0 else 'above'")=<b><span style='color: green;'>below</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>below</span></b></div><hr>

Answer: Below

