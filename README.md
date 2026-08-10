# Andru Data Science Project

Assignment materials for ITI5202 - Data Processing for Big Data (2026).

## Assignment Specifications

The full extracted text of the A2A and A2B specifications is included below. Use the linked PDF files when the original page layout, diagrams, or formatting matters.

## Assignment 2A Specification

[View the original PDF](./A2A_Specification_2026.pdf)

<details open>

<summary>Full text - Assignment 2A Specification</summary>


### Page 1

<pre>Monash    University

                   ITI5202  - Data processing for Big Data 2026

            Assignment 2A: Building Models for Building Energy Prediction

                      Due: (23:55 Sunday, 16 August 2026, End of Week 4)
                               Worth: 15% of the final marks
          Background
          Accurate energy consumption forecasting is critical for modern power grids. It enables utility
          companies to balance supply and demand, prevent outages, and integrate renewable energy
          sources more effectively. For consumers, understanding energy usage patterns can lead to
          significant cost savings and a reduced carbon footprint.

          The way we get and use electricity is changing in a big way. For a long time, large power
          plants made electricity and sent it to our homes. This was a one-way street. Now, we have
          new goals. We need our power to be:

            1. Reliable: We want to have electricity whenever we need it.
            2. Affordable: We want the cost of power to be fair and not too expensive.
            3. Clean: We need to use more clean energy, like solar and wind, to protect the
               environment.

          To meet these goals, we are building a &quot;Smart Grid.&quot; A smart grid is a modern power system
          that utilises computers and the internet to enhance its efficiency. A key part of this system is
          the smart meter. These devices are in people&#x27;s homes, and they measure how much
          electricity is being used. They send this information back to the power company very often.
          This creates enormous amounts of data.

          This data is very useful. By studying it, power companies can predict how much electricity
          people will need at any given time (energy forecasting). Good forecasting is essential for
          several reasons:

            ●  Making the Right Amount of Power: It helps companies make just enough electricity
               to meet everyone&#x27;s needs, without wasting any or running short.
            ●  Using Clean Energy: Power from the sun and wind can change a lot. Forecasting
               helps companies plan for these changes and use more clean energy.
            ●  Preventing Problems: It helps companies manage busy &quot;peak hours&quot; when everyone
               is using a lot of power at once.
          Big data processing enables us to analyse vast datasets from smart meters, weather sensors,
          and building characteristics, thereby building precise predictive models. By identifying key
          drivers of energy consumption—such as time of day, weather conditions, and appliance
          usage—we can forecast future demand with high accuracy.

          In this assignment, you will assume the role of a data scientist working for a power company.
          You will use a real dataset that shows how much electricity different buildings use over time.
          Your job will be to use Apache Spark to study this data and build a program. This program
          will learn from the old data to predict how much electricity a building will use in the future.

                                                                       1</pre>


### Page 2

<pre>Objective of the Project

          This assignment is a two-part assignment:
          In Assignment 2A, we will use Apache Spark&#x27;s MLlib to construct and train machine learning
          models. Our focus will be on accurately predicting a building&#x27;s aggregate energy consumption
          based on sensor and monitoring readings, as well as environmental data.

          Finally, Assignment 2B will utilise Apache Spark Structured Streaming and our trained ML
          model from 2A to process a live stream of energy data and make dynamic, real-time

          consumption predictions.

          The Datasets:
            -  building_information.csv: Contains building information.
            -  meters.csv: Contains energy meter reading.
            -  weather.csv: Contains weather information.
            -  Metadata: description and data type of the dataset, at the end of this document.

          What  you need to achieve

           Use case 1 Based on the historical dataset, build an ML Regression
                     model that can predict aggregated building
                     energy consumption.

          Architecture

          The following figure represents the overall architecture of the assignment setup. Part A of the
          assignment consists of preparing the data, performing data exploration and extracting

          features, and building and persisting the machine learning models.

                                                                       2</pre>


### Page 3

