Question: Is the lid that looks oval made of stainless steel?

Reference Answer: No, the lid is made of plastic.

Image path: ./sampled_GQA/n546884.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='lid')
IMAGE0=CROP(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What shape is the lid?')
ANSWER1=VQA(image=IMAGE0,question='What material is the lid made of?')
ANSWER2=EVAL(expr="'yes' if {ANSWER0} == 'oval' and {ANSWER1} == 'stainless steel' else 'no'")
FINAL_RESULT=RESULT(var=ANSWER2)
```
Rationale:

<hr><div><b><span style='color: blue;'>BOX0</span></b>=<b><span style='color: red;'>LOC</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>object</span></b>='lid')=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>IMAGE0</span></b>=<b><span style='color: red;'>CROP</span></b>(<b><span style='color: darkorange;'>bbox</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCABLAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwCOwtrJtLtGexhdjAhLFeSdopZ7SzxlbGAc/wBwVpadHA2j2DFEH+jx/j8oqwbdFQsqjpzgdq6q9et7WVpvd9WYxSMFbODP/IOg/wC+BWnFolmV3m1tCAM4MXWrscqmMRlBlTkNirsUo29sY6EVj9Yrfzv72XZdinHpWmkc6bZHAz9wVZi0fSGkMb6XaZ5GQgp8mEG4EbOn0qWAgzRuDnLZqfrNb+d/ew5URaJZW6rdwpCqomoOiqoYAKOcDBrjNWuItK8QQ6laLceRIxEhWJwNwJVwCRz07V0tvrVnYXt/FKxEi30rHjPXGKyZ54NR8MTQgjAlkdGIPBEjY/PNaVeRynOeuq697/5G1BuMkujNU6zGzbov7S8tslf3LnI7dRVeXX2AIDX5PH3rViP5Vzthr00OnCDyg7wqV3Me3ak/4SMMfmcKW/vjAFYe1pfyv7/+AKdGUZNM1LnX3hgMvk3D4/6dSOfrisSHXDeSrdSpNuPDBY2IHtTLu++0SqBK0bKMgoSRz702CZ0JSdFYNysqDBP19TTU6T+y/v8A+AZuLRoz67p1u4Wd5YnIyA0LDj16UVzniXm/g5z+4HI/3mor6zBZDhMRh4VZOSbXdf5HNKbTseiaREBo1idoz9nj5x/sitFIhnkcd6r6MC2i2BP/AD7R/wDoIrRLRxRmSRlRFGWZjgAV83iP4svVmqKLWu2TaBViKIDjPI6Vh33i+zXJsomuAPl8zO1fw71l23jVZ5tpsmC9yJMkVyNo1UGdosDFShHB602CMxuq84DDGaoWerx3Ue6GQNjqp6irsdyZJEGMZYVLHa2hxuqWom1zU35/4+37/Sq9nG40RvLfaokdWz0+82DWjfD/AIm2o89buT+lVrWaGw8MS3k4LCS8aHaehXLEn88VvX1U/VfkzSOyOeeSa2vN0cojEnyl1GVqtfxs0iRtIsmDlmUdRWjf20t3H/ooWSEkYweVHrWNezTW4MZJJZRnjIIrmijWrLmin1F+0i3IMThFyVGejD396vwagkIaJgdwPzAkEH6Vgys8+CzgqB0A4FWreURCNvJ3gcFup5qmkYkuvyM97EygFTCNv0yaKi1USNPE4BCtECMjHGTRX6TlD/2Gn6HBUVpM9e0XJ0WwAwALaP8A9BFc3401Z45ks13eUoBcjoWPTNdBo7kaHY9OLeP/ANBFcX4tWRryRj92VcKT6ivgcV/El6v8zppbnLXklwhWJMnPICjrTLSO6hnVTHIm/jJBFWYbq4tnXvtHy46/mamfUWuTsmD4K8knGK5G9DpS1NXR7mHT9WhcB/mYIxJJBB6ivQY5YmuI9gA+cZryuyBuLqKOPdsDAk+2a9C08sbuPI6uKSRNS1zP1B1TVr/cRxdSfzrn9cup00KCwa32iN3m3CQHdvckHHUcVsagvma3dRD+O6cf+PVzWvXP2m+ukXG3dtXHotdFSpyVJRaTvbe/T0a7kpXSMa01a6snGz5kBztY8VpP4gS5GZbUFwMckH9etYDK245pVRs9aSqQ/kX/AJN/8kU/U21vNPaP57Ig+ouen4Yq3btbkCeDT2Zj0Msgx9cViWsBdwzjKA9PWt2KaMLw5T/ZYZFHtIfyL/yb/wCSJa8ylqkd7fXSysgGEC4Mg6ZP+NFae0SAMZR+VFetQz/E0KapwjGy8n/mYukm7s7bS5Sui2QH/PvH/wCgiqWqW6XcRjkUMKfp/OkWXJ/1Cf8AoIpzK3pmvOxH8WXq/wAyYnGXOhzox8skr9KW28PXMzYKkD3rrgBnBBFWYmC9q5rI252ZenaEtpID1YV0Fsp+0RZJOG7moQ/zZqxbNuuEPv8A0oFc47W2K6vdtvKAXDnI7c1gX8Ba9doVLKxyNoyOa6HWTt1a7I7XDn9a6V4lIjkCkIwz8nB55H86qur1WWn7qPLzpt053fZpAvdipAq5H4evty5tjtPO4EEV3Go+Z9kZGU4DqD7jIrUtEgeMwPK0ZYbtyJu4FZcr5rJm6lCNNSau23+Fv8zghoV0ZY4xGqFwSoZhzjrT30qW1m2TqM4BGDkEV208cYu7Zol+RFkdRIcHA29fwo1yxjnsEuYednOR3U04q6ZFWy5Wla6/Vr9DiTGF4xRVtogWopGZu6Wp/smz4/5YJ/6CKtFM9a89tvEWqxWsUaXWEVAoHlrwAPpUh8Sav/z9/wDkNP8ACvqq3DuKlUk1KOrfV/5HGqiO82ZPNNKbeAOPrXCf8JJqx63f/kNP8KT/AISPVv8An7/8hr/hWP8Aq3iv5o/e/wDIr2qO9zU9m3+kIPqa87/4SLVf+fr/AMhp/hT4fEurocrd4P8A1zT/AApf6t4v+aP3v/IftUbGqqX1K7PJ/fv0+tdLpJa40224OQgH5cVxtlczXcLzzvvkeVyzYAyc+1dx4bJOlkE9JGx+leNioOniZwe6dvuNk/cQahZtLG0edpbHOM4IINUI49Tgl/dPGwPqnb866ORRtORnnv8AWoIo0S8+VQMuRWLinuXGtOCsrW9E/wA0RRQXL3MU9w6EKCuEj25yBz1PpVi2XMc9tKCVViAT3U8/1qyoBtP+AmlaGPzPO2DzCoUt3xTSUVZEVKkqjTl0+X5HCXtsbW7khb+E8H1Hait/VYIpLpWdATsHP4mioaBSP//Z">)=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCACIAIwDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDzRk/CmYIpfOI4kH4ingq3QisbGxGB6jBpwGD1p+3jpRtxxQA3Bx60oBz0pQPencg9aYhAOOlLj6UY460YoATOOpoAoJA6mrEERfDHgdvegQ6CHjcQKtbME09FAHFPI9OtAXK5WmFeeOas7famFKZLK2MYpVGakZfzpMYoAO1OAGPSkWnheKAMoqDUbRc5XIPtVvYPrS+WvpSKKe6ZfQ/hS+c3GU6elWyg9K6GPTre0gjEkaGRlBZm9T2pN2Glc5UTLjkN+VHnr6H8q6ltBguJGCFoiPTkUkvhQLErx3aMSSCpQ/LUqaHys5fzueENIXdieAK25PDtxGflZD+NVm0q4STDIcVakhNMp29uZG3NyBWiigcDtV+DQ7xlGyHj61bXw/e/xKg+rUxGWoAqQDnnpWsnh+bA3SKB6c1OugLn5pj+Ao1FcwSn4CmlevtXTroVvjl3Pf0qVdFs16oW+rU7MVzkNv51GV54rtxpdoBxAufzqRLGEciGMf8AAaLCucKsbZwFJ/CphDMekb/9812/kooG1FH0ApcY7UWC5zw8Jxgc3LH6LTl8MWwJ3TSn6V0pQioyAOoosF2YY8OWI6h2+ppuq2scjiN8hVCkYPTFbh2hckjHqTWbqUSzYAbhlxkVM9ioP3ihayyzTs2XAPAatiMNgqSSrYLVVsolTahHGO9XbuGaCCCeJkKSOU27wWGPUdQKwWps3YV7RA4AKMGGQwOeKT7DE68jd61NbrvhV2+Ru6mr8FozAZHy4yOatQM3My49DtWUymd4VVgCI2+fnPIB644z9arCHU7f5YrhZV/6aDmt4rvdY2IBJzk/w+1Nhma3nV48B4zlWwDg5688GtLNbE3uYbPqpTDRwoR1YGpIbpo22zurZPVBwKmuJbzUkuZ4JYzLDLtZJFxv9enSptMvbe5tJDJbkTq+1wcEoR1BHfNJykhpRZIOgI5FMuRKLWYxf6wISvHen22DcNGFwnUA9quiHHatIyurkNWOKudQvpdI0547jY80hSRwBwc9K29NuJ2mmsrvabmHB3L0dT0NZGs6ba2upK0r3EFszCQhVLIW9sdDW3Zixu797y2n8yUxhGXPQfSrYti2UpuzNWdntmjZ7VIXF4PvWdqtu8kAMQLMDwo70liHS1VWaRiO7jBou5HMbRqxBYdQaAuV7C1n+xyRXEQX+6CSabNCiouzGBxxVe2S8hnZ5LgtGc4XPSrcEZYyxkcE7hzSkrqwKVncbCuGWporTy5jIcNkfKT1FMgXbJ5bE+xq5HxwwBHrWEY2ZrJ3RJGm7gcGryTSWzxFhjy2DDIzz2PvVdBG0RZXG5Tyvt6irMbieLZIpLhhtfPQdxit0jIj1W8a8uLi8jiCO4LbVOQWxyR9euKxJ7kf2ZD5krETfeniG3bz+lbkm21ALozEttCjrWQZbZTNKkZNk5KXEbDmJvXHoaoEOsIzEbhZ/mmTG5x/y0XHytj1xS28KtfXdxFgxSIhYjpu5/XFXLK1MEJcyb8gBWxzsHQVp3kFva2sNnFD5UuTLcEjBLtjH6YqXG40zGSFmcuqEqgy5A6DOK0opVkJTuOme4pUaW3s5YVbCz7d6+oHIqnko/B5HSsU+VmnxIbr1nLd6TJDbxB5GIxk9OetUtM0hrW5e8urgS3TrtO1cKBXQxsJoc+vWsK81xbVph9hvGWM4LbQF/Oule8YvQ1Nvy5zQUOelN0m8XUdOjuRE0YYn5W5PWr2wHtSFcwgwzjI9qr3IO4Gsa0huLe84jlcBzyzE8VuXAyn0pB0M14f3quHYAE5BbgmntI8DxzbwFX7y+tOkXdHjIBPSklQSoVJ68Ghgi9NGCwkTkEAilaTMRKDP0osstZiNzuZOM+3aiAeXcvGw4b5lNRJdSk+hPDExG4nmuh0i2hv7drMBY7xWMkbH/loMfc+vGRWQmF4qjeX0tveRJbSFJwQ4YHuOx9KqLuDN7T7gLq0YvYA2JBJEjcZx2PuDXQTeE9PudNee3tlW8nyxHmHa/zE7cHj6GuZmvbbV7KGR2KS5Yv2aOQd6uR69cXulJYTxlJbWQYnRsbiOQR+dWkIs6RoNstmsd9fi3fcwWI4yACeOaZq0dhZXwSO+a6kK/xsGIPoT9KzL69eJAxLu7nC4OSSawEPmkxyliztxJj5kf3pNpGtOnzK72NyVyxJY1VfJ5HQVLawiJEWaR35y7dzRL5Y3hQSD0Nc8wjo7D7NtsjR5461m+JrbULyOGC1iMkBOZQGxn2NXYW23CNnrjNXboTtayfZmUTEfKXGRn3rWk9CKm5l6ddXsVxHbX0Fvbo64iRH5JH1ra4HXNcpqOn6yYkvJriOV7ZvMSONME108EvnW8cuCu5QcEdK0IMXmkIyMU6k71IFCWIHKsOAaiiiEbuBIW3cgE9KuXCc5PeqoQRSr8429AD1pi2JLGYxO25s84bjGKuTp8ysOqnIqm4wx9+atW8ySReVISH/AIT6ilvoPzLAmJj3e1YT7Jp33u32lPvqRglfUeuOtaMu+HIz8p60pj82aKTcMJzjHP51lrB2NdJK6JbaG6iiimQRySsuydT911P8X1xWpEqxIEQbVHQelQQfdOasAg1opIzaMy4luiz3B2lIZT8ncAd81NZq8kz3LoE8xR8vuO9T3Vt54UCQoucMB0IqzFCqxsCQm1Pkz/F7CpbNnP3bIY5GMYqBvL2PyQ2Bjjg+tPkPPFRqCfnPQcL7msm7sIoRF+cE8gHGfpV+N8jB61VVNpwf4c8+tSrwc1tTVkZ1HqUNT8QRabdC2a2mkkYbhtHBqgviqeUFodMmZAcZB71oavbyGezvoYy7wyYZQOqng1nzW2qWN1OlhAXt3cyL7Z6itTMtelL3oxg4pOakY2VdyVnS2+5nYbATjGR0rT7VSuYi3GcChCYsgygPU+oqE/fz6VNH8sQQkEjjIqB/lJXOKVhJlmK5WWNkn9Plb0+tSRIyuVGD3BrPY5wg7dackzxP8h5FTJXRpF2Zv42pnNKGJ7/rVCLUomAWQFT3I6Zq0k8DAOJoyOnNYtNGmjLClsAYJrQkjYpClxIIwy7lAGSB9PU+lU4Y18t5UmhBRdwB6k+grR05LOaVm1K8eKM8gRDGT7kAnpTjdhoVr63tUlLRmRYsAKj/AH39ScdOajhQBo7yYJ5SShRF6gc4x6dqmuZrFWuI7aMtmT93JngL6c85qkzs33iSB29KtQ11E5aDiQ7uw4DMTj60tV/tKKzKScqcE46VY/lWyMWTx8oPWsGfxLJFO8f9mzttYjNbsf3BT8D+7QBkyJkZFQ1aI/So3QHkdaQyEmmSKHQqc8+lSMCByKYRQIoJCYpZCc8kYyc4FOkAcH+dW2TePeq7oV7UC2KD7488Z9/SojcKvfH1FX5E3VXa139V496BrUhFwjZCnP0qMzuJ8cKqjJJqy1oEX5B+FMSBfMLGPOOSf5UirG5BKskKOuMMM1KDzniqVm5KbCQxX07VoxxZ5PTFMLi2oZYSr5yCRn1HrU2Kpt9qF0+wZj4xn9avKD1oAp3cR8yIxlFyTknoatQP5qDBBboT70540kXDjIFFoUUKuVyc4A70yS2BhQMUuPWgdKX8KAM5wRjI61GetFFSMacEcjimmMZ7iiigBhjPrSGHJOSMUUUxMabROtIYOMDpRRQFiM2zdqkjsDJFISvOOKKKB3C1iWO5KbMZ5DHqc+31rT8sjsRRRQFxwQjtmnhCe2KKKCbjxENvzAHPrWe4aC4AVAqpyuOnXA/SiimBpoQygg5Bp2T6miii4H//2Q=="></div><hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What shape is the lid?')=<b><span style='color: green;'>oval</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What material is the lid made of?')=<b><span style='color: green;'>plastic</span></b></div><hr><div><b><span style='color: blue;'>ANSWER2</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if ANSWER0 == 'oval' and ANSWER1 == 'stainless steel' else 'no'")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if 'oval' == 'oval' and 'plastic' == 'stainless steel' else 'no'")=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER2</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: no
