

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
### Understanding Data Types

Broadly categorized into two: quantitative and qualitative.

1. Qualitative (also called categorical data)
    
    1. Nominal Data: No numeric value, but a named value. Used for assigning named values to attributes. Nominal values cannot be quantified. Examples:
        
        - Blood group: A, B, O, AB, etc.
        - Nationality: Indian, American, British, etc.
        - Gender: Male, Female, Other
        
        A special case of nominal data is when only two labels are possible, e.g. pass/fail as a result of an examination. This sub-type of nominal data is called ‘dichotomous’.
        
        It is obvious, mathematical operations such as addition, subtraction, multiplication, etc. cannot be performed on nominal data. For that reason, statistical functions such as mean, variance, etc. can also not be applied on nominal data. However, a basic count is possible. So mode, i.e. most frequently occurring value, can be identified for nominal data.
        
    2. Ordinal Data: Categorical data with a meaningful order or ranking. Examples:
        
        - Education level: High School, Bachelor's, Master's, PhD
        - Customer satisfaction: Very Unsatisfied, Unsatisfied, Neutral, Satisfied, Very Satisfied
        - T-shirt sizes: Small, Medium, Large, X-Large
        
        Like nominal data, basic counting is possible for ordinal data. Hence, the mode can be identified. Since ordering is possible in case of ordinal data, median, and quartiles can be identified in addition. Mean can still not be calculated.
        
2. Quantitative Data
    
    1. Interval Data: Numeric data with known order and equal intervals between values, but no true zero point.
        - Examples: Temperature (°C, °F), Calendar dates, IQ scores
        - Properties:
            - Allows addition and subtraction
            - Measures of central tendency: mean, median, mode
            - Standard deviation can be calculated
            - No true zero point, so ratios are meaningless
    2. Ratio Data: represents numeric data for which exact value can be measured. Absolute zero is available for ratio data. Also, these variables can be added, subtracted, multiplied, or divided. The central tendency can be measured by mean, median, or mode and methods of dispersion such as standard deviation.
        - Examples: Height, Weight, Age, Income
        - Properties:
            - Allows all arithmetic operations, including multiplication and division
            - Has a true zero point
            - Ratios are meaningful (e.g., twice as tall, half as old)