<pre>Fig 1: Overall Architecture for Assignment 2 (This assignment is Part A)

          In both parts, you must implement the solutions using PySpark DataFrame/MLlib for the data
          pre-processing and machine learning pipelines. Excessive use of Pandas for data processing
          is discouraged. Please follow the steps to document the processes and write the code in your
          Jupyter Notebook.

          Getting Started

             ● Download the datasets from Moodle.
             ● Download a template file for submission purposes:
                 ●  A2A_template.ipynb file in Jupyter Notebook to write your solution.
                    Rename it into the format (for example, A2A_xxxx0000.ipynb.
                    xxxx0000 is your authcate ID.
            ●  You will use Python 3+ and PySpark 3.5.0+ for this assignment (This

               environment is the same as we used in labs.)

           IMPORTANT:

                Please answer each question in your Jupyter notebook file using code/markdown
           cell. Acknowledge any ideas or codes you referenced from others in the markdown cell or
           reference list.
                If you use generative AI tools, all prompts you use should also be included in
           the reference section.

                  Part 1: Data Loading, Transformation and Exploration (35%)

                                                                       3</pre>


### Page 4

<pre>In this section, you must load the given datasets into PySpark DataFrames and use
          DataFrame functions to process the data. For plotting, various visualisation packages can be
          used, but please ensure that you have included instructions to install the additional packages
          and that the installation will be successful in the provided Docker container (in case your
          marker needs to clear the notebook and rerun it).

          1.1 Data Loading (5%)
            1. Write the code to create a SparkSession. For creating the SparkSession, you need to

               use a SparkConf object to configure the Spark app with a proper application name, to
               ensure the maximum partition size does not exceed 32MB, and to run locally with all
               CPU cores on your machine1 (note: if you have insufficient RAM, reducing the number
               of cores is acceptable.) (2%)
            2. Write code to define the schemas for the datasets, following the data types suggested

               in the metadata file. (2%)
            3. Using your schemas, load the CSV files into separate data frames. Print the schemas
               of all data frames. (1%)
          1.2 Data Transformation and Feature Creation (15%)
          In this section, we primarily have three tasks:

            1) The dataset includes sensors with hourly energy measurements. However, as a grid
               operator, we don’t need this level of granularity and lowering it can reduce the amount
               of data we need to process. For each building, we will aggregate the metered energy
               consumption in 6-hour intervals (0:00-5:59, 6:00-11:59, 12:00-17:59, 18:00-23:59).
               This will be our target (label) column for this prediction. Perform the aggregation for
               each building.
          In the weather dataset, there are some missing values (null or empty strings). It may lower
          the quality of our model. Imputation is a way to deal with those missing values. Imputation is

          the process of replacing missing values in a dataset with substituted, or &quot;imputed,&quot; values. It&#x27;s
          a way to handle gaps in your data so that you can still analyse it effectively without having to
          delete incomplete records.
            2) Refer to the Spark MLLib imputation API and fill in the missing values in the weather
               dataset. You can use mean values as the strategy.
               https://spark.apache.org/docs/3.5.5/api/python/reference/api/pyspark.ml.feature.Impu
               ter.html
          We know that different seasons may affect energy consumption—for instance, a heater in

          winter and a cooler in summer. Extracting peak seasons (summer and winter) or off-peak
          seasons (Spring and Autumn) might be more useful than directly using the month as numerical
          values.
            3) The dataset has 16 sites in total, whose locations may span across different countries.
               Add a column (peak/off-peak) to the weather data frame based on the average air
               temperature. The top 3 hottest months and the 3 coldest months are considered
               “peak”, and the rest of the year is considered “off-peak”.

          1 More information about Spark configuration can be found in
          https://spark.apache.org/docs/latest/configuration.html

                                                                       4</pre>


### Page 5

<pre>Create a data frame with all relevant columns at this stage, we refer to this data frame as
          feature_df.
          1.3 Exploring the data (15%)
          You can use either the CDA or the EDA method mentioned in Lab 5.
          Some ideas for CDA:
            a) Older buildings may not be as efficient as new ones, therefore need more energy for
               cooling/heating. It’s not necessarily true though, if the buildings are built with higher
               standards or renovated later.

            b) A multifloored or larger building obviously consumes more energy.

            1. With the feature_df, write code to show the basic statistics: a) For each numeric
               column, show count, mean, stddev, min, max, 25 percentile, 50 percentile, 75
               percentile; b) For each non-numeric column, display the top-5 values and the
               corresponding counts; c) For each boolean column, display the value and count. (note:
               pandas describe is allowed for this task.) (5%)
            2. Explore the dataframe and write code to present two plots of multivariate analysis,

               describe your plots and discuss the findings from the plots. (5% each)
                 ○  150 words max for each plot’s description and discussion
                 ○  Note: In the building metadata table, there are some latent columns (data that
                    may or may not be helpful, their meanings is unknown due to privacy and data
                    security concerns).
                 ○  Feel free to use any plotting libraries: matplotlib, seabon, plotly, etc. You can
                    refer to https://samplecode.link

                   Part 2. Feature extraction and ML training (40%)

          In this section, you must use PySpark DataFrame functions and ML packages for data
          preparation, model building, and evaluation. Other ML packages, such as scikit-learn, would
          receive zero marks.

          2.1 Discuss the feature selection and prepare the feature columns (10%)
            1. Based on the data exploration from 1.2 and considering the use case, discuss the
               importance of those features (For example, which features may be useless and should

               be removed, which feature has a significant impact on the label column, which should
               be transformed), which features you are planning to use? Discuss the reasons for
               selecting them and how you create/transform them2
                 ○  300 words max for the discussion
                 ○  Please only use the provided data for model building
                 ○  You can create/add additional features based on the dataset
                 ○  Hint - Use the insights from the data exploration/domain knowledge/statistical
                    models to consider whether to create more feature columns, or whether to
                    remove some columns

            2. Write code to create/transform the columns based on your discussion above

          2 This is an open question in which you would need to decide what columns to use as features and
          what transformation(s) would be required for each feature. Include references when you use
          arguments from third parties or generative AI tools.

                                                                       5</pre>


