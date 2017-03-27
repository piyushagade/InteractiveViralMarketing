# Viral marketing influence propagation

In this application, implementation of two standard diffusion models: Linear Threshold Model and Independent Cascading Model to study the propagation of influence has been done. Also, Seed selection algorithm, and Seed set minimization have been implemented.


# Introduction
Viral marketing is an advertising strategy based on effect of “word-of-mouth” among the relationships of individuals to promote a product. Instead of covering massive users directly as traditional advertising methods do, viral marketing targets a limited number of initial users  by providing them incentives and utilizes their social relationships, such as friends, families and co-workers, to further spread the awareness of the product among individuals. In theory, an individual shares an interesting piece of marketing content with all of his or her network; that person's friends then pass the message on to their networks, creating a snowball effect. With the increasing popularity of the online social networks in recent years, performing viral marketing over such networks has become the focus of marketing management.	

# Description of the problem
The critical question is “How to select a fixed number of initial users from the total population with the purpose of maximizing the profit?” Extensive research has been done to address this question, answer to which can be broken down into main components:
1. Finding efficient algorithm to select small but effective set of seeds which is called seeding.
Selecting a limited number of seeds such that the influence incurred by these seeds is maximized. We call this fundamental problem as the influence maximization problem.
2. Selecting appropriate diffusion model which defines how the influence is going to be propagated from the seeding to their neighbors.

However, another common scenario of viral marketing is where companies want to find minimum number of possible seeds while influencing at least a certain number of users.	

# Proposed solution
We intend to implement our project in a way that the user will have two options:
1. If the user wants to know the number of influenced nodes based on a given number of seeds.
2. If the user wants to know the seed-set to be influenced at the beginning.

The user will be prompted to input a graph, number of influenced nodes required/number of seeds. According to the selection and the input provided by the user, the desired output will be displayed. The output will show the result of influence traversal on the given graph and the position of the seeds. We are planning to first find the minimum number of seeds for a given number of influenced nodes using J-MIN-SEED approach [2]. With the given number of seeds, we are planning to find the position of seeds in the given input graph (seed-set) that would give maximum number of influenced nodes using the influence maximization algorithm based on Monte-Carlo simulations [1].


# Group members
1. Swati Sisodia
2. Maithili Gokhale
3. Aman Chanana
4. Piyush Agade

#Screenshots
<img src="http://i.imgur.com/qv6UpFm.png">
<img src="http://i.imgur.com/kCWeaqB.png">
<img src="http://i.imgur.com/uhdhrWq.png">
<img src="http://i.imgur.com/3Nd13M3.png">
<img src="http://i.imgur.com/1rY9mcC.png">

