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
- For a thorough discussion on the history of machine learning, kindly read this.
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