### Page 6

<pre>2.2 Preparing Spark ML Transformers/Estimators for features, labels, and models (5%)
               Write code to create Transformers/Estimators for transforming/assembling the
               columns you selected above in 2.1, and create ML model Estimators for Random
               Forest (RF) and Gradient-boosted tree (GBT) models. Create two pipelines.
                 ○  Please DO NOT fit/transform the data yet.

          2.3 Training and evaluating models (25%)
            1. Write code to split the data for training and testing purposes (80/20), using seed=2025.

               Use the transformer and estimators in 2.2 to create two ML pipelines.(5%)
            2. Implement a customised evaluation metric Root Mean Squared Logarithmic Error
               (RMSLE), defined as: (10%)

                                  𝜖 𝑖𝑠 𝑡ℎ𝑒 𝑅𝑀𝑆𝐿𝐸 𝑠𝑐𝑜𝑟𝑒.
                        𝑛 𝑖𝑠 𝑡ℎ𝑒 𝑡𝑜𝑡𝑎𝑙 𝑛𝑢𝑚𝑏𝑒𝑟 𝑜𝑓 𝑑𝑎𝑡𝑎𝑝𝑜𝑖𝑛𝑔 𝑖𝑛 𝑡ℎ𝑒 𝑑𝑎𝑡𝑎𝑠𝑒𝑡.
                                𝑝 𝑖𝑠 𝑦𝑜𝑢𝑟 𝑝𝑟𝑒𝑑𝑖𝑐𝑡𝑖𝑜𝑛 𝑡𝑎𝑟𝑔𝑒𝑡.
                                𝑖
                    𝑎 𝑖𝑠 𝑡ℎ𝑒 𝑎𝑐𝑡𝑢𝑎𝑙 𝑡𝑎𝑟𝑔𝑒𝑡.𝑙𝑜𝑔𝑙𝑜𝑔 (𝑥) 𝑖𝑠 𝑡ℎ𝑒 𝑛𝑎𝑡𝑢𝑟𝑎𝑙 𝑙𝑜𝑔𝑎𝑟𝑖𝑡ℎ𝑚 𝑜𝑓 𝑥.
                     𝑖
            3. Train your model with both pipelines3, evaluate the performance for both models (i.e.
               show RMSLE scores) and save the better model (you need it for Part B of Assignment
               2). (10%)
          (Note: You may need to go through a few training loops or use more data to create a better-
          performing model.)
                          Part 3. Performance Tuning (15%)

          Using the better model identified in Part 2, apply hyperparameter tuning techniques to further
          optimise its performance.
           1. Use tools such as ParamGridBuilder and CrossValidator (or TrainValidationSplit) to
             search for the best combination of hyperparameters for your chosen model.

           2. Document your process, including the parameters you chose to tune, the range of values
             you tested, and the evaluation metric you used for tuning. Briefly discuss the results and
             the impact on model performance (no word limit but keep it concise).
           3. Save your tuned model for part B of the assignment (if it’s better than part B).

          Notes: The meters table contains missing values due to sensor or network failures,
          which prevented the recording of these values. To create a better model, you may consider
          imputing those values.

          3 Each model training might take from minutes to hours, depending on the complexity of the pipeline
          model, the amount of training data, the computing power of your laptop and the code efficiencies

                                                                       6</pre>


### Page 7

<pre>Part 4: Data Ethics, Privacy, and Security (10%)

          In the era of big data, the convergence of vast quantities of information from various sources

          raises critical questions related to data ethics, privacy, and security. For example, in the case
          of privacy, many companies are collecting much more data than they need from customers.
          In our case, we used a real-world data set with real customer information. How do you utilise
          those datasets with ethics, privacy and security in mind?

          In this part of the assignment, you are tasked to explore these topics within the context of big
          data processing, drawing on contemporary research, real-world examples, and ethical
          considerations. (word limit: 500 words, please include references)

          Context: This assignment uses real-world smart meter and building data. Imagine this pipeline
          were deployed by an Indonesian utility company.

          Mandatory Foundation
          Briefly define data ethics, privacy, and security in the big data context, and note one key
          difference between UU PDP and GDPR relevant to this scenario (e.g. consent requirements,
          cross-border data transfer rules, breach notification timelines, or the role of the data
          controller/processor).

          (Choose one of the following topics for this context) Explain the significance of these
          issues in today’s data-driven world.

          Data Ethics:
            ●  Analyse how data ethics can influence big data processing;
            ●  Examine real-world examples of how data ethics has been handled, both positively and
               negatively.
            ●  Analyse the balance between technological advancements and ethical responsibilities

          Data Privacy:
            ●  Discuss the challenges and importance of maintaining privacy in big data.
            ●  Investigate regulations and laws that govern data privacy, such as GDPR.
            ●  Evaluate tools and techniques used to ensure privacy, and suggest improvements or new
               methodologies.

          Data Security:
            ●  Explore the potential security risks associated with big data processing.
            ●  Assess the measures currently in place to secure big data, including encryption, authentication,
               and authorisation.
          Summarise the key findings of your analysis.

          Submission

          You should submit your final version of the assignment solution online via Moodle.
          You must submit the files created:

                                                                       7</pre>


