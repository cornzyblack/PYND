## MemeGenerator Module
	 
### Classes:

#### - MemeEngine

> This is a class for Generating custom Memes on Images.

 ### Dependencies:
- Pillow
- requests

### Examples

    >>> from MemeGenerator import MemeEngine    
    >>> meme_obj = MemeEngine("./pictures")    
    >>> meme_obj.make_meme('dog.png', "I love good dogs", "Luthor")
