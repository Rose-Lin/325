Rose Lin

Assignment 1

* For the nltk lib practice, I read through the related documents and examples on the website and picked out functions that might be helpful and designed some functions that can satisfy my needs.
* For the `re` lib practice, I went through the materials covered in class, inspected the source code of the web pages and figured the right regular expression to use to extract the related content. For example, on the `NOAA's weather server`, information about weather is stored in `<weather></weather>`, and information about temperature is stored in `<temperature_string></temperature_string>`. Therefore to search for the weather condition, I use the expressiont like `/<weather>.*</weather>/` to extract the weather content. This technique is not very general, because I was just inspecting these specific website, so if I apply the same mechanism on some other websites, it is very possible that I won't end up getting the same result. To be able to extract some valid results from other sources, I will need to take into consideration of upper and lower cases and etc..