### Page 8

<pre>-  Your jupyter notebook file A2A_authcate.ipynb
            -  A pdf file saved from jupyter notebook with all output following the file
               naming format as follows: A2A_authcate.pdf

          Note that both submitted (ipynb and pdf) files will be scanned using plagiarism
          detection software. The highest similarity score among students may be
          interviewed to prove the originality of the task.

          Assignment  Marking Rubric

          Detailed mark allocation is available in each task. For complex tasks and explanation
          questions, you will receive marks based on the quality of your work.

          In your submission, the jupyter notebook file should contain the code and its output. It should
          follow programming standards, readability of the code, and organisation of code. Please find
          the PEP 8 -- Style Guide for Python Code for your reference. Here is the link:
          https://peps.python.org/pep-0008/ Penalty applies if your code is hard to understand with
          insufficient comments.

          Other Information

          Where to get help

               You can ask questions about the assignment in the Assignments section in the Ed
          Forum, which is accessible on the unit&#x27;s Moodle Forum page. This is the preferred venue for
          assignment clarification-type questions. You should check this forum regularly, as the
          responses of the teaching staff are &quot;official&quot; and can constitute amendments or additions to
          the assignment specification. Also, you can attend scheduled consultation sessions if the
          problem and the confusion are still unresolved.

               Searching and learning on commercial websites/forums (e.g. Quora, Stack Overflow)
          is allowed. However, you should not post/ask assignment questions on those forums.

          Plagiarism and collusion
               Plagiarism and collusion are serious academic offences at Monash University.
          Students must not share their work with any other students. Students should consult the policy

          linked below for more information.
               https://www.monash.edu/students/academic/policies/academic-integrity
          See also the video linked on the Moodle page under the Assignment block.
          Students involved in collusion or plagiarism will be subject to disciplinary penalties, which
          can include:
             ● The work not being assessed
             ● A zero grade for the unit
             ● Suspension from the University

             ● Exclusion from the University

                                                                       8</pre>


### Page 9

<pre>Late submissions and Special Consideration
               ALL Special Consideration, including within the semester, is now handled centrally.
          This means that students MUST submit an online Special Consideration form via Monash
          Connect. For more details, please refer to the Unit Information section in Moodle.

          There is a 5% penalty per day including weekends for a late submission. Also, the cut-off
          date is 7 days after the due date. No submission will be accepted (i.e. zero mark) after the cut-
          off date unless you have a special consideration.

          Mark Release and Review

            ●  Mark will be released within 10 business days after the submission deadline.
            ●  Reviews and disputes regarding the mark will be accepted a maximum of 7 days after
               the release date (including weekends).

          Generative AI Statement
          As per the University’s policy on the guidelines and practices pertaining to the usage
          of Generative AI:

          AI &amp; Generative AI tools may be used SELECTIVELY within this assessment.
          Where used, AI must be used responsibly, clearly documented and appropriately

          acknowledged (see Learn HQ).
          Any work submitted for a mark must:

            1. Represent a sincere demonstration of your human efforts, skills and subject
               knowledge that you will be accountable for.
            2. Adhere to the guidelines for AI use set for the assessment task.

            3. Reflect the University’s commitment to academic integrity and ethical
               behaviour.
          Inappropriate AI use and/or AI use without acknowledgement will be considered

          a breach of academic integrity.
          The teaching team encourage students to apply their own critical thinking and
          reasoning skills when working on the assessments with assistance from GenAI.
          Generative AI tools may produce inaccurate content, and this could have a negative

          impact on students’ comprehension of big data topics.

          Data source acknowledgement:
          The dataset is a combination based on several real-world and synthetic datasets. We thank
          the original contributors of the datasets.

                                                                       9</pre>


### Page 10

