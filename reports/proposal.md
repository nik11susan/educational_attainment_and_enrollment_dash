# Proposal Education Attainment and Enrollment 

## Section 1: Motivation and Purpose

|                    |                                                                       |
|--------------------|-----------------------------------------------------------------------|
| Who We are         | International Data Scientist                                  |
| Our goal           | To help free education related sub sections in the UN to understand the disparity in provision of education across the globe for different groups of people.  |
| Target Audience    | Policy makers / UN staff or volunteers                                                |
| Secondary Audience | Any NGO working towards providing free and fair education to all communities in developing countries       |

Living in the 21st century, it feels like there is no more lack of provision of education in developing countries. But nothing could be further from the truth. The fifth release of the carefully accumulated dataset from [The World Bank](https://datacatalog.worldbank.org/search/dataset/0038973/Education-Attainment-and-Enrollment-around-the-World) tells us how much of the population in developing countries have actually attained basic education. This varies from country to country and also depends on whether the population is male, female, from the urban areas or from rural areas. This dashboard gives us an idea about the proportion of people belonging to different age groups, countries, gender and locality that have attained different grades.

### User Persona

Annie is an enthusiastic intern working at the United Nations Academic Impact (UNAI). As part of her latest project, her team want to understand the basic level of education that 10 developing countries have:
- Afghanistan
- Albania
- Angola
- Armenia
- Azerbaijan
- Bangladesh
- Benin
- Bulgaria
- Burkin a Faso
- Burundi
They want to compare the literacy rate of each of these countries with respect to the age group and gender. Annie has been tasked to find out more about education levels achieved and has to present this to the team through a compact presentation so that they can make decisions accordingly and work towards bridging the gap of literacy rate between developing and developed countries.

### Usage

With the Education and Enrollment Dashboard, we can how the proportion of individuals who have completed a grade decreases as the grade increases. We can get this information for different age groups belonging to different social groups. We can also compare the literacy rate of each country and their social groups by selecting the grade.


## Section 2: Description of the data

We will visualize the dataset provided by [The World Bank](https://datacatalog.worldbank.org/search/dataset/0038973/Education-Attainment-and-Enrollment-around-the-World). The original dataset contained multiple columns with different indicators but after preprocessing this data, we have a dataframe with eight columns - `country`, `attained_grade`, `age_group`, `adminregion`, `year`, `adminregionname`, `category`, `literacy_rate`.
`country` - contains a unique list of 10 countries
`attained_grade` - provides the grade cleared by individuals (ranges from 1 to 9)
`age_group` - provides the age group of the individuals (has four values in total - `15to19`, `20to29`, `30to39`, `40to49`)
`adminregion` - administrative region code
`year` - year when the data was collected
`adminregionname` - administrative region name

## Section 3: Research questions and usage scenarios

Through this application, people in the shoes of our fictional character Annie will be able to answer the following questions:

- Which age group has attained education at a certain grade the most?

- How does the mean literacy rate compare between different countries?

- Which section of the soceity seems to have least access to education?

- Are the male population in all countries more literate than the female population?


