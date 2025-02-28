Question: One dog is a gray hound with white chest patch, and at least one dog wears a collar with a charm dangling from it.

Reference Answer: True

Left image URL: https://i.pinimg.com/736x/af/e9/3a/afe93a96bb4951e1576bc6ff8e99c7fa--leelo-vito.jpg

Right image URL: http://www.maltesemaniac.com/images/xmaltese-chihuahua-dachshund-mix-lucy-21495494.jpg.pagespeed.ic.jLkCdn7gw5.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'One dog is a gray hound with white chest patch, and at least one dog wears a collar with a charm dangling from it.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCABaAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwD0BbpD3qUXEf8AerhhdXK/xU8X90O9a3Rnys7kTJ60vmIf4q4capcinjV7gdqLoVmdtuT+8KMp6iuKGtzjsaX+3ZvQ0XCzO0yvqK4P4oANptkqkbi0hX6gA1Z/t+X0Ncf4/wBblktrDKs0YkcMAPUDmoqaxdi6a99XPPpHaK+nhMQCI2AM8getdv8ADzT4r7U3lDocAbR/F65/pXOarALiC21O3Tc6r5U+Bx0+Vqfp12NKjd/tMkUjHqpwc+2Ogrmequjp20Z7jrfiCz8N6a19dOeCNkS/ekJ/hA+org9C8b+IPE3jK0g8uGKyuHw1vGmcIoJJLdePyrz3VtYub9YxNdPcBC20sSduevWvVvhVozxxS6pd2wjaaKOG1fpgDk8Hpk4574otZBuz0GXTQX3BM55NFXRcSkfLFvHr0oqQseexfZXuTBcyFDj5VUjc3oR7etcxKLm81K4trZys0b7OZSFI7Mp/pXTSW0Ny6F1IdfusnDfTNZ2l6fFFqlwIwwQSnAY847A0qjlGbbNaajKFkiB7m7tI1imjjd1GGkY43H1xVZ9ZkTJ8uMgdetbWrWiSygYOR6DrWBfWDouFQgdTVRqtkSpRQ9tezAWS2BkB7txVMeJxHkTQDcTiNc4Y1TktTHDI65GMZGaw7mCSeVPLXdIDtx7Hp+tbxlcxlGx6PbPFeQLNBIroe4PQ9xWF4qjTybaGXhZWYBvQ4GK3tC0kaTpUduyjzj88xBzlj/h0rE8dW7S21ltYrh36d+BU1X7jHRXvo4+zvm0mW5imUtEyFWU9mxwabYx29yhtJY2IKqxkBzjPPHvzjr2p9zbC4hR9gaVRtdmGTgd/rTYWWCGS2J2P5e4MBkDtg45/EVjCV1odFSNnqVobB7zW4NPtYOJJwiZ5PXn9K+iY0k06ILzJakAEgZaLHQ+4968O8H3tlZeL9KjZzIzSkO+CFQkEDk9efwr3tZMHNE29CIpaliK8meMPFsIbk/Xv/jRVI2YYloLlrdW5KKOM0VPMFjmShFOKJbag0mDh+T9cVJcSCKCSX+4pajV7uSGwku4ofNa3QSbOhKnr+hzTxDu0hUNE2TSugjeTAyq5qhohTUtE1eWcAlHjjVvTJz/SuNbxdJqDymAuEZdrRtz+RrqNMYWXgO88zId7lGIx3wcVkouK1NW0znNfAsLh0JyrIAp7daz/AA3pp1TVvNLARWzrI+R945yB+dTatqtjJKiXxxJDHjOc5J6DFa/g+2EWnS3KjbHcPlARzgcZrqpbHPVOnxmuc8XKrxWaHoXYZ9DgVv7jXPeKZAsVszkBVZiSfoKK2tNhQ/iI5uNQsyoV+6CzenHr6VDp2o28MF1E8SP5infIw6c//XqhDHe63fPHB5myX5SE6kdh+JxWRpthdXV6LIK/lqSZWAJCr6n09PxrKnCytfU3qz5ne2hoC4B1G0mEDMqTLhjwCN3HNfQNiJbmNFjBkZlHTmvLvDOgR694hs9Pmjlltml8ybyX27FXn8B096+hLLTbeygWG2iWKNRgItO3MQ3ymIugyuoZ5gjeg5oroygHHFFVyojmZ4fb69Bq+nz+RG6suFYN713GlwW+r+B7G7tyftdpEYWK9SV4Kt6jHNeVaLHLo0FvBdjD3sRmDgdHHG3P+7z+dd98M7mRb/VbEnMMgEwHoehrGu06rS2NqUbUk+pmnQrC4ctHZRQPKu9XjGBuB7gVo32nCLwjIsoCk3Csx7fd61v6NpSzape28gOyHgY7NmneNbAL4bvI4xgbC3HqBSim2KTPnq6EEt3cTTrvKv8Af/vegrsfDeuxNZxWly2HX5UbHGOwrg9ZimtIogykM5D7a0NCSV4xJLkY+7Xba2hgveR6pXK+NmxYwIBlnLKqjqTgVNba79khH2nLQoPmcfeUevuBXOfE+4WTTtJmt5QyNJIVdG4PC96Grole6zvvh94Dv4Ps17dK9qifP8ww7nHXHYfWvT7Lw7pllZT2dvYQJBcEmZRGP3hPUn1r4s+3Xf8Az9Tf9/D/AI0fb7v/AJ+p/wDv43+NRGnylSqOR9w6fpVlpkIisrOK3TAGIkC5x0z61bYEdjXwn9vvP+fqf/v43+NH2+8/5+p/+/jf40+UnmPugsc9D+VFfC/2+7/5+p/+/jf40Ucgcx7XrdzHIskDMkMShfLY9QVIxt98Zx+Na3ha8fQfEVrJckNDOjLJJF0C4+8R1HIrj9O1gX1uLW4WM3CDbE78Bs8ZJ9enHfBrRSb7Nq1rYTTMSYPkmUAHaDyG79a550pxh7y2N41qbnyxlv0PeNKktJYpLu1bcJnJZsEHI471X1si4029iwOYSRnp0rm4tPu/C/hjVbi1vmuw8JniUx42ttHTnnpXnur+Mtdt4CrTHE9qvKtkYP8ALiphd2sXyx1bOf8AE8EVzfWr4yFj5GOvPFQQThF2KpZz0Ud67G68HNqHhew1O3dzctbJLJEvVgRnj8+lcgmLTKrFtA6kjBrdVVNtlKg4xRaQ+Wn775tx+Ze2O4rzvVbmTy/sSyMbWKZzEjHO3t/QV3YErL58isiZ+UMOprz/AFbH2uXacjzWx+daxOaqtTPooopmQUUUUAFFFFAHWwzg8jI9zWtBq26981y7tsVS5PJI4P4Y/WsG371ah++PrTqTc48sgpU1CXMj6d0a5ivvDNoyuJAIQj+xAwRXLjwtoC62GayQOQXCsxKA/wC70p3gSR/Klj3ts2g7c8Zx6VpP/wAjND/1zb+YrgnG10j0aVrpssXFjaylXlvbkKOPLSQouPwxVaaXSbRgsVnDJIf9gOx/ma3dQRPs6fKvX0qhOixwgooU46gYrkaszvi+aNzy7xpa6he6kJI7Vo2kQrBCWALEdWIHQDNeYeJvDtzolnaS3MkbPMzDavOMAHk/jXtW4y6hctIS7KAAW5IGTxXnvxT/AOPTTf8ArpJ/IV6lB+4jxsT/ABGeZUUUVqYBRRRQAUUUUAf/2Q==">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'One dog is a gray hound with white chest patch, and at least one dog wears a collar with a charm dangling from it.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