<pre>1. Meters Table (meters.csv)

          This table contains the time-series data for energy consumption for each meter in each
          building.

           Column       Data Type  Description
           Name

           building_id  Integer    A unique identifier for the building where the meter is
                                   located. Foreign key to the buildings table.

           meter_type   Char(1)    The type of energy being measured from 4 different
                                   type of meters. (e.g., &#x27;e&#x27;, ‘c’, &#x27;s&#x27;, &#x27;h&#x27;).

           ts           Timestamp  The exact timestamp of the meter reading.

           value        Decimal    The energy consumption reading value. The
                                   aggregated value of 4 meters is target variable for
                                   prediction.
           row_id       Integer    A unique identifier for each individual reading in the
                                   table.

          2. Buildings Table (buildings.csv)

          This table contains the static metadata and descriptive features for each building.

           Column      Data     Description
           Name        Type

           site_id     Integer  An ID for the geographical location of the building.
                                Foreign key to the weather table.

           building_id Integer  A unique identifier for the building.

           primary_use String   The primary function of the building (e.g., &#x27;Education&#x27;,
                                &#x27;Office&#x27;, &#x27;Retail&#x27;).

           square_feet Integer  The gross floor area of the building in square feet.

           floor_count Integer  The number of floors in the building.

           row_id      Integer  A unique identifier for each building record in the table.

           year_built  Integer  The year the building was constructed.

           latent_y    Decimal  A latent feature with unknown meaning.

           latent_s    Decimal  A latent feature with unknown meaning.

                                                                       10</pre>


### Page 11

<pre>latent_r    Decimal  A latent feature with unknown meaning.

          3. Weather Table (weather.csv)
          This table contains the time-series weather data for each geographical site.

           Column Name     Data Type Description

           site_id         Integer   A unique identifier for the geographical
                                     location/site. Each site may reside in different
                                     country with different seasons.

           timestamp       Timestamp The timestamp of the weather measurement.

           air_temperature Decimal   The temperature of the air in degrees Celsius.

           cloud_coverage  Integer   The portion of the sky covered by clouds (e.g.,
                                     from 0-8 oktas). May contain missing values.
           dew_temperature Decimal   The dew point temperature in degrees Celsius.

           sea_level_pressure Decimal The air pressure in millibars, adjusted to sea level.
                                     May contain missing values.

           wind_direction  Integer   The direction of the wind in degrees from true
                                     north (0-360). May contain missing values.

           wind_speed      Decimal   The speed of the wind in meters per second.

                                                                       11</pre>

</details>

## Assignment 2B Specification

[View the original PDF](./A2B_Specification_2026.pdf)

<details open>

<summary>Full text - Assignment 2B Specification</summary>


### Page 1

<pre>Monash    University

                   ITI5202  - Data processing for Big Data 2026

             Assignment 2B: Using Streaming and ML for Building Energy

                      Consumption  Prediction and Visualisation

                             Due: (23:55 Friday 30 August 2026)
                                    Weight: 35%

          Background (The same as A2A)

          Accurate energy consumption forecasting is critical for modern power grids. It enables utility
          companies to balance supply and demand, prevent outages, and integrate renewable energy
          sources more effectively. For consumers, understanding energy usage patterns can lead to
          significant cost savings and a reduced carbon footprint.

          The way we get and use electricity is changing in a big way. For a long time, large power
          plants made electricity and sent it to our homes. This was a one-way street. Now, we have
          new goals. We need our power to be:

            1. Reliable: We want to have electricity whenever we need it.
            2. Affordable: We want the cost of power to be fair and not too expensive.
            3. Clean: We need to use more clean energy, like solar and wind, to protect the
               environment.

          To meet these goals, we are building a &quot;Smart Grid.&quot; A smart grid is a modern power system
          that utilises computers and the internet to enhance its efficiency. A key part of this system is
          the smart meter. These devices are in people&#x27;s homes, and they measure how much
          electricity is being used. They send this information back to the power company very often.
          This creates enormous amounts of data.
          This data is very useful. By studying it, power companies can predict how much electricity
          people will need at any given time (energy forecasting). Good forecasting is essential for
          several reasons:

            ●  Making the Right Amount of Power: It helps companies make just enough electricity
               to meet everyone&#x27;s needs, without wasting any or running short.
            ●  Using Clean Energy: Power from the sun and wind can change a lot. Forecasting
               helps companies plan for these changes and use more clean energy.
            ●  Preventing Problems: It helps companies manage busy &quot;peak hours&quot; when everyone
               is using a lot of power at once.

          Big data processing enables us to analyse vast datasets from smart meters, weather sensors,
          and building characteristics, thereby building precise predictive models. By identifying key
          drivers of energy consumption—such as time of day, weather conditions, and appliance
          usage—we can forecast future demand with high accuracy.

          In this assignment, you will assume the role of a data scientist working for a power company.
          You will use a real dataset that shows how much electricity different buildings use over time.

                                                                       1</pre>


### Page 2

<pre>Your job will be to use Apache Spark to study this data and build a program. This program
          will learn from the old data to predict how much electricity a building will use in the future.

          Key Information
          This is a two-part assignment (A2A and A2B) that requires staged submissions. In part A2A,
          you are going to use the provided dataset, complete the assignment tasks, and build your ML
          model; then, in part A2B, the trained ML model will be used in combination with streaming
          data to make real-time predictions.
          A2B Due Date: Friday 30 August 2026
          Submission links can be found in Moodle.

          Weight: 30% of Final Marks (15% each for 2A and 2B) A2A and A2B will be marked separately.
          The teaching team only marks A2B submissions during your demo session (Week 6/7).
          Failure to attend this demo will result in 0 marks (for A2B).
          (Please pay attention to the unit announcement in the final teaching week.)

          The Datasets:
               - weather.csv (From A2A)

               - new_meters.csv
               - new_building_information.csv
               - Metadata is the same as A2A.

          What  you need to achieve

           A2B Use   Use streaming data to perform real-time Spark Structured
           Case      prediction and visualise the results Streaming

          Architecture

          The following figure represents the overall architecture of the assignment setup.

                                                                       2</pre>


### Page 3

<pre>Fig 1: Overall Architecture for Assignment 2

          In both parts, you must implement the solutions using PySpark DataFrame/MLlib for the data
          pre-processing and machine learning pipelines. Please follow the steps to document the
          processes and write the code in your Jupyter Notebook.
          In Part B, you will utilise the model from Part A and generate operational insights for the grid
          operator.

          Getting Started

             ● Download the datasets from Moodle.
             ● Download a template file for submission purposes:
                 ○  A2B-Task1_producer.ipynb file for streaming data production
                 ○  A2B-Task2_spark_streaming.ipynb file for consuming and processing data
                    using Spark Structured Streaming
                 ○  A2B-Task3_consumer.ipynb file for consuming the data using Kafka and

                    visualising
                 ●  For submission, please append your authcate ID at the end of the
                    filename. (e.g. A2B-Task1_producer_xxxx0000.ipynb xxxx0000
                    is your authcate ID.
            ●  You will use Python 3+ and PySpark 3.5.0+ for this assignment (This
               environment is the same as we used in labs.)

                                                                       3</pre>


### Page 4

<pre>IMPORTANT:
                Please answer each question in your Jupyter Notebook file using code/markdown
           cells. Acknowledge any ideas or codes you referenced from others in the markdown cell or

           reference list.

                              A2 Part B Specification

          Your task in this application is to build a visualisation dashboard for the power grid
          operator to oversee buildings’ and sites’ energy consumption, so that they can
          optimise their power generation.

                           Part 1. Producing the data (10%)

          In this task, we will implement Apache Kafka producers to simulate real-time data streaming.
          Spark and parallel data processing should not be used in this section, as we are simulating
          sensors that often lack processing capabilities.

            1. Every 5 seconds, load 5 days of weather data from the CSV file. We refer to this as
               weather5s to explain the tasks; feel free to use your own variable name. You should
               keep a pointer in the file reading process and advance it per read. The data reading
               should be in chronological order.

            2. Add the current timestamp (weather_ts) to the weather5s and spread your batch out
               evenly for 5 seconds for each day. Since the weather data is hourly readings, each
               day you shall have 24 records (120 records in total for 5 days).
               For example, assume you send the records at 2025-01-26 00:00:00 (ISO format:
               YYYY-MM-DD HH:MM:SS) -&gt; (ts = 1737810000):
               Day 1(records 1-24): ts = 1737810000
               Day 2(records 25-48): ts = 1737810001
               Day 3(records 49-72): ts = 1737810002
               …

            3. Send your batch of weather data to a Kafka topic with an appropriate name.

          Save your code in Assignment-2B-Task1_producer.ipynb.

           Part 2. Streaming application using Spark Structured Streaming (40%)

          In this task, you will implement Spark Structured Streaming to consume the data from task 1
          and perform a prediction.

          Important:
            -  This task uses PySpark Structured Streaming with PySpark Dataframe APIs and
               PySpark ML.
            -  You also need your pipeline model from A2A to make predictions and persist
               the results.

                                                                       4</pre>


### Page 5

<pre>1. Write code to create a SparkSession, which 1) uses four cores with a proper
               application name; 2) use the Melbourne timezone; 3) ensure a checkpoint location
               has been set.
            2. Write code to define the data schema for the data files, following the data types
               suggested in the metadata file. Load the static datasets (e.g. building information) into
               data frames. (You can reuse your code from 2A.)
            3. Using the Kafka topic from the producer in Task 1, ingest the streaming data into Spark
               Streaming, assuming all data comes in the String format. Except for the &#x27;weather_ts&#x27;
               column, you shall receive it as an Int type. Load the new building information CSV file
               into a dataframe. Then, the data frames should be transformed into the proper formats
               following the metadata file schema, similar to assignment 2A.
            4. Use a watermark on weather_ts, if data points are received 5 seconds late, discard
               the data.
            5. Perform the necessary transformation you used in A2A. (note: every student may have
               used different features, feel free to reuse the code you have written in A2A. If you built

               an end-to-end pipeline, you can ignore this task.)
            6. Load your pipeline model and perform the following aggregations:
                 a) Print the prediction from your model as a stream comes in.
                 b) Every 7 seconds, print the total energy consumption for each 6-hour interval,
                    aggregated by building, and print 20 records. (Note: This is simulating energy
                    data each day in a week)
                 c) Every 14 seconds, for each site, print the daily total energy consumption.
            7. Save the data from 6 to Parquet files as streams. (Hint: Parquet files support streaming

               writing/reading. The file keeps updating while new batches arrive.)
            8. Read the parquet files from task 7 as data streams and send them to Kafka topics
               with appropriate names.
               (Note: You shall read the parquet files as a streaming data frame and send
               messages to the Kafka topic when new data appears in the parquet file.)
          Save your code in Assignment-2B-Task2_spark_streaming.ipynb.

                 Part 3. Consuming data using Kafka and Visualise (30%)

          In this task, we will implement an Apache Kafka consumer to consume the data from Part 2.
          Important:
            -  In this part, Kafka consumers are used to consume the streaming data published
               from task 2.8.
            1. Load the new meters CSV file into a data frame.
            2. Plot two diagrams to show data from 6b and 6c. For each plot, add an explanation of
               what actionable insight a grid operator would get from it and what decision it could
               inform.
            3. Plot a diagram to visualise the daily shortfall/excess energy in each site. The

               shortfall/excess energy is defined as the predicted total sum of energy in each site,
               minus the metered data (the value can be positive or negative, depending on the model
               and data quality). Again, you’re free to choose the type of plot that is the best to
               represent this data.
            4. Plot predicted vs. actual energy consumption over time for one building of your choice,
               and annotate/mark the point of largest prediction error. Hypothesise a plausible cause
               for that error, referencing the features/model you built.

                                                                       5</pre>


