import codecs

loveLetter = """

Dear Alexis,

I'm sorry that I am making this TikTok instead of hanging
out with you :(

I promise I will make it up to you!!

You're cute

Thanks,
Michael

"""

secretLetter = codecs.encode(bytes(loveLetter, 'utf8'), 'base64')
print(secretLetter)
