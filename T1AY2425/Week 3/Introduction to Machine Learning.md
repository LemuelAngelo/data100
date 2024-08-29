

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

![](images/Screenshot%202024-08-28%20at%204.32.44%20PM.png)


> [!NOTE] Note
> The approach of exploring numeric data is different than the approach of exploring categorical data

### Exploring the Dataset

Consider the following dataset taken from the UCL repository, named Auto MPG dataset.
![](../../Screenshot%202024-08-28%20at%205.34.20%20PM.png)

- What does each column mean?
    - You might need to create a summary detailing the description of each column, the measurement unit (if applicable), if it’s qualitative or quantitative, etc.
- Which column is of (1) discrete, (2) continuous data nature?

With this understanding of data columns attributes, we can separately explore qualitative and quantitative variables.

- Explore and plot (1) numerical data and (2) categorical data (like EDA). These tasks will be given as an interactive notebook.

### Data Quality

Do not expect your dataset to be flawless (in general). Among others, here are the usually encountered problems with regards to data quality:

1. Certain data elements without a value or data with a missing value.
2. Data elements having value surprisingly different from the other elements, which we term as outliers.

Factors at play leading to these issues include:

1. Incorrect sample set selection: The data may not reflect normal or regular quality due to incorrect selection of sample set.
    - For example, if we are selecting a sample set of sales transactions from a festive period and trying to use that data to predict sales in future. In this case, the prediction will be far apart from the actual scenario, just because the sample set has been selected in a wrong time.
    - Similarly, if we are trying to predict poll results using a training data which doesn’t comprise of a right mix of voters from different segments such as age, sex, ethnic diversities, etc., the prediction is bound to be a failure.
    - It may also happen due to incorrect sample size. For example, a sample of small size may not be able to capture all aspects or information needed for right learning of the model.
2. Errors in data collection: resulting in outliers and missing values.
    - In many cases, a person or group of persons are responsible for the collection of data to be used in a learning activity. In this manual process, there is the possibility of wrongly recording data either in terms of value (say 20.67 is wrongly recorded as 206.7 or 2.067) or in terms of a unit of measurement (say cm. is wrongly recorded as m. or mm.). This may result in data elements which have abnormally high or low value from other elements. Such records are termed as outliers.
    - It may also happen that the data is not recorded at all. In case of a survey conducted to collect data, it is all the more possible as survey responders may choose not to respond to a certain question. So the data value for that data element in that responder’s record is missing.

We address these issues by **Data Remediation.**

Incorrect sample set selection can be remedied by proper sampling technique (a task of statistics).

1. Handling outliers. Outliers are data elements with an abnormally high or low value. However, if the outliers are natural, i.e. the value of the data element is surprisingly high or low because of a valid reason, then we should not amend it.
    
    - Remove outliers: If the number of records which are outliers is not many, a simple approach may be to remove them.
    - Imputation: One other way is to impute the value with mean or median or mode. The value of the most similar data element may also be used for imputation.
    - Capping: For values that lie outside the 1.5|×| IQR limits, we can cap them by replacing those observations below the lower limit with the value of 5th percentile and those that lie above the upper limit, with the value of 95th percentile.
    
    If there is a significant number of outliers, they should be treated separately in the statistical model. In that case, the groups should be treated as two different groups, the model should be built for both groups and then the output can be combined.
    
2. Handling missing values. In a data set, one or more data elements may have missing values in multiple records. It can be caused by omission on part of the surveyor or a person who is collecting sample data or by the responder, primarily due to his/her unwillingness to respond or lack of understanding needed to provide a response. It may happen that a specific question (based on which the value of a data element originates) is not applicable to a person or object with respect to which data is collected.
    
    - Eliminate records having a missing value of data elements. In case the proportion of data elements having missing values is within a tolerable limit, a simple but effective approach is to remove the records having such data elements. However, this will not be possible if the proportion of records having data elements with missing value is really high.
    - Imputing missing values. Mean/mode/median is most frequently assigned value. For quantitative attributes, all missing values are imputed with the mean, median, or mode of the remaining values under the same attribute. For qualitative attributes, all missing values are imputed by the mode of all remaining values of the same attribute.
    - Estimate missing values. If there are data points similar to the ones with missing attribute values, then the attribute values from those similar data points can be planted in place of the missing value. For finding similar data points or observations, distance function can be used. For example, let’s assume that the weight of a Russian student having age 12 years and height 5 ft. is missing. Then the weight of any other Russian student having age close to 12 years and height close to 5 ft. can be assigned.

### Dimensionality Reduction

High-dimensional data sets need a high amount of computational space and time. At the same time, not all features are useful – they degrade the performance of machine learning algorithms.

Most of the machine learning algorithms perform better if the dimensionality of data set, i.e. the number of features in the data set, is reduced. Dimensionality reduction helps in reducing irrelevance and redundancy in features.

Dimensionality reduction refers to the techniques of reducing the dimensionality of a data set by creating new attributes by combining the original attributes

### Feature Subset Selection

Feature subset selection or simply called feature selection, both for supervised as well as unsupervised learning, try to find out the optimal subset of the entire feature set which significantly reduces computational cost without any major impact on the learning accuracy.

A feature is potentially redundant when the information contributed by the feature is more or less same as one or more other features.

## Learning

The learning process of machines may seem quite magical to somebody who is new to machine learning. It’s not magic, it’s just math. It tries to emulate human learning by applying mathematical and statistical formulations.

Let us take one of the structures of the learning process, irrespective of the fact that the learner is a machine or human:

1. Data Input
2. Abstraction
3. Generalization.

## Performance Evaluation

# Essential Ideas in ML

## Correlation does not imply causation!

## Bias-Variance Trade-Off

## Curse of Dimensionality

---

# Further Exploration

- Can you search other machine learning paradigms and structures in the literature?
- Can you search other machine learning workflows in the literature? How is it different from what we discussed above?
- Can you give more examples of nominal, ordinal, interval, and ratio data?

![](../../Screenshot%202024-08-28%20at%206.26.33%20PM.png)

# # References

- [https://aitskadapa.ac.in/e-books/AI&ML/MACHINE](https://aitskadapa.ac.in/e-books/AI&ML/MACHINE) LEARNING/Machine Learning ( etc.) ([z-lib.org](http://z-lib.org)).pdf