### Page 6

<pre>You can refer to the following sites:
          https://samplecode.link/(a mirror of https://python-graph-gallery.com/)
          https://matplotlib.org/

          https://plotly.com/python/

          Save your code in Assignment-2B-Task3_consumer.ipynb.

                          Part 4: Demo and Interview (20%)

           IMPORTANT: The interview is compulsory, and we only mark your A2B during the
           interview. No marks will be awarded if the interview is not attended. (0 marks for the whole
           A2B, not just this section).

          The demo/interview session details will be announced/arranged in the last teaching week.
          Please pay attention to the unit announcement email and Moodle forum.

          Each demo is roughly 10 minutes. You have 5-6 minutes to show your application; then, your
          marker will ask 3-4 questions to assess your understanding. Please come to your allocated
          demo session a few minutes early and ensure your laptop/application works correctly.

          Demo/Interview is marked on a 5-level scale:
          The demo is working, and the student has a competent understanding 20

          Working demo, partial understanding             15
          The demo is not working, partial understanding  10

          The demo is not working, low understanding      5
          No attendance or can&#x27;t answer most of the questions 0

          Submission  A2B

          You should submit your final version of the assignment solution via Moodle. You must
          submit the following:
            ●  A zip file named based on your authcate name (e.g. abcd1234). The zip file should
               contain

                 ○  Assignment-2B-Task1_producer_authcate.ipynb
                 ○  Assignment-2B-Task2_spark_streaming_authcate.ipynb
                 ○  Assignment-2B-Task3_consumer_authcate.ipynb
                    The file in submission should be a ZIP file and not any other kind of
               compressed folder (e.g. .rar, .7zip, .tar). Please do not include the data files in the
               ZIP file.

          Assignment  Marking Rubric

          Detailed mark allocation is available in each task. For complex tasks and explanation

          questions, you will receive marks based on the quality of your work.

                                                                       6</pre>


