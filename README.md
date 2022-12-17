# Game theory network model
Now let’s suppose there are a lot of people who have weird relationships with some of each other. This can be described as a network in which two people are connected if they’re friends. 
We will refer to this network as a social network. For an indefinite number of weeks, every week each person in the social network will choose to be a good friend or a bad friend. Then, each person gets some amount of happiness for each of their friendships according to the previous table. Their total happiness for some week is the total across their friendships. 
For example, suppose that Annie, Britta, and Chevy are in the social network, and that Annie and Britta are friends and that Annie and Chevy are friends. (Britta and Chevy are not friends.) Suppose one week that Annie chooses to be a good friend, Britta chooses to be a good friend, and Chevy chooses to be a bad friend. 
Then, to calculate Annie’s total happiness that week, we compute Annie’s happiness from her friendship with Britta and add it to her happiness from her friendship with Chevy. As Annie and Britta are both good friends this week, Annie gets +5 happiness, and as Annie is a good friend and Chevy is a bad friend this week, Annie gets −10 happiness. 
Thus Annie’s total happiness for the week is +5 − 10 = −5. It’s a bit easier to calculate Britta and Chevy’s happiness this week. Britta and Annie are both good friends, so Britta gets 5 happiness. Chevy is a bad friend and Annie is a good friend, so Chevy gets 10 happiness. 
(Note each week you only choose if you’re a good friend or a bad friend; you can’t be a good friend to one of your friends and a bad friend to another.)
