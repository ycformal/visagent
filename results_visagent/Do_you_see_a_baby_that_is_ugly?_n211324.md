Question: Do you see a baby that is ugly?

Reference Answer: No, there is a baby but he is beautiful.

Image path: ./sampled_GQA/n211324.jpg

Program:

```
 Do you see A that is <attr>?
Program:
BOX0=LOC(image=IMAGE,object='baby')
IMAGE0=CROP(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='Do you see a baby?')
ANSWER1=EVAL(expr="'yes' if {ANSWER0} else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>BOX0</span></b>=<b><span style='color: red;'>LOC</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>object</span></b>='baby')=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCADgASwDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDk1v5vLVgeMsGwOnIwf1xV+Au1hMzlySr/AHmz0z09KgWa0MoChHTZtLDLY9BVqKNXV1tbSd3lBH7u3b5iffHvW1zR+SPoTw9J5vhzTHznNrH/AOgitBo0cYZQw9xWb4ctp7Pw3pttcoUmitkV19DjpWmzqgyxCj1JxXO9zJjPIQD5dy8Y+ViMUoRhjEjceuDTY7q3mcpFPE7DkqjgkflUtAiMCUYyyH14xRukHVAeOzVJRQBH5hHWN/wGaPOTODuHOOVIqSigBgmiPSRfzpwZT0YH6GjAPXmmmKM9Y1/75FAGVqXhnStWvory9gaWaPAGZG2kDsVzjHNc54i0HSz4t8JW0enWscXnzuwSILuCx5wcDkZwa7fyYx0QD6VxniIK3xA8NW4SU7kuW2pIVz8gGc5yKaY0dqqqiBVAVVGABwAKoahrml6XGJL2+hhUnALNn+VSx25YgXZ84jlSR8v5etWJbeGeFoZYo5ImGGRlBBHoRSAisL+11OyivLKZZreUZR16HnFWKRI0ijWONVRFGFVRgAegFOoEJS0UUgCiiigAooooAKKKKACkPzDqfwpaYU64Zl+hoAjPnRtwRIueQeGH07H9KFuI3yB97uh4YfgacYpMfLMeP7wB/wAKoz2V1MdrT25XH3WhyD+vH4UxiSXkltcbS5CHIHnLtXj/AGu3H1qc3xSLzJIvk/vRyKwP0zjNZV5b6jb25W3uI0SPDfO7MMDnHzZx09apxT+ep+12clpHtyb21UvHIo+g4HfJH09aqyA6G31CG6UvHINqKTIpGCv5/jWeDPbXluYfka6jklkVydgxtwuQPl4P/wBY81k6hLbfY5r2G48x0iYLexMXDLjJRw2flPGcd+4NQWR8U6pFDdQ63ZxpNMuEjtFk8uMoGzuLckE7cH0zRYZ0n2pZbmBJ4DGMnImB5YY27D0bmrzXah/LSOWRx1VV6fXPSvO9Jt/Esug6QkOuDybtpFeI2UcjKAWOeeo46n1FdjbuuhW8MM8kpteFMs4G5W/vMw4IPv0+nQaBomuPtk0yMkM0RXJXDqAeMfNg4J5yPpUIuboAD7JLKR1aNjjPcdRz9BitYyRPhCyneMhSeSBj/EfnVGz0+RI5TfzfaJXmd1IYgRoWJVB6gDuaExHzRqPiu51Ux/bLe3l8sEJuThc9eBj0p58ba2I1iW9dI0AVUV2wAOgHNcyZSoKg8Goy5NTzs9VUIdjsrbxNqmoW/wBl/tK5juFJMarOypJ6jGeD/OoEv5rhiJpJGcHDCRiSD+NcsshXkHkdOa3Laf8AtRQQQuoIPoJ1H/s3860hO+jOavQ5fejsdJoGoPpuu2V3HJ5XlzLuYcDbkBs+2M17/Frmkz/6nU7N/ZZ1z/OvmvT7r9/DIOGSRSQeoINfQ82pWE/F1bwNn/nrC4/9Cjp1EcZto6yLuRgw9VOadXLsnhmRvmsdPVvVDGh/mDU0cOiAYhmni9DDeuP5OazsB0WRRWEkNumDHrWoIPRpQ/8A6EpqUx3H/LLXj9JYYz/IClYDYorKRNVAO3U7CT/etSP5SU8HWAeDp8g9vMX/ABosBpVx+ond8VNFX+5p1w35kCt6W41lHQJp9nKD1P2tkI/OOuA1C/1sfFq3EGnW5u104qIXuCyCMsctuCj8sU0gR6gQCMGhRgYzn61Rt9Wt5dqS74JioLJKhUA+m48E/Q1fpCCikJA6mmtKiDLOqj3NIB9FIGBGQQR7UuaACiiigDOn1qytjMJWlXySQ2IWOcDJxgc1Haa19uSJ7eyuikjD5nj2qqn+LJ9sHA9aq+L7iS20K4Zbkxh42iEaweYzsVOMcjHGTntjNT6DBeRaVaCa5hdfIj2IkGzaNo4zuOarQZsUUwZHfj6U7HvUiFpC1G0etG0UAJuqncTNGwBBcE/KUzlfrjtj2q7gUhXJOemMe4pgYENveX8zSLqG6zfDDIwc8AjGORx1OPp3qyNNNuPluZIuc5gfZu/Bsinx6HaRXEk3ltI0hBYyzM2SO+Og/wDrClfToXdl2kIFwArs2c/7J44x+tO4zFuNLmeG7Fnq4gubjzEdJ1UBycrkhQMn3xn3rnLaxilsBHqPih9PvrebybmOSeOIo645RsAlSMYPofrXb3WmxPDJBdh5bKX7ySYKg/7QAzjp37c01fDHh1oAz6Rp8ijkubdD+uOntTuO55Ro3iGKy0uKCbxDPJI8nkiGxbdNDFnPChTnvyDnn2GNrxN4y1N1FtZafevGq7i91b/Z2KkEMMOw3ArnnHB961tDudOsvAloLWW0i1HazrEiAvKwZjtIUbhkd+o69q4bV/ENz4pulkNnPIlujNcWsC4KgZ27mwdxGc8DOCcA9ady4q7Om0/4hmPTEefQdSPlwIPkhD7yx2qSQwHzEDt1qrdeMPHcs5ddCaBCPlRpUU/j175qCw0PVrnTf7aubtGSMrBFEr+WuwDGMcgZBwAOgJ71xtzdvJOzQRywR9BHbyZQfT/PXNKUrDUbvQ4TNGa0ZrWxuL62t9OldhIcOXzx+Y9M1pnT9GlnbTo963KjiTJPOPyP0qVBs73XS6M5vNPSRo2DKSrA5BB5Bq7pVoj6z9luow4XerKfUVqKNDnuzZC2KSligbBHI9DmiMG+oTrKLta5HDfLexPcghLyFd0oHAlUfxfWvofT9a0C92RW3iMtMUU7Pt3Pb+9XzXbW7Wmo31sTnbbygH1GMiohLjDA7sYGDzzVuTtqcNWEVL3dj61FnIORqF5g9MsjD9Vpjac8n3rxm/34Im/9lr5y0jx14h0C3aKxu2WN+THKokCnjkZ6celX7j4meI72za2k1FgjNuZ4lCOOc4DDnHtU8yMuR3Pe20cE5LWx/wB+yQ/4UHRlPHl2BH/Xpj+TV892vjPWbW4eWPWLuOR1wxEm7PPo2QPwFd9ovxkhSF4tbtJWeNRtntUyJPXIJ4PfjjrRdCaaPQ/7DQHIhsh/uxup/RqedIPaOAj3eQf1qDw94q0nxPA8ml3JkaPHmRupV0z6j+o4rbyaeormSNHRH3eTk44xcy4z9N1cJaWP/F4p7aOW53W9gSWN05YMSrYDNnKgNgA8V6hzmuIj5+NMmP8AoDj/ANCFCBM2NS1XU7Eh1sorm15WRLh/IfrjIbBQj67e1ULbxBaSXMwhafT4UHMmQ8W7qRjkevQit7V7K1uI0mvJSkcXQHpkkY47/wD165TU9LW6uTBCPPtwrBpID+8Vvw+9nH4D1otdDTItR8a+XJPHFIz54SQKNobHUZyAMHsc1zmqeINTkg+0LKRj5MSn7wIGGAxyenf09624dJhtLGFLhbiS9jUkO8IYNjnovOQDjmqd5oU8sDXMTpeQY/jO9AvTC9Qfpwc1Lg2ik0UNM8ZajZKYZ5XaBDnauM9zgM3I6/piuht/iItxcROVEec7ox8wwM854/8A11w2sRyxSWqzWjWwZlMasrMABnIx0Ix68j1xxVMpprQvMk7xuWOEKjGOvXrWLvDRMtWe6PcNP8S2OoTyRxPwGCoSCC3rRd+IbeFgsRV3D7XT+Icccf56V4lFqlxbFbiGYr5RwAGBA6du3T9K2bjxDPcW6XLJaQTFTuZ8gTHbg7uPvYIx9KuNRNbEuFjrNW8QJq0epznb9j07T55UeJtwaSRSiZ9G27+P9qu002WN7G3jSZXKwoeCDxjAPH0P5V853Ory3FvdM8k6faWZpFVMAjAAHX0AwK1/DPjO90RrhYQgaZQSxGeRnH5Z/Sj2mmoOHY9l8S+K9O8LWsc2oOS8jbY4o+Xb1OD2AzVrTtfsdUhSWykaaNyACEI6jI6j0r5+1y7n8Waqj3zkys6Rq4JwikgH6DvXp+n+I00GLyLoWtrZmVIlYyMxU+UpxhRjGAOeOtXTkpq6JlFx3PRNzf3P1prSFFJYKB7muVj8e+HGthLLqcaD0KMSffAzgZ9aoXPjvQ7qdY7LUUk2/Ow8pl6fUVahqRqdn9tjZQVlQ5BICjOfpVaLWLa4d44ZWkdDiRV4K+px6CuT/wCE08P2Edw0mpxuUZgiK+4leoAwPcflWBbfEHw9Y6jIx3P50zYlWHJjTAIGTg4Jz0/GnyxHqeqxzRsdh2mQdcsP8am3OeAuPwP/ANavG/EHxcihvYI9DgjmgGWmN1HncfQen1rCi+KmtGSF5DGixyFpBCuxZFzkKcflkVDsVys+gsNnlq4zxD4o0HSWn8+xaa6RSApiJBIOPmIBAGT1754rjNC+Ja3b3La3fXEUbEmOC3JAxjoTyfyPOa5PX9eXWLqf7ArW1mr/ACIBgnP3ifrjmk5KKuyowbY+bxNBb6TplsYt7QR4l2TsjkEnKgj7q4I6de+azY9baKC7kkvh9oO3AkDM8mDnG5TtP488VlSr5tsF6lFOPaoYNPkMgMqr5YGeDWbqJNm8VHlNW48RX1+BBNdGOENI0dtH8iRFj0CjAHt3xVby25JLAkk8kj+VVREHuGcSbAG64zz9PSnvtdyQWPPas5TvsUyrogxr0QPYv/I0iymPxJvzyLog/i2KbZyi28QqScATsp/Ekf1qa4tJB4nCbGw8wkBx2zkn+ddC2+Zq37132LQAi8Ykf3iT+aVYGkJBqjX0t0gRZDJtPGO/JzVOSQHxipB6OF/8drL1cY1e6H/TQmrukm7dTNRlJpJ20L8N0t5r88qfckjkVfcbCB/KqEdzsjwduccZHtT9FP8AxNoR/eDD81NUicL+AqV7y1M665ZJLsXlcyKXb5+mMnk0yRTE28AgZ49qLMBlKMflI7etSOhkkKl2zsJwR1/GovZ2MraXBJDImW4A+6R61NHJJHgkNtzzVdSwTYcj0weKfuygRtwz0xSZaSsX7LUJrOUzWk0kL5BzGxB/MV6D4T+Kmo6fIlvqrNfWpYbndiZIx3IPf6H868uiXy2IY84/OhZtkmUK5JxhRTt2M/U+t9J1rTtbtPtWnXSXEXQleCp9CDyD9a5SF/8Ai9c4PT+xxj/voV5R4G8Xv4f8QxAgGG4Kwzhm2gAnr6DHr6Zr0ODXtKl+MDXSajbG2bSxCJvMAQvkfKCeM1pHVambVnodleavNKpS0gdWV8FnxyB1wOuazvssUYDCZw43Des5AOeSD2BrVvLzSIbM3l1cWywEEiQuBux12nufpXP3HxJ8MW1ks8Ekly5z+5ih+ce7ZwB+dVohK72NNbV7yUSKhlaDG1GdXz759xxnjBFYsvhjTri6mu5L2eFpmLFUTMhwQCCe+D2IOP1rj9N+JVzLqTyXtolzbFTsi8pVZD14Yc+3NVNa+INzdTO2mpPpwyTlZzIzjGBkNwDwOnpSdupdmin4mk1K1vtj3s5ictKkspPBVduBj0B25GBmsRpltQkUc6M7giQheF9gQeR6/SqOp6jdXskZubiSXauAWY8AnOBn3Gaos+ck5Jx3rNpM0WxuLdIkTwJcYjcKpYpnHXAH51X+1xPZMsyP5jqFUqeAQcEkfTI4rOSVUiHBZs8ZY4qsJG4Ubj2GPWkkMvSOGBCgYPBx1xV2FwBu3cgjA9BispiR1VhjA59e9SO+SoDY5GB61Eo3Virm0sgkb5z8w5OOakvprnUrmW7lmeWaQgsXPU9M/kMViyT+QiYYcnPvUiXbMuFBI7gdqxSlDWJTs9yV1mTPmShOwUc1WaR1Y/O5+iAVYkuUdBtAVl6gGqglCn5lCsTycAV1UZykveIkkkRnfJJt+baTyQOg9akRYlB3h3GeDnAqQSkM5LFdwHA/iFZ8k7KwBjIJPUU5a6IlF2SGJl8yP5W7qxzx7UhQCPg5A5I9qIZI1IaVnIPACYGfxPT8qV71dpUxRCLoY2Q/nn72ffNSoO2rHzeRVMxLfJjGevpWk10v2ePaScjnNZfmW32hRC8gVuGVyPl+h7/lVmeNIiqq5Kg4GayrJXSKi7q4iTFWPOQDUz3K+WVycEY61meZh2AOMnJpDJwRjtn61MoXkxp2RoKGaJ2ClueT6cUzzFXhgAR6jFVUnVflDHJ45NDSncQFzjjNLlBMozzGe4kmI2l2LYHbJrVj8TXaW+xo43kAwJDnP4jvWNiiuhSa2O2VOMlZoliu5YrxbrIaVX35bnJ96S5uXurmSdwodzkhRxUVS21tJdTpDEu52PHt7n2pXew7JalzRFP9pRznAig+eRz0VcVQkyHOBwfWtVvLkxY2pzaxtmST/ns/r9B2q/8A8Iw13bm9Mwii2k8rn7vB71slZHnVqnPK5hW5YHnBT2p80xd+FGM44PWt2bwutoiFLksWbq5CL0z1559qjutANqqh5AZSeAMFTkAjDDjJz0/rWclrcy5jEQyBWbaSRyfagSyLwSP8a77wt4Xs9TsGeS4dJQxXyVlwRgckj65rcs/AGkTW0M0kJd5EVyS7dSBVwp3Vxe0seU+eWO4gcccmmwHbIGYAc5ANe22ngnRoH3CxgJ/2lJ/ma17fQtPSX5LOABBgYiHU8/4VoqYnUueE2kJkuhtVnJbgKCxP5V0unaVNfeIBaLYshNsSY5FZTjj5uRXtdtaRREGKJFx/dQD+VcLqF3PbfGy0Z7kxxPAqsWbaPL2E7SfTI/Ony8or8xz134Q8QXsxWCyldYht2gnA9xnjtzimv4I8TQ2pA0ybJbGEPOPX6V63N4k0W3/1uq22R2Em7+Wa5vxB8QLGPT3i0m4drlmCiRVwUGR8w3KQeM9amfL1YRlLoeex+G/EyzgS6DdyIOCqKBn8QelU9R8OeIYI5bmbR7q3hXLszRnCr15OT0r0Sx+J1nb6ZAtza3dxeBP3rsUGWye4/LgVwGp6vf6pdXMtxfz+VPKZTbqx8sc5AAJPFZ81NFXb3OcO7LK+AoUY9zS84b5G44Jx0P51qQtHDGoaMFsc5UUq7QSwiBJJzn65qfaroh3MWR0RtuSST0x2qRUVVDMjHvnIq5e3IiEaG25dsgImSSKrNqQghSKW1kUYx80eNwruo4HF1YKpCno/T0Jc4rRshkyUKkMCepNEcRLqpfAAA+taNix1aQpEjIYsSfMB+FasOjSKArSpwS3Xv+FYVqNWjLkqRsy4tPVHPzKWZQuTwMj045qSFHjEkUyEI7DdtUMcexHIrqYdAU8vznklUP8AOrkOjWcbZJIP++B/LJrJLyKZiad4QvLqMTRRQ+W6nkyjPXglccfT3q1H4LWOXZrTyWsG0mJrVTKzksM7tqnp2GBx9K6W3WC3GIyq/Tcf8KsidDgFnYem4KP0/wAaoVjhZPDF9bxtbva3dyA29JbeJipRh8pJwT6cHp3xV628GGOOKXULK83IcPs24J9gSOAfcV2UeoJBkRlI8jB2Dkj3NK2vmMHaSc92NC9Bnnl3odzYlpJbeV4gzviFixQY+XcQD+X6isN7sCVmUgyMCMMoyM+gIOPw5r0m71mJ5B5ghVjyCQB+Oau2cljdw+XPcWt4w5EZAcqPqeTUt9EFjymztYQzPNFwHUnf7c4+lJdXIeUgdC3HNX9S8Naul/cSLBP9j8xmT/dzxwOlZstnKSSZFXB+6B0rFp31Y0UmkAbJOOaQMNwIAP1q19jGPvbjjOAKQ20UfzO/H+0oNNtXArrvD/IudpyQPans0m45Yg55pRJDvypZieu3A/pR5KSfMyPk/wC1UvUL2KuOeaGADEKSVzwSMV0TtpPkkppgaTPABO0/rUGlzaZdX5gu9NjjjCk7oizHOfQmtFG/U63io9mYiqzuFVSzE4AA5JrTmH2GJtPhINzIMXMi/wAI/wCeYP8AOt97bToFD6fbPHc7SBKw+4T3GSeazbfSBG2QSSeSSwqo2TMK1fnVloiO1hESACulgFtLoMSXMroEaQp5RyxPBwV64PrWamngA75h/wAB5qUW8YGN0n03Af0q53cbRRzGjHeWk+nlL2W4kOzbHCowo6deevHv19sVjXbTXN4s/mQxpGVKRAEgYx/hVzZCFxsz7k81GIYM8Ln9az9nN7sNEW7HXLjTVkFukO+QcvsJw2ckgZ96uW3jLVrZYUVYHjiQJtdPvAd8g9azltCRkW7keuw1J9mdOsar/vMo/rVqLX2gt5GjP4z1eYYTyYSVwTGG5/Xis+61rWL6bzZrx1IwQseVAIOc4Hf3pdiL1mgH0Yt/IUpaEf8ALwT/ALsZ/qRVWvu2A261TXb7Pm6lctuGCAxUY+gwKy5NNuJpRK0sgkHRu9a3mwDtM34hf8aPOTtB/wB9OT/hRyoCmtncFcM5z67sU8WJHBkX8WJq15x7RxL/AMBz/OnefKOkpX/dGP5Uci7BcgXTi/q3+6hqX+zVA+Zcf72B/WgyFj80jN9WzSAqOi0+UdxwsoFPJi/76z/KpVhtxj7v/AY8/wA6iDEdhShz60WAoaiIxrOkbQ2PMfPAHYVD4nsUuraKcOEePKjc2d2f8Ki1u4aC90+aNRIyM7BScDoO9ULyPUJ42nup1kVX27VUqFPcAEZxXbjtMNQa/lf/AKXIdBJ1Gn/WhqeHo1ttTnjRlYLaxfNtzngEnmuk85u0jjP904/lXH+HmYahcgHJ8tQK3zKwODu/AdanMakVOF/5If8ApCGoO7S7v8zRLqerMfctmkMygfeP51nCTcwUMST2zz+VXINJ1C4Py2siKf4pPkH68/pXm+2v8KK9m+o430a/xfrUT6gf4QfzrWtvDMh/4+blR6rEuf1P+FWmsdD08hrhkZv+mr7icf7I/wAKTlUfkO0TnY5rq5k2QKXY9kUsavw6BqVw26UrEp/56NyPwFac/iWwtV8q2QyEAEKq7F+nP+FYd94rvHikaN1hjAyREuSPxP8ASobXV3H6I1h4c0u0USX86t/vEID/AFP51TvNc8PacNsNhFIyHAbywAPfJ5rz3U9Xa8lbfIWAJw+SWP4ms9rkO2Xdifc5/Wmr200JcjsdU8WmXIyqjqI4RgD6nqa5yTWrl8ZVCCDnK8+3NZjXSYwBk+9M+0nPykgClyX3Jc2aYvbokOJGVeAewH4VA58zHmNkZGdxql5+6Tac4HY0wz7n3ENnr1p8orl4SxqeQWHQBeKUspOdo/HmqDTHeTnBPfHSm+YVAAOKfKFzu44WJHlwSH6Ka5/TEZPEcsWAG+dSGOMc1tvLK/35Xb6kmsCEbPERHYsw/SujUTsdT5YH3ri3X6Et/IUZtgOblyfRIv8AEiqnGOuaUEDsKLPuK6LXm2o/hnf6uF/kDR9oiH3bVP8AgbM39RVXcKXcadhXLP2uQfcihT6Rj+uaU3l0Rg3DgeinH8qq5PtRk0cqC7JmdnPzyM31OaT5RUefY0ZH/wCumImDLS7/AEqLNHmKO9AEwc0uT3pkaySkeVGzknsK0IdDv5sblSMf7Tf0FF0OxTzjqaNyitVvDFwVGy6j3d9yHH4YoHhi7GP9LtgfXymP9ahztsUomX5noM/Sl3tjOAB7mtlfDd0Rhr+L2xCeB/31Q3hiUj/kIqOP+eB/+KqHOb2RajHuYu8ZwZBn2o3JnAYk1uJ4aVkBe9du/wDqQCP1qzD4fsYiPMEkxHPzsQPyGKzftH1HaKPO7nV7aa9s5pLaXyYnbeBj5hgcA1LL9oPheW9S3ZLZp8KcfKoLdOvPOag1zS4rDX/7OhmldBhvmwNpYZwP0rZmmWPwDqGnTXcTtaXIjhZGH7zlWwPXBLc+1fUZtSwTwlH6um303+G8u/n/AFY56UpqTbMnwuUlu7gzPIuYx/qot56/UYrsUufD9qV+0R3jt1HnDAP4Aiuf+HDFdXuiDj/R/wD2YVn+N4biPxBM8s7XCuAysR9wY+76cV4+Z05e3jZ29yHT+4j0qFWhGmvaU3Ju7vzW6vyZ6FB4o0eFMQQyIB/ciUfyNV7rxgnS0hGfWQ8/kK838LMza4kexXRopdwYZGAhOfqCBXq+ix40i0ZFRSUyxCcnk968331Plb6djerHDzw3tqcHFqSW99032XYwjqesXxYL9rdTkgRRED6dBUEeh6pI2RaMozwHZU/E8122WxyT+NG4/wCRVcie7OHmOXTw1fyLiV7ePPUhmY/oAKzvEnh7+z9Akn+0lyjD5VTA5P1ruCxA5bFc14q1exGiXMH2kPKwGwRckMOQcjpT5IolydjyiVt+fTsTUQLHpgnGfrQ5B3H3pFyhB/WqMhCd33u9APygcdOabtG3p75zTsAZPGPTHNMBoLbsDGeuc9KdyDwe3JpNoJyTSN84GCSOntQAFi3Cvz60ZwAM898k0p5Gc5pu4KMDP5UAdxzzWHIdniFPdx+orarEvvk1uJh03Ia1YM3fp1pefpTd30o3fhQId+NOzxUWcmpoLS5usiGJ3x1IHA+p6U7isNzRuwOnFbNp4bkkIa4nAHpGM/qePyzWtFodnAOI8n+8eW/M1DmhqJzdlp09+heOaONV67lJP4D/AOvWrB4ejPMrzy+3EY/TJreSNUACgcdM807I71PMyrIzk8P2BUB7dB7Bmz+eatwaTp1t/q7WLd/eYbj+tTZHr+gpfMAHBNK7CxLtTg4GRwDjpS5HrxUQk+tG89cUDJgwHT+VG71qHfn3pQcnGKAJd4FJuFMI9RTWJ6DAoAkL8HH86rzTsqnbtJ+tK82z+7+JquGaVsqQPc00M5i+0OS91m6vLyNZIpQoiQsQQQAOg+lLF4NtJtrPCUUdlc8/nXVCNFYM53cYyfXipvujo35V1U8diqUVCnUkkuibSJ5It3aOWt7bT/Dmp3EioY41twTgkk8jiuS1vVZNWm3zRxqxGMoMHHYHnmuy1p7Rb65+3Ro8Rt1wr5xuzx0wa8/uFDSsyMmCeAMgAVyKtOrKU6snJ33bu/xPTxdB/u/ZxsuSO3oXtAuPsbyLBDuuJAVMgTcdh4IHp35r07R2xo9r/uf1Ncb4KiVdN1SY8SspjGe4CkkD/PpXX6T/AMgi19Nn9TWUv4vy/wAhR/3B/wCNf+kyNAt6mo5bgRoXZwqj1PFA6D5ieOpprlSMdQfWtDhONvvEE06OoZFEnXy0IL/1rE1ACWwkVIyGjUbsYDZznJHcY9Pxq9qVrNa38zCOMIhyUcDgHvj096zkQTWUqb8gMSUYZ3DHGD1zkY/Gstb6lrY5hjkYPY80iH5eg4qxdwG3nMbHDA8rg/L7GqwIAO45BrY5xwXdn5gMc9OtJwxJHpQQBg9felBIUkfhQAijIGNox3ppQZ43EehNJubcTg5P6U8AlOgGeCTwKAG8jpjHr6Uq9PmPPsaXhcbfX8qeBnPzd/WgDrd4HBI/OsbVSBfRMD2H862hHnksx/CsfW4xHJERj7p6DFaNgbWG3EBCT69qs2lhcXb7Yo8+pHQfU1Z0nT/tzqzlhCMbiBjPsK6JY4pVCRx7bdT90cBz/h/P+cuXQdijZ6Daphp289vTJEY/xrZUIihV24HQDAA+gpmW9R9PSkJ49ai9xkpl/wBr8c0eaO5zVc7c4IAP5UZ9HI9t1AidnB9aTzMdiPrUILH+L9M0DPUsAPcUwJvMz/epd2R6DqahyxGAQ30zTm3bHLIQNp70wJwxx83B70FwOTikKcsc0ipg4L7j69KVxkiNn1H4U8fWoxgd80/ceOePpQMUqD3P50nlg8FTUbPhsU/zCR1NIBhgjznb+dOGAcAECkYsKMsfSmAbsHpSbv7vA/u9v/rU1uv1+lVry5js7WS4mJ2IMnH5UAcr4vlU32dofAClT2O0+n1BrkxgEEqzY6gnrXYNNbXF6bhbaSVLhTLy5XrjHbso/Wqd9ZXj3O+1/dQvgbDhth+vU1w+15JSWm76v/I+gVfC1KcOdyTUUtEmtP8At5fkZmjteNdSCzjACnzWTd/DtYHr14Jr0TSH3aVBxgAY5789a4eW1u7SzuZJrqMvtzECm3GDk/XgY+pFdH4d1BbrSERpTJLESjkDA65GB9D+lbUnKo+folb+tDjxNXDRoOjSbbck9Ul0a/mfc6HOCCW4BB5FRMUwf3jYOc45qHzenA9qLiSWSHZAxjVmBY8EgeuT34HFdB5hz+uxWqwtLFMsbhlV1dck8dcnk4GPz69a55R5SkqG+Ziwfo31I/lXSanAUmkuZvNvFdgNj7n2E4646/dPpWXMLKVnlLpvYfKoYqQOmCcn8gSePas5ItX3Rg6xa+ZtliQjOSflAJrE2hlGeg610OpQQSQSSxxBWQc/vMEemR3NYByjANThsZzVmN3A5xwBQMDnr70p247D8KacDvkj9KsgUn5eM4pcfKBkcU0nIx3FOBXAA64oAMd+Mnng9qjK7jkOF9s1IOJOOB3HrQEiIySRmkB2a7XYK0gQf3iCR+Q5rJ1tcwxMGBAZl4+laVtbTXlwIYQcnq3YD3q54ssIbPQLaOID5J8s2OWJU5Jq2ynsdJpgRtGslh43QIXIP3cqMj6n/ParLOq4AYLgYA4wKz/DSK/h2xcd4+Rnqc4/pWpsSMZOAuewrOw7jM4XuxPpzSDcedrY96mGDkgHj1pdvH0poRCc/wB0D9aArfSpsAY6UEN6fnRcQwIvfJ/GnBADwP0p4X1P4ZoyB7D3ouMPmA4APtQ4ZoiOhYEUGRcf4VE0pPQfnQBKBuUNjqAefegAL6e/FRQ7yrJnBRyuAO3Ufoak8nJzkk+9ADgyjv8ArTS/zcqSPanrEcdaCgH8XFAxobGdqYzyeaTcx/8A1UuFJ+9mjigBRnsTml2nHPSjdgUm80AJkL6VieJ1eXw/dCMEsu18AdQGBNbDNnjH6VmXqPONjDCntmmgZwuhN/orefPsjD5UbuSMHIx25wamnuGEuYpTt/ukZ/WtyTTYhkBB+FVzpqdSoxUulBu7QKclpcw50luYpD5n3Y2z2/D9K1fCEkgs5mXG0ydCcZ4/+vV5dIDoqqvDAbuOK17SzitYhGgUAdcVSSirILtu7J4pwSAxKsegbgn/ABqUsxbHKgHqe9AQEbcA+xqLypEmyrqkWPugEnP59KBjyzKd2CxyPu8HFYOswy3ZmEUUUZzkeUn3T6deOnp6VvFsfeXI9V5/SqtzdQ26rMwYoTgsiltv1x0FJoLnIS28lvHta02siZV3iID9jnk5PPbiuZuXzKTjHWvSdSgguj5yKZp1O4Dlg2eu7t+dYF7ZWOoK7tF9jmVccEkFh1z6Ae350lEUnc44n5P0pMlsAfe9ac6bHbqe9MXPBPUVRA47VbgZIHWjB25xg0p+6CDzjnFBIIORyelAAMZGDg4zSFB2xRnbyo9qkCnHOz8aAPXNMsE06zEeN0p+8fU+lZ/i5N3hyQnlllRifxI/rW5GhADt1PQH+dZviZPM8OXoUEgKGz6YIo6lvYZ4QYyeGrbn7rOv5Mf8a22APRivupwa53wLmTQXUY+Sdh19QDXTiLH3mHFS9xIgQBTtBY+x5/Wn5Azllp/lbh0OKRii8Abm/ur/AJxRcY3eAOASe3akDOTjaM/nUgTPITH16047YxliAB68UrhYh2MTyTmnpA3oo/nVWfWrC24+0Atn7ka7ifyqo3ie0Q/LE7EjOWYCi47Gv5AByTzSeUo5PNYyeJ1dmxb5IHQOCf0q3a65a3IXnaScf3hn69vxp3YWLZYR3CttwkoEbezD7p/mPyqQNk+1RyYZGDYKsMHBqJXO9YpG/eEfK5GBIP8AH1FAiyXzwKjeQ5A9f0pp+XjjI60hcDHOKYATg+poMhAyetIW54/KjIOaAAPk8UhYgkd6a3Y80hPtTEEkoVT0z6GqLkk8YJPvmlkbLEgHH1poODVIRDIrZwcCpIoFI+cflU8abmyRwOtOkmgRsbtz/wB1fmP5ChsEKijGB0+tPRTt+frk/c5GM8dfaowZyQUg2D1kbH6DJ/lTxE7cSyuQT0X5R/jU2Hcc8iQrmSRQP9psVH9qLf6iB5B642r+Zx+lSxwQxHckahv73U/meacSPWiw7lfbcuPmkjjHcINx/M4H6U1raM5Zw0resjZ/Tp+lWM4BwKiaQHPP1oAjJx8oO0enYVha1ZXDSfaIlV0Iw4HO41qz3CKcFgPrVZ7pkGFXIPrTEcPeWAIkkij27W5XHI6VmtG45CHBOPxrtLy283M0WAfbisa6UuAsbKGByQ5AJ+nY0OwrHP42MeOO3NJyDgd+9aJiDk7wFYcYx/TtVV7dlJxjikIhXA4/iNOCnHyjimbGB5B4oLkHhKdgPdljUHcQCfpVTWU87RL6Prm3f+Watbic4H07VHPG01rLHjO5GGAPUGs7mzRy3w/mAsL2InpMrAfVf/rV2BmK/dj59+K4f4fs3nX8QOPkRj+ZH9a7oRle1Kd7kx2KzSXDHmMsPToKrz3lxbrkW4AHYda0cEdSB+FVpVUkEYJHrWLhJ9TRSS6HPTa/etE2V2sDj5Oaz5nnuR+8m3gnuTn+o/z0rRutFuCzvbOjhjna/UfSqg0rUQoQW8jEc5baR/MYrSMUhOVzMk2kkiVcgdS23B/Hmokdd2HJcA8uG4Ptnj863W0m+kIIhiXA6sFJ/nU0XhsuVa4mAbGDt6n8sVaZOhkrEZYSFEvlId25lwc+gLD9a0LCwnuXaSQbY3Iy2TjA7Ln+fStuHS7eBQCWkYDjzDux+Hap/mJxnrRcB4RVQAMSAPXNRvD5gIJbaDnjqD6g+tShTnp26U5l2jG7BPSmiSsryf6tyDIBx6Eeo/w7Uu7Ixk8dcU+VPNULu+Ycq45Kn/Cow+HZZAEkGMgcgj1BpiF35/xoDEKTikaWPjknPbFJ++bmOIgYzlzt/wA/lQA4YPBP05psjrHGWYgD1ppgdsmSbA9Ix/U/4VEY4ieFyR3f5j+tUoibKxm3N+5jZ/cDj8+lOSKWRuWVM+nzH/Cp9rE8ZxViKJs7iKqwrkcdlGMBy0ns54/LpVhFEa7YwFHoBinbenXIPFKOnAwaQxuDyDyfpTSMe/ankZFIR2oAiYgVC0hB6dqnwMkenUVFIAQe/wBKQFaWV2Hy5+tUpJZzxjP41dcdcKOBnNVmBycAfhQBUPnSHG0g+u2onimxycCp5xOR8rkexqsZJVIyW75oAQkIeWJz2AzWff2vmsrqfKA4K7c7v8K0TMcNjgnqDxms65VpAXEoUgjPPagZh3cBQ5J5zndkmqwlbPzAEDvWzMAQ4V8FxhgVzx7ZrLkiTOVOR3xQAwBJPukc1E0b5+5n6Ujx4PAINPSQou3apx7kUxHtgRT1609VwQFx15FJ936/Wl3qMck+wrnbN7HBeDP3HiS+gzj924/75cV3hYgnGT3rgtLYWXxCu0fEYLzLhjjGeRXcPKUOG4+hyacnqZpaD8k9eKiKgk5JA+tRmUnPPXvSq2cc8ii4yRUAbJA2gcACjzABgdPSkdlx8pz9DwajU9hTEPOWPJyPSk5AIHNMDfQc96RpkiGZWVRn+JsGgCQBiMEjikOxW+Ygj+7Ucdwz/wCqt5XHY/cX8z/QGn+TOyncyJnrt+Y/rgfpVWJuOMgHVTjtUb3QDYQGQ91HzH8hSraQ/edTIw7uc/p0/SpgOAAAB2A4FOwuYrFbiQAA+Wv+2f6D/GmyWgli2PPIG6qy/Lg/Tv8AjVwr2I5prICeM8d6oRVt5dhaJovLkXqUXCsPUH/JFWsZGePxqrJYQSOXYMJc5WTcdyn1Hai3uGD+TOuJgOCPuuPUf1HagZaZeCO9QCE91qwGyAQPwowPXPOaq4iJYR3wak5z7Up4FN3cHnpSAUjjFJ+NGTmkJGen40DELZ6/hSE9x3wKDkrg5IPYDmgD5fvEUAIep/nUbL1xgGnk4+lRs45I/lQAxxxUEkeOeBUrMx56CmHaR1yfSkBTljJ71Surfam4g9Og71qNgVQuGzlQM0AUH2rxgk+9Vw+DwoGOMnvU8kbE4A/Wq727nHzY55xVAQMEdm42nPJI61WlhGccAdqumIL1bdUbKCeAPxpgZkkW18BMjFVmh5+5j6mth1OegIqIx5OdpHtRYDv7m/cnIVUGcAAVDOb2dBDbSpGx5Z884+vap9wkPyCpBGq8k7fp1rz3Tvuzt57bIw7fwhCl8bu71J3fOSka5zn1Jrel27QkQKRIuFBPYUx5o4cebIqA9AzYJ/DrUkcruR5MMr8feZRGv5tz+lapMwbESJmjBGSOuTwKFVuW/h9ulSGO4kPzSxxf9c13t/303H6UfYbdiGlRpyO8zFh+XT9KtIhsrveRqxVG81v7sQLn9Kcgu3IK2wiX1ncKf++Vyf1FX12om1QFUdlGBSZAGapJEmeumBrkzy3Mm4nOyHMa/wAyT+dW4bWCH5o4kVu7Yyx/E81OCAORzSZ5PTFMQc7s0uB360h5o4yeaYBwRxTckMVK4A6Gm5Ixkjpzik3jcTgc9eKBD8+/fignjrTM4wRSZ6mi4Aw74z3qGaJJ02NkEHKsp5VvUVKTnkf4Uh5IwBQMrQTSJIILjAlx8rD7sg9R7+o7fSre70PPftVaaBLiIxyZ25yGU4KnsR6GoIbkpcC1uWX7QBujfoJB6+x9RRcLF3dk/jS5A6Dn2pu7d1yD39KDJ2BouA/8MCmkhQD396Zuz0puSfpii4D2lAFM8xmJABx60mMN0J9KC2Rmi4CE980jHrgc0evPB7U3I70XGNYl+3HbnBpNuBwM+9P9v5U1jtXPGaLgVZyOinqKpuDzVp+Tmqx8wS4wGRuQw7expiKxHOKjdT6CrhQZNMKAjpTuBRaLcOnX0NRGEKehzWg0eMdPyprDAwAMU7gUMH0qNghPKGrrjP3RzVdkbPI/KncLH//Z"></div><hr><div><b><span style='color: blue;'>IMAGE0</span></b>=<b><span style='color: red;'>CROP</span></b>(<b><span style='color: darkorange;'>bbox</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">)=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Do you see a baby?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if ANSWER0 else 'no'")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if True else 'no'")=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: Yes
