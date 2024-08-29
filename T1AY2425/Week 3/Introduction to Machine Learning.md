

# Introduction to Machine Learning

> Lectures by Jazzie R. Jao, MSc | jazzie.jao@dlsu.edu.ph 
> *References provided at the end.*
# Objectives



# Background

Arthur Samuel, an early American leader in the field of computer gaming and artificial intelligence, coined the term “Machine Learning” in 1959 while at IBM. He defined machine learning as “the field of study that gives computers the ability to learn without being explicitly programmed.” However, there is no universally accepted definition for machine learning. Different authors define the term differently. We use “machine” to denote a system that can be programmed.

> How do machines learn?
> 
> A computer program is said to learn from experience E with respect to some class of tasks T and performance measure P, if its performance at tasks T, as measured by P, improves with experience E.

- What this essentially means is that a machine can be considered to learn if it is able to gather experience by doing a certain task and improve its performance in doing the similar tasks in the future. When we talk about past experience, it means past data related to the task. This data is an input to the machine from some source.
- For a extensive discussion on the history of machine learning, kindly read this.
- A computer program which learns from experience is called a machine learning program or simply a learning program.

**Examples**

- Handwriting recognition learning problem
    - Task T: Recognizing and classifying handwritten words within images
    - Performance P: Percent of words correctly classified
    - Training experience E: A dataset of handwritten words with given classifications
- A robot driving learning problem
    - Task T: Driving on highways using vision sensors
    - Performance measure P: Average distance traveled before an error
    - Training experience E: A sequence of images and steering commands recorded while observing a human driver
- A chess learning problem
    - Task T: Playing chess
    - Performance measure P: Percent of games won against opponent
    - Training experience E: Playing practice games against itself

![AltText|500](images/Screenshot%202024-08-28%20at%205.59.14%20PM.png)

![AltText|500](images/Screenshot%202024-08-28%20at%206.01.06%20PM.png)


# General Steps Involved

It is important to note that the general steps in machine learning mentioned below is not STRICT. In real-life situation, these steps typically involve iterative processes and are not one-way (usually a cycle and non linear). We aim to introduce these steps as a building block of understanding how machine learning is usually conducted since we assume that the students are relatively new to the topic.

1. Preparing to Model
2. Learning
3. Performance Evaluation
4. Performance Improvement

## Preparing to Model

Note: you might find that this section is kind of similar to EDA.

### Understanding the Context of your Dataset

The dataset given below is of table format, a structured data. In reality, unstructured data also exist which creates more complex analysis. For the sake of explaining the concept, we will start with a simple case of structured dataset like a table. Read this resource for more discussion on different types of data that you might encounter.

A data set is a collection of related information or records. For example we may have a data set on students in which each record consists of information about a specific student.
![](images/Screenshot%202024-08-28%20at%204.38.06%20PM.png)
We can have a data set on student performance which has records providing performance, i.e. marks on the individual subjects:
![](images/Screenshot%202024-08-28%20at%204.55.36%20PM.png)