### Page 7

<pre>In your submission, the Jupyter Notebook file should contain the code and its output. It
          should follow programming standards, readability of the code, and organisation of code.
          Please find the PEP 8 -- Style Guide for Python Code for your reference. Here is the link:
          https://peps.python.org/pep-0008/ Penalty applies if your code is hard to understand with
          insufficient comments.

          Other Information

          Where to get help

               You can ask questions about the assignment in the Assignments section in the Ed
          Forum, which is accessible on the unit&#x27;s Moodle Forum page. This is the preferred venue for
          assignment clarification-type questions. You should check this forum regularly, as the
          responses of the teaching staff are &quot;official&quot; and can constitute amendments or additions to
          the assignment specification. Also, you can attend scheduled consultation sessions if the

          problem and the confusion are still unresolved.
               Searching and learning on commercial websites/forums (e.g. Quora, Stack Overflow)
          is allowed. However, you should not post/ask assignment questions on those forums.

          Plagiarism and collusion
               Plagiarism and collusion are serious academic offences at Monash University.

          Students must not share their work with other students. Students should consult the policy
          linked below for more information.
               https://www.monash.edu/students/academic/policies/academic-integrity
          See also the video linked on the Moodle page under the Assignment block.
          Students involved in collusion or plagiarism will be subject to disciplinary penalties, which
          can include:
             ● The work is not being assessed
             ● A zero grade for the unit

             ● Suspension from the University
             ● Exclusion from the University

          Late submissions and Special Consideration
               ALL Special Consideration, including within the semester, is now handled centrally.

          This means that students MUST submit an online Special Consideration form via Monash
          Connect. For more details, please refer to the Unit Information section in Moodle.

          There is a 5% penalty per day, including weekends, for a late submission. Also, the cut-off
          date is 7 days after the due date. No submission will be accepted (i.e. zero mark) after the cut-
          off date unless you have a special consideration.

          Mark Release and Review
            ●  Mark will be released within 10 business days after the submission deadline.
            ●  Reviews and disputes regarding the mark will be accepted a maximum of 7 days after
               the release date (including weekends).

                                                                       7</pre>


