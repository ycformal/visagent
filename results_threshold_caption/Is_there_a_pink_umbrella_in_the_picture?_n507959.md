Question: Is there a pink umbrella in the picture?

Reference Answer: No, there is an umbrella but it is green.

Image path: ./sampled_GQA/n507959.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='umbrella')
IMAGE0=CROP(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What color is the umbrella?')
ANSWER1=EVAL(expr="'yes' if {ANSWER0} == 'pink' else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>BOX0</span></b>=<b><span style='color: red;'>LOC</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>object</span></b>='umbrella')=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCADJASwDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDyi9srmVrWaJWVljCvg4ZSDVyC/ezFrPNud0VlcMcMeDXRXfh6SUeZDdElRgk5B/IVg3+g6ymSIWnVe8WD/L/CtuVrUz5kyOLxFdR3Dbm82Jj8nGO9bFhq7ajbStFGElicKVY5Bz34rl/LaDCzExsh6MCCPwNaejyLBcBZJYyzjgbMMT9fw9amMnewNKxI3ieN3KGL5c43BiBWve3OrrPpNvZNPHbzRASSxpuCtkjk4I6YrlZPDV+ZH8trduSQPMwcfQiu0XX104w2n2ZpVIxE6yqpkA7hTV3fULLoRaFqN9qf221v1LNbttVim0sCGHOAAeg/OuP+1fa5C7gKzryAu3pjtXe2Gvxahq8cCwzxuobO9lIHHTg1iaxrmi6rZtFAjRXBkBLtBg/mPU0pJNbgt9jmLmMLAQQDgE5ptwuEXdwdnXPXpVyeEOhJXHGGxzgg81XkBuG3sOBjj8OKzRdh0ExMy4Yjdj881Nbx7ba4YnkkH8OKqxp+9jZM7d9WrYl7WVCRl1UD9aBWGwDzZVKchGHP45qfYEtXJI5lyfbrn+dFsixQsCOoyDUxRZLeMD5t53D0pFFWKN9s2FxwCPrjP9BX0J8GIFbwlPK8a7mucg+20H+ea8PtUhS7hWfcIjy5A5FfQ3w7vtNGjWunWCEkQGaZs8Bsgbf1/Cq6E9bDvijJ5fgK9Ax+8khTGeuZB/hWZ4S1nTdB8DW0N04iuPs0l8Iz1kUsxyv94gCrnxZcr4PRFwTJdxLjOOm4/wBK88vra+1zRbc2kunXdhaIqAQzuZIpNoDdR8voyj5T1HIzTjsTI7yPWNA1i1skhlEkt4pljiLqGOMgAAnGSSQAe+c9DXmfxEgjgu9Pisx5VocvHE7FZI5BgOJEPKknHseSDzU/h1Lfwjq0dzcxrc6gY2WAwgutsM7WYrxuJ5AGR0NV/GdpLrc663p+pyapG08dqy3IEciMwwAI8DClunvnHqau9hROj8P/AA/0rX9L/tGGzuLdGQBJJjnzjgbnCg9M5HvWRa6KPDvia50F5DJBqNoyROByJVBIG0nByCwwevAr1jwHpEuk+EbGC4V1m8v5gzsRgkkfKfu9enrXPfEjRYLizN3BMsN/bYuIZsnKFTkYx/tCnGV9AaPna6llkvFExDNEqxEjuE+UfoB+Vdd4H0SbVdWjkKsywsGKhGII9OBjvVG40K81XWpplh2PKPNkURhQrk/MMDoMgnj8q9R8CaONCtQ09vFFduAUlmclWycYGB7fnmhLW4nsehaTpkVlbDbEqMeo24xV8rTrSYXNur4AJHQA4qUpT5tdSbFYrTStWSlMKU1ImxWKmmlaslKYUq1IVisVrmNZvNT028xHepJHL86o1uv7sZxjIPP1PNdaUrhfGz7b9FUgOttlSRnBLGm5WVwIW17VRnMsRx38gY/nWXrur6jdeH9VjkniWMWjs3+jg7hkDHJ4znr2rOF7BtCOoMg4baO/Ge3uKz9VuYhoutbAQfIij/76kX/4k0Kcr2sF9Tq/hra+T4Jt3xzNNLJ9fm2j/wBBrp3jqp4NtPs3gnRoyME2qufq2W/rWs8dagZckdVWj+atV46rNHzRcDznazLhG2k8E4q3bKInZVYBiB8uc/lUaJtX2Bzk1VjUTu8nPzsCPXbWEpWdkXZbsuy2lvOjxzwRS57OA3481nyeGNMMoeGJoZcg4RvlPXseKkR3jjZgWX5uMHtV2K5fkMyucZGVwMVmqil0G1bqcXqHw21Bbh5rG/ikZmLAS5jYHPqM1py+HS6WFxexTCe1HBRgVJznn1rrY5vtGCFIKPg4bg1IAyKOp4PT6048rV0DbWjPO002Cx1Oa5V3LXLHKkDCnrx/9ek8WWEMc9peNBghD5hQAZbdkZ9eK7nV7eOTS7hmjjZ1jLBtoyp9qz7/AEG313aZpZ4mWJSrRYxyO4PXpVSjeDSBPU89iuY3R8g4AJI9ahjxIm4AKpGB781s3HhJYpS1trNpcIOiSZjJ/mKyzY3UE5iaLK9irBh+lcftIrdr7zuWCxX/AD7l/wCAv/Ihtl3Fm2nauSPfmp4lCwqO/UYH1pEgmiEmY32nOS1WoV3SksAP3YH071UWpapmdSlUpO1SLT81YZJ+7hKnnKFQT9KS1bNta4ABWM59gCQPzpssy+esaoxDOcH0/wABSTfJa/KQDtwOf8+lWZl92jiTexTcRxu6Y/Ct3wr4ofSvEEN0shSVttvEipmNFbOScn1H1Oa4qW4Z5mWXJVVxke3/ANetvwmTNq0DS4CBvkcnALYyFx6nnH0oW5LO88T+MZfFmkxB0ULaXzREiPaSwUg45IIrhn1O5t7yWSGaRHVywMQEfT5c4HscZ69a6XW1tobOKOyjhRHuWaXysffC85x355rkdWsZ7fVtkqFHZVb5uPlK7h+YIqpaAtUa1p4hu7FXignYZyWJOdynPGD+PTnmuo0TS7CfT9KvRDcIJdWt4ZMT745QWJ2leodeOvUNkZya89t0kmuYU2fM5x9ev+Net6Zoj6L4U8PJdwhZrnW7eYls9CpwPw5H5VKC2p7FOzRQO6JvYAkDOK4DxDqGo3FhOpsYPJlDRvC8uWfnaQFUEkZz9eo6Vta54wtdNklhfdF5X+skJA28j646jnHf2rzh/HEuoaq5ikLQgmQ5GNiYIYjH19+lEdAlqcXpc2oHxhIyE+ZvIkN04GQADhycA9Pxz610+vfEDUBd3NtNpcZUbQyi5bCDAIHAz06g5rAeyhmlledpUlvN10iyArheSpBON2QB+XtWC97Oxn/eBhMRuJHJA6c079hNHvfg3xzBrVkkcyR21woG7e5CkZxwTXcgq4+VgcdcGvmjSEsodKubi5maOZSBbogBMje/dfr9OteoeAdau7yNPMcG38vZ5s3ADqR8pIwD8pBHJPBFLcVj0YrTSlRQ6jaSSeUt1E0nYBxlunQfiPzqeOWOZQ0bBlPccii7DlIylMKVZK00pVKRNiqVrzXxrNH/AMJBLG7YxFEn1JycfrXqDJXj3i+C+ufGOpNGIVjV0RWcnPCDpgcfmKbvJWRLRzaSxyXcm1iMqdpwMEk8kEdeMfnWbrB8nw5eqpJM91FGPoquf54rXGkujjygm/YH+ZHCjtgEZwfwrP1KzmabRtOlQK1xfjhW3Aj5Fz/48a2StLyJs73PcrC0+y6ZaWwGPJgjj/JQP6U5460JE+ZsepqBkqlLQdjOdKrtH81aTx1WaPmncLHkCT3ZlZCyEfwhkzn8qiS5CRGXYQwGAFcj8gwropNCiVRJAWMqnPzNjd7e1YepadewabKI4JSxO0DGc5PTjrWU6b6lqSBJUmTYHDYXogBP6H+lSrNEqMpkCnAU5O0j8xWLc6NqNjPC66fM2VVshdzZOMgsM85/KoI5NQsrxreWGXzfu+Uy857fUVi6Vn5j5+52Fs0MdigEy78sT84yOv8AgKsIxKcO24bT+GRz/OuX0mY3kksV0RK23eheMDI6HB7jNaSQbYt0Tsu0lRtZhj9apQ5VZDvfU0NWkk/sycA/ejYHj6UmnN5kaqp5EKLn3/yapu9y1jMjO8n7tw2TkcD3Ge9N0Z54yXONroGXJzgYH0xzmtY6ImSOM1jUbe0svKUkXhmLnCn/AFYHTPTr/KtvwiLXVLS4juIUklhIbec5IbOAe3auX12Ji0UoAJZmX/P51u+CLlLO7uLRgS0ygggc5GTj8smuDCUqboxbivuPfzrG4mnmFSMKkkr7KTtsjXvdNtDq1lb/AGdPKlU70wcNyalufDFk7fuTJE7DGVO4fkamvZF/t/TTnAAIORjHJrWd1Ygh1PPY1ph4pSmkuv6IxzSpOdLDym224bvX7UjgNR8F3YkMtpcxu4xkHKZ/mOlZeoaXfw2qefayIVYkkLuH5jNeoPCMknpUDqTgDjHHFbuCPJUjyOIZO4ZOcqfzrrdGh0NPsYguRcXkZSRoomIKuM884BGTXStpVtcSKZbeNmbKliozgjB561DF4T0/TrsTWgkie5V4mBfcqjGcgHp+dKMLMHJGZe21vaRRxWwYedPJNIjMGYM2M9OlXNdWXXrKC6LotxCUgToF2hVXn/vkGqeq6Q+n63JcB0f7YRJ027duF69/WqOtadcz26WVzHPaJFK0gkeMskm4DjIPb/Gna9xdjovh3Z6XJqA1fWJmSCHIgj8otuf+8cdAP1P0rp/iJ43sb65s9N0+V/KtT9skuI1ZWjYK21VBxzg5/KvO9KjurLRp447tFkKSsjI5Cq52BevQ8H86n1W8S4iiheQ5WI+e23kHbjJOOepqXFbjuypHNJqrw27XE87sCzZVisbnJbHXcScc456cVVkjSA+UJDuC75ChwFHZQT1z/hWT9tYIkaO6hc8BsDrkVctHgis2aaJ3VmyVjYDOCOue3J6VAyxdahd6u9uty7SvDEkEe4j5VH3VA9s1VAVHcHB2nBZRkE+1akM2jCyXz9PuzMIyRIZPkYjOOM9BkVkb02KqvtYk7l2YAHY5zz/SnKPLsCdyxGTuUjkk8cjrXoXhe0ur5UkE8abn8qRbgBUc45j3Dp8ueD1xwc15zseMrnbgqGBXnNes+ALqHWdJ/s6cMlzDwkgODMoIIUjAyVxxk9ODUpg0du2g2d+U+ysqTxZKz27AOVxghjz16574rc0iO4hhMEziQxkqWAI5Ht2BGDx71JpBEllG48zG0KBIMEEfXn8DV4lQwBIDN09TQ5FWEIpCKkqC6uYLO3e4uZkihQZZ3OABRcVhSueK8j1uUS63fuWbm4k5Q9ADj+lenX2pSw2EV5YWovo3IOVnSNQp/i3Nwe3514+/gHxfOLll1LzpJWZlIuA2wE5xjcfWtqTS1ZLiPOCwCldobJBAII9OnArLgjF38TfDFqACqS+cRgD+Jmz/AOOCpG8I+KNPHlXN/CJuoBu0jx/wGo/A8U6/Fi0i1CdXuLK1dXkZ1Id9hAwRwf8AWcVq5qzI5Wj3MrxUTJUj3MMc0MLuFkmDGNT/ABbRk4/Oh6zUgsU3Wq7J81XHxVSR0RsM6qfdsVXOKx5fd+J4bG9uYJ4SFgYDKuCSCSM4/D9RWta39reDbFIN3ykowwwBGRx9K5TU7q5tPFV1HDMNs0aN5Rg8wEYGS34A478VY8PXSX2sRXBhWKRoXfbH9xvmA3Y/hJ49fwwc7qoublFbS50E2oJbTvEIJyyqCNg4bjOBVqB1liE5BjJUfeIyPxrJ1SBZL+I/uiyxO210Zi2xs8AezdOp7Va0OSK60pVhkjdCmNyKQOp6qeQeeQa1shdC00Fm7tJ5Vu820ndsUtg8E59+eaS4i0tXignEClB8ibtvyn1HcfWuMsBcxyRgWlvGpOJWX5TndkAdycY5yRwa2tauLKO8ha4S5aRrcSlolyFVWwSRjrnHX0pyikhXZelttNgufs8MX7yWN02r3DdRknHU0620qzjQqjMMhUB3nI56YPfgfWsuW3jvltvs05IEDyRzbcbssOPYirujo3mybpdxIRch85IP/wCuoajaxo72PKtZf94idkcsPx//AFUWNwLC+trthwk4Lf7o4P6VHrX/AB8OO4H9TUbnzLYEdxury8J/Bienn/8AyMqvr+iPRL5EXxFpoTG0g8j6mtvaCMYRvYivH4CRp93knqCPoQKk00/unAPOc5yRToTtOenX9EPMf4GG/wAH/t0j19UC9IcD/ZFMuLy00+xnuZ4Fk24CxkAFjnoMj0yfwrzNJ7hPuzyL9JGp7Xd1MAJLh3APAdicfnXTznknf2er6ZfSoq6fdwsTgEYwM/jS3VyTfwx+WSiMxU55YYrk9F1EQ2E9068xyZ+Y+nf9K049Ss7ySBoLmTzUcjYQRxnq3ocVSi2rjbRFrtx9p1mARqQscajB7Hcc/wBK6dLhCAjSLk9V6Vx1/MiasHkPA2/xYoTxZCZOY1V92Bl8gD34rLRO7NEm1ZHQ32lW15LGkSrbyyhlaeNBuIGGwex5FYd5ZokBMwIV3K5A6oCPStCK/hl1CaJdsqW6K6uCPm3YyMY/2sfhWLrerb7a2RkVQ6SH9zncDt4wc+9HMm7eVx8kkr/13Mq70O3b5oLpQD2ZsflxVWbTZREIVcOyMTkEdxTrJpdSkWyGp3NlPzs35ffn1II5rXvNG1aGyN6l3tibcA+7HmEjC/8AfPvUuIJmVEYzpg2zFpmjkHllgeMjGBS2Vk89rNNINscTcJjBZjgD8P8ACpI7PV3AVJlCqFAXcmRhSMcj+9WxG7WeiP8AasvcfakyCVB2gjnAxx1GaJR5hK0THaRGEUUhladSSxYgLsxkDGM7s55PbHFdV4E1y10e7eS/tpJImGYZEVQd6843Ebh1HQ/UEGues45Xu7i3eXbDc8OGHJJ5H48/zpLOSIebB5zqzNtPlqCeuBj8x+GaxcXt1NPM9Xb4nXV1pz2otkhu7jiCZWwMehUnIOM4IPXFN8P+NGi1iBNQ1Ay2P70xnl3DBR8h9eteZQXEa+RKJm+0wgCEg7CnucZz3HamJEFzJA2Y0Qys5OcJxyRj/PFVCm7XkJyV9D6atNYsr2BZYpdquxVfMG0t7gHtXkXjHxRqN/czQtLItqsjeVGg29CQMjqTjJwa4+x1qYDclxL5UivvdgcsGBTgZ7Z/Su6tZ7W30rT4ZU+0GELhhgM27LE7uo4I+mBWdSMrFRsZ6XcsfheGxuZZROymQfeULG2Cox075rMlvNRt7EfYHuA7AKwjm2F1PJyfrjipfEQmgursOMW1qgXDMpZfbHXpiub0q9n1Fp5NPdVG9eXUA7VUZGD3zTg/duRyvnNGGO7kOZbaZHMjKeQeAuc5x3OB+NYui+fca9qNysUm+OMnC9VbIwOnXg/lWtNF4kjnkK3UZTd8mAAoHvxWDoA1CS4ubi0eFfMcbmlIAJ5P9a1S91lNu6PVNS1K5m8GWl4uoldUtLh2Zi3zuG6tjt6elc2/izX4bcTSavMkbHaGeTAJ9jWZbnVXs919bxShEY7Sy7Sd3Tj25pmqTQ/2RaIbSNyEeQxI3COCMAYOecGnGC5NyW3e1jTPjLXliSU6rKI3G5SW+8Pb1qtPrGp3UplnZ5ZGAy7x5JrNlYzQwxGyQpEFRFVzgEAZXI9CSMH0rXldtwEcSyKBgENxVezTuLnaN/VNEW/u4blX8uRFKkqvzMPQN1Xv065qDRdHfSWMo3EFAgiZgQgz2IH0rdbqpo613cqvcwuULh2eYXMcO57csNm7BIdMdR74/Cqmk2kukaeyKVL+YxcDsSQxAPU9cZOTRprJd32pI3MbTleD/dAH9DWtKqJA2FAAyxx396LdQMv+wLhZ1kOpySIshcI8Y4yc4yD+H86dcaf58pmERZ0jePKgHg84wfWtpG3xKw7qDUNs3+kzr/u4/Kq30EYUUA0qRYlRxDFFtjU9fmfn69OKt2bLLcHyDyciYFSCmR0BHGfzqfVCBe26beGU/N6EZx/Oo4HZJSA55YcMcisZP3jRfCeQ6xxdnPcAf+PGooD/AKMvtxS65IRqCqMBcZPvycCqgy1spP1wO3P/ANavOwn8GJ6mfr/hRq+v6ItRzRyaZd+WchTjNJprD5v8+lQWw2aVqAHTdkfpRprdami/fn6/oh5kv3GG/wAH/t0jY3YpEfg/U/zqAtlDSKs1xL5EMkSOysymQ4BI5x+I6V1JXPHNqxdItLuCfuqUY7h22g/jWsurWlzDItvLuZ5dpIiCkHGfm/KuSuhqFvYGRr+Mxsq/KkWFfC4AyRzwOfxq9ZaZPBqz32S9vcJ9oSQHr5h6EexPP4VrGWlrFuPmM1yRS00Y5yRyTgEj3rAnjeyjBG8s+NoPTOc4q/qLNNPJGCMljyf8+1XLHShe22jxzsSl7OFDbs7V25H0OQRXNUfvJd9DaNlC5SsdfurIMxjjVnXaA6ZIGQfX1FSPqSXcUazQ7/K+6EcjsB079BVDVIkZIZUDRswyFPIA+v1rO8x4CC4Kjse1OPI1qtRS9pF6M6mC8sZNj+Wu1eNxX5k9wevtWndXrtZLA8pKAMkeBlQxxgsB6EVz2ladd6hBNcwxKyJnfubaXwOcfhWe+sXMksUi4VIgFCj+Mf7XrmlyuOzL51J3a/ryNm1vLmCBpZ4JzKzFiqocZycAe3P0qO8Fx/a94t3OI2MSMgDEqoOMA49M/nUkxvHNrJYXcsccse7akpAJz1wO/wDhV1YJiqveXDyyiJg27LbQP7pAOOx980U+aWr2FUsnZCQGN7JDbIy3YgAeYT7xkLjjBIAyc+oqzqc0V7eE6bbRRWvkgNiPBDKF3DHYnoD+NNjtXt5Y2lmjSFkO1G+VsnHJzjPH86tiCFrWSJZAxZWAxjuPatrdDK9iIWtksSTqNt2qb1EjZVuh2YPXj86rTE6kVSEKst2rFIhIAgUAng+59ewq35ULabJbsu+SKHap2nhwMZFWNDsbc6ot1ERujiAWFSMIGz2HTitpwXMkupEZ3TbOVvBqGmQJZzyGMq5yivkdjnI4/Kuj0+/udU0VJLq6kaZZdvA5bsM4rL8cq0eu/MpRWUNjHU4ANaWkxTLo9nPbrvAUsUDDcWDHscZH41k47pl36o3tTiNyt2Huo5FZ1D7Qdxx/tZ56enSufheCzt2gjbyXlnVNxfnk8k457dferc+pSXkmJEaJ0UFkD9iO69f8Kxri1RmXUrqKV7dZCoiRCWfAIBHI43UKEUrJBd7stvaCFdUu4LqRzI7TH5do2jPB564P6UzwvDL/AGf58Uknm7nKorDBIAA4PHXv9O2aivZAmhXMVvcKjIVEqYOSmcEfmRVzQre5j0a2lG4oQzHBwArZNW4W0J5r6nSTaTqMNvEovUw8W1hLdrvDZPI4yDz/ACrGudAvm8yMBZpX2rmaQ4HJYsWU/N14HWhZrO51143t4xcb9ryyRtubsfmz0x+la1tbavb2NrbW76Y0UMjcxptAjx8oA9ck5zUqKHzMw7mfUJWt/tcdsyu+E8sMflzgsRng/WqKJcLu+1MIXJyIyFyq9ga3PsusQ3yFLXT3gaR/PKHDqu47cDIz8uM+5qq0OlIfLuLqaR0+XdLnd685X1JpOKY1Kx6IzfKPwqOa4W3t5Z2PyxKXP4DNcN/wl2oF1DR25jAGQAQT+OTU83ihb+xurU27xySAKHDAjnkjt2/nXVzoysXPCEpbz92dxl3NkdyMmukvpBHYXDtkBY2JJGOxrzi3vZ7RJY4JSnmcFl4b6g9jVfeTkM7t9ST/ADqeayCx6dZ3sItYfMlRQyDBZgM9Ky7rxLaWN8ylWmG0HdCVYdMY61w2/gDG7tz2prSoGDSOsaYyzN0FHOB18niJNRu7NY7dlRpD8zOCRx0wPpnrTtZvp7HTL+7tghngQugcZHGD/LNctNNLYXkKQxIFEyeWjEGSRiOOnc57cDNUPEmpatbyXEErmOKdTlVClSpXpnnt71jNlJOxia0xbUoWI/5Z5/U1DASVIzxjj861rjSvtxhuhLhCgVdoB3ZP196bbaQkWHkleSNTh9o2k8+vOOleZhq8YU1GV7+j/wAj6fN8rr4nGVKtLlcXt78e3myrDC76beqgyzYwM+gqjYPjcO+eldJfW4NhLAsLoi5XCKWI6HB9+f1qnDd21rAFmt0dIDtkKnHnMcD5sDJxnPuOo4qsO3Pmna13+hy5tQdOFCk2m1Gzs0/tN9L9ysHboOpOMetElndpNHOYJfK3NHJg4Kgj06gYJ56VegufLn+0W1mkbT4jVlk4Rd2QQCPl5wD9Ko6herPI0b+YZQSGCqDhRleDjOCDnGcdzXQpNSVjxuRJG3p1gJmT7e0EUU6YLR3JkDn2/hUduvpUsWrxWOlXOlSndPbq0UUi9GRju59MZFc9JNdaeIbOKKcrMpwAwO4HqMEYH/1xVZZ7aC83XunXSMR8sSnYD788nvnFaRk46XG0maNvam4v4/Mk22zEBmTl+R6Hjrx1rbSOPSLXRlmnDCyvclwCodASThevRgKoW2pWNx5Sadpg8xhhQ38JycD8eeamiMk48+6DGUE4GRhfYY4//VU8rbTfR3E3ozJ5ewuUkG7KEqfTacisfT7uWG/ikTGUOcNyPfiuwmeBzLapLG0zoVVAvByp6N/9btXHtaz216BLG0e7IGR/KnJvRPoPduXc6CXxjfTLsjMZSVDG6GP5uRgkN2rPl0qF7q3jspYw5UK6M2cH69P5VVj0m4LRYKCOWTYjFifXr+VdJp2jR6cRcXMiSbeQuPk/nmkmuonzNlm20hrMwxww280gPyB2JbcT1OP8fSthEeMMlwIFlB+7ESR/+us99Sgsp1luJ1ikyQH2/NuHXkexpV1jT5yMXkZPvxWqt0JdxLu3t7rWrRZokkVYJGwwyOoAqO806yinsTBbrGzXKjKZGRgn+gp8ZSbXN0bB0W04ZTkcv/8AWp96pOo6agz/AKx2/JD/AI0gHWszT6lMwVgik5yeuCQP5VZ1CJZ1t9g2t5nLLwfut3qCKxMNwZRcS4OcpgYP1qfyyXBDN8vPBxTcpSXvCSjF6GVqumpqUOny/aD5Yhb5+oOF3Dk/Q1r2KJaWUEMZBRUGMnr3qBtNRrJbUPIsaoUXDdAf51N5BjjVVz8oAHPXH9aENj76VPsjTblTyhuO49R6Vagntbu3MIeN2VArg5BTIz3Hf1rFvVupoHhjiBRxhiW5x7D/AOvT7N5oWnk8soZX3bWAIwBgCmpO4WVjm7qR/wCy7mWaJkkuHjZGBwrKSzYx+Ga3rK/t4tDBs5WkcQqhjQL85XHB4z1zWd4lJuTYxb3LNJt2FQoHQZAHHeuhuvDum3xLXFvEZO0kY2N+nX8apuT1FoVLm3vnmFzbmCc7hIqmfYQcdOh/nUUOrapZTFpdEll4xhZgfxq5H4R0VM4juEzzxcHn86uWukWOnb/J8w7x0kfd+VQoyBtGS/i5RPtuNKubcBerZOPyqWPxbaOg3zQ8cDhs4981qrBamQs0YJx0IqGXR9Ink3tapk+gFO0u4rxOXJlMv+qI5G75uD706J3WXa+51PO70+lRG4QH5mHNV21CJQNpzj0p3SCxplgG6575qPzQSQax5tRkbO3Cr79aktJZriTbHavcNxgRqzH9Kn2i2Q+VmmLiIMA77FyNz4ztHc49BTrS8ivVtriW0hjsEmZGeWPPmSBeBuOTzwdoGKU291Zpvms1tztL5nZQFA/iIPTn1rLtJ45zsEkzy7PvHo3J56YPXFKcpW8i6aTdjYi1b7ffIuxYYUcn5TkbV6NxwvfpnrSXEa6pbXJvpbppQzMltEygIy8DO7kbl/nWXFaCAuSWIYMuAex+tW7ZrbYI3tY5JkQCMnJZ8cAHHp9Kzp1Ip6mzi3Es6Ne2ULT/AGbTFMbFQpkAEuQcKozwc89Mc0ltot/FepLPPFDg/Om4sQrZ44GPQY+la1vZ3dn90CAS8qq7VDKB+Z6k+tEiC2mePYiu687NquXz/EzDOB19ap01e5HtJW5SpL4evbUNJDeIwZgw3SHcBznGMYHJ/wAaq22l3ISRjLHumIOwOUDAjB+Ujk+561vG5t4BGxRnCrhy1wNrEemQMAen61MPIeMTyAJGcHP+Ld6pJX3DmZl3OkX0ds8HnxQkgbYjGEYD1I53ccZwuKx4vDd5OQlxAzcbPMZwMD25HrjpXUC4DsYLOHKhc7vLCgfmOaj822jZjNL50g5KrjCn0wOKhOL0jqKV95HKXOnNa6zpJR22SOYBIW4xjG3nPb+dbrRWdqSbx1uZQQQqxgkHpx3x27DisTxNqVxPcaXlY1UzeYqKTlWBx19MEUyeaS1niMSB4GIEh9Vzg/nyc0LzB6aGRp9y1sPJRyJFlLRKvUFSTyew4q9b39yJrfU2u5TLEvnSIFyPLJ2t14JAzzyc1nWJuILu5kiiVmjdlODjbk4JGf8AIq5YKI7k27XTyRwsZAgHO8ghlz0+uPX60LRaCZr2l5a3FzHbwQxqySl2LDa+QrD3J47Z4qnqiRjU7dm53MSB2A2/407TjaWke6VV/tCOUxSEOSQoHXHTkY59qZfNuvrL1Acce2KiV7jQs6NGtgh+88mQCMdEP+NXrmCUWrkAjeg464x3/WoL6VjNpqpFv2h2UA8t+7q7ezSMJYx8m5fkJHYikMW48m51fSVZAz4klYFcgkIOffkZ/KtSS3s5j5NxFbsW7HAb/GuWe9eG70m54bAcsfVTtB5+lXdSggn1G6LMN6FSCwzwAMAfXP61tDYzluHhJcyX0hB2JhAx6Y3N3rYnAfXrJRyFgmfI99orn9HsILnRY5J/NjBbgrtww3Hj1rROlPGEmtbq7Mf8SlentkVSTsS2rnQbfao2Vg2VFQ+XpsS2xF/d21ysY3iUs8cx75H8J/HFSM0hXgEe55ptWEncXzGHBGKQy+oNQ4YsOp+gpzA4+6aQyUKzDIGCfWmuhOVb8RUWSOhIqaJ942Sdf4W/oaYGZPolrNJ5kiyM2cg7zx9K0Y5JIwFO9wOMsefzp7qVOGHNRkjHUmncCykrN91s+2cH8qd5x6EGs9ivfNAlA6gEeoGDTTFYvZXIPzDByBnjNU5TfmRtn2cpn5e3Hv70bsjKnI9qjMpB6mgEc5YaI95MRc3EVsiAMWc5Jz6Vrr4SsnYKuqM3BLbIgQP7p69PU1mLqF6u0C4YqDwpw34c8mrKSSSQiR1zECcFQBg9PbI9u3tU+zRo7mzbeHtM0q9ZHuYJWO0gXMYYxjr175znOKsnWhErIIZAF4CqwwfoB/8AWrBTUvKjQHzJZMcs5yMZ6Z+nSpF1GN5vLGxQp5CBCW/A9frTT5dLCcSG+aZ55pkRnhaTOWXA6Z4z1xVcXTqFbyVwR0MePy9qnu/tF1MphnCcFQFRix5455x+AxU9tp1ps3ajdSRyquGUlgAM4wSecj65rzqmCpzleLsdEK1lZlP7RBIcS26NjorZNN8uxIwImTsCkhBFR6teWbTAWIIAwdzDrgY6DjnGaoxz+fJgDDgcc9c1hVwdWmuaM2zojJNaqxrW8Onx+ZvWWUOMYeQ4H0wR+vpXQW+txpCYkt4xEgPykFsDjgZJrkCxjO1/lz68Zq9B8thM5/ixiuX6ziKWnMDpU59Ddv7qHdHLLLZ2yZwS0QYHjIxu6d/w7VVaSwtE863ia5cHO4fdHuO+P93FcrqN3I88G6TakQ25zjHGCc4OOv6Vaa9l+wgCUJBtLM3OT+J5r1MPFzhzVnd/h9xzTk4vlhojR1C/mmhtkMgEbzxBlUYDfNznHX6Vdux9r0GOINzHcHDHPykjPXsa5Um6vGjKERNbncBLkk55GQOmOfzqVb2eFwZnV5FB4jBxyR69+K6rq5i0Z2o3f26AvINsluFQDdnd8xyf5VsDS7t7d0mmhRCOm4E9M4+UE9h0z1rDniR1uW3ENJyigYAOc81dlvJ2tUe2u5hcKgHMvT2H61KKv3M64YW2ozSLIGeO44I6MO9aDNL5P24uY5d+7CgAmMgDJ7ZAwc4rElS4llZ2jYvkE4FaOnPIzJFIZgMgIAOp6Y568VK3Bm1pmyXUJHFsj2nl7C5xjcD1Ge3UfzqBbVjPHuuGYxhlEqLuTPAzwcjp6GkcLHCqvbzoijg4EigfQ5p0X2e5Zkh2mVeQGtlGfoBirt0JuXFt5f7UsoJHGyNJMMOVGVGOfftVmRYzDbxzENltjZ74x/j2qGC5uEs2WHdE8UhjnjVzsIxlWAPT0xWtbNGryhQpDEPggY59P0pOCBSMC1sRPqdpZ3cUilIZH28qTyuOn0NV764ki1u4U8eXNlMDggdjW+XB8WW5PRLNz+b1zsEplsL8yLkzPJKGPt6UWtoG5b0iGF7O28xBIwQff5x1PFWrdCt5hI8R5zhWKgcexqhp7TW8VsNu5XiVhtPTNaEFvcfafM8uTpkDuc1cdiHuWC8wVJVZl2yIo3SMQoLDPBPpXQJF5UYRGACjArn47b7fZTQsHj4OfXpx+tbVlO0+n28rdZIlYn3wM009AJ43kJyCuPfrUv3lKkDkdBxUJwR1z+NKrnIG4H607gM8gEZKY+tRSQkfcTPt/gauZAz6UEfgKLgU3klwFkUgqeHxwajaQIx87Kof4lHT6/41dIUg5xULqMYPI9e4oAPIA5DYHrimmAg5LjH0pqjylEagADoO2PalJb+8R9DT0FqMMLKcqwBHp1pPN5O9QWz1DY/Sgs5JIY4qNtxPP8qNAMAW0ZhSUFYy6HO5cBuex6flg0PBMCq8uZPmAV2O7j0Oeac+qJE8QnuftKR/MFVB1PbOB0qi2rMspkhUq2SQzMWP15PX3qm0jeMZsux2crW7TmExxqeWclce2Ov6VWNysQI8xiDwRw38xxWfLdTTsWkkZj6k5qMGpcuxqqf8xoJqlxDGY4H8tTjJUAHjp9PzqvNczTuXmleRicksxOagzRnik3c1UUthWbg1HE5F1FhiucfNjOOaR27VC7EbDnuRUNilsdILC3jglYqXlKNmR/mbp/npRYOP+EcgHAPkk/zxSRX3mQIxKjcuDkkc/lVOyuVOhra85KsmAPc96p8vU4bSRVvGCxg8bgmRnsajaaedIwzF8Sb2LtktimXhS1gKt8zspCjOTjHWpYZohDhcGRCNwPbJ4rGK1sa7mro1hNqd7KeVhG3zJMfoPetua30jzDbm2chONxUgZ/3uprPsdU0yO2hjublopFXnBIGTzziteCSK6UtbXgmXrwQ//wBetbK5lK5VXRNHuHWNGmiZuBiXIJ/EUybwfDk+TdPn/aUH/CtAxhl+ZIm9iCOau29zubEish9TyD+NKyFzM4PUNHuNOlKyAY2lw6nggdevfkcVUiuJUniYsWAJwB1zjr9a67xjG0mnJIoGI2yzZ7dP5tXHxloSJAcMDlfaobszRao0l1RSpJRGPfjFE08bwwvEhEqTRt9Pm5qoblJ33P5RY9S0ZUn8sirNvcWYlRXtVyxCh1djz2zkCru+5NvI0FcOmpMvRplBx3wBUtvcD7TCAeDGAR+FUXPl3bgYjD3BUgnAwY16/pUq6a0d5FcytHcQFv8AVxSkggDgZHQdKHqEdCZ2K69M5GNlgfbqxrEk+WG6ffn90UA9ABiuilnW/wB6rpcGmzuNomQbkdf7jY+6PfBrBurG8gjlhntJVVhgsuSPwOMGkwRZikVfs6lfuxoOn+zmtrT7oTbJHwCcgY9ulc4k+HRmVlBGAcccDFadsWhjzhvlQnp3qoslo1tNKMJct94gfrmtKFFhhjiiGI0GAM5wKx9KkxEWZfm3gc/Q1qnLA9AexFPogJS4yBzuPagbifmAxj8aZvCLll49RzTtxxkZ9vSgB6qMctn2an56gH9ajBB6kilL46EfQ0ALjnvmkIJ9xQp3DjHB6UHpyPyNAELKF4Iyv8qidSpBz9CKsMNwGOfxqu/7vhhlD69qYEbPtPUfQ1CZeeuKlYNwe3rUTI2fuGkBwYbcTyKeKmnu1ivZRBapHCw2PFKgODjBPsQc49KZMiRzMscnmx5+SQDG4djilY7IyvuJRTc0ZoNB2aQmm5pCaLgIxqKU5j+hBpxNMPKsPUVLIZdtLx4o9qW5m5z8vUU63u0Sdo3heONzlQ4xtJ/pVfTnYXERXnJwfpWvKEdCjKSrdc9KDCe5haoZDfPGSMELt+UcDHr1p1sVWeTkjco6nrzUF0n+mtFvJZSEDMO1WxYPFqKRy5YGMOSD2I//AFVEbqVxG7p0q2q7lAZCfnUj1659RV99L02YtL9lRSejRkof0IrJSNxEMNwOM96ngnuIFCNjb6kH+lW3qS0XDaTQLvsdSnQjokr+Yh9uea0ILsXWli5kj8uWPLOM9CuQw9+hqnBdRKVLIu3/AGDnmnwTJZy3EXkPJZXG51cJnymIO5T/ALJ6g0riMzUtXl1SKRIIX+zwHzHLHJI9fp7VhLJucNk4zkZrv4LG2EEUSW8ccZIDhVxkn1/l+NeeuFgujCRwhK/kcVMiou+hdQJ5mXiB9xxU8/krYtJFEVkUq+ck4wwrPV9rjZNj/ZfirS+bcRGJp0VWG0nrgVRJpxySLeyyyj51cFUOByygDr9K04765iO1rJGHXEc//wAVisATO2qFT8674yWA4yAf8RWsspJyRyOKLhYvfb1LDzdPvFP+4G/kalhMMkm22e5gmxuxueM46ZAJwevpiqUUxL4PrVh2JvdP2nnfJyPTYf8A61O4rGbr7Gb7DcMqq8qt5m0YDOp2lse4xUwheSBRDIo83HLLjA9ODT/FcaQ22nhQBtZxx9Af51FaTqFgQseBn9aFuD2RZs7iOO78ja2AjfOe5UjJx24IrULKBwDk1lQqsty0yDJIYZ9mx/8AE1dErDAI/XmrET7wVAbcCeMGkR2HRiAB+FMEjFxgZGMHJ6UoGHJKjn060DJkmOCGxntjvUiOQeOO+D3qsrL0Y/mMUZ2HMbc9QB3oAvFgSAVppyCf7v1pisrjhj9M8ijPoc0AKdoOQcfjTX54JBHcYpQxJKnH0NA3YwGB+tAiq8WzGGyn16UzDjoxqxIwBwwHP41WdHDfKoI96APPWYuSzElicknuatW7LNbm3basinMO2P5nYkZUn0wMj/69U81JEsrMXhDZTBLL/D6HPbmpjudcthwNLmrWpq4uxJKsqzSoHlEkez5/4sD0qnmnJWdioy5lcUmmk0ZqaG1knI42r/eI/l61IN2K5poPNbcdjbxDJjZyO7DP/wBalvLMzWTCNFD8FQoAosZ+0RiWzmGVWH8LZroCc8DDZ7ZrmuUYhgeOua6K2Dvaw7wVYLyD1/8A10okz2Kd3pfmyxyRoVYuN7Bug9QPWr1tYRxLgZyepY8n61bSH5fmP6VKE2jG7iqSRldkBxCAM8Hsaktvmwik8Hg/0qGc7FzkMCeSetMt5B5jgZyRx9cGkw6GwgQRKxwSenvUsUakF5Og6ADp71RhlJiQnkYGKvWrLIHQN83pnrSEaLlVt22noOP515rrEezWrmNQBmZgPxNejOSYCR3XkmuA11dmt3R778/oDSnsVDc21soniEckY+UBcMAelRvpNovzCEAd60lUkDJ5xzgU4xg8EnOc1dibmbJHFZQBxGQvTaoyST/+ulh1OzkwJJWgcj7zjaD/AEqS/wAs8KNypfOQPTn+lMhf5AvBA4xipe4y5HdWYIzeWp996k1qWgjkjZ0ZHBB+ZSD/ACrPtQhb/Vx4/wBwVZt1RdZkCALutQzYGNxD4BP0oEzO8Tg3eq6fZZ+VssfxOP6VXtdHSRFmLEjnac9RnAP5Vb1u1iuvElkkq70EJYj1wWrQUKjoiAKDnIBwKpId9CtHB5AAUlR3qVMsFY+meBVnagyWGPQmonjCygJkDpxVEihSp4Oc07JAJYUqkjGQKUjOVIxx3oAYRv3DtjBqZfkUB1+pFRsu3jB5ODimCRlIXrz34NAyzvUntQSvGG47gUwjIBxz7ipMr3OPqMUABAOOlJkr0OAfXmgjuKjYkDOeKBClmbIOB/WouV4z09aU1GQSetAHGafpEl0I5ZiY4GcJv2kqD3yR6ccDnmu00zQ7XSLloLy3glmmBktisnyq2Dgc8gn3znFU4b0Q6Zq2nhVjktA8iPkZIzg4yMj5SBx/Wsm58QoZtHvQoa6toz5ip8o/2QSP8/nXWnTpLTcT56jH+Irv+1NMsL98GeN3tpPXA+Zc8nsf51zoBY4AyaseZcXEeyRysRkaXYOhY9TT9qxSRBRw3B9/85rjnJTk2joi+SNiS2s1BDS8t2UdBWipxx1qtECq9QB2qdeuM8j2qURKV9ybdhclaFQ9eVB/h60wsFdSxznovf8ACpwRjIIqiCJ7OCaRJXQF1OQfX/GpgmCDnkZwDS7hjqKTJbgZzjJPpQFx4fnkEH0pJJABnB/KlUbScHj0prrnigCjdz/un4PTCD+83QfrVy1AX9zIPYMoHB/z0qjcKweNjjasiNj6MKuzcSrKpPzcGlezGyZSYiY3wTnIIqeI4O7G70I6imLEQMsB+IFV57l4reR4ANw+VTj+InA/UipEbaSg25GeV7GuE1ueO41S4liO5Dj5vU4AzW3fai2nIdKto5JJwoUzMc5yASR75z9Ky0sElvvKLJ5cGAcDmQjv+dJ66FR01N+Jj9nQuP4Bu/KnebuXK5I9hTd+4KvJGckkVYxntWhJk3srebEOmDn8On9RSwncuas3lmLhARwy8g/0rPCy2xJZDgDJI5qHe5Rs27bCPU1OJAuuWx7S20ifiCG/xrKt7mB1+ZuevzHFX45bRGSZpIQ8edmTk89QAO9CJH3X73xNuYDbFbLj3yTV4KMY2gj0rHtlYFpZGYSyYLFhn6CrqSMDtOdx9O4q0BaCYcshILYznkUmS+einPWmoz7eceuQaVQ46jjdkbaYg2lyVYD6eopWjX5CUHy/jikV1eUgqQexqUkHG7BI55oAQupwN1QyA4yoyRyKcGIkUttyRhsVIf5UDBZVbHzYPdW7U9jjntVcjd2+maaHZGOG69qAJW3BDsHzdcZpMqy55P1pAd4HzdfU0jKF6Ej6GgBGGPaoCzZOTT2dgP72PSoTKAccj2xQBxtxf3F5d3cqExrctlwD1GeATSRRBADjJ+tRw/cX6VZXrWV29zXbRD1DY6DPakcgmF/4t+DmpU6VA/8ArB/10H8qpEM1khBwSBntUwU8ADNC1Kn3PwNUSIqc5Hb+L/CnqoAyFApI/wDUJ9BUq9B9KYDfpzmlMZYAHOe2O1Kfv0N/qX/3TQA2Pc2cqDjjI4BoKc/dH4nmnxfdT6Up/i+tIZVmgEmFZRtHYVVEd3EhVG82POVDDBFah6imL1k/3qVgK4vCY1SaN0ZRg8cGo2uYpWgTzAqiZGb2VTk5/Krx61Bcf6l/pSaAtzXUdxGfs25ix5dgQB+dV4LdY2LhcFgAR9P/ANdSx9Wp/wDCPoapIQgVt/RduPU5pxGxCwyAO3rTl6j8KH/1Y/31pgPCMRzgfrTZLZZIWVjwwwcCrH+FHYfQUAU/s6Z2sgOPQdPwpyRpn5UXaOpA6Va/jP4VVuPvN9KAJMqRggAdsmmhwLhWY8bCM/jTY/u/hU8nST6D+VADyffr3p6N+VVY/wDUj6f0NTRfcSgCRlU5OBuxwaReVGec0g+8fxpIv9Wv+e1AhwOzC98fnSnAUY4qOf7/AOAp/wDyzoGRNKQMgginCNnwWbb3FQT/AOrk+hq1H0X6D+VICMqVJ2nPfBprS4ABBz+dSy96rt9+gBGcetQsyk/MAT71HL92ohQB/9k="></div><hr><div><b><span style='color: blue;'>IMAGE0</span></b>=<b><span style='color: red;'>CROP</span></b>(<b><span style='color: darkorange;'>bbox</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">)=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What color is the umbrella?')=<b><span style='color: green;'>green</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if ANSWER0 == 'pink' else 'no'")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if 'green' == 'pink' else 'no'")=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: No
