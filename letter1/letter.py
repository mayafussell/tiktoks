import base64

loveLetter = b"""

Dear Alexis,

I'm sorry that I am making this TikTok instead of hanging
out with you :(

I promise I will make it up to you!!

You're cute

Thanks,
Michael

"""

secretMessage = base64.b64encode(loveLetter)
print(secretMessage)