### Page 8

<pre>Generative AI Statement

          As per the University’s policy on the guidelines and practices pertaining to the usage
          of Generative AI:
          AI &amp; Generative AI tools may be used SELECTIVELY within this assessment.

          Where used, AI must be used responsibly, clearly documented and appropriately
          acknowledged (see Learn HQ).
          Any work submitted for a mark must:

            1. Represent a sincere demonstration of your human efforts, skills, and subject
               knowledge for which you will be accountable.
            2. Adhere to the guidelines for AI use set for the assessment task.

            3. Reflect the University’s commitment to academic integrity and ethical behaviour.
          Inappropriate AI use and/or AI use without acknowledgement will be considered

          a breach of academic integrity.

          The teaching team encourages students to apply their own critical thinking and
          reasoning skills when working on the assessments with assistance from GenAI.
          Generative AI tools may produce inaccurate content, which could have a negative
          impact on students’ comprehension of big data topics.

                                                                       8</pre>


### Page 9

<pre>Appendix: Metadata  of the Dataset Schema

          This table contains the time-series data for energy consumption for each meter in each
          building.

           Column       Data Type  Description
           Name

           building_id  Integer    A unique identifier for the building where the meter is
                                   located. Foreign key to the buildings table.

           meter_type   Char(1)    The type of energy being measured from 4 different
                                   type of meters. (e.g., &#x27;e&#x27;, ‘c’, &#x27;s&#x27;, &#x27;h&#x27;).

           ts           Timestamp  The exact timestamp of the meter reading.

           value        Decimal    The energy consumption reading value. The
                                   aggregated value of 4 meters is target variable for
                                   prediction.

           row_id       Integer    A unique identifier for each individual reading in the
                                   table.

          2. Buildings Table (buildings.csv)

          This table contains the static metadata and descriptive features for each building.

           Column      Data     Description
           Name        Type

           site_id     Integer  An ID for the geographical location of the building.
                                Foreign key to the weather table.

           building_id Integer  A unique identifier for the building.

           primary_use String   The primary function of the building (e.g., &#x27;Education&#x27;,
                                &#x27;Office&#x27;, &#x27;Retail&#x27;).

           square_feet Integer  The gross floor area of the building in square feet.

           floor_count Integer  The number of floors in the building.

           row_id      Integer  A unique identifier for each building record in the table.

           year_built  Integer  The year the building was constructed.

           latent_y    Decimal  A latent feature with unknown meaning.

           latent_s    Decimal  A latent feature with unknown meaning.

                                                                       9</pre>


### Page 10

<pre>latent_r    Decimal  A latent feature with unknown meaning.

          3. Weather Table (weather.csv)
          This table contains the time-series weather data for each geographical site.

           Column Name     Data Type Description

           site_id         Integer   A unique identifier for the geographical
                                     location/site. Each site may reside in different
                                     country with different seasons.

           timestamp       Timestamp The timestamp of the weather measurement.

           air_temperature Decimal   The temperature of the air in degrees Celsius.

           cloud_coverage  Integer   The portion of the sky covered by clouds (e.g.,
                                     from 0-8 oktas). May contain missing values.
           dew_temperature Decimal   The dew point temperature in degrees Celsius.

           sea_level_pressure Decimal The air pressure in millibars, adjusted to sea level.
                                     May contain missing values.

           wind_direction  Integer   The direction of the wind in degrees from true
                                     north (0-360). May contain missing values.

           wind_speed      Decimal   The speed of the wind in meters per second.

                                                                       10</pre>

</details>
