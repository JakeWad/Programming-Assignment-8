Lewis University SP23-CPSC-46000-LT1-Programming Languages

Programming-Assignment-8

NLP is a field that attempts to have computers understand natural (i.e., human) language. There are many exciting breakthroughs in the field. While NLP is a complicated field, it is fairly easy to create a simple program to respond to English sentences.

For this programming, you will explore some of the basics of NLP. As you explore this, you will work with a variety of methods of the String class and practice using the if statement. You will trace a complicated method to find words in user input.

Chatbots are programs that are designed to respond like humans to natural language input.  We are developing a chatbot as this programming assignment’s goal.

	Have it responds “Tell me more about your dad” when the statement contains the word “dad” or “mom”, “brother”,or “sister” 	For example, a possible statement and response would be:
		Statement: Where does your sister live?
		Response: Tell me more about your family.

	Have it responds “Tell me more about your pets” when the statement contains the word “dog” or “cat.” For example, a 	possible statement and response would be:
		Statement: I like my cat Mittens.
		Response: Tell me more about your pets.

	Have it responds “Why so negative?” when the statement contains the word “no”, For example, a possible statement and 	response would be:
		Statement: I have no money.
		Response: Why so negative?

	Have it responds favorably when it sees the name of your teacher. Be sure to use appropriate pronouns! For example, a 	possible statement and response would be:
		Statement: Mr. Finkelstein is telling us about robotics.
		Response: He sounds like a good teacher.

	Have the code check that the statement has at least one character. You can do this by using the trim method to remove 	spaces from the beginning and end, and then checking the length of the trimmed string. If there are no characters, the 	response should tell the user to enter something. For example, a possible statement and response would be:
		Statement:
		Response: Say something, please.

If no matching of the keyword, then add 5 more noncommittal responses to the possible random responses.

No partial match.  If you are matching the word “cat”, then “catch” should not be an acceptable answer

Case-insensitive.

Exit the program when “bye” is entered.

This program is a simple REPL application

 

Sample Dialog between human and chatbot:

		Hi, How are you? This is Chatbot Q.

		I can answer all your questions.

		You>>

		Q>> Say something, please.

		You>>dog

		Q>> Tell me more about your pets.

		You>>cat

		Q>> Tell me more about your pets.

		You>>catch

		Q>> Wait a moment!

		You>>fish

		Q>> I don't know

		You>>sister

		Q>> Tell me more about your family

		You>>data

		Q>> I am not sure. Can you repeat again?

		You>>dad

		Q>> Tell me more about your family

		You>>How about your sister?

		Q>> Tell me more about your family

		You>>I know your mom.

		Q>> Tell me more about your family

		You>>Never mind

		Q>> What is the key point?

		You>>I go to catch a fish.

		Q>> I don't know

		You>>I am not a doggy.

		Q>> Tell me more!

You>>bye
