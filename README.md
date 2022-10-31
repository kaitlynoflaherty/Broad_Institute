# The Broad Institute
# MBTA Take Home Assessment

Question 1
1. Write a program that retrieves data representing all, what we'll call "subway" routes: "Light Rail" (type 0) and “Heavy Rail” (type 1). 

The program should list their “long names” on the console.
Partial example of long name output: Red Line, Blue Line, Orange Line...


The routes were filtered using the following method:
Rely on the server API(i.e.,https://api-v3.mbta.com/routes?filter[type]=0,1) to filter before results are received

ANSWER: I chose this method because the file size is much smaller which makes it much easier to get the relevant data. It is more efficient
to filter the data before iterating through it. Because it is looping through the entire file, as the file size gets bigger the amount of time it takes to iterate through it will also increase. 

Question 2

Extend your program so it displays the following additional information.
1. The name of the subway route with the most stops as well as a count of its stops.
2. The name of the subway route with the fewest stops as well as a count of its stops.
3. A list of the stops that connect two or more subway routes along with the relevant route
names for each of those stops.

ANSWER: I used the following server API to filter the data to show stops for heavy and light rail, and show the routes associated. Due to the intibilty to 
retreive data with an ID number to the specific train line, I used the desciption section of the data in my solution. My approach to this problem is inefficient and does not work on a variety of files. If I had a way to connect each line to it's stops (for example, with an ID number), I would have counted the frequency of the ID number in a list that was separated from the data, as well as the index of the value. With this, I would print the name of the line with the most stops, as well as the number of stops. I would have taken a similar approach to find the least frequent. To answer the final problem, I would separate the data with 2 or more routes.


Question 3

Extend your program again such that the user can provide any two stops on the subway routes you listed for question 1.
List a rail route you could travel to get from one stop to the other. We will not evaluate your solution based upon the efficiency or cleverness of your route-finding solution. Pick a simple solution that answers the question. We will want you to understand and be able to explain how your algorithm performs.
Examples:
1. Davis to Kendall -> Redline
2. Ashmont to Arlington -> Redline, Greenline
  
ANSWER: Although I did not complete the second question, I made an attempt at the third. For my solution I used the same separation of the description by "-" that I had done earlier, and using the components of the description, I compared the name of the route at each stop. If the starting stop had the same route name as the destination, the name of the route is returned. If not, a message is returned. If I had more time to adjust my code, I would make my get_stop_lines() function more useable by using the index I wanted to find as a parameter so I could call get_stop_lines() in find_direct_routes() so I could resue the function to find varying data.
