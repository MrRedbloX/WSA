# WSA
WSA is scrapping the Web in order to give you its overall sentiment on a specific subject.
## Dependencies
If needed you can install the required pip modules.  
  
`pip install -r requirements.txt`  
  
Also, in *runtime.txt* you have the python version used.
## Usage
You can run *wsa.py* like this:  
  
`python wsa.py topic=cute_kitten`  
  
Or you can use the function inside like so (need to be in the same directory):  
  
`from wsa import wsa`  
`sentiment = wsa("cute kitten", language="en", num=10)`  
  
The parameters *language* and *num* (number of webpages to scrap) are set by default to the values above.  

## Meanings
The normalized sentiment will be around 0.  
A positive result indicates a positive sentiment. A greater result means a more positive sentiment.  
A negative result indicates a negative sentiment. A smaller result means a more negative sentiment.  
In practice, you can take a 10 % margin to say the sentiment is neutral (when the result is over -0.1 and under 0.1).

## Specification
Almost 7000 words are used to describe positivity and negativity.  
The execution time can be significantly reduced by removing words. Of course,  this will also impact the sentiment correctness.  
Only english language is supported for now.  
Some of the webpages will be skipped if they cannot be read.

## Version
Currently in alpha version 0.1.  
